#!/usr/bin/env python3
"""Fetch candidate articles for the literature pipeline's scout agent.

Queries PubMed, Europe PMC, and bioRxiv/medRxiv over a date window, merges and
lightly dedupes the results, and writes one JSON file of candidates. It does
*no* relevance scoring -- that is the scout's job, and deliberately not
automated here.

Usage:
    python3 scripts/fetch.py --date 2026-10-15 --out /tmp/candidates.json
    python3 scripts/fetch.py --date 2026-10-15 --lookback 30 --out backfill.json
    python3 scripts/fetch.py --date 2026-10-15 --sources pubmed,biorxiv --out c.json

Only PyYAML is needed beyond the standard library. Set NCBI_API_KEY to raise
the PubMed rate limit from 3 to 10 requests/second.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG = ROOT / "config" / "queries.yaml"
USER_AGENT = "lit-agent-scout/1.0 (literature monitoring; contact: repo owner)"

# Be a good citizen even with an API key; NCBI blocks aggressive clients.
PUBMED_DELAY_WITH_KEY = 0.12
PUBMED_DELAY_NO_KEY = 0.40


# --------------------------------------------------------------------------
# HTTP
# --------------------------------------------------------------------------

def _ssl_context() -> ssl.SSLContext:
    """Default verification, honouring an explicitly configured CA bundle.

    The agent proxy terminates TLS with its own CA, so an env-provided bundle
    has to win over the system store. Verification stays on either way.
    """
    for var in ("SSL_CERT_FILE", "REQUESTS_CA_BUNDLE", "CURL_CA_BUNDLE"):
        path = os.environ.get(var)
        if path and Path(path).is_file():
            return ssl.create_default_context(cafile=path)
    fallback = Path("/root/.ccr/ca-bundle.crt")
    if fallback.is_file():
        return ssl.create_default_context(cafile=str(fallback))
    return ssl.create_default_context()


_CTX = _ssl_context()


def http_get(url: str, params: dict[str, Any] | None = None,
             retries: int = 3, timeout: int = 45) -> bytes:
    """GET with exponential backoff. Raises the last error if all tries fail."""
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    last: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=timeout, context=_CTX) as resp:
                return resp.read()
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
            last = exc
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
    # Keep the underlying reason in the message: a 403 from the agent proxy
    # (network policy denying the host) looks nothing like a timeout, and the
    # scout's log is where that distinction gets noticed.
    raise RuntimeError(f"GET failed after {retries} tries ({last!r}): {url}") from last


def http_get_json(url: str, params: dict[str, Any] | None = None, **kw) -> Any:
    return json.loads(http_get(url, params, **kw).decode("utf-8", "replace"))


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def norm_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (title or "").lower())


def fmt_authors(names: Iterable[str], limit: int = 3) -> str:
    names = [n for n in names if n]
    if not names:
        return ""
    if len(names) <= limit:
        return ", ".join(names)
    return ", ".join(names[:limit]) + ", et al."


def flatten_queries(cfg: dict) -> list[dict]:
    """queries.yaml groups -> flat list of {name, q, group, weight}."""
    out = []
    for group, block in (cfg.get("queries") or {}).items():
        weight = block.get("weight", 1.0)
        for item in block.get("items") or []:
            q = " ".join((item.get("q") or "").split())
            if q:
                out.append({
                    "name": f"{group}/{item.get('name', 'unnamed')}",
                    "q": q,
                    "group": group,
                    "weight": weight,
                })
    return out


def exclusion_clause(cfg: dict) -> str:
    excl = (cfg.get("filters") or {}).get("exclude_publication_types") or []
    return "".join(f" NOT {pt}" for pt in excl)


# --------------------------------------------------------------------------
# PubMed
# --------------------------------------------------------------------------

def pubmed_search(base: str, term: str, start: date, end: date,
                  retmax: int, api_key: str | None) -> list[str]:
    params = {
        "db": "pubmed", "term": term, "retmode": "json", "retmax": retmax,
        # Entrez date, not publication date: papers are indexed days to months
        # after their stated publication date, so edat is what "new today" means.
        "datetype": "edat",
        "mindate": start.strftime("%Y/%m/%d"),
        "maxdate": end.strftime("%Y/%m/%d"),
        "sort": "date",
    }
    if api_key:
        params["api_key"] = api_key
    data = http_get_json(f"{base}/esearch.fcgi", params)
    return list((data.get("esearchresult") or {}).get("idlist") or [])


def _text(node: ET.Element | None) -> str:
    if node is None:
        return ""
    return " ".join("".join(node.itertext()).split())


def pubmed_fetch(base: str, pmids: list[str], api_key: str | None) -> list[dict]:
    """efetch in batches of 200, parsed from PubMed XML."""
    records: list[dict] = []
    for i in range(0, len(pmids), 200):
        batch = pmids[i:i + 200]
        params = {"db": "pubmed", "id": ",".join(batch), "retmode": "xml"}
        if api_key:
            params["api_key"] = api_key
        root = ET.fromstring(http_get(f"{base}/efetch.fcgi", params))
        for art in root.findall(".//PubmedArticle"):
            records.append(_parse_pubmed_article(art))
        time.sleep(PUBMED_DELAY_WITH_KEY if api_key else PUBMED_DELAY_NO_KEY)
    return records


def _parse_pubmed_article(art: ET.Element) -> dict:
    pmid = _text(art.find(".//PMID"))
    # Abstracts arrive as multiple labelled sections; join in document order.
    abstract = " ".join(
        f"{sec.get('Label')}: {_text(sec)}" if sec.get("Label") else _text(sec)
        for sec in art.findall(".//Abstract/AbstractText")
    ).strip()

    authors = []
    for a in art.findall(".//Author"):
        last, init = _text(a.find("LastName")), _text(a.find("Initials"))
        if last:
            authors.append(f"{last} {init}".strip())
        elif _text(a.find("CollectiveName")):
            authors.append(_text(a.find("CollectiveName")))

    doi = ""
    for aid in art.findall(".//ArticleId"):
        if aid.get("IdType") == "doi":
            doi = _text(aid)
            break

    pub_types = [_text(pt).lower() for pt in art.findall(".//PublicationType")]

    # Prefer the structured ArticleDate (electronic pub) over the journal issue
    # date, which is often a month or a season rather than a day.
    d = art.find(".//ArticleDate")
    if d is None:  # not `or`: an empty element is falsy but still the right one
        d = art.find(".//Journal//PubDate")
    year, month, day = (_text(d.find(x)) if d is not None else ""
                        for x in ("Year", "Month", "Day"))

    return {
        "id": f"PMID:{pmid}",
        "alt_ids": [f"DOI:{doi}"] if doi else [],
        "title": _text(art.find(".//ArticleTitle")),
        "authors": fmt_authors(authors),
        "journal": _text(art.find(".//Journal/ISOAbbreviation"))
                   or _text(art.find(".//Journal/Title")),
        "date": _iso_date(year, month, day),
        "source": "pubmed",
        "is_preprint": "preprint" in pub_types,
        "is_review": any("review" in pt for pt in pub_types),
        "publication_types": pub_types,
        "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else "",
        "doi": doi,
        "abstract": abstract,
    }


_MONTHS = {m: f"{i:02d}" for i, m in enumerate(
    "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), start=1)}


def _iso_date(year: str, month: str, day: str) -> str:
    if not year:
        return ""
    mm = _MONTHS.get(month[:3].title(), month.zfill(2) if month.isdigit() else "01")
    return f"{year}-{mm}-{(day or '01').zfill(2)}"


# --------------------------------------------------------------------------
# Europe PMC
# --------------------------------------------------------------------------

def europepmc_search(base: str, term: str, start: date, end: date,
                     retmax: int) -> list[dict]:
    query = (f"({term}) AND (FIRST_PDATE:[{start.isoformat()} TO {end.isoformat()}])")
    data = http_get_json(f"{base}/search", {
        "query": query, "format": "json", "resultType": "core",
        "pageSize": min(retmax, 100),
    })
    out = []
    for r in ((data.get("resultList") or {}).get("result") or [])[:retmax]:
        pmid, doi = r.get("pmid"), r.get("doi")
        src, ext = r.get("source", ""), r.get("id", "")
        is_preprint = (r.get("pubType") or "").lower().find("preprint") >= 0 or src == "PPR"
        out.append({
            "id": f"PMID:{pmid}" if pmid else (f"DOI:{doi}" if doi else f"EPMC:{src}/{ext}"),
            "alt_ids": [f"DOI:{doi}"] if doi and pmid else [],
            "title": r.get("title", ""),
            "authors": r.get("authorString", ""),
            "journal": ((r.get("journalInfo") or {}).get("journal") or {}).get("title")
                       or r.get("bookOrReportDetails", {}).get("publisher", "")
                       or ("preprint server" if is_preprint else ""),
            "date": r.get("firstPublicationDate", ""),
            "source": "europepmc",
            "is_preprint": is_preprint,
            "is_review": (r.get("pubType") or "").lower().find("review") >= 0,
            "publication_types": [p for p in [r.get("pubType")] if p],
            "url": (f"https://europepmc.org/article/{src}/{ext}" if src and ext else ""),
            "doi": doi or "",
            "abstract": r.get("abstractText", "") or "",
            "is_open_access": r.get("isOpenAccess") == "Y",
        })
    return out


# --------------------------------------------------------------------------
# bioRxiv / medRxiv
# --------------------------------------------------------------------------

def biorxiv_window(base: str, server: str, start: date, end: date,
                   max_pages: int = 20) -> list[dict]:
    """Walk the details endpoint's cursor pagination over a date window."""
    out, cursor = [], 0
    for _ in range(max_pages):
        url = f"{base}/details/{server}/{start.isoformat()}/{end.isoformat()}/{cursor}"
        data = http_get_json(url)
        batch = data.get("collection") or []
        if not batch:
            break
        out.extend(batch)
        total = int((data.get("messages") or [{}])[0].get("total", 0) or 0)
        cursor += len(batch)
        if cursor >= total:
            break
        time.sleep(0.3)
    return out


def biorxiv_filter(raw: list[dict], server: str, kw: dict) -> list[dict]:
    """Local keyword filter: the API has no query support.

    A record is a candidate only if it matches at least one platform term AND
    at least one delivery term -- "antibody" alone is far too broad.
    """
    platform = [t.lower() for t in (kw.get("platform") or [])]
    delivery = [t.lower() for t in (kw.get("delivery") or [])]
    out = []
    for r in raw:
        blob = f"{r.get('title', '')} {r.get('abstract', '')}".lower()
        if not any(t in blob for t in platform):
            continue
        if not any(t in blob for t in delivery):
            continue
        doi = r.get("doi", "")
        out.append({
            "id": f"DOI:{doi}",
            "alt_ids": [],
            "title": r.get("title", ""),
            "authors": fmt_authors([a.strip() for a in (r.get("authors") or "").split(";")]),
            "journal": server,
            "date": r.get("date", ""),
            "source": server,
            "is_preprint": True,
            "is_review": False,
            "publication_types": ["preprint"],
            "url": f"https://doi.org/{doi}" if doi else "",
            "doi": doi,
            "abstract": r.get("abstract", "") or "",
            "is_open_access": True,
            # Set by the server once a preprint reaches a journal; the scout
            # turns this into the "preprint_published" flag.
            "published_doi": r.get("published") if r.get("published") not in (None, "NA") else None,
        })
    return out


# --------------------------------------------------------------------------
# Merge
# --------------------------------------------------------------------------

def merge(groups: list[tuple[str, list[dict]]], cap: int) -> list[dict]:
    """Dedupe across sources by ID then normalized title, keeping query hits.

    Source order matters: PubMed records are richest, so they are merged first
    and later duplicates only contribute their query_hits and alt ids.
    """
    by_key: dict[str, dict] = {}
    by_title: dict[str, str] = {}

    for qname, records in groups:
        for rec in records:
            keys = {rec["id"], *(rec.get("alt_ids") or [])}
            if rec.get("doi"):
                keys.add(f"DOI:{rec['doi']}")
            keys = {k.lower() for k in keys if k}

            hit = next((by_key[k] for k in keys if k in by_key), None)
            if hit is None:
                tkey = norm_title(rec["title"])
                if tkey and tkey in by_title:
                    hit = by_key.get(by_title[tkey])

            if hit is not None:
                if qname not in hit["query_hits"]:
                    hit["query_hits"].append(qname)
                for alt in keys - {hit["id"].lower()}:
                    if alt not in [a.lower() for a in hit["alt_ids"]]:
                        hit["alt_ids"].append(alt.upper() if alt.startswith(("pmid", "doi")) else alt)
                # A published version supersedes a preprint record.
                if hit.get("is_preprint") and not rec.get("is_preprint"):
                    hit["is_preprint"] = False
                    hit["preprint_published"] = True
                continue

            rec = dict(rec, query_hits=[qname])
            rec.setdefault("preprint_published", False)
            for k in keys:
                by_key[k] = rec
            tkey = norm_title(rec["title"])
            if tkey:
                by_title[tkey] = rec["id"].lower()

    merged = {id(r): r for r in by_key.values()}.values()
    out = sorted(merged, key=lambda r: (r.get("date") or "", r["title"]), reverse=True)
    return list(out)[:cap]


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--date", default=datetime.now(timezone.utc).date().isoformat(),
                    help="run date, YYYY-MM-DD (default: today UTC)")
    ap.add_argument("--lookback", type=int,
                    help="days back (default: settings.lookback_days from config)")
    ap.add_argument("--out", required=True, help="output JSON path")
    ap.add_argument("--config", default=str(DEFAULT_CONFIG))
    ap.add_argument("--sources", help="comma-separated subset, e.g. pubmed,biorxiv")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    log = (lambda *a: None) if args.quiet else (lambda *a: print(*a, file=sys.stderr))

    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    settings = cfg.get("settings") or {}
    sources = cfg.get("sources") or {}

    end = date.fromisoformat(args.date)
    lookback = args.lookback if args.lookback is not None else settings.get("lookback_days", 2)
    start = end - timedelta(days=max(lookback - 1, 0))

    wanted = set(s.strip() for s in args.sources.split(",")) if args.sources else None

    def on(name: str) -> bool:
        if not (sources.get(name) or {}).get("enabled"):
            return False
        return wanted is None or name in wanted

    queries = flatten_queries(cfg)
    retmax = settings.get("max_per_query", 60)
    excl = exclusion_clause(cfg)
    status: dict[str, str] = {}
    groups: list[tuple[str, list[dict]]] = []

    log(f"window {start} .. {end} ({lookback}d), {len(queries)} queries")

    if on("pubmed"):
        base = sources["pubmed"]["base"]
        key = os.environ.get(sources["pubmed"].get("api_key_env") or "", "") or None
        log(f"pubmed: api key {'set' if key else 'not set'}")
        errors = 0
        for q in queries:
            try:
                pmids = pubmed_search(base, q["q"] + excl, start, end, retmax, key)
                recs = pubmed_fetch(base, pmids, key) if pmids else []
                groups.append((q["name"], recs))
                log(f"  pubmed {q['name']}: {len(recs)}")
                if len(pmids) >= retmax:
                    log(f"  !! {q['name']} hit max_per_query ({retmax}) -- consider tightening")
            except Exception as exc:
                errors += 1
                log(f"  pubmed {q['name']}: FAILED {exc}")
            time.sleep(PUBMED_DELAY_WITH_KEY if key else PUBMED_DELAY_NO_KEY)
        status["pubmed"] = "ok" if not errors else f"partial ({errors} queries failed)"

    if on("europepmc"):
        base = sources["europepmc"]["base"]
        errors = 0
        for q in queries:
            try:
                recs = europepmc_search(base, q["q"], start, end, retmax)
                groups.append((q["name"], recs))
                log(f"  europepmc {q['name']}: {len(recs)}")
            except Exception as exc:
                errors += 1
                log(f"  europepmc {q['name']}: FAILED {exc}")
            time.sleep(0.2)
        status["europepmc"] = "ok" if not errors else f"partial ({errors} queries failed)"

    if on("biorxiv"):
        base = sources["biorxiv"]["base"]
        kw = cfg.get("preprint_keywords") or {}
        oks, errs = [], []
        for server in sources["biorxiv"].get("servers", ["biorxiv"]):
            try:
                raw = biorxiv_window(base, server, start, end)
                recs = biorxiv_filter(raw, server, kw)
                groups.append((f"preprint_scan/{server}", recs))
                log(f"  {server}: {len(recs)} of {len(raw)} in window")
                oks.append(server)
            except Exception as exc:
                errs.append(server)
                log(f"  {server}: FAILED {exc}")
        status["biorxiv"] = "ok" if not errs else (
            f"partial (failed: {','.join(errs)})" if oks else "failed")

    candidates = merge(groups, settings.get("max_total_candidates", 300))
    raw_total = sum(len(r) for _, r in groups)

    payload = {
        "run_date": end.isoformat(),
        "window": {"start": start.isoformat(), "end": end.isoformat(),
                   "lookback_days": lookback},
        "source_status": status,
        "counts": {"raw": raw_total, "deduped": len(candidates)},
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "candidates": candidates,
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    log(f"wrote {len(candidates)} candidates (from {raw_total} raw) -> {out}")

    if status and all(v.startswith("failed") for v in status.values()):
        log("all sources failed")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Merge several candidate files from scripts/fetch.py into one set.

A long backfill is retrieved in chunks (one per month) so that it is resumable
and one failure costs one month. The chunks overlap -- Europe PMC uses a wider
window than the chunk it was asked for -- so they have to be deduped against
each other before screening, or the scout pays twice for the same paper.

Usage:
    python3 scripts/merge_candidates.py --out merged.json chunks/*.json

Dedup follows the same rules as fetch.merge: ID first (PMID, then DOI), then
normalized title, since a preprint and its published version are one article.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch import norm_title  # noqa: E402


def keys_for(rec: dict) -> set[str]:
    keys = {rec.get("id", "")} | set(rec.get("alt_ids") or [])
    if rec.get("doi"):
        keys.add(f"DOI:{rec['doi']}")
    return {k.lower() for k in keys if k}


def merge_files(paths: list[Path]) -> dict:
    by_key: dict[str, dict] = {}
    by_title: dict[str, dict] = {}
    out: list[dict] = []
    windows, status, raw_total, dup = [], {}, 0, 0

    for p in sorted(paths):
        data = json.loads(p.read_text(encoding="utf-8"))
        windows.append(data.get("window") or {})
        raw_total += (data.get("counts") or {}).get("raw", 0)
        for src, st in (data.get("source_status") or {}).items():
            # Keep the worst status seen: one month's failure is not erased by
            # eleven months of success.
            if src not in status or st != "ok":
                status[src] = st

        for rec in data.get("candidates") or []:
            keys = keys_for(rec)
            hit = next((by_key[k] for k in keys if k in by_key), None)
            if hit is None:
                tkey = norm_title(rec.get("title", ""))
                hit = by_title.get(tkey) if tkey else None

            if hit is not None:
                dup += 1
                for q in rec.get("query_hits") or []:
                    if q not in hit["query_hits"]:
                        hit["query_hits"].append(q)
                for k in keys - keys_for(hit):
                    if k.upper() not in [a.upper() for a in hit["alt_ids"]]:
                        hit["alt_ids"].append(k.upper())
                if hit.get("is_preprint") and not rec.get("is_preprint"):
                    hit["is_preprint"] = False
                    hit["preprint_published"] = True
                continue

            rec = dict(rec)
            rec.setdefault("query_hits", [])
            rec.setdefault("alt_ids", [])
            rec.setdefault("preprint_published", False)
            out.append(rec)
            for k in keys:
                by_key[k] = rec
            tkey = norm_title(rec.get("title", ""))
            if tkey:
                by_title[tkey] = rec

    out.sort(key=lambda r: (r.get("date") or "", r.get("title") or ""), reverse=True)
    starts = [w.get("start") for w in windows if w.get("start")]
    ends = [w.get("end") for w in windows if w.get("end")]

    return {
        "run_date": max(ends) if ends else "",
        "window": {"start": min(starts) if starts else "",
                   "end": max(ends) if ends else "",
                   "chunks": len(paths)},
        "source_status": status,
        "counts": {"raw": raw_total, "chunk_candidates": raw_total and None,
                   "cross_chunk_duplicates": dup, "deduped": len(out)},
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "candidates": out,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("inputs", nargs="+", help="candidate JSON files to merge")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    paths = [Path(p) for p in args.inputs]
    missing = [str(p) for p in paths if not p.is_file()]
    if missing:
        sys.exit(f"missing input files: {', '.join(missing)}")

    payload = merge_files(paths)
    payload["counts"].pop("chunk_candidates", None)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
                              encoding="utf-8")
    c = payload["counts"]
    print(f"merged {len(paths)} chunks: {c['deduped']} unique candidates "
          f"({c['cross_chunk_duplicates']} cross-chunk duplicates removed), "
          f"window {payload['window']['start']} .. {payload['window']['end']}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

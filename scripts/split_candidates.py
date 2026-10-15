#!/usr/bin/env python3
"""Split a candidate set into parts for parallel screening.

A 12-month backfill holds a few thousand abstracts -- far more than one scout
run can screen. Splitting lets several scouts work at once, but they must not
each update state/seen_ids.json: concurrent writers would clobber each other
and the dedup state would silently lose ids. So each scout writes only its own
part file, and the state update happens once, afterwards, from the merged
result.

Parts are cut on month boundaries rather than by flat count, so each scout
sees a coherent slice of time and its screening log is interpretable.

Usage:
    python3 scripts/split_candidates.py --in merged.json --out-dir parts/ --parts 10
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


def split(candidates: list[dict], parts: int) -> list[list[dict]]:
    by_month: dict[str, list[dict]] = defaultdict(list)
    for c in candidates:
        by_month[(c.get("date") or "unknown")[:7]].append(c)

    months = sorted(by_month)
    target = max(1, len(candidates) // parts)
    out: list[list[dict]] = []
    cur: list[dict] = []
    for m in months:
        # Keep a month whole unless that would push the part well past target.
        if cur and len(cur) + len(by_month[m]) > target * 1.5:
            out.append(cur)
            cur = []
        cur.extend(by_month[m])
    if cur:
        out.append(cur)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--parts", type=int, default=10)
    args = ap.parse_args()

    data = json.loads(Path(args.inp).read_text(encoding="utf-8"))
    groups = split(data.get("candidates") or [], args.parts)

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for i, g in enumerate(groups, 1):
        dates = sorted((c.get("date") or "") for c in g if c.get("date"))
        payload = {
            "part": i,
            "of": len(groups),
            "run_date": data.get("run_date", ""),
            "window": {"start": dates[0] if dates else "",
                       "end": dates[-1] if dates else ""},
            "source_status": data.get("source_status") or {},
            "counts": {"candidates": len(g)},
            "candidates": g,
        }
        p = out_dir / f"part_{i:02d}.json"
        p.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
                     encoding="utf-8")
        chars = sum(len(c.get("abstract") or "") for c in g)
        print(f"{p}  {len(g):>4} candidates  {payload['window']['start']}..."
              f"{payload['window']['end']}  {chars:,} abstract chars")
    print(f"total {sum(len(g) for g in groups)} candidates in {len(groups)} parts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

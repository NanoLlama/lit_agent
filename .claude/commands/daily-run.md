---
description: Run the three-agent literature pipeline (scout -> summarizer -> strategist) for one date
argument-hint: "[YYYY-MM-DD | today] [--backfill N]"
allowed-tools: Agent, Bash, Read, Write, Glob, Grep
---

Run the daily literature pipeline.

**Arguments:** `$ARGUMENTS`

- No arguments, or `today` → use today's UTC date.
- A `YYYY-MM-DD` date → run for that date.
- `--backfill N` → see "Backfill" below.

## Steps

Set `RUN_DATE` from the arguments, then run the three agents **in order**,
passing `RUN_DATE` to each. Each stage depends on the previous stage's file, so
they cannot run in parallel.

1. **scout** — "Run the daily scout for RUN_DATE=<date>." Wait for it to write
   `data/<date>/new_articles.json`. Verify the file exists and parses as JSON
   before continuing; if it does not, stop and report rather than running the
   summarizer on nothing.

2. **summarizer** — "Write the daily brief for RUN_DATE=<date>." Verify
   `reports/<date>.md` exists.

3. **strategist** — "Fold the <date> report into the digest and update the
   experiment ideas." On a Monday, add: "Also re-rank the experiment ideas."

## Then

- Report to the user: article counts, the Top-picks titles, and anything the
  strategist flagged `[COMBINATION]`, `[CONTRADICTED]`, or `[SCOOPED]`. Keep it
  to a short block — the report file has the detail.
- Commit the run: `git add data reports digest state && git commit -m "lit: daily run <date>"`.
  Do not push unless the user asked for it.
- If any source failed, say which, once.

## Backfill

With `--backfill N`, seed the digest from the last N days instead:

- Run the **scout** once with `lookback_days=N` (override the config value for
  this run only; do not edit `config/queries.yaml`), writing to today's data
  folder.
- Run the **summarizer** once over that whole set. Title the report
  `Backfill Brief: <start> to <end>` and group Top picks by theme rather than
  listing them flat — a 30-day flat list is unreadable.
- Run the **strategist** to build the initial digest, then have it write the
  first `state_of_field_<date>.md`.

A 30-day backfill is the recommended way to start, before switching to daily.

## Notes

- Never skip the scout to "save time" — the digest's audit trail depends on
  every claim tracing back to a `data/<date>/new_articles.json` entry.
- If `reports/<date>.md` already exists, ask before overwriting. A re-run that
  silently replaces a report loses whatever a human annotated on it.

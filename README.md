# lit_agent

A three-agent Claude Code pipeline that watches the literature daily for
**antibody/nanobody cargo-delivery** work, writes a short daily brief, and
maintains a cumulative digest that proposes next experiments.

Emphasis: **increasing the amount of cargo actually delivered** — payload
capacity, transit across barriers, cellular uptake.

```
[daily trigger]
      |
      v
 scout        -- searches PubMed / Europe PMC / bioRxiv, dedupes, scores 0-5
      |          -> data/YYYY-MM-DD/new_articles.json
      v
 summarizer   -- writes the daily brief
      |          -> reports/YYYY-MM-DD.md
      v
 strategist   -- updates the running synthesis and experiment ideas
                 -> digest/cumulative.md, digest/experiment_ideas.md
```

Agents hand off through files on disk, so every run is auditable and any stage
can be re-run on its own.

## Layout

| Path | What it is |
|---|---|
| `CLAUDE.md` | Research focus and the rules every agent follows. Read first. |
| `config/queries.yaml` | Sources, search strings, filters, watchlists, run settings |
| `config/relevance_rubric.md` | The 0–5 scoring bands |
| `.claude/agents/` | The three agent definitions |
| `.claude/commands/daily-run.md` | `/daily-run` — the orchestrator |
| `scripts/fetch.py` | Stdlib + PyYAML search helper used by the scout |
| `tests/test_fetch.py` | Offline tests for the helper's parsing and dedup |
| `state/seen_ids.json` | Dedup state across runs |
| `data/`, `reports/`, `digest/` | Agent outputs, committed as the timeline |

## Getting started

```bash
# 1. Seed the digest from the last 30 days (recommended before going daily)
/daily-run --backfill 30

# 2. Then run daily
/daily-run
```

Optional: set `NCBI_API_KEY` to raise the PubMed rate limit from 3 to 10
requests/second. [Get one here](https://account.ncbi.nlm.nih.gov/settings/).

The helper can also be run directly, which is the fastest way to check whether
the queries are returning sensible volumes before spending agent turns:

```bash
python3 scripts/fetch.py --date 2026-10-15 --lookback 3 --out /tmp/c.json
python3 scripts/fetch.py --date 2026-10-15 --sources pubmed --out /tmp/c.json
python3 -I tests/test_fetch.py          # offline; no network needed
```

## Network access

The three source APIs need to be reachable: `eutils.ncbi.nlm.nih.gov`,
`www.ebi.ac.uk`, and `api.biorxiv.org`. In a cloud environment they are added
under Network access -> Allowed domains, keeping "Allow package managers"
ticked ([steps](https://code.claude.com/docs/en/cloud-environments#network-access)).
Verified working as of 2026-10-15.

Nothing is mocked: a blocked or failing source is recorded in the run's
`source_status` and in the screening log, never substituted with invented
results.

### Source quirks worth knowing

- **PubMed is searched by *entry* date** (`datetype=edat`), not publication
  date, because indexing lags publication by days to months. A paper published
  in August can legitimately turn up in today's run; its `date` field is the
  publication date, so expect dates outside the lookback window.
- **Europe PMC searches full text by default**, which floods results with
  papers that merely mention "uptake" somewhere in the body. `fetch.py`
  rewrites each query clause to `TITLE_ABS:(...)` to match PubMed's behaviour.
- **Europe PMC indexes late.** `FIRST_PDATE` returns literally nothing for the
  last few days, so the helper filters on `FIRST_IDATE` and gives this source
  its own longer window (`sources.europepmc.lookback_days`, default 10).
  Dedup makes the overlap free.
- **bioRxiv/medRxiv have no query API**, so the helper pulls the date window
  (a few hundred preprints) and filters locally on `preprint_keywords`,
  requiring both a platform term and a delivery term.

## Scheduling

Three options, in rough order of least to most setup:

- **Claude scheduled tasks** — keeps everything in the Claude app; good if you
  want the brief pushed to your phone.
- **GitHub Actions on a cron** — runs in the cloud, commits outputs back to the
  repo, so git history is the archive. Needs an API key in repo secrets.
- **Local cron or a systemd timer** — simplest if you have a machine that is
  always on.

None is wired up yet; say which you want and it can be added.

## Tuning

Expect to tune after week one. Read what the scout kept *and* dropped (the
per-run `screening_log.md` lists the drops and any query that hit its result
cap), then adjust `config/queries.yaml` and the rubric.

The known noise source is oncology ADC clinical reporting. The rubric already
caps those at 1–2 unless they address loading, uptake, or delivery mechanism,
and `filters.noise_patterns` demotes trial-readout language — tighten both if
they still flood the results.

## Design notes

- **No scoring in code.** `scripts/fetch.py` only retrieves and dedupes;
  relevance judgement is the agent's, against a rubric a human can edit and
  argue with. A keyword scorer would be cheaper and much worse.
- **Never invent a number.** Agents write "not reported in abstract" rather
  than a plausible figure. Every claim in the digest carries an article ID.
- **Preprints are labelled everywhere**, and a preprint that reaches a journal
  is flagged as an upgrade rather than silently re-reported.
- **The digest is edited, not regenerated.** Its value is the accumulated
  record of how a conclusion was reached.

## Open questions

From §8 of the plan, still unanswered — the answers mostly land in
`config/queries.yaml`:

1. Which targets/shuttles are you working on, so they get prioritized?
   (`targets_and_shuttles` currently lists the generic brain-shuttle set.)
2. Which cargo types matter most — proteins/enzymes, oligonucleotides, small
   molecules, imaging agents?
3. Which barriers or tissues — blood-brain barrier, tumor, intracellular only?
4. Include patents (Google Patents / Lens.org)?
5. Where should the daily report land — repo file only, email, push?
6. Any labs or journals to track regardless of keyword match?
   (`watchlists` in the config is empty and ready for them.)

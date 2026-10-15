# Daily Literature Agent — Project Context

Read this file before doing anything in this repo. It is the shared context for
all three agents (scout, summarizer, strategist).

## Research focus

Antibody- and nanobody-based systems for **carrying cargo**, with emphasis on
**increasing the amount of cargo actually delivered** — transit across
barriers, cellular uptake, and payload capacity per targeting molecule.

Concretely, we care about:

- **Loading**: drug-to-antibody ratio (DAR), site-specific conjugation,
  multi-payload and branched linkers, carrier formats that raise cargo per
  targeting unit.
- **Transit**: receptor-mediated transcytosis, blood-brain barrier shuttles,
  FcRn-mediated recycling and transport, epithelial transport.
- **Uptake and fate**: receptor-mediated endocytosis efficiency, endosomal
  escape, lysosomal sorting and degradation, recycling vs. degradative routes.
- **Design levers**: valency, avidity, affinity tuning, format (VHH, scFv,
  bispecific, fusion, nanoparticle-displayed).

Cargo types of interest: proteins/enzymes, oligonucleotides (siRNA, ASO),
small molecules, imaging agents.

## What is *not* the focus

- Pure oncology ADC clinical efficacy reporting with no delivery/loading
  mechanism content (this is the main noise source — downweight it).
- Antibody discovery, affinity maturation, or humanization with no cargo angle.
- Diagnostics, in vitro assays, and structural work with no delivery angle.
- Case reports, editorials, and (by default) reviews. Reviews are kept in a
  separate low-priority bucket, never in Top picks.

## Pipeline

```
[trigger] -> scout -> summarizer -> strategist
```

| Agent | Reads | Writes |
|---|---|---|
| scout | `config/queries.yaml`, `config/relevance_rubric.md`, `state/seen_ids.json` | `data/YYYY-MM-DD/new_articles.json`, `state/seen_ids.json` |
| summarizer | `data/YYYY-MM-DD/new_articles.json` | `reports/YYYY-MM-DD.md` |
| strategist | today's report, `digest/cumulative.md`, `digest/experiment_ideas.md` | both digest files |

Agents hand off through files on disk. Nothing is passed in memory, so every
run is auditable and any stage can be re-run alone.

## Hard rules for every agent

1. **Never invent a number.** Every fold-change, DAR, %ID/g, or concentration
   must be traceable to an abstract or open-access full text. If a number is
   not stated, write "not reported in abstract".
2. **Every claim carries an article ID** (PMID or DOI) so a human can check it.
3. **Do not edit another agent's output files.** Scout does not touch reports;
   summarizer does not touch the digest.
4. **Date is always the run date in `YYYY-MM-DD`** (UTC) and is passed down the
   pipeline unchanged.
5. **Experiment ideas are discussion prompts, not instructions.** They get
   verified by a human against the primary papers before anyone acts on them.
6. Mark preprints as preprints, everywhere they appear.

## Conventions

- Dates: ISO `YYYY-MM-DD`.
- IDs: `PMID:12345678` for PubMed, `DOI:10.1101/...` otherwise. Prefer PMID
  when both exist.
- JSON files: 2-space indent, UTF-8, newline at EOF.
- Commit the outputs. Git history is the timeline of how the digest evolved.

## Tooling notes

- `scripts/fetch.py` is a plain-stdlib helper that queries PubMed, Europe PMC,
  and bioRxiv/medRxiv and emits candidate records. The scout may use it or make
  the HTTP calls itself; the helper exists so screening does not burn tokens on
  boilerplate.
- `NCBI_API_KEY` in the environment raises the PubMed rate limit from 3 to 10
  requests/second. Optional.
- Outbound HTTPS goes through the environment's proxy; use the system CA bundle
  and do not disable TLS verification.

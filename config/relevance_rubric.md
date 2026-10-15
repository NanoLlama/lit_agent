# Relevance Rubric

Scored by the scout, 0–5, from title + abstract only. Keep **3 and above**.

The question every score answers: *does this change what we would build or test
to get more cargo delivered?*

## Bands

### 5 — Directly on thesis, with numbers
Reports a method, format, or design change that **increases the amount of cargo
delivered** — per targeting molecule, per cell, or across a barrier — and gives
quantitative evidence.

Signals: fold-change in uptake or transcytosis; DAR raised without loss of
binding or PK; %ID/g or brain/plasma ratio; measured intracellular cargo;
payload copies per molecule; delivered-enzyme activity.

### 4 — Novel platform or chemistry, relevant to loading or uptake
A new nanobody/antibody delivery platform, shuttle, carrier format, or
conjugation chemistry whose relevance to loading or uptake is clear, even if
the cargo-amount comparison is incomplete or qualitative.

Signals: new shuttle receptor or epitope; new site-specific conjugation
handle; branched/dendrimer/polymer linker; antibody-displayed nanoparticle or
vesicle; new valency architecture.

### 3 — Mechanistic insight that could inform design
Trafficking, transcytosis, endosomal escape, or receptor-biology work with no
delivery construct of its own, but with a usable design implication.

Signals: sorting determinants between recycling and degradation; affinity vs.
transcytosis relationships; receptor density or turnover measurements;
endosomal escape mechanisms.

### 2 — Tangential
Same target, tissue, or barrier but a different modality (peptide, AAV, LNP
without antibody targeting); or antibody engineering with no cargo angle. Also
the ceiling for **reviews** — a review never scores above 2, no matter how
on-topic, and never enters Top picks.

### 0–1 — Off-topic
No antibody/nanobody, or no delivery/cargo/uptake content. Clinical efficacy
reporting with no mechanism. Diagnostics. Case reports.

## Tie-breaking

When an article sits between two bands:

- **Quantitative cargo-amount comparison present** → take the higher band.
- **No construct and no measurement, only speculation** → take the lower band.
- Matches a `queries.yaml` watchlist → floor of 3, tagged `watchlist`.
- Matches a `noise_patterns` entry and has no loading/uptake/transit content
  → start one band lower.
- Preprint vs. published is **not** a scoring factor. Score the content; flag
  the status.

## Noise guard

Oncology ADC papers are the dominant false positive. An ADC paper scores ≥4
only if it addresses **loading, uptake, or intracellular delivery mechanism**.
A trial readout, a survival analysis, or a new target with a stock vedotin
payload is a 1 or 2.

## Writing `relevance_reason`

One sentence, ≤25 words, naming the specific delivery-relevant finding — not a
restatement of the title.

- Good: "Branched linker reaches DAR 8 with unchanged clearance in mice; direct
  read on cargo-per-antibody limits."
- Good: "Maps TfR affinity window where transcytosis peaks before lysosomal
  sorting dominates."
- Bad: "Paper about nanobody delivery." (says nothing)
- Bad: "Could be relevant to our work." (says nothing)

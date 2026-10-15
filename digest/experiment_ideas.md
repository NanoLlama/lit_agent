# Experiment Ideas

Maintained by the **strategist** agent. Re-ranked weekly.

> These are **discussion prompts, not protocols.** Every one needs verifying
> against the primary papers before anyone sets up a bench experiment. The
> motivation citations are the starting point for that check. Nothing here is
> a finding; findings live in `digest/cumulative.md`.

IDs are stable and never reused or renumbered. Statuses: `new`, `refined`,
`tested`, `scooped`, `dropped`.

Flags: **`[COMBINATION]`** joins findings from two or more papers that did not
cite each other (most likely to be novel) · **`[CONTRADICTED]`** premise
undercut by newer work · **`[SCOOPED]`** essentially done by someone else ·
**`[SCOOPED, PARTIAL]`** the headline claim is published but a stated part
remains open, so the idea is narrowed rather than dropped.

> **Caveat on the `[COMBINATION]` flag after the 12-month rebuild.** Everything
> here is screened from abstracts; reference lists were not fetched. Where a
> combination joins two papers in literatures that routinely cite each other
> (e.g. two TfR1 shuttle papers), the flag is stated as **unverified** and the
> human check should include looking at whether one cites the other. Where it
> joins clearly separate literatures (e.g. solid-tumour ADC penetration and BBB
> shuttle engineering), non-citation is likely but still unverified.

---

## Current ranking

**Ranked 2026-10-15 (second ranking, after the 12-month rebuild.** The first
ranking, from the 30-day seeding run, is kept below for the record.)
Criteria in order: direct read on cargo amount > mechanistic leverage >
novelty > feasibility.

| Rank | ID | Idea | Status | Difficulty |
|---|---|---|---|---|
| 1 | 11 | Valency × affinity matrix re-run with the cargo attached [COMBINATION] | new | high |
| 2 | 10 | Is the DAR turnover the avidity turnover? [COMBINATION] | new | med |
| 3 | 15 | Three loading platforms normalised per mg antibody [COMBINATION] | new | high |
| 4 | 6 | Site-specific attachment of a high-copy payload backbone [COMBINATION] | refined | med |
| 5 | 3 | Multi-payload loading turnover on a VHH [SCOOPED, PARTIAL] | refined | high |
| 6 | 16 | HALA co-dosing applied to a brain shuttle [COMBINATION] | new | med |
| 7 | 13 | Cytosolic fraction as the reported quantity | new | med |
| 8 | 12 | Anchor-stability-corrected antibody-LNP comparison [COMBINATION] | new | low |
| 9 | 5 | pIgR-directed siRNA conjugate for airway epithelium [COMBINATION] | refined | high |
| 10 | 7 | Pretargeting vs direct display, cargo per targeting molecule [COMBINATION] | refined | high |
| 11 | 14 | Is binding-to-release immune to internalization-blocking resistance? [COMBINATION] | new | med |
| 12 | 2 | Affinity tuning to reduce lysosomal sorting [SCOOPED, PARTIAL] | refined | med |
| 13 | 1 | Valency vs transcytosis at matched affinity [SCOOPED, PARTIAL] | refined | med |
| 14 | 8 | TfR1 VHH clones classified by trafficking route [SCOOPED, PARTIAL] | refined | med |
| 15 | 4 | Co-delivered endosomal escape enhancers [SCOOPED, PARTIAL] | refined | med |
| 16 | 9 | Targeting-ligand *ratio* on co-display LNPs | refined | low |

**Why the top three are top.** All three are direct reads on delivered cargo
amount rather than on a surrogate, which is the gap the year's own
normalisation pass quantified — 12 papers demoted from score 4 to 3 for having
no delivered-cargo measurement [2026-10-15 · cumulative §6]. **Idea 11** is top
because it resolves a live conflict (does bivalent really match monovalent
[cumulative §6], and does cargo conjugation erase that conclusion) with brain
cargo mass as the endpoint, which nobody in the year reports. **Idea 10** is
second because it proposes a single mechanism — excess-avidity receptor
degradation, measured on nanoparticles [PMID:41834375] — for the otherwise
unexplained DAR4 ≈ DAR8 free-payload equality [PMID:41927976], so one
experiment both explains a conflict and yields a payload number. **Idea 15** is
third because cargo per mg of antibody is literally the project's thesis
variable and three published platforms claim it in mutually incomparable units.

Ideas 1-4 were seeds written before this pipeline had read any literature.
They were first reality-checked on the 30-day run and re-examined against the
year on 2026-10-15; **all four are now at least partly scooped**, and all four
are kept with narrowed scope. See their Notes.

**Previous ranking (30-day seeding run, 2026-10-15), kept for the record:**
6, 3, 8, 5, 1, 7, 2, 4, 9.

---

### 1. Valency vs. transcytosis at matched affinity — [SCOOPED, PARTIAL]
- **Hypothesis (narrowed 2026-10-15, year rebuild):** At matched *cell-surface*
  binding strength, the monovalent-vs-bivalent choice changes **delivered cargo
  mass** in the brain even though it does not change brain uptake of the naked
  construct.
- **Test:** Monovalent vs bivalent constructs against one shuttle receptor at
  one epitope, matched by measured cell-surface binding strength (the published
  matching criterion) *and* separately by monomeric SPR affinity — the two are
  not the same control, and which one you match determines what the result
  means. Both arms carry an identical quantifiable cargo.
- **Readout:** Delivered cargo mass per dose in brain parenchyma (cargo-specific
  assay, e.g. hybridisation ELISA for an oligonucleotide), with
  parenchyma-vs-capillary separation; surface vs internalized receptor by flow
  cytometry; reticulocyte count as the published safety axis.
- **Motivation:** seed idea. 30-day check: no matched-affinity comparison found.
  **Year check: largely answered for uptake.** A systematic scan varied affinity
  and valency on two anti-TfR1 antibodies with distinct epitopes and pH
  sensitivities and found bivalent "equally effective in brain uptake as
  monovalent antibodies if engineered to have similar cell-surface TfR1 binding
  strength, with prolonged brain exposure and less severe adverse effects",
  explicitly challenging monovalent superiority
  [2026-10-15 · PMID:41287279]. Context: fast-dissociating intermediate-affinity
  monovalent VHHs linked to efficient transcytosis
  [2026-10-15 · PMID:41110474]; affinity-dependent valency effects on VHH PK
  with a ~100 nM threshold [2026-10-15 · PMID:41599718].
- **Difficulty:** med
- **Status:** refined
- **Notes:** 2026-10-15 seeded. 2026-10-15 (30-day) first reality check: the
  matched-affinity comparison was not found, so the idea stood; two
  refinements added — (a) rigidity/spacing of multivalent display may carry the
  effect, not valency count alone [PMID:42766830]; (b) epitope should be held
  constant or it will confound [PMID:42855849].
  **2026-10-15 (year rebuild) judgment: partially scooped, and the honest
  reading is that the headline is gone.** Stated plainly for checking against
  the primary paper:
  - *Scooped:* "does valency matter at matched binding, for an antibody shuttle"
    is published for TfR1 brain uptake, in a design that also varies epitope and
    pH sensitivity — a better experiment than the one proposed here
    [PMID:41287279]. Proposing to show valency can be separated from affinity is
    no longer a contribution.
  - *Also vindicated:* the 30-day refinement that epitope must be controlled is
    exactly what that paper reports ("epitope, as well as affinity and valency,
    factors into selecting a shuttle").
  - *Still open:* (i) **no cargo.** The scan's readouts are brain uptake and
    reticulocyte depletion; the normalisation pass demoted it 4→3 for having no
    stated delivery figure [cumulative §6]. (ii) **Antibody formats only** — the
    VHH/nanobody case is untested. (iii) **Matched surface binding ≠ matched
    monomeric affinity**; a bivalent construct tuned down to match surface
    binding has a different off-rate landscape, and which control is right is
    an open design question.
  - *Net:* keep, rank lowered, and note that idea **11** is the better successor
    — it takes this comparison and adds the cargo, which is the part left open.

### 2. Affinity tuning to reduce lysosomal sorting — [SCOOPED, PARTIAL]
- **Hypothesis (narrowed 2026-10-15, year rebuild):** Net **delivered cargo**
  peaks at intermediate affinity, and the falling arm at high affinity is
  caused by receptor degradation/lysosomal sorting rather than by reduced
  release.
- **Test:** An affinity ladder (ideally single-residue variants on one scaffold
  and one epitope) against one receptor, each variant carrying an identical
  cargo, measuring capture, surface receptor loss and delivered cargo in
  parallel. Run an epitope arm alongside, or a flat ladder will be
  over-interpreted as "affinity does not matter".
- **Readout:** Delivered cargo (mass or activity) per dose; surface receptor
  level after exposure; colocalization with LAMP1 vs recycling markers.
- **Motivation:** seed idea. **Year check: the trend part is published from at
  least four directions.** Transcytosis and receptor degradation were trended
  against affinity and connected to in-vivo brain uptake
  [2026-10-15 · PMID:41287279]; excess ligand density on VHH-LNPs induced
  receptor degradation and produced a bell-shaped delivery optimum at
  ~0.1 VHH/100 nm² [2026-10-15 · PMID:41834375]; MD predicted strong Fab
  affinity correlates with poor internalization
  [2026-10-15 · DOI:10.64898/2026.03.13.711720, PREPRINT]; VHH PK stopped
  improving below a ~100 nM affinity threshold
  [2026-10-15 · PMID:41599718]. Counter-evidence that the optimum is not
  universal: picomolar anti-TfR1 nanobodies crossed the BBB in humanized rats
  [2026-10-15 · PMID:41462276]. Engineerability of lysosomal routing:
  [2026-10-15 · PMID:41887220] [2026-10-15 · PMID:42816619].
- **Difficulty:** med
- **Status:** refined
- **Notes:** 2026-10-15 seeded. 2026-10-15 (30-day) first reality check:
  premise not contradicted and not tested; the month's evidence pointed at
  epitope and binding geometry rather than affinity as the lever being pulled
  (PMID:42816619, DOI:10.64898/2026.09.11.750848), and PMID:42855849 showed
  routing differences with no affinity difference reported; refinement was to
  run an epitope arm alongside the ladder.
  **2026-10-15 (year rebuild): partially scooped on the trend, still open on
  the quantity.** What broke: "affinity trades off against degradative sorting"
  is no longer a hypothesis — it is reported, with a named mechanism
  (excess-avidity receptor degradation) on a nanoparticle [PMID:41834375] and
  trended on an antibody shuttle [PMID:41287279]. What remains: **nobody plots
  delivered cargo against affinity.** Every curve in the year is uptake,
  transfection, potency or PK. Also newly relevant, and a reason the ladder
  must carry cargo: ASO conjugation itself *moves* apparent affinity in opposite
  directions for high- and low-affinity shuttles [PMID:42332368], so a naked
  ladder may not be the ladder you dose. Keep; rank lowered; see idea 11, which
  folds this concern in.

### 3. Multi-payload linkers without losing receptor engagement — [SCOOPED, PARTIAL]
- **Hypothesis (re-narrowed 2026-10-15, year rebuild):** On a *nanobody*
  scaffold, delivered payload per dose turns over somewhere between 8 and ~60
  copies per molecule, and the turnover is set by clearance and
  surface-receptor loss rather than by loss of binding affinity.
- **Test:** One site-specific conjugation handle on one VHH, a
  payload-per-molecule series spanning the 1-8 range (where the answer is now
  partly known) and the 8-60 range (where it is not). The control that makes it
  interpretable is a copy-number series on the *same* binder, since the
  published high-DAR result changes backbone and loading at once.
- **Readout:** Cargo copies per molecule (MS), retained binding affinity,
  uptake per cell, clearance, **and** intratumoral free payload — the published
  work does not report the last two together with the first.
- **Motivation:** seed idea, anchored and then re-anchored. High loading:
  DAR 61 polypeptide backbone with retained binding, endocytosis and
  subnanomolar activity [2026-10-15 · PMID:42819270]; DAR 8 past a cited DAR 4
  ceiling with an unmodified payload [2026-10-15 · PMID:41558564]; DAR ~23
  polymer conjugate at 210-fold lower IC50 than mirvetuximab soravtansine in
  vitro [2026-10-15 · PMID:42570634]; DAR 7.92 exatecan at <1% aggregation
  [2026-10-15 · PMID:42296596]. The DAR>1 oligonucleotide penalty and its fixes
  [2026-10-15 · DOI:10.64898/2026.09.23.753708, PREPRINT]
  [2026-10-15 · PMID:42612014]. Turnover evidence: DAR4 ≈ DAR8 in intratumoral
  free payload and efficacy, DAR4 penetrating better
  [2026-10-15 · PMID:41927976]; site-specific DAR 4 beating cysteine DAR 8 in
  vivo [2026-10-15 · PMID:41799094]. Nanobody copy-number series:
  VHHkappa-Zan1/2/4, 4-copy ~10-fold more potent in influenza protection
  [2026-10-15 · PMID:41183201]. Site-specific handle, probes/PEG only
  [2026-10-15 · PMID:42809913].
- **Difficulty:** high
- **Status:** refined
- **Notes:** 2026-10-15 seeded. 2026-10-15 (30-day) judgment: partially
  scooped — the headline that copies can be raised past DAR 2-8 with retained
  binding is done (PMID:42819270); the DAR1→DAR2 oligonucleotide penalty and
  its chemical fix are answered (DOI:…753708); still open were (i) where the
  curve turns over, (ii) the four readouts together, (iii) the nanobody
  scaffold, (iv) site-specificity with a real payload.
  **2026-10-15 (year rebuild): more of it is scooped, and the remainder is
  sharper.**
  - *Newly scooped, (i) in part:* the curve **does** turn over, and it turns over
    earlier than expected. DAR4 and DAR8 gave equal intratumoral free payload
    and equal efficacy at dose-matched payload, with DAR4 penetrating better
    [PMID:41927976]; site-specific DAR 4 beat cysteine DAR 8 in vivo
    [PMID:41799094]. "Where does it turn over" is answered for one payload
    class in the 4-8 window.
  - *Newly scooped, (iii) in part:* a **nanobody** copy-number series exists —
    1, 2 and 4 site-specific zanamivir copies on a VHH, with the 4-copy adduct
    ~10-fold more potent [PMID:41183201]. It stops at 4 copies and reports
    protection potency, not delivered mass.
  - *Still open:* the **8-to-60 range on any scaffold with a delivered-payload
    readout**, and the whole range on a VHH where the absent Fc makes the
    clearance penalty of a large payload backbone the likely limiter. Nobody
    has reported copies, affinity, uptake per cell, clearance and free payload
    together.
  - *Net:* keep, narrowed to the 8-60 range on a VHH with free-payload
    measurement. Drop any framing that treats high loading, or the existence of
    a turnover, as novel.

### 4. Co-delivered endosomal escape enhancers — [SCOOPED, PARTIAL]
- **Hypothesis (narrowed 2026-10-15, year rebuild):** For protein and
  oligonucleotide cargo, the escaped fraction of internalised cargo is the
  dominant loss term, and an escape enhancer moves that **ratio** rather than
  total uptake.
- **Test:** Nanobody-cargo conjugate with and without an escape agent, with a
  cytosolic functional readout **and** total uptake measured on the same
  samples so the ratio is the reported quantity. Include a
  lipid-modified-payload arm, since lipid modification is a plausible competing
  explanation. Controls: conjugate without cargo (for enhancer toxicity), and
  an enhancer-free arm at matched total uptake.
- **Readout:** Cytosolic-activity reporter (split-enzyme complementation,
  knockdown for siRNA, editing for Cas9) **divided by** total internalised
  cargo — reported as a fraction, not a fold-change.
- **Motivation:** seed idea. 30-day check: **no paper measured escape at all.**
  **Year check: escape work exists, and one instance is close to this idea.** A
  Staufen1 dsRBD34 bifunctional antibody carrying siRNA at 1:1 had its silencing
  potency augmented **seven-fold (IC50 200 → 28 nM)** by small-molecule
  enhancers on the siRNA terminus, attributed to endosome-to-cytosol import;
  the same paper reports that 32-fold higher dsRBD-siRNA affinity gave neither
  stronger silencing nor better stability, and that circulating sulfated GAGs
  altered PK enough to block in-vivo assessment
  [2026-10-15 · PMID:41569158]. Antibody-CPP-cargo trifunctional conjugates
  showed escape by imaging plus Cas9 editing, cell models only
  [2026-10-15 · PMID:41208769]. Antibody-as-cargo escape via an acid-triggered
  buffering nanocarrier [2026-10-15 · EPMC:AGR/IND609298393]. Nuclear delivery
  by a cell-penetrating anti-DNA antibody
  [2026-10-15 · PMID:41127334].
- **Difficulty:** med
- **Status:** refined
- **Notes:** 2026-10-15 seeded. 2026-10-15 (30-day) first reality check:
  nothing tested it and the absence was itself notable; refinements were (a)
  scope the premise to protein and oligonucleotide cargo, since a cleavable
  small-molecule payload acted without internalization
  (DOI:10.64898/2026.10.09.757939, preprint), and (b) include a
  lipid-modified-payload arm so lipid effects and escape effects stay
  separable.
  **2026-10-15 (year rebuild): partially scooped.** The enhancer concept is
  published on an antibody-siRNA system with a 7-fold number
  [PMID:41569158] — but the enhancer was **covalently on the cargo**, not
  co-delivered, and the paper reports a potency shift, not an escaped fraction.
  **Still open, and now the more interesting half:** no paper in 225 reports
  escaped cargo as a fraction of internalised cargo [cumulative §4, §6]. The
  idea survives by moving its readout from "does an enhancer help" to "what
  fraction escapes" — which is now spun out as idea **13**, with this idea
  retained as the intervention arm of it. The internalization-independent
  payload caveat is reinforced by PhoPEx binding-to-release
  [PMID:42649302]: for cleavable small molecules this premise may not apply at
  all.

### 5. pIgR-directed siRNA conjugate for airway epithelium — [COMBINATION]
- **Combines:** pIgR transit results — bispecifics enriching 5-10-fold in cyno
  bronchoalveolar lavage fluid with rapid serum clearance
  [2026-10-15 · PMID:42829333] and **stem-zone** nanobodies (HDX-MS epitope
  residues 578-612, distinct from the dIgA site) giving apical-to-basolateral
  Transwell transport and inhaled efficacy at one-tenth the IP reslizumab dose
  [2026-10-15 · PMID:42496279] — with AOC chemistry that doubles siRNA per
  antibody (C16 lipid at DAR2) and shifts silencing extrahepatically via a
  charge-balancing ionizable linker
  [2026-10-15 · DOI:10.64898/2026.09.23.753708, PREPRINT]. The pIgR papers are
  transit results with no oligonucleotide cargo; the AOC preprint is a
  loading/cargo result with no epithelial barrier. Citation relationship
  unverified, but the two literatures are separate.
- **Hypothesis:** A pIgR-stem-binding nanobody carrying C16-modified siRNA at
  DAR2 delivers more functional siRNA to airway epithelium per mg of targeting
  protein than a non-pIgR isotype/format-matched conjugate, and the rapid serum
  clearance of pIgR engagement raises rather than lowers that ratio.
- **Test:** pIgR-targeting vs non-targeting conjugate, both at DAR2-C16, dosed
  at matched **siRNA** dose (matched siRNA, not matched protein, is what
  isolates targeting from loading). A DAR1-C16 pIgR arm separates the loading
  contribution from the targeting contribution. Inhaled and systemic arms, since
  the stem-zone work is inhaled and the bispecific work is systemic. **Added
  2026-10-15 (year):** characterise binding *after* conjugation, not before.
- **Readout:** Target-transcript knockdown in airway epithelium (% vs control),
  with siRNA mass in lung and serum over time, per mg of targeting protein
  dosed.
- **Motivation:** [2026-10-15 · PMID:42829333] +
  [2026-10-15 · PMID:42496279] +
  [2026-10-15 · DOI:10.64898/2026.09.23.753708] (+ binding caveat:
  [2026-10-15 · PMID:42332368]; pH-off-rate design input:
  [2026-10-15 · PMID:41737496])
- **Difficulty:** high
- **Status:** refined
- **Notes:** 2026-10-15 created. Species was the main obstacle — the bispecific
  result is cyno, and the pIgR paper reports lavage fluid, not tissue, so
  "reaches epithelium" was an inference needing checking.
  **2026-10-15 (year rebuild): strengthened, and the obstacle is smaller.** The
  year adds a mouse-model pIgR result with a defined stem-domain epitope and an
  inferred ~10-fold dose-sparing [PMID:42496279], plus an in-vitro
  structure-activity handle (faster acidic-pH off-rate correlates with pIgR
  transcytosis [PMID:41737496]). Two new caveats to carry in: the 10-fold is
  **inferred from efficacy, not measured mass** (the paper says so), and ASO/siRNA
  conjugation has been shown to shift shuttle avidity in opposite directions
  depending on starting affinity and to delay transcytosis in a different
  receptor system [PMID:42332368] — so the conjugate's binding and transcytosis
  must be re-measured, not assumed from the naked nanobody.

### 6. Site-specific attachment of a high-copy payload backbone — [COMBINATION]
- **Combines:** a click-chemistry polypeptide backbone reaching DAR 61 with
  binding and endocytosis retained [2026-10-15 · PMID:42819270], and an
  engineered transglutaminase that conjugates trastuzumab Q295 despite N297
  glycan hindrance at 3.6-fold wild-type activity, tested only with probes and
  PEG [2026-10-15 · PMID:42809913]. One solves "how many", the other "exactly
  where". Citation relationship unverified.
- **Hypothesis:** Anchoring the high-copy polypeptide backbone at a single
  defined site gives the same payload copies per antibody as stochastic
  attachment but with narrower species distribution and slower clearance, so
  more payload is actually delivered per dose.
- **Test:** Same backbone and same nominal copy number, attached
  site-specifically (Q295, or the Q295+N297 dual-site route) vs stochastically,
  on the same antibody. The interpretable control is a copy-number-matched pair
  verified by MS rather than assumed from reaction stoichiometry.
- **Readout:** Copies per antibody and species-distribution width (MS),
  retained affinity, plasma clearance, and payload mass delivered to target
  tissue per dose (free payload by MALDI-IMS or tumour-lysate quantification).
- **Motivation:** [2026-10-15 · PMID:42819270] +
  [2026-10-15 · PMID:42809913] + (year) a two-site enzymatic route at Q295 and
  N297 [2026-10-15 · PMID:42227168], and direct evidence that attachment
  geometry can outweigh copy number — site-specific Fc N-glycan DAR 4 beat
  cysteine DAR 8 in vivo [2026-10-15 · PMID:41799094], and a supramolecular
  site-specific MMAE ADC beat higher-loaded cysteine ADCs on survival
  [2026-10-15 · PMID:42620052, PREPRINT]. Watch-out: an sdAb site-specific vs
  random comparison found **comparable** tumour uptake (3.7 vs 3.4 %IA/g), the
  gain being reduced kidney retention
  [2026-10-15 · DOI:10.21203/rs.3.rs-9664465/v1, PREPRINT]. Artifact watch:
  "phantom DAR" from iminothiolane lysine chemistry
  [2026-10-15 · PMID:41391917].
- **Difficulty:** med
- **Status:** refined
- **Notes:** 2026-10-15 created; closest thing on the list to
  tractable-and-direct, since both reagents are published and the readout is a
  cargo amount. PMID:42809913's authors state their enzyme is not validated
  with cytotoxic payloads, so payload compatibility is the first thing to
  check; a non-cytotoxic payload could de-risk it. Related to idea 3 but
  distinct: idea 3 asks where loading turns over, this asks whether attachment
  geometry moves the turnover point.
  **2026-10-15 (year rebuild): not scooped, and better supported.** The premise
  that geometry moves delivered payload now has two in-vivo instances
  (PMID:41799094, PMID:42620052) and a two-site enzymatic option
  (PMID:42227168). One honest discount: the sdAb radiolabel comparison
  (rs-9664465) found site-specificity bought cleaner biodistribution rather than
  more delivered cargo, so "narrower species distribution → more delivered
  payload" should be treated as the thing being tested, not assumed.

### 7. Pretargeting vs direct display: cargo per targeting molecule — [COMBINATION]
- **Combines:** pretargeting, where a pre-dosed antibody acts as a docking site
  for later-infused particles so one antibody can in principle recruit many —
  now with a clean quantified instance, an anti-EGFR/anti-PEG bispecific that
  **more than tripled** tumour retention of a 212Pb nanocarrier versus the
  untargeted nanomaterial by SPECT and gamma counting
  [2026-10-15 · PMID:41687816] — and direct click display of a nanobody on
  LNPs [2026-10-15 · PMID:42764379]. Same underlying trick (an affinity/click
  handle on a particle) in opposite architectures; citation relationship
  unverified.
- **Hypothesis:** For a given number of targeting molecules, two-step
  pretargeting delivers more cargo per targeting molecule than one-step direct
  display, because each docked antibody can capture multiple particles.
- **Test:** Same cell target and same cargo, comparing (a) binder directly
  displayed on the particle and (b) bispecific or handle-modified binder
  pre-dosed then particle infused — **normalized to targeting molecules used,
  not to particles used.** Controls: particle with no pre-dosed binder, and
  pre-dosed binder with a non-capturable particle, to show the capture step is
  doing the work. Hold lipid/polymer composition constant across arms.
- **Readout:** Cargo delivered (mass, %ID/g, or transfected/edited cells) per
  nmol of targeting molecule, plus particle association per cell.
- **Motivation:** [2026-10-15 · PMID:41687816] +
  [2026-10-15 · PMID:42764379] (+ TCO/tetrazine pretargeting chemistry
  [2026-10-15 · PMID:41705578] [2026-10-15 · PMID:41449469]
  [2026-10-15 · PMID:41198055]; superseded motivation
  [2026-10-15 · PMID:42839730])
- **Difficulty:** high
- **Status:** refined
- **Notes:** 2026-10-15 created. The amplification claim is the attractive part
  and is exactly what the host-guest pretargeting abstract did not quantify (no
  fold-enrichment, no %ID/g); two-step dosing in vivo adds a timing variable to
  hold constant.
  **2026-10-15 (year rebuild): the confound is gone and the idea is cleaner.**
  The year's anti-EGFR/anti-PEG bispecific result [PMID:41687816] replaces the
  host-guest CB[7] paper as the pretargeting arm: it has a real number (>3-fold
  retention) and none of the NLG919-lipid/cytokine-cargo confounding that made
  PMID:42839730 uninterpretable for this purpose. **Still open and still the
  whole point:** that number is versus an *untargeted nanomaterial*, not versus
  direct display, and nothing in the year normalises delivery per targeting
  molecule. Also note PMID:41705578 reports the opposite tradeoff within
  pretargeting itself (highest stochastic loading gave top tumour uptake at
  10.4 %ID/g, site-specific gave better tumour-to-blood), which is worth folding
  into the design.

### 8. Classify TfR1 VHH clones by trafficking route, with a cargo number — [SCOOPED, PARTIAL]
- **Hypothesis:** Clone-level divergence in brain localization is a trafficking-
  route difference (degradative vs recycling/transcytotic) measurable in a
  live-cell assay, and that route assignment predicts which clone delivers more
  parenchymal cargo.
- **Test:** Run clones through live-cell endocytosis and lysosomal-routing
  readouts in brain endothelial cells, then dose both with an identical
  quantifiable cargo in vivo. The control that makes it interpretable is
  capillary depletion (or equivalent) to separate parenchymal from
  vessel-associated signal.
- **Readout:** Surface vs internalized vs lysosomal receptor fraction in vitro;
  parenchymal cargo as %ID/g and parenchyma-to-capillary ratio in vivo.
- **Motivation:** [2026-10-15 · PMID:42855849] (30-day set; **not in the
  12-month kept set**) + [2026-10-15 · PMID:42816619]. Year additions:
  quantitative transcytosis plus imaging-based intracellular-trafficking assays
  in brain endothelial cells, built and applied to TfR1 shuttle variants
  [2026-10-15 · PMID:42332368]; in-vitro transcytosis and receptor degradation
  connected to in-vivo brain uptake across an affinity/valency/epitope panel
  [2026-10-15 · PMID:41287279].
- **Difficulty:** med
- **Status:** refined
- **Notes:** 2026-10-15 created; was ranked 3rd for mechanistic leverage, on
  the argument that if route predicts parenchymal delivery then clone screening
  gets a cheap in-vitro surrogate. Caveat flagged then: the clones' affinities
  are reported only as ">100 nM" for all three, so they may not be
  affinity-matched.
  **2026-10-15 (year rebuild): partially scooped, and the mechanistic-leverage
  argument is weakened.** Two papers have now built the in-vitro route assays
  and connected them to in-vivo brain uptake across a designed panel
  [PMID:42332368, PMID:41287279] — i.e. the "cheap in-vitro surrogate" is
  substantially established, which removes the novelty that put this idea
  third. **Still open:** the cargo number and the capillary-depletion control
  are absent from both (PMID:41287279 was demoted 4→3 for having no stated
  delivery figure; PMID:42332368 is in vitro only and was demoted for the same
  reason). Also note the motivating clone paper (PMID:42855849) is not in the
  12-month kept set [cumulative §6, cross-run discrepancy], so its result should
  be re-verified before being used as a premise.

### 9. Targeting-ligand *ratio* on co-display LNPs
- **Hypothesis (narrowed 2026-10-15, year rebuild):** On an LNP co-displaying
  two different targeting antibodies, cargo delivered per cell depends on the
  **ratio** of the two ligands, with an optimum away from 1:1, *separately from*
  total ligand density — whose optimum is now published.
- **Test:** A ratio series at **fixed total functional-ligand density set at the
  published optimum**, plus a density series at fixed ratio. The two series
  together separate ratio from density. Single-ligand and non-conjugated LNPs
  as controls. Quantify *functional* ligands per particle rather than input
  stoichiometry.
- **Readout:** Cargo delivered per cell type (% transfected / % CAR-positive)
  and particles associated per cell, by flow cytometry, for each cell type
  addressed; surface receptor level after exposure, since excess avidity
  degrades the receptor.
- **Motivation:** [2026-10-15 · DOI:10.64898/2026.09.21.753074, PREPRINT] +
  [2026-10-15 · PMID:42764379] (shared click handle chemistry). Year additions
  that supply the method and the density answer: bell-shaped density optimum at
  ~0.1 VHH/100 nm² with single-particle nanoflow quantification of functional
  ligands, and receptor degradation at excess density
  [2026-10-15 · PMID:41834375]; antibody-per-particle tuning at ~340/760/1200
  with the lowest density best for uptake and bone-marrow accumulation
  [2026-10-15 · PMID:42160160].
- **Difficulty:** low
- **Status:** refined
- **Notes:** 2026-10-15 created. Cheapest on the list, ex vivo throughout, but
  the weakest read on *amount* of cargo per targeting unit, so it ranked last
  despite being easy; the co-display preprint reports no fold-change, so the
  baseline must be re-established first.
  **2026-10-15 (year rebuild): density axis scooped, ratio axis untouched —
  which makes the idea sharper and cheaper, not weaker.** PMID:41834375 supplies
  both the density optimum and a functional-ligand assay that the ratio series
  needs; PMID:42160160 supplies an independent density result. Nothing in the
  225 varies the *ratio of two specificities at fixed total density*. Rank
  unchanged (still last) only because the readout remains % transfected rather
  than cargo mass.

### 10. Is the DAR turnover the avidity turnover? — [COMBINATION]
- **Combines:** the nanoparticle finding that delivery efficiency is
  **bell-shaped** in ligand density, with an optimum at ~0.1 VHH/100 nm² and
  **excess ligand density inducing receptor degradation**
  [2026-10-15 · PMID:41834375], and the ADC finding that DAR4 and DAR8 gave
  **equal** intratumoral free payload, equal efficacy at dose-matched payload,
  and better penetration for DAR4 [2026-10-15 · PMID:41927976]. These sit in
  different literatures (mRNA-LNP targeting vs ADC DAR optimization) and
  near-certainly do not cite each other, though that is unverified from
  abstracts.
- **Hypothesis:** The reason higher DAR stops adding delivered payload is the
  same mechanism as the nanoparticle avidity optimum — high-payload conjugates
  lose target receptor from the cell surface (via accelerated degradation or
  reduced recycling), so copies per antibody and receptors available to be
  engaged trade off against each other.
- **Test:** One antibody, one payload, a copy-number series spanning the
  4-to-8-and-above range, measuring surface receptor level after exposure
  alongside delivered payload. The control that makes it interpretable is a
  copy-matched series using a **non-binding** isotype conjugate (to show
  receptor loss is engagement-driven) and a payload-free backbone series at
  matched backbone mass (to show it is not a backbone-mass effect).
- **Readout:** Surface target receptor per cell over time (flow cytometry) and
  intratumoral free payload (MALDI-IMS or lysate quantification), plotted on
  the same copy-number axis.
- **Motivation:** [2026-10-15 · PMID:41834375] +
  [2026-10-15 · PMID:41927976] (+ supporting: site-specific DAR 4 beat cysteine
  DAR 8 in vivo [2026-10-15 · PMID:41799094]; internalization rate rather than
  receptor abundance governs targeted-LNP delivery
  [2026-10-15 · PMID:42173446])
- **Difficulty:** med
- **Status:** new
- **Notes:** 2026-10-15 created in the year rebuild. The appeal is that one
  mechanism would explain a conflict currently recorded as unresolved
  [cumulative §6, "Does raising DAR raise delivered payload?"] while producing
  a free-payload number. Caveats to check in the primary papers before taking
  it seriously: PMID:41927976 compares at dose-matched payload (6 vs 3 mg/kg),
  so antibody mass differs between arms and receptor occupancy is not matched —
  that has to be handled in the design; and the receptor-degradation claim in
  PMID:41834375 is for a multivalent *particle*, where geometry is very
  different from a payload-laden single antibody, so the mechanism may simply
  not transfer. A negative result is informative either way.

### 11. Valency × affinity matrix re-run with the cargo attached — [COMBINATION]
- **Combines:** the systematic TfR1 affinity/valency/epitope scan, which
  concluded bivalent matches monovalent for brain uptake at matched cell-surface
  binding strength and which carried **no cargo**
  [2026-10-15 · PMID:41287279], and the finding that ASO conjugation
  *increased* brain-endothelial binding of low-affinity shuttles via avidity
  while *reducing* it for high-affinity ones and significantly delayed
  transcytosis of high-to-moderate affinity binders
  [2026-10-15 · PMID:42332368]. Both are TfR1 shuttle papers in the same
  journal family, so **non-citation is unverified and should be checked first**;
  the combination is still that one paper's central variable is the other
  paper's uncontrolled one.
- **Hypothesis:** The conclusion "bivalent ≈ monovalent at matched surface
  binding" does not survive cargo conjugation, because conjugation shifts
  apparent avidity in opposite directions for high- and low-affinity binders —
  so the format ranking obtained with naked constructs mis-ranks the
  conjugates, and the correct ranking must be established with cargo on.
- **Test:** The valency × affinity matrix (two epitopes, monovalent and
  bivalent, an affinity ladder) built twice: naked, and conjugated with an
  identical oligonucleotide cargo at a fixed, MS-verified copy number. Match
  cell-surface binding strength **after** conjugation, not before. The control
  that makes it interpretable is a conjugate carrying a
  size/charge-matched inert cargo, which separates "any cargo" from "this
  cargo".
- **Readout:** Delivered cargo mass in brain parenchyma per dose (cargo-specific
  assay) with parenchyma-vs-capillary separation; in-vitro transcytosis rate and
  surface receptor loss on brain endothelial cells for each matrix cell;
  reticulocyte depletion as the safety axis.
- **Motivation:** [2026-10-15 · PMID:41287279] +
  [2026-10-15 · PMID:42332368] (+ affinity-dependent valency/PK threshold
  [2026-10-15 · PMID:41599718]; monovalent shuttle determinants
  [2026-10-15 · DOI:10.64898/2026.08.13.744307, PREPRINT])
- **Difficulty:** high
- **Status:** new
- **Notes:** 2026-10-15 created in the year rebuild; successor to ideas 1 and 2,
  both of which the year partly scooped. Why it ranks first: it is the only
  idea on the list whose primary readout is **delivered cargo mass** on a
  question the field currently answers with uptake, and it resolves a stated
  conflict [cumulative §6]. Why it is hard: it is a two-dimensional matrix
  doubled, which is a lot of constructs; a reduced design (two affinities × two
  valencies × ±cargo at one epitope) may be the realistic entry point, and
  PMID:41287279's own panel may already contain reusable constructs. Verify
  whether the two papers cite each other before claiming the combination is
  novel.

### 12. Anchor-stability-corrected antibody-LNP comparison — [COMBINATION]
- **Combines:** an orientation-controlled antibody-LNP giving **over 100-fold**
  greater cellular association than unmodified LNPs **in vitro**
  [2026-10-15 · PMID:42612711], and the finding that **DSPE-PEG-mAb sheds from
  LNPs within 1 h in blood** while a PCL-b-PEG anchor holds the antibody over
  24 h [2026-10-15 · DOI:10.64898/2026.07.02.736109, PREPRINT]. One is a
  targeting-chemistry paper, the other a formulation-stability preprint;
  citation relationship unverified but the literatures are separate.
- **Hypothesis:** A large fraction of the in-vitro targeting advantage reported
  for PEG-lipid-anchored antibody LNPs does not survive circulation, and anchor
  chemistry — not antibody affinity, orientation or density — accounts for much
  of the in-vitro-to-in-vivo gap in this format.
- **Test:** One antibody, one LNP composition, one cargo, two anchor
  chemistries (PEG-lipid vs a covalent/polymer anchor), with **paired** in-vitro
  association and in-vivo delivered-cargo readouts on the same preparations.
  The control that makes it interpretable is measurement of antibody remaining
  per particle after serum incubation at the in-vivo sampling times, so
  "targeting failed" and "the antibody left" are distinguishable.
- **Readout:** Antibody molecules per particle after 0, 1, 4, 24 h serum
  exposure (single-particle or depletion assay); in-vitro association fold vs
  untargeted; in-vivo delivered cargo in the target tissue (mass if possible,
  expression if not, stated as which).
- **Motivation:** [2026-10-15 · PMID:42612711] +
  [2026-10-15 · DOI:10.64898/2026.07.02.736109] (+ the pattern it would
  explain: nanobody-displaying EVs gave only slight bone-marrow gains and
  raised off-target accumulation [2026-10-15 · PMID:42310937]; composition
  screening gave 148-fold in vitro while the binder added just over 2-fold in
  vivo [2026-10-15 · PMID:42674453])
- **Difficulty:** low
- **Status:** new
- **Notes:** 2026-10-15 created in the year rebuild. Lowest-difficulty new idea
  and it addresses a structural gap recorded in §6 ("in-vitro targeting gains
  have an unexamined in-vivo discount"). It is a methods result rather than a
  delivery mechanism, which is why it does not rank higher — but if the
  shedding result holds, a large slice of the carrier-format literature needs
  re-reading, which is cheap leverage. The anchor-stability source is a
  **preprint**; confirming it is step zero.

### 13. Cytosolic fraction as the reported quantity
- **Hypothesis:** For protein and oligonucleotide cargo delivered by an
  antibody or nanobody, the escaped (cytosolic) fraction of internalised cargo
  is small enough to dominate the delivery budget, and it varies more across
  carrier formats than total uptake does.
- **Test:** One binder, one cargo, three formats (direct conjugate, CPP-bearing
  trifunctional conjugate, particle-encapsulated), each measured for cytosolic
  arrival **and** total internalised cargo on the same samples, so the reported
  quantity is a fraction. The control that makes it interpretable is a
  no-escape-pathway arm (e.g. a non-internalising binder, and a cargo that
  cannot act unless cytosolic) plus a known-escape positive control.
- **Readout:** Cytosolic cargo / total internalised cargo, as a percentage, per
  format. Cytosolic arm by split-enzyme complementation or an equivalent
  cytosol-restricted reporter; total internalised by labelled-cargo
  quantification.
- **Motivation:** the absence itself — four papers in the year reach cytosol or
  nucleus [2026-10-15 · PMID:41569158] [2026-10-15 · PMID:41208769]
  [2026-10-15 · EPMC:AGR/IND609298393] [2026-10-15 · PMID:41127334] and **none**
  reports escaped cargo as a fraction of internalised cargo
  [2026-10-15 · cumulative §4, §6]. The one quantified escape-attributed gain is
  7-fold on silencing IC50 (200 → 28 nM)
  [2026-10-15 · PMID:41569158]. Supporting the premise that uptake is the wrong
  endpoint: internalisation did not predict mRNA translation
  [2026-10-15 · PMID:42272747]; internalization and lysosomal degradation are
  temporally uncoupled [2026-10-15 · PMID:42286928].
- **Difficulty:** med
- **Status:** new
- **Notes:** 2026-10-15 created in the year rebuild, spun out of idea 4 when
  the year scooped idea 4's intervention but left its *measurement* untouched.
  This is a measurement proposal, not a mechanism — its value is that it would
  make every subsequent escape-enhancer claim (including idea 4's) interpretable
  in a common unit. Honest weakness: cytosol-restricted reporters each have
  their own artifacts, and whoever runs this should expect the method
  development to be the project. Note PMID:41569158's own warning that
  circulating sulfated GAGs altered PK enough to block in-vivo assessment of
  their system — a reason to keep this in vitro first.

### 14. Is binding-to-release immune to internalization-blocking resistance? — [COMBINATION]
- **Combines:** PhoPEx binding-to-release chemistry, which releases payload via
  a nucleophile in the **binding pocket** rather than after endocytosis and gave
  5.9-fold higher tumour MMAE AUC0-120 h than the internalization-dependent
  small-molecule conjugate and a 3.6-fold better tumour-to-blood ratio than the
  ADC [2026-10-15 · PMID:42649302], and the resistance mechanism in which
  AKR1C1 **blocks NECTIN4-ADC internalization and exports the ADC in
  extracellular vesicles** [2026-10-15 · PMID:42167230]. A chemistry paper and a
  resistance-biology paper; non-citation likely, unverified.
- **Hypothesis:** Conjugates that release payload on binding are insensitive to
  resistance mechanisms that act by blocking internalization or exporting the
  conjugate, so the delivered-payload gap between binding-to-release and
  internalization-dependent conjugates widens in resistant cells.
- **Test:** Matched binding-to-release and internalization-dependent conjugates
  against the same target, in isogenic sensitive vs internalization-blocked
  cells (e.g. AKR1C1-high vs -low, or an equivalent engineered pair). The
  control that makes it interpretable is a non-cleavable, non-releasing
  conjugate in both backgrounds, and confirmation that surface target levels are
  matched between backgrounds.
- **Readout:** Intracellular free payload per cell (LC-MS) and viability IC50,
  in both backgrounds, with surface target density and conjugate internalisation
  measured in parallel.
- **Motivation:** [2026-10-15 · PMID:42649302] +
  [2026-10-15 · PMID:42167230] (+ the cleavable-payload-without-internalization
  preprint [2026-10-15 · DOI:10.64898/2026.10.09.757939]; FLOT2 loss as an
  opposite-direction internalisation modifier
  [2026-10-15 · DOI:10.64898/2026.05.15.725439, PREPRINT])
- **Difficulty:** med
- **Status:** new
- **Notes:** 2026-10-15 created in the year rebuild. Attractive because it
  turns a mechanism into a selection rule: if it holds, binding-to-release is
  the format of choice for poorly internalising or resistance-prone targets,
  which is a design decision with a cargo-amount consequence. Two things to
  verify first: PhoPEx's headline comparator is a **small-molecule** conjugate,
  not an antibody [cumulative §6 caveats], so an antibody-format version may not
  exist yet; and the AKR1C1 result is one target in one system, so the isogenic
  pair may have to be engineered rather than found.

### 15. Three loading platforms normalised per mg antibody — [COMBINATION]
- **Combines:** three independent claims to raise cargo per targeting unit that
  are reported in mutually incomparable units — a polypeptide backbone at **DAR
  61** with no PK or tumour-response numbers in the abstract
  [2026-10-15 · PMID:42819270]; an antibody-**nanogel** that matched T-DM1
  efficacy with **4-fold less antibody** but does not report its DAR
  [2026-10-15 · PMID:41433257]; and an antibody-**polymer** conjugate at
  **DAR ~23** with a 210-fold lower in-vitro IC50 than mirvetuximab soravtansine
  [2026-10-15 · PMID:42570634]. Three different fields (bioconjugation,
  nanogels, polymer therapeutics); mutual non-citation likely, unverified.
- **Hypothesis:** When the three formats are compared on one antibody, one
  payload and one tumour model with **antibody mass** as the normaliser, they do
  not rank in the order their individual headline numbers imply, and the ranking
  is set by clearance and penetration rather than by copies per antibody.
- **Test:** One antibody, one payload, three formats, dosed at **matched
  antibody mass** and separately at **matched payload mass** (the two
  normalisations answer different questions and both are needed). Controls:
  the conventional DAR-4 or DAR-8 ADC of the same antibody/payload as the
  shared reference point all three papers lack, and a free-payload arm.
- **Readout:** Payload copies per antibody (MS, including for the nanogel where
  it is unreported), plasma clearance, intratumoral **free payload** by
  MALDI-IMS, tumour penetration depth by IHC, and efficacy — reported per mg
  antibody dosed.
- **Motivation:** [2026-10-15 · PMID:42819270] +
  [2026-10-15 · PMID:41433257] + [2026-10-15 · PMID:42570634] (+ the reason
  copies may not predict payload: DAR4 ≈ DAR8 free payload with better DAR4
  penetration [2026-10-15 · PMID:41927976]; the non-antibody per-particle
  loading benchmark, 100 enzymes per particle and 15-fold intracellular
  activity [2026-10-15 · PMID:41881071])
- **Difficulty:** high
- **Status:** new
- **Notes:** 2026-10-15 created in the year rebuild. This is the project's
  thesis variable stated as an experiment: cargo actually delivered per mg of
  targeting protein. It ranks third rather than first only because it is a
  large comparative study rather than a single mechanistic question, and because
  reproducing three published platforms is substantial work — a two-format
  version (nanogel vs conventional ADC, since the nanogel paper already claims
  the 4-fold antibody-sparing) would be the sensible pilot. Caveat from the
  brief: the DAR scoring boundary is fragile and two of these three abstracts
  name no baseline DAR [cumulative §6 caveats], so the published numbers should
  be re-derived, not quoted.

### 16. HALA co-dosing applied to a brain shuttle — [COMBINATION]
- **Combines:** unconjugated **High-Avidity, Low-Affinity** antibody co-dosed
  to auto-tune ADC delivery to the local target level, improving in-vivo tumour
  distribution of T-DM1 and T-DXd and giving equal or greater efficacy across a
  range of HER2 expression [2026-10-15 · PMID:41468362], and the TfR1
  affinity/valency/epitope scan showing that transcytosis and receptor
  degradation trend with affinity and that shuttle performance is a tuning
  problem rather than a maximisation one [2026-10-15 · PMID:41287279]. Solid-
  tumour ADC penetration and BBB shuttle engineering are separate literatures;
  non-citation likely, unverified.
- **Hypothesis:** Co-dosing an unconjugated high-avidity, low-affinity
  anti-TfR1 antibody alongside a TfR1 shuttle-cargo conjugate raises
  **parenchymal** cargo, by relieving the capillary binding-site barrier that
  traps conjugate on the luminal endothelium, without the receptor loss that
  comes from raising conjugate affinity or valency.
- **Test:** Shuttle-cargo conjugate alone vs conjugate plus co-dosed HALA
  anti-TfR1, with a dose series of the HALA antibody. Controls that make it
  interpretable: a co-dosed **high-affinity** unconjugated anti-TfR1 (predicted
  to compete and reduce delivery) and an isotype control at matched protein
  mass, so competition and barrier relief are distinguishable. Reticulocyte
  counts throughout, since unconjugated anti-TfR1 load is the known safety axis.
- **Readout:** Parenchymal cargo mass per dose with capillary depletion, i.e.
  parenchyma-to-capillary ratio, plus distribution homogeneity by light-sheet
  imaging of a cleared hemisphere (the method exists
  [2026-10-15 · PMID:41310626]).
- **Motivation:** [2026-10-15 · PMID:41468362] +
  [2026-10-15 · PMID:41287279] (+ affinity cocktails proposed for the
  binding-site barrier in a radioligand setting
  [2026-10-15 · DOI:10.64898/2025.12.22.696075, PREPRINT]; whole-hemisphere
  quantification method [2026-10-15 · PMID:41310626])
- **Difficulty:** med
- **Status:** new
- **Notes:** 2026-10-15 created in the year rebuild. The transfer is the
  speculative part: the binding-site barrier argument was developed for solid
  tumours with heterogeneous antigen, and the BBB endothelium is a monolayer
  with a very different geometry, so the mechanism may not map. It is listed
  because the intervention is cheap (co-dose an unconjugated antibody), the
  readout is parenchymal cargo mass, and a clean negative would still be
  informative about whether luminal binding-site saturation limits TfR1
  shuttles. Safety is the obvious obstacle — added unconjugated anti-TfR1 load
  interacts with the reticulocyte effects that PMID:41287279 tracks.

---

## Dropped / scooped

Nothing dropped as of 2026-10-15. Ideas are never deleted — they get a status
and a reason, so an idea that becomes relevant again keeps its history.

- **Idea 3** remains **[SCOOPED, PARTIAL]**: after the year, both its headline
  (high loading is possible) and part of its turnover question (DAR4 ≈ DAR8 on
  free payload) are published, and a nanobody copy-number series exists up to 4
  copies. Narrowed to the 8-60 range on a VHH with a free-payload readout.
- **Ideas 1, 2, 4 and 8** were moved to **[SCOOPED, PARTIAL]** in the
  2026-10-15 year rebuild. In each case the mechanism or trend is now published
  and the delivered-cargo quantity is not. They are kept with narrowed scope and
  lower rank; ideas **11** and **13** are their successors.
- **Idea 9**'s density axis is scooped [PMID:41834375, PMID:42160160]; its ratio
  axis is untouched by anything in the 225, so it is narrowed rather than
  dropped.
- No idea has been dropped on the grounds of being wrong. If one is, the reason
  goes here with the citation that broke it.

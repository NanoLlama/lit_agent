# Experiment Ideas

Maintained by the **strategist** agent. Re-ranked weekly.

> These are **discussion prompts, not protocols.** Every one needs verifying
> against the primary papers before anyone sets up a bench experiment. The
> motivation citations are the starting point for that check.

IDs are stable and never reused or renumbered. Statuses: `new`, `refined`,
`tested`, `scooped`, `dropped`.

Flags: **`[COMBINATION]`** joins findings from two or more papers that did not
cite each other (most likely to be novel) · **`[CONTRADICTED]`** premise
undercut by newer work · **`[SCOOPED]`** essentially done by someone else ·
**`[SCOOPED, PARTIAL]`** the headline claim is published but a stated part
remains open, so the idea is narrowed rather than dropped.

---

## Current ranking

**Ranked 2026-10-15** (first real ranking, after the seeding backfill).
Criteria in order: direct read on cargo amount > mechanistic leverage >
novelty > feasibility.

| Rank | ID | Idea | Status | Difficulty |
|---|---|---|---|---|
| 1 | 6 | Site-specific attachment of a high-copy payload backbone [COMBINATION] | new | med |
| 2 | 3 | Multi-payload loading turnover on a VHH [SCOOPED, PARTIAL] | refined | high |
| 3 | 8 | TfR1 VHH clones classified by trafficking route, with a cargo number [COMBINATION] | new | med |
| 4 | 5 | pIgR-directed siRNA conjugate for airway epithelium [COMBINATION] | new | high |
| 5 | 1 | Valency vs transcytosis at matched affinity | refined | med |
| 6 | 7 | Pretargeting vs direct display, cargo per targeting molecule [COMBINATION] | new | high |
| 7 | 2 | Affinity tuning to reduce lysosomal sorting | refined | med |
| 8 | 4 | Co-delivered endosomal escape enhancers | refined | med |
| 9 | 9 | Targeting-ligand ratio and density on co-display LNPs | new | low |

**Why the top three are top:** all three turn this month's biggest gap —
loading and localization are demonstrated, delivered cargo is not measured
[2026-10-15 · cumulative §6] — into a number, and each has published reagents
to build on: idea 6 pairs a DAR-61 backbone with a defined conjugation site and
is the most feasible direct read on cargo per antibody; idea 3 is the project's
central thesis narrowed to the part the DAR-61 and AOC papers left open; idea 8
has the most mechanistic leverage, since a route-based in-vitro surrogate would
make shuttle-clone screening cheap.

Ideas 1-4 were seeds written from the project's standing focus before this
pipeline had read any literature. On 2026-10-15 each got its first reality
check; see their Notes. None was dropped.

---

### 1. Valency vs. transcytosis at matched affinity
- **Hypothesis:** At matched apparent affinity, a bivalent shuttle nanobody
  delivers more cargo per receptor than a monovalent one — or, if avidity
  drives receptor crosslinking into the degradative route, less.
- **Test:** Monovalent vs. bivalent constructs against the same shuttle
  receptor, affinity matched by surface plasmon resonance rather than by
  assumption. Both directions are informative; the point is to separate
  valency from affinity, which most published comparisons confound.
- **Readout:** Transcytosed cargo per receptor (transwell or in vivo brain
  concentration), plus surface vs. internalized receptor by flow cytometry.
- **Motivation:** seed idea. First literature contact 2026-10-15: nearest
  neighbours are a multivalent-vs-monovalent internalization comparison on a
  rigid DNA framework [2026-10-15 · PMID:42766830] and a two-specificity
  co-display format [2026-10-15 · DOI:10.64898/2026.09.21.753074]; neither
  matches affinity, and neither uses an antibody or nanobody shuttle.
- **Difficulty:** med
- **Status:** refined
- **Notes:** 2026-10-15 seeded. 2026-10-15 first reality check: **the
  matched-affinity comparison was not found in this month's set, so the idea
  stands.** Two updates to it. (a) PMID:42766830 suggests rigidity/spacing of
  the multivalent display, not valency count alone, may carry the effect — so a
  rigid-vs-flexible linker arm is worth adding to the design. (b) The TfR1 VHH
  clones [2026-10-15 · PMID:42855849] show clones against one receptor
  diverging in brain localization at indistinguishable reported affinity
  (">100 nM" for all three), which argues epitope should be held constant in
  any valency comparison or it will confound the result. Caveat: this month's
  valency evidence is aptamer-based and affinity-unmatched, so it is context,
  not support.

### 2. Affinity tuning to reduce lysosomal sorting
- **Hypothesis:** Lowering shuttle affinity below the point that maximizes
  binding increases *net* cargo delivered, by reducing lysosomal sorting at the
  expense of capture efficiency — so net delivery peaks at intermediate
  affinity.
- **Test:** An affinity ladder (ideally single-residue variants on one scaffold,
  to hold format constant) against one receptor, measuring both capture and
  final delivered cargo.
- **Readout:** Delivered cargo (mass or activity) per dose; parallel
  colocalization with LAMP1 vs. recycling markers.
- **Motivation:** seed idea. First literature contact 2026-10-15: lysosomal
  routing is shown to be an engineerable variable — TfR1 bispecifics
  deliberately route a target to lysosomal degradation with >1-2 orders of
  magnitude potency gain [2026-10-15 · PMID:42816619] — and routing is
  epitope-sensitive at ASGPR1 [2026-10-15 · DOI:10.64898/2026.09.11.750848,
  preprint]. Clone-level divergence at indistinguishable reported affinity:
  [2026-10-15 · PMID:42855849].
- **Difficulty:** med
- **Status:** refined
- **Notes:** 2026-10-15 seeded. 2026-10-15 first reality check: premise not
  contradicted and not tested by anything in this month's set. But the month's
  evidence points at **epitope and binding geometry, rather than affinity, as
  the lever actually being pulled** on lysosomal sorting
  (PMID:42816619, DOI:10.64898/2026.09.11.750848) — and PMID:42855849 shows
  big routing differences with no affinity difference reported. Refinement: run
  an epitope arm alongside the affinity ladder, or the ladder may come back flat
  and be over-interpreted as "affinity does not matter". Note the ASGPR1 and
  GTAC work measures degradation, not delivered cargo, so neither tells you
  which direction net delivery moves.

### 3. Multi-payload linkers without losing receptor engagement — [SCOOPED, PARTIAL]
- **Hypothesis (narrowed 2026-10-15):** On a *nanobody* scaffold, raising cargo
  copies per molecule with a multi-payload backbone turns over at some copy
  number, and the turnover is set by clearance and uptake-per-cell rather than
  by loss of binding affinity.
- **Test:** One site-specific conjugation handle, a payload-per-molecule
  series, holding the binder constant. Measure where the curve turns over. The
  control that makes it interpretable is a copy-number series on the *same*
  binder, since the published high-DAR result changes both backbone and
  loading at once.
- **Readout:** Cargo copies per molecule (mass spectrometry), retained binding
  affinity, uptake per cell, and clearance — the gain is only real if all four
  are reported together. Add delivered cargo per dose in vivo; that is the
  number the published work does not give.
- **Motivation:** seed idea, now anchored. Loading to DAR 61 with retained
  antigen binding, endocytosis and subnanomolar cellular activity on a
  click-chemistry polypeptide backbone
  [2026-10-15 · PMID:42819270]; the DAR>1 potency penalty for siRNA conjugates
  and its chemical fix, with a dose-matched DAR1 vs DAR2 comparison
  [2026-10-15 · DOI:10.64898/2026.09.23.753708, preprint]; a site-specific
  Q295 conjugation handle, probes/PEG only and explicitly not validated with
  cytotoxic payloads [2026-10-15 · PMID:42809913].
- **Difficulty:** high
- **Status:** refined
- **Notes:** 2026-10-15 seeded. **2026-10-15 judgment: partially scooped — not
  fully scooped, and not merely supported.** Reasoning, stated plainly so it
  can be checked against the primary papers:
  - *Scooped:* the headline claim that copies per antibody can be raised far
    past DAR 2-8 while retaining antigen binding and internalization is done.
    PMID:42819270 reports DAR up to 61 with binding and endocytosis retained
    and subnanomolar activity. Proposing to show "many payloads per targeting
    unit is possible" is no longer a contribution.
  - *Scooped:* the specific sub-question "does loading past DAR 1 cost potency
    for oligonucleotide cargo, and can chemistry fix it" is answered for siRNA
    at DAR2 — C16 lipid on the siRNA restored activity, and at matched 1 mg/kg
    siRNA the DAR2-C16 AOC needed half the antibody of DAR1-C16.
  - *Still open:* (i) **where the curve turns over.** Neither paper reports a
    copy-number series — PMID:42819270 reports a lead at "up to 61",
    DOI:...753708 compares DAR1 vs DAR2 only. (ii) **The four readouts
    together.** PMID:42819270's abstract gives no PK parameters, dosing or
    tumor-response numbers, so copies-per-antibody is never tied to
    cargo-delivered-per-dose. (iii) **Nanobody scaffold.** Both papers use
    full-length antibody formats; a ~15 kDa VHH has no Fc and a much shorter
    half-life, so the clearance penalty of hanging a large payload backbone on
    it is the part most likely to differ and is wholly untested here.
    (iv) **Site-specificity.** PMID:42809913's Q295 handle has not been used
    with a payload at all.
  - *Net:* keep the idea, narrowed to (i)-(iii) on a VHH. Drop any framing that
    claims high loading per se is novel.

### 4. Co-delivered endosomal escape enhancers
- **Hypothesis:** Cargo that reaches the endosome but not the cytosol is the
  binding constraint for protein and oligonucleotide payloads, so a
  co-delivered escape enhancer raises functional delivery without touching the
  targeting module.
- **Test:** Nanobody-cargo conjugate with and without an escape agent, against
  a functional cytosolic readout rather than total uptake.
- **Readout:** A cytosolic-activity reporter (e.g. split-enzyme
  complementation, knockdown for siRNA), with total uptake measured in parallel
  to show the ratio moved and not just the dose.
- **Difficulty:** med
- **Status:** refined
- **Motivation:** seed idea. First literature contact 2026-10-15: **no paper
  in this month's set measured endosomal escape or cytosolic delivery at all**
  [2026-10-15 · cumulative §4]. Indirectly relevant: a C16 lipid on siRNA
  restored DAR2 AOC potency, but the abstract does not state the mechanism, so
  whether it acts on uptake, escape or stability is unresolved and must not be
  read as an escape result [2026-10-15 · DOI:10.64898/2026.09.23.753708,
  preprint]. A cleavable-linker payload acted with little antibody
  internalization via extracellular cathepsin L
  [2026-10-15 · DOI:10.64898/2026.10.09.757939, preprint].
- **Notes:** 2026-10-15 seeded. 2026-10-15 first reality check: nothing tests
  this, and the absence is itself notable — the whole backfill contains no
  escape measurement. Two refinements. (a) The premise should be **scoped to
  protein and oligonucleotide cargo.** The melanoma T-DXd preprint shows a
  cleavable small-molecule payload can act without internalization, so for that
  payload class "endosome-trapped cargo is the binding constraint" is not safe
  as a general claim; partial undercut, not a contradiction of the
  protein/oligo case. (b) Since C16-lipid modification is a plausible
  confounder-or-mechanism here, any escape-enhancer test should include a
  lipid-modified-payload arm so the two explanations are separable. Toxicity of
  escape agents remains the obvious confound; the control is the conjugate
  without cargo.

### 5. pIgR-directed siRNA conjugate for airway epithelium — [COMBINATION]
- **Combines:** pIgR bispecifics enriching 5-10-fold in cyno bronchoalveolar
  lavage fluid with rapid serum clearance [2026-10-15 · PMID:42829333], and
  AOC chemistry that doubles siRNA per antibody (C16 lipid, DAR2) and shifts
  silencing extrahepatically via a charge-balancing ionizable linker
  [2026-10-15 · DOI:10.64898/2026.09.23.753708, preprint]. The two papers do
  not cite each other; one is a transit result with no cargo, the other a
  loading/cargo result with no barrier.
- **Hypothesis:** A pIgR-engaging bispecific carrying C16-modified siRNA at
  DAR2 delivers more functional siRNA to airway epithelium per mg of antibody
  than a non-pIgR isotype-matched conjugate, and the rapid serum clearance of
  pIgR engagement raises rather than lowers that ratio.
- **Test:** pIgR-targeting vs non-targeting conjugate, both at DAR2-C16, dosed
  at matched siRNA dose (not matched antibody dose — matched siRNA is what
  isolates targeting from loading). A DAR1-C16 pIgR arm separates the loading
  contribution from the targeting contribution.
- **Readout:** Target-transcript knockdown in airway epithelium (% vs control),
  with siRNA mass in lung and in serum over time, per mg antibody dosed.
- **Motivation:** [2026-10-15 · PMID:42829333] +
  [2026-10-15 · DOI:10.64898/2026.09.23.753708]
- **Difficulty:** high
- **Status:** new
- **Notes:** 2026-10-15 created. Species is the main obstacle — the pIgR result
  is cyno, and cross-species pIgR expression was explicitly characterized in
  that paper, which is worth reading before assuming a mouse version works. The
  pIgR paper reports lavage fluid, not tissue, so "reaches epithelium" is an
  inference from it and needs checking, not assuming.

### 6. Site-specific attachment of a high-copy payload backbone — [COMBINATION]
- **Combines:** a click-chemistry polypeptide backbone reaching DAR 61 with
  binding and endocytosis retained [2026-10-15 · PMID:42819270], and an
  engineered transglutaminase that conjugates trastuzumab Q295 despite N297
  glycan hindrance, 3.6-fold wild-type activity, tested only with probes and
  PEG [2026-10-15 · PMID:42809913]. Neither cites the other; one solves "how
  many", the other "exactly where".
- **Hypothesis:** Anchoring the high-copy polypeptide backbone at a single
  defined site (Q295) gives the same payload copies per antibody as stochastic
  attachment but with narrower species distribution and slower clearance, so
  more payload is actually delivered per dose.
- **Test:** Same backbone and same nominal copy number, attached
  site-specifically at Q295 vs stochastically, on the same antibody. The
  interpretable control is a copy-number-matched pair, verified by mass
  spectrometry rather than assumed from reaction stoichiometry.
- **Readout:** Copies per antibody and species distribution width (MS),
  retained affinity, plasma clearance, and payload mass delivered to target
  tissue per dose.
- **Motivation:** [2026-10-15 · PMID:42819270] +
  [2026-10-15 · PMID:42809913]
- **Difficulty:** med
- **Status:** new
- **Notes:** 2026-10-15 created. Closest thing this run has to a
  tractable-and-direct experiment: both reagents are published and the readout
  is a cargo amount. PMID:42809913's authors state their enzyme is not
  validated with cytotoxic payloads, so payload compatibility is the first
  thing to check, and a non-cytotoxic payload could be used to de-risk it.
  Related to idea 3 but distinct: idea 3 asks where loading turns over, this
  asks whether attachment geometry moves the turnover point.

### 7. Pretargeting vs direct display: cargo per targeting molecule — [COMBINATION]
- **Combines:** host-guest pretargeting, where a pre-dosed
  adamantane-antibody acts as a docking site for later-infused CB[7]-LNPs so
  one antibody can in principle recruit many particles
  [2026-10-15 · PMID:42839730], and direct click display of a CD4 nanobody on
  LNPs, which transfected up to 48% of resting CD4+ T cells
  [2026-10-15 · PMID:42764379]. The two papers do not cite each other and use
  the same underlying idea — a click/affinity handle on a particle — in
  opposite architectures.
- **Hypothesis:** For a given number of targeting molecules, two-step
  pretargeting delivers more cargo per targeting molecule than one-step direct
  display, because each docked antibody can capture multiple particles.
- **Test:** Same cell target and same mRNA cargo, comparing (a) nanobody
  directly displayed on LNP and (b) adamantane-nanobody pre-dosed then
  CB[7]-LNP infused — normalized to targeting molecules used, not to particles
  used. Controls: CB[7]-LNP with no pre-dosed antibody, and pre-dosed antibody
  with non-CB[7] LNP, to show the capture step is doing the work. The published
  pretargeting result is confounded by an NLG919 lipid and a cytokine cargo, so
  the lipid must be held constant here.
- **Readout:** Cargo delivered (transfected or edited cells, %) per nmol of
  targeting molecule, plus particle association per cell.
- **Motivation:** [2026-10-15 · PMID:42839730] +
  [2026-10-15 · PMID:42764379]
- **Difficulty:** high
- **Status:** new
- **Notes:** 2026-10-15 created. The amplification claim is the attractive
  part and is exactly what the pretargeting abstract does not quantify (no
  fold-enrichment, no %ID/g). Two-step dosing in vivo adds a timing variable
  that the comparison has to hold constant.

### 8. Classify TfR1 VHH clones by trafficking route, with a cargo number — [COMBINATION]
- **Combines:** TfR1 VHH clones that diverge in brain localization at
  indistinguishable reported affinity — Y11 neuronal and sustained to 48 h, A1
  vascular and declining, imaging only with no %ID/g or cargo
  [2026-10-15 · PMID:42855849] — and the GTAC work showing TfR1 engagement
  geometry can be engineered to drive endocytosis and lysosomal routing, with
  live-cell trafficking readouts, at >1-2 orders of magnitude potency gain
  [2026-10-15 · PMID:42816619]. Both concern TfR1; they do not cite each other,
  and one has the assay the other is missing.
- **Hypothesis:** The A1 vs Y11 difference is a trafficking-route difference
  (degradative vs recycling/transcytotic) measurable in a live-cell assay, and
  that route assignment predicts which clone delivers more parenchymal cargo.
- **Test:** Run both clones through GTAC-style live-cell endocytosis and
  lysosomal-routing readouts in brain endothelial cells, then dose both with an
  identical quantifiable cargo in vivo. The control that makes it
  interpretable is capillary depletion (or equivalent) to separate parenchymal
  from vessel-associated signal — the ambiguity the imaging data leaves open.
- **Readout:** Surface vs internalized vs lysosomal receptor fraction in vitro;
  parenchymal cargo as %ID/g and parenchyma-to-capillary ratio in vivo.
- **Motivation:** [2026-10-15 · PMID:42855849] +
  [2026-10-15 · PMID:42816619]
- **Difficulty:** med
- **Status:** new
- **Notes:** 2026-10-15 created. Highest mechanistic leverage on the list: if
  route predicts parenchymal delivery, clone screening gets a cheap in-vitro
  surrogate. Caveat to verify first — the clones' affinities are reported only
  as ">100 nM" for all three, so they may not in fact be affinity-matched, and
  that would have to be measured before the comparison means anything.

### 9. Targeting-ligand ratio and density on co-display LNPs
- **Hypothesis:** On an LNP co-displaying two targeting antibodies, cargo
  delivered per cell depends on the *ratio* of the two ligands, with an optimum
  away from 1:1, separately from total ligand density.
- **Test:** A ratio series (anti-CD5 : anti-CD222) at fixed total ligand
  density, plus a density series at fixed ratio — the two series together are
  what separate ratio from density. Single-ligand and non-conjugated LNPs as
  controls, which is where the published work's missing comparator sits.
- **Readout:** Cargo delivered per cell type (% transfected / % CAR-positive)
  and particles associated per cell, by flow cytometry, for each cell type
  addressed.
- **Motivation:** [2026-10-15 · DOI:10.64898/2026.09.21.753074, preprint] +
  [2026-10-15 · PMID:42764379] (shared DBCO-azide click handle chemistry)
- **Difficulty:** low
- **Status:** new
- **Notes:** 2026-10-15 created. Cheapest idea on the list and ex vivo
  throughout, but the weakest read on *amount* of cargo per targeting unit, so
  it ranks low despite being easy. The co-display preprint reports no
  fold-change or percentages, so the baseline has to be re-established before a
  ratio series means anything.

---

## Dropped / scooped

Nothing dropped as of 2026-10-15. Ideas are never deleted — they get a status
and a reason, so an idea that becomes relevant again keeps its history.

- **Idea 3** is flagged **[SCOOPED, PARTIAL]** rather than moved here: its
  headline claim is published [2026-10-15 · PMID:42819270,
  DOI:10.64898/2026.09.23.753708] but the turnover curve, the four-readout
  pairing and the nanobody scaffold remain open. It stays in the active list,
  narrowed. See its Notes for the reasoning.

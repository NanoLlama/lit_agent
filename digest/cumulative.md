# Cumulative Digest: Antibody/Nanobody Cargo Delivery

Running synthesis, organized by theme rather than by date. Maintained by the
**strategist** agent; edited incrementally, never rewritten.

Each entry ends with `[<report date> · <article ID>]`. An entry supported by
several papers accumulates citations rather than spawning duplicate bullets —
a theme with six citations is the signal worth being able to see at a glance.

**Status:** populated from the 2026-10-15 seeding backfill (30-day lookback,
17 articles). One month of evidence only; no trends can be read from it yet.
All entries below derive from abstracts — no full text was fetched for the
seeding brief [2026-10-15 · report housekeeping].

---

## 1. Shuttle receptors and targeting strategies

- **pIgR carries IgG-format cargo from blood into a mucosal lumen in non-human
  primates.** pIgR-targeted bispecifics enriched 5-10-fold in cynomolgus
  bronchoalveolar lavage fluid versus normal IgG, after a cross-species check
  that cyno pIgR expression (RNA and protein) resembles human. The measurement
  is in lavage fluid, not tissue; GI mucosa was evaluated but no GI number is
  reported in the abstract. [2026-10-15 · PMID:42829333]
- **The PK cost of a transcytosing epithelial shuttle is fast serum
  clearance.** The same pIgR bispecifics cleared rapidly from serum — a dosing
  constraint to plan around rather than an incidental observation.
  [2026-10-15 · PMID:42829333]
- **TfR1 VHH clones that bind the same receptor can differ in where they end
  up in brain.** Three human/mouse cross-reactive TfR1 VHH-Fc clones (A1, Y11,
  Z1) from NGS-guided diverse selection all gave ELISA EC50 ">100 nM". After IV
  dosing in mice, Y11 brain-associated fluorescence persisted to 48 h and
  localized to NeuN-positive neuronal regions, while A1 started high, declined,
  and localized to lectin-positive vasculature. Evidence is fluorescence
  imaging and microscopy only; no %ID/g, no parenchyma-to-capillary ratio and
  no cargo are reported in the abstract, so measured brain *delivery* is not
  shown. [2026-10-15 · PMID:42855849]
- **ASGPR1 epitope position, not just receptor identity, is a design choice for
  uptake.** A bispecific (BiAb J31, knobs-into-holes/CrossMab) binding ASGPR1
  residues 62-100 — membrane-proximal, outside the carbohydrate-recognition
  domain — recruited TNF-α and drove uptake into LysoTracker-positive
  compartments in HepG2 cultures (supernatant TNF-α signal fell ~60% over
  90 min). In vitro only. PREPRINT.
  [2026-10-15 · DOI:10.64898/2026.09.11.750848]
- **CD222 is a candidate internalizing receptor for myeloid and T cells.** A
  new anti-CD222 antibody (CLCM08) is described as facilitating internalization
  and gave the largest phagocytic gain in monocytes when displayed on mRNA
  LNPs; no number supports the size of the gain in the abstract. PREPRINT.
  [2026-10-15 · DOI:10.64898/2026.09.21.753074]
- **CD4 is usable as an uptake receptor on resting lymphocytes**, which are
  normally refractory to LNP transfection (see section 5).
  [2026-10-15 · PMID:42764379]

## 2. Valency, affinity, and avidity effects

This theme is **genuinely thin in this month's set** — it had no top picks, and
is populated only from score-3 papers. No paper in the backfill separates
valency from affinity at matched affinity in an antibody or nanobody shuttle.

- **Multivalent, rigidly spaced display improves internalization over
  monovalent and flexible display.** A tetrahedral DNA framework presenting
  multiple aptamers gave "substantially improved internalization" and ~71%
  target degradation at 100 nM / 24 h versus flexible and monovalent
  comparators. The internalization fold-change is not reported in the abstract,
  the ligand is an aptamer rather than an antibody, and affinity is not matched
  across the comparison — so this is suggestive of a valency lever, not a
  controlled valency experiment. [2026-10-15 · PMID:42766830]
- **Affinity differences did not explain clone-level delivery differences for
  TfR1** — all three VHH clones were reported at EC50 ">100 nM", yet their
  brain localization profiles diverged, pointing at epitope or trafficking
  rather than affinity. The abstract does not resolve affinity more finely than
  ">100 nM". [2026-10-15 · PMID:42855849]
- **Co-display of two different targeting antibodies on one carrier** (anti-CD5
  plus anti-CD222 on CAR-mRNA LNPs) is a distinct lever from raising the
  valency of one specificity; it addressed two cell types with one particle.
  Ex vivo only, fold-change not reported in abstract. PREPRINT.
  [2026-10-15 · DOI:10.64898/2026.09.21.753074]

## 3. Conjugation and loading strategies (DAR, site-specific, multi-payload)

- **Payload copies per antibody can reach DAR 61 with antigen binding and
  endocytosis retained.** A click-chemistry polypeptide backbone carried many
  payloads per antibody; lead ADC 6c reached DAR up to 61, still recognized
  antigen, was endocytosed, and showed subnanomolar cellular activity. The
  abstract describes "excellent" PK and potent antitumor efficacy in mice but
  gives no PK parameters, dosing or tumor-response numbers — so whether payload
  *per antibody* became more payload *delivered in vivo* is not quantified in
  the abstract. Published 2026-08-14, before the backfill window; indexed in
  it. [2026-10-15 · PMID:42819270]
- **The DAR>1 potency penalty for siRNA conjugates has a chemical fix.** A
  single C16 lipid on the siRNA improved silencing over the unmodified AOC and
  restored activity at DAR2; at an equivalent 1 mg/kg siRNA dose, the DAR2-C16
  AOC needed half the antibody of the DAR1-C16 AOC for comparable knockdown —
  i.e. twice the siRNA per antibody without the usual penalty. Percent
  knockdown values and the animal model are not reported in the abstract.
  PREPRINT. [2026-10-15 · DOI:10.64898/2026.09.23.753708]
- **A charge-balancing ionizable linker (CBIL) shifted AOC activity
  extrahepatically**, increasing silencing in heart and skeletal muscle without
  a matching rise in liver activity — a linker-chemistry lever on tissue
  distribution rather than on loading. PREPRINT.
  [2026-10-15 · DOI:10.64898/2026.09.23.753708]
- **Site-specific conjugation at trastuzumab Q295 is enzymatically
  accessible.** A computationally guided microbial transglutaminase variant
  (M3-MTGase-Sm, R48K/G283S/S303G) had 3.6-fold wild-type activity and
  conjugated Q295 despite N297 glycan hindrance. Only probes and PEG were
  tested; the authors state it is not validated with cytotoxic payloads.
  [2026-10-15 · PMID:42809913]
- **Non-covalent/physical loading formats report entrapment rather than DAR.**
  A bevacizumab-functionalized exosome-chitosan nanocomposite gave 68.50 ±
  2.15% temozolomide entrapment and 15.96 ± 0.18 wt% loading with
  74.9 ± 2.9% retained VEGF binding; biodistribution and PK
  were not done and the abstract itself calls for them.
  [2026-10-15 · PMID:42828315] Rituximab-PLGA-PEG nanoparticles reported 7-8%
  paclitaxel loading with CD20-dependent association versus an IgG control;
  PK and biodistribution are stated as still needed.
  [2026-10-15 · PMID:42764913]
- **Multi-warhead concatenation on a non-antibody scaffold is so far a
  concept.** "Catamers" propose a DNA scaffold concatenating a PSMA binder,
  deruxtecan, a cleavage site and a half-life extender; the paper is molecular
  simulation only and the authors state the advantages are untested. PREPRINT.
  [2026-10-15 · DOI:10.64898/2026.09.23.753027]

## 4. Intracellular trafficking and endosomal escape

This theme is also **thin in this month's set**: no top picks, and nothing in
the backfill measured endosomal escape or cytosolic delivery. What exists is
trafficking-and-degradation work where the "cargo" is degradation rather than a
delivered payload — useful as routing design rules, not as delivery results.

- **Receptor trafficking can be rewired as the mechanism of action, with large
  potency gains.** TfR1 bispecifics (GTACs) drove GPCR endocytosis and
  lysosomal degradation with more than one to two orders of magnitude greater
  potency than conventional antibody antagonists. The cargo here is
  degradation, not delivery, but the live-cell trafficking design rules are
  candidates for transfer to TfR1 shuttles. [2026-10-15 · PMID:42816619]
- **Small nanobody-nanobody fusions can route surface proteins to
  degradation.** TROP2-targeting chimeras (TRTACs, ~30 kDa) degraded EGFR,
  HER2 and PD-L1 preferentially in tumor cells; a HER2 TRTAC-drug conjugate
  reduced SKBR3 viability by 50% at 0.2 nM. No comparison to a non-degrading
  conjugate is reported in the abstract, so the contribution of degradative
  routing to the drug effect is not isolated. [2026-10-15 · PMID:42801692]
- **A cleavable-linker payload can act without antibody internalization.**
  ERBB2-knockout melanoma xenografts responded to trastuzumab deruxtecan
  similarly to ERBB2-positive ones initially; melanoma cells took up little
  trastuzumab in vitro, and extracellular cathepsin L may cleave the linker
  outside cells. This decouples payload effect from uptake and trafficking for
  cleavable small-molecule ADCs. PREPRINT.
  [2026-10-15 · DOI:10.64898/2026.10.09.757939]
- **Lysosomal routing after uptake is epitope-sensitive**: the
  membrane-proximal ASGPR1 binder drove uptake into LysoTracker-positive
  compartments. [2026-10-15 · DOI:10.64898/2026.09.11.750848]

## 5. Carrier formats (nanoparticles, fusion proteins, bispecifics)

- **A nanobody clicked onto an LNP transfects resting primary human CD4+ T
  cells.** DBCO-azide attachment of a high-affinity CD4 nanobody gave LNPs that
  transfected up to 48% of non-activated CD4+ T cells in PBMC co-culture and
  delivered CRISPR-Cas9 components to activated CD4+ T cells with up to 32%
  editing (both in vitro). In humanized NSG-SGM3 mice they selectively
  associated with and transfected circulating and bone-marrow human CD4+ T
  cells with minimal murine off-target activity; in vivo percentages are not
  reported in the abstract, and no untargeted-LNP comparator number is given.
  "Highest efficiency reported so far" is the authors' claim.
  [2026-10-15 · PMID:42764379]
- **Two targeting antibodies on one LNP can serve two cell types.** Anti-CD222
  (CLCM08) co-displayed with anti-CD5 on CAR-mRNA LNPs "substantially enhanced"
  CAR-monocyte and CAR-T generation from primary cells versus non-conjugated
  LNPs; ex vivo only, no fold-change or percentages in the abstract. PREPRINT.
  [2026-10-15 · DOI:10.64898/2026.09.21.753074]
- **An antibody can be used as a docking site rather than as a carrier.**
  Pre-dosed adamantane-conjugated anti-PD-L1 primed tumors to capture
  later-infused cucurbit[7]uril-functionalized LNPs carrying IL-2-Fc circRNA;
  the authors report improved intratumoral retention and cellular uptake plus
  tumor suppression and longer survival. No fold-enrichment, %ID/g or survival
  numbers are reported in the abstract, and the antitumor benefit is confounded
  by an NLG919-modified lipid and the cytokine cargo, so the pretargeting
  contribution to delivery is not isolated. In principle one antibody can
  recruit many particles, which is a loading lever of a different kind.
  [2026-10-15 · PMID:42839730]
- **Nanobody-displayed viral vectors redirect tropism, but say nothing about
  transit.** An anti-mGluR5 nanobody inserted at VP1 T456 of an HSPG-ablated
  AAV-DJ capsid (AAV-m5) gave an eight-fold higher proportion of transduced
  hippocampal neurons than wild-type AAV-DJ at equivalent titers — mouse,
  stereotactic injection, so local delivery only. Vector, not antibody cargo.
  PREPRINT. [2026-10-15 · DOI:10.64898/2026.09.18.752817]
- **Antibody-decorated vesicle and polymer particles are reported at the
  loading-and-binding stage**, with PK and biodistribution explicitly
  outstanding in both cases.
  [2026-10-15 · PMID:42828315] [2026-10-15 · PMID:42764913]

## 6. Open problems and conflicting results

No head-to-head contradiction between two papers surfaced in this first month.
What this section holds instead are structural gaps — places where the
month's papers each stop short of the measurement the thesis needs.

- **Loading is demonstrated; delivered cargo is not.** DAR 61 is reported with
  retained binding and endocytosis, but with no PK parameters and no quantified
  in-vivo payload delivery in the abstract [2026-10-15 · PMID:42819270]. The
  only paper that ties copies-per-antibody to a dose-matched in-vivo outcome
  does so at DAR 1 vs 2 [2026-10-15 · DOI:10.64898/2026.09.23.753708]. **What
  would resolve it:** a payload-per-antibody series with cargo copies, retained
  affinity, uptake per cell and clearance reported together on one scaffold.
- **TfR1 clone differences: delivery or just localization?** Y11 (neuronal,
  sustained to 48 h) vs A1 (vascular, declining) is imaging only, with no
  %ID/g, no parenchyma-to-capillary ratio and no cargo
  [2026-10-15 · PMID:42855849]. **What would resolve it:** capillary-depletion
  or quantified parenchymal cargo measurement on the same clones.
- **Does uptake matter for cleavable ADCs?** Section 4's melanoma result argues
  a cleavable payload can act with little antibody internalization via
  extracellular cathepsin L [2026-10-15 · DOI:10.64898/2026.10.09.757939],
  while the whole targeted-uptake program (sections 1 and 5) assumes
  internalization is the bottleneck. These are not strictly in conflict — the
  mechanisms may coexist and the payload classes differ — but they imply
  different optimization targets. **What would resolve it:** a
  non-internalizing-control conjugate with a non-cleavable linker, run
  alongside the cleavable one in the same model. PREPRINT on one side.
- **Targeted-nanoparticle results are consistently missing their untargeted
  comparator numbers**, which is what sizes the gain
  [2026-10-15 · PMID:42764379] [2026-10-15 · DOI:10.64898/2026.09.21.753074]
  [2026-10-15 · PMID:42839730] [2026-10-15 · PMID:42828315]
  [2026-10-15 · PMID:42764913]. Several of these abstracts also defer PK and
  biodistribution entirely.
- **Degradation is being used as a proxy for delivery.** Three of this month's
  trafficking papers measure target degradation, not payload delivered
  [2026-10-15 · PMID:42816619] [2026-10-15 · PMID:42801692]
  [2026-10-15 · PMID:42766830]. Their routing rules may transfer to shuttles,
  but that transfer is untested in this set.
- **Endosomal escape and cytosolic delivery were not measured by any paper in
  this backfill.** Noted as an absence, not a finding.
- **Flagged for human read:** PMID:42824429, an unflagged mini-review on
  ultrahigh-DAR ADCs — on-thesis for loading but rubric-capped at 2 and not
  reviewed for the brief [2026-10-15 · report housekeeping].

When two papers disagree, both land here with both citations and one line on
what experiment would resolve it. Contradictions are not silently overwritten.

---

## Maintenance log

| Date | Change |
|---|---|
| 2026-10-15 | Seeded by scaffold; no literature folded in yet. |
| 2026-10-15 | First fold-in: 2026-10-15 seeding backfill (17 articles, 7 at score 4-5, 10 at score 3). All six themes populated. Sections 2 and 4 flagged as genuinely thin — no top picks, score-3 papers only, and no endosomal-escape measurement anywhere in the set. Section 6 holds structural gaps rather than paper-vs-paper conflicts; none surfaced this month. Abstract-only evidence throughout. |

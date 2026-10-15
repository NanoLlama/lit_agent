# Cumulative Digest: Antibody/Nanobody Cargo Delivery

Running synthesis, organized by theme rather than by date. Maintained by the
**strategist** agent.

Each entry ends with `[<report date> · <article ID>]`. An entry supported by
several papers accumulates citations rather than spawning duplicate bullets —
a theme with six citations is the signal worth being able to see at a glance.

**Status:** rebuilt on 2026-10-15 from the **12-month backfill**
(`reports/2026-10-15-year.md`; window 2025-10-12 to 2026-10-15, 225 articles,
36 preprints, 13 at score 5, 50 at 4, 162 at 3). This supersedes the 30-day
seeding version of this digest, whose entries have been folded in, promoted
into broader patterns, or kept with their original citations where the year's
set does not contain the paper (see Maintenance log).

**Standing caveats that apply to every entry below.**

- All of it is screened from abstracts; no full text was fetched for either
  brief [2026-10-15 · report housekeeping].
- 36 of 225 are **preprints** and are marked as such wherever they appear.
- Many "delivery" numbers in the set are *expression*, *efficacy*, *potency* or
  *imaging signal* rather than delivered cargo mass. Where that is true the
  entry says so, because the distinction is the point of this project.
- The year's own normalisation pass re-scored 100 articles against one
  standard. It demoted 13 papers from score 4 to 3, and 12 of those demotions
  give the absence of a delivered-cargo measurement as the reason
  [2026-10-15 · data/2026-10-15-y12 normalisation field]. That is itself a
  structural finding about the field and is recorded in §6.

---

## 1. Shuttle receptors and targeting strategies

**Established by the year.** TfR1 is the field's default brain shuttle and has
moved from platform demonstration to clinical readout: a TfR1 antibody-
oligonucleotide conjugate lowered DMPK mRNA 37-46% in human muscle biopsies
[2026-10-15 · PMID:41707138], with a companion report on the same program
[2026-10-15 · PMID:41821312]. Around it sits a dense preclinical layer in
rodents and non-human primates, summarized in the bullets below. The year's
other consolidated point: TfR1 is no longer the only validated receptor —
CD98hc, CA-IV, IGF1R, LRP1 and pIgR all carried cargo across a barrier in at
least one in-vivo study in this window.

- **A TfR1 shuttle on a therapeutic antibody is dose-sparing, measured in
  tissue.** A mouse TfR1-binding Fab fused to aducanumab gave higher and more
  homogeneous brain distribution than unmodified aducanumab (whole-hemisphere
  light-sheet imaging of cleared APP/PS1 brains), and a **five-fold lower dose**
  reduced plaque burden comparably to high-dose chronic aducanumab. The
  brain-delivery fold-change itself is not reported in the abstract.
  [2026-10-15 · PMID:41310626]
- **TfR1 carries oligonucleotide cargo across the BBB in several independent
  formats, with knockdown as the readout.** Monovalent TfR1 VHH-Fc carrying
  siRNA/ASO in rodents and NHPs, with affinity, DAR and conjugation site named
  as the main determinants [2026-10-15 · DOI:10.64898/2026.08.13.744307,
  PREPRINT]; pH-dependent anti-TfR1 nanobodies giving up to 60% muscle
  knockdown at two weeks and 30-60% in CNS cell types
  [2026-10-15 · DOI:10.64898/2026.07.29.741483, PREPRINT]; 1:1 TfR1 VHH-siRNA
  conjugates giving 50-80% brain knockdown with ED50 below 1 mg/kg in mice and
  NHPs, with no comparator reported
  [2026-10-15 · DOI:10.64898/2026.05.20.726486, PREPRINT]; a TfR1 AOC giving
  ~75% reduction of DUX4-regulated genes eight weeks after a single dose in
  FSHD mice [2026-10-15 · PMID:41994867]. Knockdown is a functional surrogate,
  not delivered mass.
- **TfR1 protein and enzyme cargo.** Humanized picomolar anti-TfR1 nanobodies
  (NewroBus) crossed the BBB in humanized rats without blocking transferrin,
  and a TNF-nanobody fusion kept CSF exposure for three days
  [2026-10-15 · PMID:41462276]. An AAV-expressed anti-TfR1 VHH-I2S fusion
  cleared CNS lysosomal burden in MPS II mice better than a C-terminal VHH or
  untagged I2S [2026-10-15 · PMID:41457681]. A trimeric anti-TNFα/anti-TfR1
  nanobody reached a CSF-to-serum ratio up to ~0.4 in humanized rats, with no
  baseline reported [2026-10-15 · DOI:10.64898/2026.04.28.721316, PREPRINT].
- **Non-TfR1 shuttle receptors now form a real set.** Active-learning-evolved
  cross-species CD98hc shuttles gave long-lived brain delivery, with no
  brain-uptake figure in the abstract [2026-10-15 · PMID:42410049]; a
  carbonic-anhydrase-IV-binding *small-molecule* shuttle conjugated to
  antibodies and oligos crossed the BBB in mice and neonatal macaques with
  parenchymal levels sustained seven days
  [2026-10-15 · PMID:42649418]; an anti-IGF1R antibody carried siRNA to CNS,
  muscle, heart and lung with in-vivo knockdown
  [2026-10-15 · DOI:10.64898/2026.01.30.702950, PREPRINT]; Angiopep-2 installed
  on the IVIG Fc glycan drove LRP1 transcytosis and significantly higher brain
  accumulation than unmodified IVIG, fold not reported in abstract
  [2026-10-15 · PMID:41236640].
- **pIgR is the year's epithelial/mucosal transit story, with three independent
  papers.** pIgR-targeted bispecifics enriched 5-10-fold in cynomolgus
  bronchoalveolar lavage fluid versus normal IgG after a cross-species check
  that cyno pIgR expression resembles human; measurement is lavage fluid, not
  tissue, and no GI number is in the abstract
  [2026-10-15 · PMID:42829333]. Four nanobodies to the pIgR **stem** domain
  (HDX-MS epitope residues 578-612, distinct from the dIgA site) gave
  apical-to-basolateral Transwell transport (not quantified in the abstract),
  and inhaled nanobody-reslizumab bispecifics were effective at **one-tenth**
  the intraperitoneal reslizumab dose in a murine asthma model while
  reslizumab alone at equivalent concentrations failed — dose-sparing inferred
  from efficacy, so delivered mass was not measured
  [2026-10-15 · PMID:42496279]. An anti-pIgR VHH transcytosed in epithelial
  models comparably to dimeric IgA, in vitro
  [2026-10-15 · PMID:41737496].
- **The PK cost of a transcytosing epithelial shuttle is fast serum
  clearance** — a dosing constraint to design around, not an incidental
  observation. [2026-10-15 · PMID:42829333]
- **Binding kinetics, not affinity magnitude, is the recurring epitope-level
  design rule for transcytosis.** Cross-species TfR1 VHHs to a dimer-interface
  epitope: intermediate affinity with fast dissociation was linked to efficient
  transcytosis [2026-10-15 · PMID:41110474]. A faster acidic-pH off-rate
  correlated with pIgR transcytosis in vitro
  [2026-10-15 · PMID:41737496]. pH sensitivity is one of the two axes in the
  systematic TfR1 scan [2026-10-15 · PMID:41287279] (see §2).
- **Two arms can beat one, including a second arm inside the brain.** A dual
  TfR/intra-brain-MOG antibody gave higher Cmax and four-month brain retention
  versus either arm alone, fold not reported in abstract
  [2026-10-15 · PMID:42665535]. A bispecific CD98hc/TfR1 Brainshuttle restored
  in-vitro transcytosis efficiency that ASO conjugation had degraded
  [2026-10-15 · PMID:42332368].
- **Masking the cargo or the conjugate is a transit lever in its own right.**
  An anti-ASO antibody mask on TfR antibody-ASO conjugates improved
  TfR-mediated uptake and reduced nonspecific accumulation, fold not reported
  in abstract [2026-10-15 · PMID:41166443]. An MMP2-cleavable PEG mask on a
  nanobody-sialidase conjugate gave a **144-fold** longer systemic half-life
  and **9.3-fold** higher tumour-site accumulation than the unmasked control;
  the abstract does not separate how much of the accumulation comes from the
  half-life extension [2026-10-15 · PMID:42241306].
- **Targeting inflamed endothelium can substitute for crossing the BBB.**
  VCAM-antibody-conjugated LNPs distributed to brain ~4x more than nonspecific
  LNPs, with brain cargo **expression** 10x higher, in mice with intracerebral
  haemorrhage; hematoma size fell ~69% at 72 h and motor behaviour improved
  ~65%. The 10x is expression, not cargo mass, and the comparator is an
  untargeted LNP — one of the three least antibody-specific score-5 results
  (see §6). [2026-10-15 · PMID:41088400]
- **Pretargeting: the antibody as a docking site rather than a carrier.** An
  anti-EGFR/anti-PEG bispecific primed tumours for a subsequently dosed
  PEG-based 212Pb nanocarrier; pretargeting **more than tripled** tumour
  retention of the nanomedicine over the untargeted nanomaterial in an EGFR+
  breast xenograft (SPECT plus gamma counting of excised organs) and increased
  receptor-mediated internalization in vitro
  [2026-10-15 · PMID:41687816]. TCO-modified antibodies with tetrazine payloads
  are the other pretargeting chemistry in the set
  [2026-10-15 · PMID:41705578] [2026-10-15 · PMID:41449469]
  [2026-10-15 · PMID:41198055].
- **Human shuttle-target expression looks stable enough to be a dependable
  design input.** In a human brain dataset, 612 of 631 comparisons (97%) of
  shuttle-target expression were not significantly different across region,
  sex, age or disease. PREPRINT.
  [2026-10-15 · DOI:10.64898/2026.05.21.726908]
- **FcRn transcytosis is reduced by the antibody's own antigen.** Cognate
  antigen cut FcRn-mediated transcytosis of sotrovimab by 46.7% versus 23% for
  B38 [2026-10-15 · PMID:41339598]. This is one of two results in the year
  showing the cargo/target is not a passive passenger (see §6).
- Carried over from the 30-day seeding set, not present in the 12-month kept
  set: **TfR1 VHH clones against one receptor diverged in where they ended up
  in brain** (Y11 neuronal, persisting to 48 h; A1 vascular and declining; all
  three ELISA EC50 ">100 nM"), imaging only, no %ID/g and no cargo
  [2026-10-15 · PMID:42855849]. **ASGPR1 epitope position is a design choice**
  — a bispecific binding residues 62-100, membrane-proximal and outside the
  carbohydrate-recognition domain, drove uptake into LysoTracker-positive
  compartments in HepG2 cultures; in vitro only, PREPRINT
  [2026-10-15 · DOI:10.64898/2026.09.11.750848]. **CD222 as a candidate
  internalizing receptor for myeloid and T cells**, no number in the abstract,
  PREPRINT [2026-10-15 · DOI:10.64898/2026.09.21.753074]. **CD4 as an uptake
  receptor on resting lymphocytes** [2026-10-15 · PMID:42764379].

## 2. Valency, affinity, and avidity effects

**No longer thin.** The 30-day version of this digest recorded that no paper
separated valency from affinity in an antibody or nanobody shuttle. The year
contains that experiment, plus a quantitative avidity optimum on a
nanoparticle, a co-dosing strategy built on deliberately mismatched
avidity/affinity, and evidence that attaching the cargo changes the avidity you
designed for. The theme's recurring message is that **more ligand, more
valency and more affinity are each non-monotonic in delivered cargo.**

- **Bivalent can match monovalent for brain uptake, if cell-surface binding
  strength is matched.** Affinity and valency were systematically varied for
  two anti-TfR1 antibodies with distinct epitopes and pH sensitivities;
  transcytosis and receptor degradation were trended against affinity and
  connected to in-vivo brain uptake and reticulocyte depletion. Bivalent
  anti-TfR1 antibodies were "equally effective in brain uptake as monovalent
  antibodies if engineered to have similar cell-surface TfR1 binding strength,
  with prolonged brain exposure and less severe adverse effects", and the
  authors state epitope factors in alongside affinity and valency. They
  explicitly challenge the view that monovalent formats are inherently
  superior. **No delivery figure is stated in the abstract and no cargo is
  conjugated**, which is why the normalisation pass held it at score 3.
  [2026-10-15 · PMID:41287279]
- **Ligand density on a particle has a measurable optimum, and the mechanism is
  receptor degradation.** A VHH-LNP platform with controlled orientation,
  tunable density and single-particle nanoflow quantification of *functional*
  ligands showed a bell-shaped dependence of delivery efficiency on ligand
  density with an optimum at **~0.1 VHH per 100 nm²**; excess ligand density
  induced receptor degradation, while optimal avidity balanced multivalent
  engagement against receptor preservation. Optimized LNPs gave in-vivo CAR-T
  generation with dose-dependent B-cell depletion at 10-30 µg/kg.
  [2026-10-15 · PMID:41834375]
- **Four more density studies point the same way, on four different
  chassis.** Post-conjugation Ab-LNPs at antibody-to-particle ratios of ~340,
  760 and 1200: the **lowest** density gave the highest binding capacity,
  internalization and bone-marrow accumulation in a disseminated MM1S xenograft
  [2026-10-15 · PMID:42160160]. Low antibody density on nanoshells (~60 vs ~170
  Ab/NS) gave ~2x higher binding avidity than high density
  [2026-10-15 · PMID:41696244]. Ligand density on anti-PD-L1 liposome
  conjugates tuned binding strength, tumour retention and tissue penetration,
  with binding and blockade rather than cargo as the readout
  [2026-10-15 · PMID:41939214]. VHH-ELP nanoparticle valency/density tuning
  improved neutralization potency, not cargo delivery
  [2026-10-15 · PMID:41566147]; anti-CD7 polymersomes used tunable nanobody
  density [2026-10-15 · PMID:42253849]. Three of these were demoted 4→3 for
  having no delivered-cargo measurement (§6).
- **Conjugating the cargo changes the avidity you engineered.** ASO
  conjugation "profoundly alters the cellular fate" of a TfR1 Brainshuttle:
  conjugation *increased* binding to brain endothelial cells for **low**-affinity
  shuttles via avidity effects while *reducing* binding strength of
  **high**-affinity shuttles, and transcytosis of high-to-moderate affinity
  binders across the BBB model was significantly delayed. A bispecific
  CD98hc/TfR1 design, using a second non-competing pathway, significantly
  enhanced in-vitro transcytosis. In vitro only; demoted 4→3 on that basis.
  [2026-10-15 · PMID:42332368]
- **Deliberately mismatching avidity and affinity is a dosing tool.** Co-dosed
  unconjugated **High-Avidity, Low-Affinity (HALA)** antibody auto-tuned ADC
  delivery to the local HER2 level: tumour distribution of T-DM1 and T-DXd
  improved in vivo, giving equal or greater efficacy across a range of HER2
  expression, and Fc-enhanced HALA antibodies gave a strong response in an
  immunocompetent model. The abstract reports no distribution figure.
  [2026-10-15 · PMID:41468362]
- **Valency effects on PK are conditional on affinity, with a threshold.** For
  albumin-binding VHH constructs, nanomolar binders reached maximal systemic
  exposure and further affinity gains (KD below ~100 nM) did not improve PK;
  valency effects were negligible at high affinity but pronounced at low
  affinity, where bivalency *reduced* systemic exposure and *raised* kidney
  uptake toward the non-binding control.
  [2026-10-15 · PMID:41599718]
- **Higher affinity may actively cost internalization.** Molecular dynamics
  predicted that strong Fab affinity correlates with poor internalization,
  PREPRINT [2026-10-15 · DOI:10.64898/2026.03.13.711720]. Separately, a
  "normalized internalization" metric combining binding and uptake ranked
  CEACAM6 ADC potency better than antigen abundance or affinity at matched
  loading [2026-10-15 · PMID:42309467]. Both sit against the picomolar-nanobody
  BBB result [2026-10-15 · PMID:41462276] — see §6.
- **Payload copies matched to the target's own valency raise effect.** A
  nanobody against mouse kappa light chain carried 1, 2 or 4 site-specific
  zanamivir copies; the 4-copy adduct was **~10-fold more potent** than the
  single-copy adduct in protecting mice from influenza A, and intranasal dosing
  protected against lethal challenge. The ~10-fold is potency in protection,
  not measured payload delivered. This is the year's only copy-number series on
  a nanobody. [2026-10-15 · PMID:41183201]
- **Small-scale crosslinking can buy avidity without triggering degradation.**
  Cryo-EM of TfR1-8D3 with small-scale crosslinking. PREPRINT.
  [2026-10-15 · DOI:10.64898/2026.06.30.735565]
- **Affinity cocktails have been proposed to address the binding-site
  barrier** for Ac-225 delivery. PREPRINT.
  [2026-10-15 · DOI:10.64898/2025.12.22.696075]
- Carried over from the 30-day set: **multivalent, rigidly spaced display
  improved internalization over monovalent and flexible display** on a
  tetrahedral DNA framework (~71% target degradation at 100 nM / 24 h);
  internalization fold-change not reported, ligand is an aptamer, affinity not
  matched [2026-10-15 · PMID:42766830].

**What the year does *not* show in this theme:** no study reports **delivered
cargo mass** as a function of valency at matched affinity in vivo. The
systematic scan reports brain uptake and reticulocyte depletion with no cargo
attached [2026-10-15 · PMID:41287279]; the avidity-optimum work reports
transfection and pharmacology, not mass [2026-10-15 · PMID:41834375]. Recorded
in §6.

## 3. Conjugation and loading strategies (DAR, site-specific, multi-payload)

**Established by the year.** Homogeneous DAR 8 with retained binding and
acceptable aggregation is now achievable by several independent linker
chemistries, and DAR far beyond 8 is chemically attainable. The open question
has shifted from "can copies per antibody be raised" to "does raising them
raise delivered payload", and the year contains direct evidence on both sides.

- **The DAR ceiling has been broken in at least four distinct ways.** A
  click-chemistry polypeptide backbone reached **DAR up to 61** with retained
  antigen recognition, endocytosis and subnanomolar cellular activity; the
  abstract describes excellent PK and potent antitumour efficacy but gives no
  PK parameters, dosing or tumour-response numbers, and names no baseline DAR
  [2026-10-15 · PMID:42819270]. A hydrophilic **Y-shaped PEG12 pendant
  linker** gave trastuzumab-VC-pABC-MMAE at **DAR 8** against the DAR 4 ceiling
  the authors cite for approved ADCs, with the payload structure unchanged;
  "excellent tumor accumulation and in vivo efficacy" is reported without a
  number [2026-10-15 · PMID:41558564]. An antibody-polymer-drug conjugate at
  **DAR ~23** gave an IC50 **210-fold lower** than mirvetuximab soravtansine in
  FRα+ cells, in vitro, on an established polymer platform
  [2026-10-15 · PMID:42570634]. A hydrophilic exatecan linker gave a
  homogeneous HER2 ADC at **DAR 7.92** with under 1% aggregation
  [2026-10-15 · PMID:42296596].
- **More DAR 8 chemistries, same pattern.** β-glucuronidase-cleavable linker
  giving homogeneous DAR 8 cetuximab conjugates with preserved binding and
  lysosomal trafficking, PREPRINT [2026-10-15 · PMID:42183362]; a short
  hydrophilic glucuronide spacer giving DAR 8 exatecan-trastuzumab with
  improved plasma stability [2026-10-15 · PMID:42157849]; DAR 8 cetuximab-I21
  with >400-fold selectivity [2026-10-15 · PMID:42333517]; pyridazinedione
  chemistry giving defined payload ratios 1-8 and up to three different
  payloads on thio-trastuzumab, characterized with fluorophores only
  [2026-10-15 · PMID:41726384].
- **Counterweight: payload copies and delivered payload came apart when
  someone measured the payload.** MALDI imaging mass spectrometry of
  intratumoral **free payload** found similar intensity and distribution for
  DAR4 and DAR8 ADCs at 2 h and 24 h, with comparable in-vivo efficacy at
  dose-matched payload (DAR4 6 mg/kg, DAR8 3 mg/kg) — and DAR4 penetrated
  tumour *better* by IgG IHC without that translating into efficacy. The
  authors conclude DAR optimization is target- and payload-specific and that
  design should prioritize active payload release over passive distribution.
  [2026-10-15 · PMID:41927976]
- **Attachment site can beat copy number.** An Fc N-glycan site-specific DXd
  ADC at **DAR 4 outperformed a DAR 8 cysteine ADC in vivo**, with less
  aggregation and less payload loss [2026-10-15 · PMID:41799094]. A
  supramolecular site-specific MMAE ADC gave better survival than cysteine
  ADCs carrying higher loading in a rat model, PREPRINT
  [2026-10-15 · PMID:42620052].
- **Loading vs targeting traded off explicitly, with both numbers reported.**
  In CC49 pretargeted imaging, the **highest stochastic TCO loading gave the
  top tumour uptake at 10.4 %ID/g**, while site-specific loading improved
  tumour-to-blood ratios. One of the few papers in the set that reports a
  loading series and a delivered-cargo number together.
  [2026-10-15 · PMID:41705578]
- **The DAR>1 penalty for oligonucleotide cargo has at least two independent
  chemical fixes.** A single C16 lipid on the siRNA restored the potency
  normally lost going from DAR1 to DAR2 AOCs, and at an equivalent 1 mg/kg
  siRNA dose the DAR2-C16 AOC needed **half the antibody** of the DAR1-C16 AOC
  for comparable knockdown; a charge-balancing ionizable linker (CBIL) shifted
  silencing toward heart and skeletal muscle relative to liver. Knockdown
  percentages and the CBIL fold shift are not reported in abstract. PREPRINT.
  [2026-10-15 · DOI:10.64898/2026.09.23.753708] A neutral phosphoryl-guanidine
  siRNA backbone fixed the rapid clearance of DAR2 TfR1 AOCs in mice, with no
  numbers in the abstract [2026-10-15 · PMID:42612014]. A third approach used
  the siRNA itself to offset payload hydrophobicity in an
  antibody-siRNA-exatecan conjugate at DAR 1-2, in-vitro killing only; demoted
  4→3 for having no delivery or PK readout [2026-10-15 · PMID:41314050].
- **Carrier-format loading raises cargo per antibody without touching linker
  chemistry.** HER2 antibody-nanogel conjugates with covalently encapsulated
  DM1 matched T-DM1 efficacy in a BT-474 xenograft while requiring **4-fold
  less antibody**, with comparable in-vitro cytotoxicity. The DAR is not
  reported in the abstract and the authors call it proof of concept.
  [2026-10-15 · PMID:41433257] Gas vesicle nanoparticles displayed multiple
  antibodies and ADCs at high density, with no quantification in abstract
  [2026-10-15 · EPMC:AGR/IND609286246].
- **Site-specific conjugation chemistry matured on several fronts.** An
  engineered microbial transglutaminase (M3-MTGase-Sm, R48K/G283S/S303G) with
  3.6-fold wild-type activity conjugated trastuzumab **Q295** despite N297
  glycan hindrance, tested only with probes and PEG and explicitly not
  validated with cytotoxic payloads [2026-10-15 · PMID:42809913]. mTG plus
  Endo-S2 installed **two different payloads** at Fc Q295 and N297
  [2026-10-15 · PMID:42227168]. A photo-crosslinking Fc-binding peptide raised
  site-specific conjugation yield to 95.5% from 78.4% and attached MMAE at
  Met252 [2026-10-15 · PMID:41292069]. VyPAL2 asparaginyl ligase installed
  radiolabel handles on a single-domain antibody in 15 min at 55-65% recovered
  product, with no uptake data [2026-10-15 · PMID:41176193]. Butelase-1
  Fab-DM1 with an albumin-binding domain
  [2026-10-15 · PMID:42384122]; aminooxy coupling for trivalent conjugates
  carrying MMAE plus a fluorophore [2026-10-15 · PMID:41558005]; HUH-tag
  antibody-DNA conjugation, PREPRINT
  [2026-10-15 · DOI:10.64898/2026.08.31.746762]; phosphine reductants for
  engineered cysteines [2026-10-15 · PMID:41950231]; DisacLink at DAR1
  [2026-10-15 · PMID:42520171].
- **A site-specificity negative worth keeping.** Site-specific (VyPAL2) versus
  random single-domain-antibody radiolabeling gave *comparable* tumour uptake
  (3.7 vs 3.4 %IA/g); the gain was reduced renal retention (35.5 vs
  105.5 %IA/g), i.e. less off-target accumulation rather than more delivered
  cargo. Demoted 4→3 on exactly that distinction. PREPRINT.
  [2026-10-15 · DOI:10.21203/rs.3.rs-9664465/v1]
- **DAR can be an artifact.** Iminothiolane lysine conjugation produces a
  "phantom DAR"; a 14C assay was needed to detect it.
  [2026-10-15 · PMID:41391917]
- **Fc-free nanobody-drug conjugates can be given half-life without an Fc.** A
  Nectin4/Trop2 bispecific nanobody-drug conjugate with a C18 fatty acid had a
  20 h half-life and low kidney uptake [2026-10-15 · PMID:41101697].
- **Multivalent prodrug scaffolds as an alternative to linkers.**
  Gemcitabine-prodrug oligonucleotide-like chains as multivalent scaffolds on
  HER2/CD38 antibodies; no DAR in abstract
  [2026-10-15 · PMID:42501801].
- **A non-antibody loading benchmark worth knowing.** An enzyme-loaded LNP
  carried **100 enzymes per particle** and gave **15-fold** higher
  intracellular enzyme activity. Strong loading data, **no antibody involved**;
  scored 3 and flagged for a human read.
  [2026-10-15 · PMID:41881071]
- Carried over from the 30-day set: non-covalent/physical loading formats
  report entrapment rather than DAR — a bevacizumab-exosome-chitosan
  nanocomposite at 68.50 ± 2.15% temozolomide entrapment, 15.96 ± 0.18 wt%
  loading, 74.9 ± 2.9% retained VEGF binding, with PK and biodistribution not
  done [2026-10-15 · PMID:42828315]; rituximab-PLGA-PEG nanoparticles at 7-8%
  paclitaxel loading [2026-10-15 · PMID:42764913]. Multi-warhead "catamer"
  concatenation on a DNA scaffold remains simulation only, PREPRINT
  [2026-10-15 · DOI:10.64898/2026.09.23.753027].

## 4. Intracellular trafficking and endosomal escape

**The 30-day absence has narrowed but not closed.** Four papers in the year
report cytosolic or nuclear arrival of cargo, and one attaches a number to a
shift it attributes to endosome-to-cytosol import. **No paper in the 225
quantifies the cytosolic fraction of internalised cargo** — the readouts are
functional (silencing, editing, efficacy) or imaging. The gap is now "escape is
not measured as a ratio", not "escape is not studied".

- **The closest thing to a quantified escape gain.** A Staufen1 dsRBD34
  bifunctional antibody tethers siRNA non-covalently at 1:1 stoichiometry;
  functionalizing the siRNA terminus with small-molecule enhancers augmented
  silencing potency **seven-fold (IC50 200 → 28 nM)**, which the authors
  attribute to endosome-to-cytosol import. Notably, arginine-scanning affinity
  maturation gave 32-fold higher dsRBD-siRNA affinity but **neither stronger
  silencing nor better plasma stability**, and competition from circulating
  sulfated GAGs altered PK enough to prevent a practical in-vivo assessment.
  [2026-10-15 · PMID:41569158]
- **Escape shown, not sized.** Heterotrifunctional bio-orthogonal conjugates
  combining an antibody or receptor ligand, a cell-penetrating peptide and
  cargo: fluorescent cargo "revealed endosomal escape and intracellular
  accumulation", a peptidomimetic MYB inhibitor was active against AML cells,
  and Cas9 conjugates achieved cell-type-specific editing. Cell models only; no
  escape efficiency reported. [2026-10-15 · PMID:41208769]
- **Antibody as the cargo that needs to escape.** A metal-phenolic network
  polymeric nanocarrier (~30 nm, near-neutral charge, no cationic component)
  encapsulated antibodies on mixing, showed good PK and tumour accumulation
  after IV dosing, and facilitated endosomal escape through a buffering effect
  from coordination-bond dissociation at endosomal pH, releasing antibody to
  bind a cytoplasmic antigen and improving efficacy in orthotopic breast
  tumours. [2026-10-15 · EPMC:AGR/IND609298393]
- **A cell-penetrating antibody reaches the nucleus.** The lupus-derived
  anti-DNA antibody 3E10, mutant D31N, carried triplex-forming oligonucleotides
  into HER2+ cell nuclei with superior binding and delivery in vitro and in
  vivo; no efficiency figure in abstract. [2026-10-15 · PMID:41127334]
- **Uptake does not predict functional delivery — four papers, independently.**
  Antibody-LNP internalisation in primary T and B cells **did not predict**
  mRNA translation [2026-10-15 · PMID:42272747]. Receptor **internalization
  rate**, not receptor abundance, determined CD7-targeted LNP delivery
  [2026-10-15 · PMID:42173446]. ADC internalization and lysosomal degradation
  are **temporally uncoupled** on dual-probe live imaging
  [2026-10-15 · PMID:42286928]. A normalized internalization metric outranked
  antigen abundance and affinity for predicting ADC potency at matched loading
  [2026-10-15 · PMID:42309467]. Taken together this is the year's strongest
  mechanistic argument that uptake is the wrong endpoint.
- **Trafficking can be engineered upward on purpose.** Receptor-ubiquitination-
  targeting ADCs (ubitaADCs) bind the target receptor and an E3 ligase
  simultaneously, accelerating EGFR internalization and lysosomal trafficking,
  increasing intracellular drug release and tumour-cell killing, with superior
  in-vivo antitumour efficacy versus conventional ADCs; no uptake fold-change
  in abstract [2026-10-15 · PMID:41887220]. An EGFR:LGR5 bispecific ADC was
  100- to 1000-fold more potent than the monospecific ADC in vitro, PREPRINT
  [2026-10-15 · DOI:10.64898/2026.06.22.733843].
- **Internalization can be bypassed entirely.** Phosphorus(V)-phenol exchange
  (PhoPEx) releases payload via a nucleophile in the **binding pocket** rather
  than after endocytosis. A FAP-targeted binding-to-release small-molecule
  conjugate gave **5.9-fold** higher tumour MMAE exposure (AUC0-120 h) than the
  internalization-dependent small-molecule conjugate, matching the
  internalization-dependent ADC, with tumour-to-blood ratio **14.7-fold**
  higher than the small-molecule conjugate and **3.6-fold** higher than the
  ADC. The headline comparator is a small-molecule conjugate, not an antibody.
  [2026-10-15 · PMID:42649302]
- **Receptor clustering as an uptake rescue.** Anti-uPAR antibody on cationic
  liposomes carrying Sirt6 plasmid induced uPAR clustering and enhanced
  clathrin-mediated uptake: 1.7-2-fold in vitro and 1.5-fold in vivo versus
  antibody-free Lipo-Sirt6. Comparator is an untargeted liposome; one of the
  three least antibody-specific score-5 results (§6).
  [2026-10-15 · PMID:41117256]
- **Trafficking determinants of ADC resistance are becoming mapped.** AKR1C1
  blocks NECTIN4-ADC internalization and exports the ADC in extracellular
  vesicles [2026-10-15 · PMID:42167230]; FLOT2 loss increases T-DM1
  internalization, PREPRINT [2026-10-15 · DOI:10.64898/2026.05.15.725439];
  blocking caveolar endocytosis with nystatin raised anti-GD2 ADC cell
  accumulation and cut IC50 1.5-2.5-fold **in vitro but gave no in-vivo gain**,
  demoted 4→3 [2026-10-15 · PMID:42499678].
- **Degraders dominate this theme numerically and measure the wrong thing for
  this project.** Roughly 15 of the 37 score-3 trafficking papers are
  lysosome-targeting or degrader chimeras whose readout is target degradation
  rather than delivered cargo [2026-10-15 · report, score-3 trafficking
  section]. Named instances: TfR1 bispecific GTACs driving GPCR endocytosis and
  lysosomal degradation with >1-2 orders of magnitude greater potency than
  conventional antagonists [2026-10-15 · PMID:42816619]; ~30 kDa
  nanobody-nanobody TRTACs degrading EGFR, HER2 and PD-L1, with a HER2
  TRTAC-drug conjugate reducing SKBR3 viability by 50% at 0.2 nM and no
  non-degrading comparator reported [2026-10-15 · PMID:42801692]; a hyaluronan
  nanoparticle chassis recruiting unmodified IgG, with CD44 transcytosis
  driving near-complete PD-L1/HER2 depletion within 3 h at single-digit nM,
  demoted 4→3 as a degrader readout [2026-10-15 · PMID:41787855]; an LZ-8-based
  multivalent "Multibody" LYTAC drug conjugate delivering MMAE or doxorubicin,
  demoted 4→3 for having no delivered-cargo number, PREPRINT
  [2026-10-15 · DOI:10.21203/rs.3.rs-8651044/v1]; the rigid aptamer framework
  [2026-10-15 · PMID:42766830]. Their routing assays are the transferable part.
- Carried over from the 30-day set: **a cleavable-linker payload can act
  without antibody internalization** — ERBB2-knockout melanoma xenografts
  responded to trastuzumab deruxtecan similarly to ERBB2-positive ones
  initially, with little in-vitro trastuzumab uptake and extracellular
  cathepsin L a candidate linker cleaver. PREPRINT.
  [2026-10-15 · DOI:10.64898/2026.10.09.757939] Note this is mechanistically
  adjacent to, and independent of, the PhoPEx binding-to-release result above.

## 5. Carrier formats (nanoparticles, fusion proteins, bispecifics)

**Established by the year.** The antibody-decorated LNP is the single largest
format bucket in the set (10 of the 50 score-4 papers and 49 of the score-3
papers), and the dominant architecture is now *antibody supplies specificity,
carrier supplies capacity*. Attachment chemistry, orientation and density have
become explicit, measurable design variables rather than implementation
details. The theme's weakness is uniform: targeting is usually demonstrated by
in-vitro association, imaging or efficacy, with delivered cargo unquantified.

- **Attachment chemistry and antibody orientation produce the largest reported
  in-vitro gains in the set.** Orientation-controlled trastuzumab via an
  FcBP-HFQ lipid on mRNA-LNPs gave **over 100-fold** greater cellular
  association than unmodified LNPs in HER2+ cells, in vitro
  [2026-10-15 · PMID:42612711]. Tetrazine-TCO versus maleimide insertion into
  LNPs gave ~97% GFP+ cells versus <30% for controls and a 3-fold MFI
  difference, in vitro [2026-10-15 · PMID:41615769]. A monomeric
  streptavidin-Fc-binding fusion docked unmodified antibodies onto LNPs and
  gave up to **98%** transfection of primary T cells
  [2026-10-15 · PMID:41178209]. Fc-binding-peptide orientation of anti-PD-L1 on
  siRNA LNPs for glioma [2026-10-15 · PMID:41155935]; an anti-ALFA nanobody EV
  adapter for plug-and-play multi-ligand display, with mouse tumour delivery
  only qualitative, PREPRINT [2026-10-15 · DOI:10.64898/2026.02.28.708726]; a
  FITC-binding scFv "snorkel" for EVs [2026-10-15 · PMID:41421744].
- **Anchor stability is the year's most important newly quantified failure
  mode, and it undercuts the in-vitro numbers above.** DSPE-PEG-mAb **sheds
  from LNPs within 1 h in blood**, while a PCL-b-PEG anchor held the antibody
  over 24 h. PREPRINT. [2026-10-15 · DOI:10.64898/2026.07.02.736109]
- **Ligand density has an optimum** — see §2
  [2026-10-15 · PMID:41834375] [2026-10-15 · PMID:42160160].
- **Formats beyond the LNP.** An antibody-displaying phage T4 co-delivered
  mRNA and a ~507 kDa tetrameric protein into primary human HSCs at up to 20%
  efficiency, PREPRINT [2026-10-15 · PMID:41659505]; chimeric nanobody-lipid
  co-assembly gave PEG-free targeted mRNA LNPs with improved tumour delivery
  and retention [2026-10-15 · PMID:41346710]; antibody/Fab-targeted DNA-LNPs
  raised endothelial expression magnitude, duration and specificity, no fold in
  abstract [2026-10-15 · PMID:41556437]; click-conjugated anti-APN nanobodies
  on LNPs enhanced mRNA delivery to gut epithelium
  [2026-10-15 · PMID:41161497]; scFv-exosomes gave 79.3% tumour-cell uptake
  versus 47.9% for liposomes after nebulization
  [2026-10-15 · PMID:41845388]; anti-HLA-G VHH on EVs loaded with doxorubicin
  or temozolomide improved targeting and xenograft efficacy over free drug,
  demoted 4→3 for efficacy-only readouts
  [2026-10-15 · PMID:41390497]; a nanobody-dendrimer nanomicelle with
  Angiopep-2 crossed a BBB model, demoted 4→3 for unquantified cargo transit
  [2026-10-15 · PMID:41073553]; anti-CD7 nanobody polymersomes delivering
  vincristine with improved survival in an orthotopic T-ALL model, demoted 4→3
  [2026-10-15 · PMID:42253849]; antibody-nanogel conjugates
  [2026-10-15 · PMID:41433257]; gas vesicle nanoparticles
  [2026-10-15 · EPMC:AGR/IND609286246]; a hyaluronan chassis that recruits
  unmodified IgG [2026-10-15 · PMID:41787855].
- **Antibody fragments on viral capsids.** Click chemistry attached defined
  numbers of anti-HER2 nanobody to an AAV capsid and **outperformed genetic
  fusion retargeting** [2026-10-15 · PMID:41625253]. Carried over from the
  30-day set: an anti-mGluR5 nanobody inserted at VP1 T456 of an HSPG-ablated
  AAV-DJ capsid gave eight-fold more transduced hippocampal neurons than
  wild-type AAV-DJ at equivalent titers, by stereotactic injection, so local
  delivery only, PREPRINT [2026-10-15 · DOI:10.64898/2026.09.18.752817].
- **Two negatives that should temper the format enthusiasm.**
  Nanobody-displaying EVs gave only a slight increase in bone-marrow delivery
  and **raised off-target accumulation** [2026-10-15 · PMID:42310937]. In a
  beta-cell system, formulation composition screening produced a **148-fold**
  in-vitro transfection gain while adding an antibody or nanobody contributed
  just **over 2-fold** pancreatic expression — i.e. the chemistry outweighed the
  targeting [2026-10-15 · PMID:42674453].
- **One-pot antibody functionalization of inorganic particles works but says
  little about the antibody.** Tannic-acid grafting of anti-CD44 antibody onto
  PAATiOx nanoparticles gave ~2-fold higher binding to CD44+ cells, 2.4-fold
  (MIAPaCa-2) and 6.5-fold (MDA-MB-231) higher in-vitro internalization, and
  ~2-fold higher in-vivo tumour accumulation (p < 0.05) than unmodified
  nanoparticles. Comparator is an untargeted nanoparticle; one of the three
  least antibody-specific score-5 results (§6).
  [2026-10-15 · PMID:41208811]
- **Route and depot formats are a separate lever on exposure.** A hydrogel
  depot gave 78% relative bioavailability of a subcutaneous trastuzumab-ADC in
  primates with a **7.6-fold lower peak free DM1** than IV. PREPRINT.
  [2026-10-15 · DOI:10.64898/2026.05.21.726796]
- Carried over from the 30-day set: a CD4 nanobody clicked onto LNPs
  transfected up to 48% of non-activated primary human CD4+ T cells and
  delivered CRISPR-Cas9 with up to 32% editing in activated cells, with
  selective association in humanized NSG-SGM3 mice; in-vivo percentages and an
  untargeted comparator number are not in the abstract
  [2026-10-15 · PMID:42764379]. Two targeting antibodies (anti-CD222 plus
  anti-CD5) on one CAR-mRNA LNP served two cell types, ex vivo, no fold-change,
  PREPRINT [2026-10-15 · DOI:10.64898/2026.09.21.753074]. Host-guest
  pretargeting with adamantane-anti-PD-L1 and CB[7]-LNPs carrying IL-2-Fc
  circRNA, confounded by an NLG919 lipid and the cytokine cargo, with no
  fold-enrichment or %ID/g [2026-10-15 · PMID:42839730] — note the year
  provides a cleaner pretargeting number in §1
  [2026-10-15 · PMID:41687816].

## 6. Open problems and conflicting results

The 30-day version of this section held only structural gaps. The year
contains **real paper-versus-paper conflicts**, listed first. Each carries both
citations and one line on what would resolve it. Nothing here is silently
overwritten.

### Stated conflicts

- **Does raising DAR raise delivered payload?** The DAR-raising program
  reports chemistry and potency: DAR 61 [2026-10-15 · PMID:42819270], DAR 8
  past a cited DAR 4 ceiling [2026-10-15 · PMID:41558564], DAR ~23 with
  210-fold lower IC50 in vitro [2026-10-15 · PMID:42570634], DAR 7.92
  [2026-10-15 · PMID:42296596]. Against it, the one paper that measured
  intratumoral **free payload** found DAR4 and DAR8 equal in payload intensity,
  distribution and efficacy, with DAR4 penetrating better
  [2026-10-15 · PMID:41927976], and a site-specific **DAR 4** ADC beat a **DAR
  8** cysteine ADC in vivo [2026-10-15 · PMID:41799094]. These are not strictly
  incompatible — different payloads, targets and ranges — but they point in
  opposite design directions. **What would resolve it:** a copy-number series on
  one binder and one payload, with intratumoral free payload (e.g. MALDI-IMS),
  retained affinity, uptake per cell and clearance reported together, extended
  above DAR 8 rather than stopping there.
- **Are monovalent shuttle formats inherently better?** Much of the TfR1
  oligonucleotide-shuttle work is built monovalent
  [2026-10-15 · DOI:10.64898/2026.08.13.744307, PREPRINT], and fast-dissociating
  intermediate-affinity monovalent VHHs are linked to efficient transcytosis
  [2026-10-15 · PMID:41110474]. The systematic scan explicitly challenges that
  view: bivalent matched monovalent for brain uptake when cell-surface binding
  strength was matched, with prolonged brain exposure and less severe adverse
  effects [2026-10-15 · PMID:41287279]. **What would resolve it:** the same
  matched-surface-binding comparison with a quantified cargo attached — which
  no paper in the year reports.
- **Does high affinity help or hurt?** Picomolar anti-TfR1 nanobodies crossed
  the BBB in humanized rats [2026-10-15 · PMID:41462276], while MD predicts
  strong Fab affinity correlates with poor internalization
  [2026-10-15 · DOI:10.64898/2026.03.13.711720, PREPRINT], and affinity gains
  past a threshold (KD below ~100 nM) stopped improving VHH PK
  [2026-10-15 · PMID:41599718]. **What would resolve it:** an affinity ladder on
  one scaffold and one epitope with delivered cargo, not uptake, as the
  endpoint — and reported as a curve, since the papers above are all consistent
  with a non-monotonic optimum.
- **Is the cargo a passive passenger?** Two independent results say no: ASO
  conjugation raised brain-endothelial binding of low-affinity TfR1 shuttles via
  avidity while *lowering* it for high-affinity ones and delaying transcytosis
  [2026-10-15 · PMID:42332368], and cognate antigen cut FcRn transcytosis of
  sotrovimab by 46.7% versus 23% for B38 [2026-10-15 · PMID:41339598]. If this
  generalizes, every valency/affinity conclusion drawn from *naked* constructs
  (including PMID:41287279) needs re-checking with the cargo attached. **What
  would resolve it:** repeat one valency/affinity matrix with and without the
  intended cargo on the same constructs.
- **Does uptake efficiency matter at all for cleavable payloads?** A cleavable
  ADC payload acted on ERBB2-knockout melanoma with little antibody
  internalization, possibly via extracellular cathepsin L
  [2026-10-15 · DOI:10.64898/2026.10.09.757939, PREPRINT], and binding-to-release
  PhoPEx chemistry deliberately removes the internalization requirement, giving
  5.9-fold higher tumour MMAE AUC than the internalization-dependent
  small-molecule conjugate [2026-10-15 · PMID:42649302]. The whole targeted-uptake
  program (§1, §4, §5) assumes internalization is the bottleneck. **What would
  resolve it:** a non-internalizing-control conjugate with a non-cleavable
  linker run alongside the cleavable one in the same model.

### Converged, and worth stating as settled

- **"More ligand" is not monotonically better.** Independent chassis agree:
  bell-shaped optimum at ~0.1 VHH/100 nm² with receptor degradation as the
  mechanism at excess density [2026-10-15 · PMID:41834375]; lowest of three
  antibody-per-particle densities best [2026-10-15 · PMID:42160160]; low
  nanoshell density gave ~2x avidity [2026-10-15 · PMID:41696244]; ligand
  density tunes liposome retention and penetration
  [2026-10-15 · PMID:41939214]. Treat total ligand density as a parameter with
  an optimum to be found, not maximized.
- **Internalisation is a poor predictor of functional delivery.** Four
  independent results [2026-10-15 · PMID:42272747]
  [2026-10-15 · PMID:42173446] [2026-10-15 · PMID:42286928]
  [2026-10-15 · PMID:42309467].

### Structural gaps (absences, recorded as absences)

- **Loading capability is demonstrated far ahead of delivered-cargo
  measurement, and the year quantifies that claim about itself.** The
  normalisation pass demoted **13** papers from score 4 to 3, and **12** of
  those demotions cite the absence of a delivered-cargo measurement as the
  reason [2026-10-15 · data/2026-10-15-y12 normalisation field]. The demoted
  set: [2026-10-15 · PMID:42332368] [2026-10-15 · DOI:10.21203/rs.3.rs-9664465/v1]
  [2026-10-15 · PMID:41787855] [2026-10-15 · DOI:10.21203/rs.3.rs-8651044/v1]
  [2026-10-15 · PMID:41696244] [2026-10-15 · PMID:41566147]
  [2026-10-15 · PMID:41939214] [2026-10-15 · PMID:42499678]
  [2026-10-15 · PMID:41390497] [2026-10-15 · PMID:41314050]
  [2026-10-15 · PMID:41287279] [2026-10-15 · PMID:41073553]
  [2026-10-15 · PMID:42253849].
- **Cytosolic delivery is still not measured as a fraction.** Four papers reach
  the cytosol or nucleus [2026-10-15 · PMID:41569158]
  [2026-10-15 · PMID:41208769] [2026-10-15 · EPMC:AGR/IND609298393]
  [2026-10-15 · PMID:41127334]; only one attaches a number to a shift it
  attributes to escape (7-fold IC50
  [2026-10-15 · PMID:41569158]). **None reports escaped cargo as a fraction of
  internalised cargo.** **What would resolve it:** a cytosolic-activity reporter
  run in parallel with total uptake on the same construct, so the ratio is the
  reported quantity.
- **Degradation continues to be used where delivery is the claim.** Roughly 15
  of 37 score-3 trafficking papers are degrader chimeras
  [2026-10-15 · report, score-3 trafficking section]; named instances in §4.
  Their assays transfer; their endpoints do not.
- **Targeted-nanoparticle papers still routinely omit the comparator number
  that sizes the gain**, and several defer PK and biodistribution outright
  [2026-10-15 · PMID:42764379] [2026-10-15 · DOI:10.64898/2026.09.21.753074]
  [2026-10-15 · PMID:42839730] [2026-10-15 · PMID:42828315]
  [2026-10-15 · PMID:42764913] [2026-10-15 · DOI:10.64898/2026.02.28.708726].
- **In-vitro targeting gains have an unexamined in-vivo discount.** The >100-fold
  in-vitro association figure [2026-10-15 · PMID:42612711] and the 1-h
  PEG-lipid antibody shedding result
  [2026-10-15 · DOI:10.64898/2026.07.02.736109, PREPRINT] have never been put
  in the same experiment. **What would resolve it:** paired in-vitro and in-vivo
  readouts on one antibody with two anchor chemistries.

### Caveats carried forward for a human reader

- **The three least antibody-specific score-5 results.** Antibody-targeted
  versus untargeted nanoparticle comparisons, meeting the rubric's band-5
  wording but weakest for antibody-intrinsic delivery:
  [2026-10-15 · PMID:41088400] [2026-10-15 · PMID:41117256]
  [2026-10-15 · PMID:41208811]. Beyond those,
  [2026-10-15 · PMID:42649302] has a small-molecule conjugate as its headline
  comparator and [2026-10-15 · PMID:41183201] reports potency rather than
  delivered mass [2026-10-15 · report housekeeping].
- **The DAR scoring boundary is fragile.** Papers sit at score 4 only because
  their abstracts name no baseline DAR: [2026-10-15 · PMID:42819270] (DAR 61),
  [2026-10-15 · PMID:42296596] (DAR 7.92), [2026-10-15 · PMID:42183362]
  (cetuximab DAR 8, PREPRINT). [2026-10-15 · PMID:41558564] reached 5 because it
  names the DAR 4 ceiling it beats. [2026-10-15 · PMID:42157849] (score 4) and
  [2026-10-15 · PMID:42333517] (score 3) sit on opposite sides with similar
  abstract content. A human should check this boundary before treating the
  score tiers as a loading ranking [2026-10-15 · report housekeeping].
- **Strong loading data with no antibody.** Enzyme-loaded LNP, 100 enzymes per
  particle, 15-fold intracellular activity, held at score 3
  [2026-10-15 · PMID:41881071]. It is the best per-particle loading number in
  the set and the most relevant non-antibody benchmark.
- **Cross-run discrepancy to check.** Eight papers that the 30-day seeding run
  kept are **not** in the 12-month run's kept set, despite falling inside its
  window: PMID:42764379, PMID:42839730, PMID:42828315, PMID:42764913,
  DOI:10.64898/2026.10.09.757939, DOI:10.64898/2026.09.21.753074,
  DOI:10.64898/2026.09.18.752817, DOI:10.64898/2026.09.23.753027. Their entries
  above are flagged "carried over from the 30-day set". No cause is inferred
  here; it is a screening-consistency question for a human.
- **Flagged for human read, unchanged:** PMID:42824429, an unflagged
  mini-review on ultrahigh-DAR ADCs — on-thesis for loading but rubric-capped
  and not reviewed [2026-10-15 · report housekeeping].
- **Screening-stringency caveat.** Eleven scouts each screened a month; the
  earliest months (2025-10 to 2026-02) were screened before calibration, so
  their score-3 sets may be slightly more generous. Month-to-month counts
  reflect publication volume, not screening stringency
  [2026-10-15 · report housekeeping]. No trend should be read off the monthly
  distribution of this backfill.

---

## Maintenance log

| Date | Change |
|---|---|
| 2026-10-15 | Seeded by scaffold; no literature folded in yet. |
| 2026-10-15 | First fold-in: 2026-10-15 seeding backfill (17 articles, 7 at score 4-5, 10 at score 3). All six themes populated. Sections 2 and 4 flagged as genuinely thin — no top picks, score-3 papers only, and no endosomal-escape measurement anywhere in the set. Section 6 holds structural gaps rather than paper-vs-paper conflicts; none surfaced this month. Abstract-only evidence throughout. |
| 2026-10-15 | **REBUILD from the 12-month backfill** (`reports/2026-10-15-year.md`; 225 articles, 36 preprints, window 2025-10-12 to 2026-10-15). **This supersedes the 30-day seeding entries above**: they have been folded in, promoted into broader patterns where the year showed the one-month finding to be one instance of several, or retained with their original citations and marked "carried over from the 30-day set" where the 12-month run did not keep the paper (eight such papers, listed in §6). Changes of substance: §2 is **no longer thin** — it now holds a systematic TfR1 affinity/valency/epitope scan (PMID:41287279), a quantitative VHH-LNP avidity optimum with a receptor-degradation mechanism (PMID:41834375), HALA high-avidity/low-affinity co-dosing (PMID:41468362), an ASO-conjugation avidity shift (PMID:42332368) and an affinity-dependent valency/PK threshold (PMID:41599718). §4 is **no longer empty of escape work** — four papers reach cytosol or nucleus and one quantifies a 7-fold escape-attributed gain (PMID:41569158), but **no paper in 225 reports escaped cargo as a fraction of internalised cargo**, so the gap is narrowed and restated rather than closed. §6 gained five real paper-versus-paper conflicts (DAR vs delivered payload; monovalent superiority; affinity direction; cargo as active participant; uptake-dependence for cleavable payloads) plus the year's self-measurement of the delivered-cargo gap: 13 demotions from 4 to 3, 12 of them for the absence of a delivered-cargo measurement. Still abstract-only throughout. |

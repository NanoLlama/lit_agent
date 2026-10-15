# State of the Field — 2026-10-15 (12-month view)

**Scope.** This rests on the 12-month backfill: 225 kept articles from
2025-10-12 to 2026-10-15, 36 of them preprints, 13 at score 5 and 50 at 4, all
screened from abstracts with no full text fetched [cumulative header]. It
supersedes `state_of_field_2026-10-15.md`, which rested on 30 days and 17
articles and said so; that file is left in place as the record of what a month
looked like. A year is enough to argue about direction. It is not enough to
call a trend from month-to-month counts, which in this backfill reflect
publication volume and pre-calibration screening drift rather than the field
[cumulative §6, screening-stringency caveat].

## Testing the one-month claim

The 30-day synthesis argued that **loading capability has outrun
delivered-cargo measurement**. Against a year, that claim **survives, but in a
changed and more useful form**. Two pieces of the year's evidence cut in
opposite directions, and the resolution is the most important thing in this
document.

**It strengthens, as a description of the literature's habits.** The year's own
normalisation pass is the cleanest evidence anyone could ask for: re-scoring
100 articles against a single standard demoted 13 papers from score 4 to 3, and
**12 of those demotions name the absence of a delivered-cargo measurement as
the reason** [cumulative §6]. That is not an outside critic's judgement; it is
the pipeline discovering, while trying to be consistent, that "no delivered
cargo" is the single most common reason a promising paper cannot be ranked
highly. The demoted set spans the whole field — a systematic TfR1
affinity/valency/epitope scan, a CD44 transcytosis degrader, three
ligand-density studies, two targeted-vesicle papers, an antibody-siRNA-exatecan
conjugate [cumulative §6]. The habit is structural, not a few authors' choice.

**But the simple form of the claim is wrong, because the measurement does
exist — and when it is made, the loading gains largely fail to appear.** This is
the year's genuine news. MALDI imaging of intratumoral **free payload** found
DAR4 and DAR8 ADCs indistinguishable in payload intensity, distribution and
efficacy at dose-matched payload, with DAR4 penetrating *better*
[cumulative §3 · PMID:41927976]. A site-specific DAR 4 conjugate beat a
cysteine DAR 8 conjugate in vivo [cumulative §3 · PMID:41799094]. In
pretargeted imaging, the one study that reported a loading series alongside a
delivered-cargo number found the highest stochastic loading gave top tumour
uptake (10.4 %ID/g) while site-specific loading bought tumour-to-blood ratio
instead [cumulative §3 · PMID:41705578]. And a site-specific versus random
single-domain-antibody comparison found **comparable** tumour uptake (3.7 vs
3.4 %IA/g), with the real gain being reduced kidney retention
[cumulative §3 · DOI:10.21203/rs.3.rs-9664465/v1, preprint].

So the honest restatement is this: **loading has outrun its own justification.**
The capability is real — DAR 61 with retained binding and endocytosis
[cumulative §3 · PMID:42819270], DAR 8 past a cited DAR 4 ceiling with an
unmodified clinical payload [cumulative §3 · PMID:41558564], DAR ~23 at a
210-fold lower in-vitro IC50 than mirvetuximab soravtansine
[cumulative §3 · PMID:42570634], DAR 7.92 at under 1% aggregation
[cumulative §3 · PMID:42296596]. But the papers that raise copies per antibody
and the papers that measure delivered payload are disjoint sets, and the
measuring set reports that copies stop mattering around 4-8. The field has not
contradicted the high-DAR program; it has declined to test it, in a window where
it demonstrably knows how.

**A third qualification, which the brief's housekeeping forces.** Three of the
13 score-5 results are antibody-targeted-versus-**untargeted-nanoparticle**
comparisons [cumulative §6 · PMID:41088400, PMID:41117256, PMID:41208811].
Their numbers are real (~4x brain distribution and 10x cargo *expression* for
VCAM-LNPs; 1.7-2x in vitro and 1.5x in vivo uptake from uPAR clustering;
2.4-6.5x internalisation and ~2x tumour accumulation from tannic-acid antibody
grafting) but their comparator is a particle with no targeting ligand at all —
a low bar that says little about antibody-intrinsic delivery. Add that the
PhoPEx result's headline comparator is a small-molecule conjugate rather than an
antibody [cumulative §4 · PMID:42649302], and that the multivalent
nanobody-zanamivir result reports protection potency rather than mass
[cumulative §2 · PMID:41183201], and nearly half the top tier is weaker as
antibody-delivery evidence than its score implies. **The top of the evidence
pile is thinner than the count suggests, and it is thin in the same direction:
toward surrogates.**

## Where the real gains were measured

If copies per antibody did not produce the year's measured gains, what did?
**Exposure, retention and dose-sparing** — and they were measured in tissue.

- A cleavable PEG mask on a nanobody-sialidase conjugate: **144-fold** longer
  systemic half-life, **9.3-fold** higher tumour accumulation
  [cumulative §1 · PMID:42241306].
- A TfR1 Fab fused to aducanumab: higher and more homogeneous brain
  distribution by whole-hemisphere light-sheet imaging, with a **five-fold
  lower dose** matching plaque reduction [cumulative §1 · PMID:41310626].
- Inhaled pIgR-stem nanobody bispecifics effective at **one-tenth** the
  intraperitoneal comparator dose [cumulative §1 · PMID:42496279].
- A HER2 antibody-nanogel matching T-DM1 efficacy with **4-fold less antibody**
  [cumulative §3 · PMID:41433257].
- An anti-EGFR/anti-PEG bispecific **more than tripling** tumour retention of a
  212Pb nanocarrier over the untargeted material, by SPECT and gamma counting
  [cumulative §1 · PMID:41687816].

Three of those five are dose-sparing inferred from efficacy rather than mass,
and the papers say so. But the pattern is consistent: the lever that moved
delivered cargo this year was **how long the conjugate is available and where it
goes**, not how much it carries. The loading literature and the delivery
literature are optimising different variables, and only the second one is
currently winning.

## What is converging

**Non-monotonicity is now the field's most reproducible design rule.** Four
chassis, four groups, same shape: a bell-shaped VHH-LNP delivery optimum at
~0.1 VHH per 100 nm² with excess density inducing receptor degradation
[cumulative §2 · PMID:41834375]; the lowest of three antibody-per-particle
densities (~340 vs 760 vs 1200) best for uptake and bone-marrow accumulation
[cumulative §2 · PMID:42160160]; low nanoshell density giving ~2x the avidity of
high [cumulative §2 · PMID:41696244]; ligand density tuning liposome retention
and penetration [cumulative §2 · PMID:41939214]. Treating density, valency or
affinity as something to maximise is now the identifiable amateur move.

**Uptake has been retired as an endpoint, by four independent results.**
Antibody-LNP internalisation did not predict mRNA translation in primary T and
B cells [cumulative §4 · PMID:42272747]; receptor internalisation *rate*, not
abundance, determined CD7-targeted LNP delivery
[cumulative §4 · PMID:42173446]; ADC internalisation and lysosomal degradation
are temporally uncoupled [cumulative §4 · PMID:42286928]; a normalised
internalisation metric outranked antigen abundance and affinity for predicting
ADC potency at matched loading [cumulative §4 · PMID:42309467]. This is a
quiet, important consolidation: the surrogate the field used for a decade has
been shown to be a bad one, four times, in one year.

**The shuttle-receptor problem is no longer TfR1-only, and TfR1 reached
patients.** A TfR1 antibody-oligonucleotide conjugate lowered DMPK mRNA 37-46%
in human muscle biopsies [cumulative §1 · PMID:41707138], while CD98hc, a
carbonic-anhydrase-IV small-molecule shuttle, IGF1R, LRP1 and pIgR each carried
cargo across a barrier in vivo in this window [cumulative §1]. The design rule
that recurs across receptors is kinetic rather than thermodynamic: fast
dissociation and pH sensitivity, not affinity magnitude
[cumulative §1 · PMID:41110474, PMID:41737496, PMID:41287279].

## What is stuck

**Cytosolic delivery is still not a measured quantity.** The 30-day digest
recorded that nothing measured escape. The year corrects that — four papers
reach cytosol or nucleus, and one attaches a number to a shift it attributes to
endosome-to-cytosol import, a 7-fold silencing improvement from IC50 200 to
28 nM [cumulative §4 · PMID:41569158, PMID:41208769,
EPMC:AGR/IND609298393, PMID:41127334]. But **not one of the 225 reports escaped
cargo as a fraction of internalised cargo** [cumulative §6]. The absence moved
from "nobody studies escape" to "nobody reports escape in a unit that can be
compared across papers", which is a smaller gap and a more fixable one.

**Valency conclusions are being drawn from constructs that carry no cargo.** The
year's best valency experiment concluded that bivalent anti-TfR1 matches
monovalent for brain uptake at matched cell-surface binding strength, with
longer exposure and milder adverse effects — explicitly challenging monovalent
orthodoxy [cumulative §2 · PMID:41287279]. In the same year, a separate group
showed that **conjugating an ASO raises brain-endothelial binding of
low-affinity shuttles via avidity while lowering it for high-affinity ones, and
delays transcytosis** [cumulative §2 · PMID:42332368]. Both cannot be safely
applied at once: the first ranks naked formats, the second says the cargo
changes the ranking. The field is writing design rules for molecules it does not
intend to dose. The same point lands on FcRn, where an antibody's own cognate
antigen cut transcytosis by 46.7% [cumulative §1 · PMID:41339598].

**Targeted-carrier papers still omit the comparator that sizes the gain**, and
the year supplies the reason it matters: in a beta-cell system, formulation
composition screening produced a 148-fold in-vitro transfection gain while
adding an antibody or nanobody contributed just over 2-fold pancreatic
expression [cumulative §5 · PMID:42674453]; nanobody-displaying EVs raised
off-target accumulation while barely improving bone-marrow delivery
[cumulative §5 · PMID:42310937]. And the in-vitro numbers may be structurally
optimistic: DSPE-PEG-mAb **sheds from LNPs within 1 h in blood** while a
PCL-b-PEG anchor holds for 24 h [cumulative §5 ·
DOI:10.64898/2026.07.02.736109, preprint] — a preprint that, if it holds,
discounts a large slice of this literature.

## What nobody is doing

Four experiments the year did not contain, in descending order of how much they
would change the picture.

1. **Cargo per milligram of antibody, across formats, in one hand.** Three
   platforms claim antibody-sparing or high loading in incomparable units — DAR
   61 with no PK reported, a nanogel with 4-fold antibody-sparing and an
   unreported DAR, a DAR ~23 polymer with only in-vitro potency
   [cumulative §3 · PMID:42819270, PMID:41433257, PMID:42570634]. Nobody has
   put them on one antibody, one payload and one model with antibody mass as the
   normaliser.
2. **A valency × affinity matrix built twice, with and without the cargo.** The
   constructs for one half exist [PMID:41287279]; the assay for the other half
   exists [PMID:42332368]. The result would settle a conflict currently recorded
   as open [cumulative §6].
3. **An escaped fraction, reported as a fraction.** Any format, any cargo. The
   unit is the contribution.
4. **A copy-number series extended above DAR 8 with intratumoral free payload
   measured.** The measurement method is published
   [cumulative §3 · PMID:41927976] and stops at DAR 8; the chemistry is
   published [PMID:42819270] and starts above it. The two have never met.

The one-month synthesis ended by saying that until someone ran a copy-number
series with delivered cargo, "higher DAR remains a chemistry claim rather than
a delivery claim." A year later that still stands — but the sentence now has
teeth it did not have in October, because the delivery claim has been tested at
DAR 4 versus 8 and **failed**. The burden has shifted. The high-DAR program is
no longer waiting for someone to confirm it; it is waiting to explain a negative
result obtained one rung below where it operates.

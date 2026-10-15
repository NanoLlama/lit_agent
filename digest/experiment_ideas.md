# Experiment Ideas

Maintained by the **strategist** agent. Re-ranked weekly.

> These are **discussion prompts, not protocols.** Every one needs verifying
> against the primary papers before anyone sets up a bench experiment. The
> motivation citations are the starting point for that check.

IDs are stable and never reused or renumbered. Statuses: `new`, `refined`,
`tested`, `scooped`, `dropped`.

Flags: **`[COMBINATION]`** joins findings from two or more papers that did not
cite each other (most likely to be novel) · **`[CONTRADICTED]`** premise
undercut by newer work · **`[SCOOPED]`** essentially done by someone else.

---

## Current ranking

Ideas 1–4 are seeds written from the project's standing focus, not from
literature this pipeline has read. They have no citations yet and exist to give
the strategist something to refine, confirm, or drop on the first real run. The
ranking below is provisional for the same reason.

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
- **Motivation:** seed idea — no citations yet.
- **Difficulty:** med
- **Status:** new
- **Notes:** 2026-10-15 seeded. Needs a literature check first: the matched-
  affinity version of this comparison may already exist.

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
- **Motivation:** seed idea — no citations yet.
- **Difficulty:** med
- **Status:** new
- **Notes:** 2026-10-15 seeded. The ladder is the cost here; check whether a
  published variant panel can be reused.

### 3. Multi-payload linkers without losing receptor engagement
- **Hypothesis:** Branched or dendrimer linkers can raise cargo copies per
  nanobody several-fold before binding, receptor engagement, or clearance
  degrade enough to cancel the gain.
- **Test:** One site-specific conjugation handle, a payload-per-molecule
  series, holding the binder constant. Measure where the curve turns over.
- **Readout:** Cargo copies per molecule (mass spectrometry), retained binding
  affinity, uptake per cell, and clearance — the gain is only real if all four
  are reported together.
- **Motivation:** seed idea — no citations yet.
- **Difficulty:** high
- **Status:** new
- **Notes:** 2026-10-15 seeded. Most directly on the project's thesis; also the
  most likely of the four to be partly published already.

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
- **Status:** new
- **Motivation:** seed idea — no citations yet.
- **Notes:** 2026-10-15 seeded. Toxicity of escape agents is the obvious
  confound; the control is the conjugate without cargo.

---

## Dropped / scooped

*Nothing yet.* Ideas are never deleted — they get a status and a reason, so an
idea that becomes relevant again keeps its history.

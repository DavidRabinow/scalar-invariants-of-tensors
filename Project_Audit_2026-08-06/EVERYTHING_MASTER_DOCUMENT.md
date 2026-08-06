# EVERYTHING MASTER DOCUMENT
## Scalar Invariants / 6D Reproduction / 10D Chiral 5-Form Project

**Generated:** 2026-08-06 13:37:49Z  
**Purpose:** One giant consolidated document containing the audit, research logs, literature gate, catalogs, Python outputs, claims, tests, and file locations.  
**Existing separate files are kept unchanged.** This is an additional mega-document.

**Primary folders:**
- Mathematica Research: `/Users/davidrabinow/Downloads/26-27 Prep/Stux Technologies/Research`
- Python MIT original: `/Users/davidrabinow/Projects/UPRSXxXCEL/Research/scalar-invariants-of-tensors/MIT`
- This bundle copy: `/Users/davidrabinow/Downloads/26-27 Prep/Stux Technologies/Research/MIT_Code_And_Audit_Bundle_2026-08-06`

---

# TABLE OF CONTENTS

1. Quick status (yes/no)
2. Where every important file lives
3. Full forensic audit report
4. Claims register (CSV)
5. Test register (CSV)
6. File manifest (CSV)
7. RESEARCH_LOGv4 (Stages 1–5)
8. 10D representation / literature gate
9. Degree-6 catalog CSV
10. Degree-8 invariant formula catalog (TXT)
11. Degree-8 formula catalog CSV
12. Python 6D outputs (generators, ranks)
13. Python 6D/10D reports
14. Python smoke rerun
15. SHA-256 digests (Research top-level)
16. Appendix: key Mathematica module headers / excerpts
17. Appendix: paper equation reminders

---

# 1. QUICK STATUS

## 6D paper reproduction
**YES — essentially complete** (Mathematica Gates 1–5 observed; Python blind discovery matches `[2,4,4,6,8]`).

## 10D chiral 5-form full classification
**NO — incomplete.** Strong low-degree Mathematica work through degree 8; degree-10 foundations only; Python 10D is smoke/self-duality only; Krull 81 and completeness unresolved.

| Workstream | Est. completion (non-exact) |
|---|---|
| 6D reproduction | 85–95% |
| 10D low-degree (≤8) | 55–70% |
| Full 81-parameter project | 5–15% |

---

# 2. WHERE EVERY IMPORTANT FILE LIVES

## Open these first
1. This file: `/Users/davidrabinow/Downloads/26-27 Prep/Stux Technologies/Research/MIT_Code_And_Audit_Bundle_2026-08-06/EVERYTHING_MASTER_DOCUMENT.md`
2. Audit PDF: `/Users/davidrabinow/Downloads/26-27 Prep/Stux Technologies/Research/MIT_Code_And_Audit_Bundle_2026-08-06/Project_Audit_2026-08-06/TenD_SelfDual_FiveForm_Project_Audit.pdf`
3. Mathematica `.wl` files: one level up in `/Users/davidrabinow/Downloads/26-27 Prep/Stux Technologies/Research`

## Bundle layout
```
MIT_Code_And_Audit_Bundle_2026-08-06/
  EVERYTHING_MASTER_DOCUMENT.md   ← this file
  WHERE_EVERYTHING_IS.txt
  Project_Audit_2026-08-06/       ← full audit package
  python_mit/                     ← Python code + outputs copy
```

## Mathematica Research (parent folder) — key files
- AntisymmetricPForms.wl
- MetricContractions6D.wl
- FunctionalIndependence6D.wl
- AppendixRelations6D.wl
- GraphEnumeration6D_FIXED.wl
- InvariantBenchmarks_CORRECTED_V2.wl
- TenDLorentzianFoundations_V2.wl
- TenDRepresentationTargets.wl
- TenDDegree4Invariants_V4.wl
- TenDDegree6* (enum, trace, N1050_V2, catalog_V2, batches)
- TenDDegree8* (enum, discovery A–D, basis validation, formula catalog)
- Degree8CanonicalGraphKeys.wl
- TenDDegree10Foundations_V1.wl
- RESEARCH_LOGv4.md
- TenDChiralFiveForm_Representation_Literature_Gate.md
- TenDDegree6Catalog.csv
- TenDDegree8InvariantFormulaCatalog.csv / .txt

## MISSING (important)
- TenDDegree6ContractionPlanning_V1.wl (required by Batch A; ABSENT)

## Do not use (superseded)
- GraphEnumeration6D.wl (use _FIXED)
- InvariantBenchmarks.wl (use _CORRECTED_V2)
- TenDLorentzianFoundations_V1.wl (use V2)
- TenDDegree4Invariants_V1–V3 (use V4)
- TenDDegree6Catalog_V1.wl (wrong K6 sign; use V2)
- docs/invariants_78.json in MIT (not validated science)

---

# 3. FULL FORENSIC AUDIT REPORT

# TenD Self-Dual Five-Form Project Audit

**Document title:** TenD_SelfDual_FiveForm_Project_Audit  
**Audit date:** 2026-08-06  
**Auditor role:** forensic technical audit (documentation and provenance only)  
**Nondestructive:** no existing project files were modified, renamed, moved, overwritten, or deleted.  
**Outputs directory:** `Project_Audit_2026-08-06/`  

**Scopes inspected:**
1. Mathematica Research folder: `/Users/davidrabinow/Downloads/26-27 Prep/Stux Technologies/Research/`
2. Python MIT repository: `/Users/davidrabinow/Projects/UPRSXxXCEL/Research/scalar-invariants-of-tensors/MIT/`

**Primary papers:**
- Elamaran–Ferko–Scarlett, *Machine Learning Invariants of Tensors*, arXiv:2512.23750 (local PDF present).
- Cederwall–Hutomo–Kuzenko–Lechner–Sorokin, *Some remarks on invariants*, arXiv:2509.14350 (cited in project notes; **no local PDF found** in Research folder).
- Hutomo–Lechner–Sorokin, *On non-linear chiral 4-form theories in D=10*, arXiv:2509.14351 (cited; **no local PDF found**).

**Mathematica availability to auditor:** `wolframscript` / `math` **not found**. Therefore Mathematica modules are classified **OBSERVED RUN** when RESEARCH_LOG / exported catalogs / TestReport design strongly indicate prior execution, **not** RERUN PASSED.

**Python availability:** smoke rerun performed 2026-08-06 (graphs N=2,4,6; blind discovery through degree 6; self-duality). Result: `SMOKE_OK` (see `supporting/rerun_smoke.txt`).

---

## 1. Executive summary

### Ultimate research question

What are the independent Lorentz-scalar polynomial invariants of a real self-dual (chiral) 5-form \(F=*F\) in ten-dimensional Lorentzian spacetime, what are their degrees and generating structure, and what are the syzygies among candidate contractions—starting from a validated reproduction of the six-dimensional Euclidean 3-form analysis of Elamaran–Ferko–Scarlett?

### Strongest current 6D result

**Strongest claim that is well supported:** the project has reproduced, in **exact Mathematica arithmetic** (Gates 1–5, as recorded in `RESEARCH_LOGv4.md`) and independently in a **Python blind discovery path** (`tensor_invariants` / `outputs/6d/`), the paper’s connected graph counts \((1,2,6,20)\), same-degree ranks \((1,2,3,6)\), and generator-degree pattern \([2,4,4,6,8]\) for metric-only contractions of a generic antisymmetric 3-form in Euclidean \(d=6\). Exact Jacobian rank 5 for the five paper polynomials and exact vanishing of Appendix A relations on finite integer holdouts are recorded for Mathematica. Python discovery ranks are primarily SVD with modular syzygy checks.

### Strongest current 10D result

**Strongest claim that is well supported in code artifacts:** Lorentzian self-duality conventions with \(\star^2=+1\), 252 generic / 126 chiral components; degree-4 recovery of a 1-dimensional invariant space identified with \(I_4=\mathrm{tr} M^2\); degree-6 census \(12043\) labeled / \(54\) canonical / \(49\) connected with two independent directions (trace and \(N^{(1050)}\)); degree-8 Burnside census \(1753\) canonical (\(1689\) connected) with a **seven-dimensional** validated basis including \(I_4^2\) and six named graphs; degree-10 **foundations only** validating the two lower products and stating a conditional target of 12 new directions. These 10D computational claims are **OBSERVED RUN** from Mathematica sources/exports; they were **not** rerun by this auditor. The Python 10D path has **no generators**.

### Maximum degree investigated

- **6D:** through degree 8 exactly (graphs/ranks); Appendix relations at 6 and 8; paper stabilization through 18 is **cited but not shown as executed** in RESEARCH_LOG Stages 1–5. Python checked \(n_{\mathrm{new}}=0\) at degree 10 on a **sample** of 12 graphs.
- **10D:** foundations through degree 10 products; graph discovery through degree 8; **no** degree-10 graph enumeration completed.

### What has / has not been established

| Established (with caveats) | Not established |
|---|---|
| 6D paper graph counts & ranks (exact MMA; Python match) | Completeness of 6D five-generator set as full invariant ring |
| 6D five polys algebraically independent (exact Jacobian) | Symbolic proof of Appendix A identities |
| 10D conventions / self-duality | Independent proof of Krull dimension 81 |
| 10D low-degree Hilbert **targets** copied/checked as integers | That metric-only graphs exhaust \(SO(1,9)\) invariants |
| Degree-8 seven-direction finite-sample certificate (claimed) | Reduction of all 1753 degree-8 graphs; degree-10 generators |
| | Full syzygy resolution; Hironaka decomposition; 81-parameter structure |

### Most important methodological risk

**Matching a published singlet dimension (e.g. 7 at degree 8) using metric-only graph evaluation does not by itself prove that every \(SO(1,9)\) scalar built with Levi-Civita tensors reduces to the metric-only span after \(F=*F\).** Without an explicit epsilon-reduction certificate for the project’s conventions, Hilbert agreement is **conditional evidence of completeness**, not a proof. Secondary risks: Mathematica **kernel-state contamination** across `Get` chains; **missing** `TenDDegree6ContractionPlanning_V1.wl`; Python 6D discovery using **SVD** as primary truth; degree-10 claims easily overstated as “12 generators found” when only product rank 2 was validated.

### Estimated completion ranges (not mathematical measurements)

| Workstream | Estimated range | Rationale |
|---|---|---|
| 6D reproduction vs arXiv:2512.23750 §4.1 + App. A | **85–95%** | Counts, ranks, independence, App. A holdouts done; stabilization through 18 and symbolic identities incomplete |
| 10D low-degree study (deg ≤8 vs Cederwall targets) | **55–70%** | Deg 4/6/8 substantial Mathematica work + catalogs; not auditor-rerun; epsilon/SO gap; missing planning file |
| Complete ultimate project (81-parameter generators+syzygies) | **5–15%** | Only low degrees; no deg-10 discovery; no full syzygies; no completeness proof |

---

## 2. Complete file inventory

Machine-readable full inventory: `TenD_Project_File_Manifest.csv` (204 rows + missing dependency). SHA-256 digests: `supporting/sha256_all_research.txt`, `supporting/sha256_mit_core.txt`.

### 2.1 Mathematica modules (current recommended chain)

**Use these (latest):**
`AntisymmetricPForms.wl` → `MetricContractions6D.wl` → `FunctionalIndependence6D.wl` → `AppendixRelations6D.wl` → `GraphEnumeration6D_FIXED.wl` → `InvariantBenchmarks_CORRECTED_V2.wl` → `TenDLorentzianFoundations_V2.wl` → `TenDRepresentationTargets.wl` → `TenDDegree4Invariants_V4.wl` → `TenDDegree6TraceInvariant_V1.wl` + `TenDDegree6N1050Invariant_V2.wl` + `TenDDegree6GraphEnumeration_V1.wl` + `TenDDegree6Catalog_V2.wl` → `TenDDegree8GraphEnumeration_V1.wl` + `Degree8CanonicalGraphKeys.wl` + discovery batches + `TenDDegree8BasisValidation_V1.wl` + `TenDDegree8FormulaCatalog_V1.wl` → `TenDDegree10Foundations_V1.wl`.

**Do not use (obsolete / superseded):**
`GraphEnumeration6D.wl`; `InvariantBenchmarks.wl`; `TenDLorentzianFoundations_V1.wl`; `TenDDegree4Invariants_V1–V3.wl`; `TenDDegree6N1050Invariant_V1.wl`; `TenDDegree6GraphBasis_FinalK6_V1.wl`; `TenDDegree6Catalog_V1.wl` (wrong K6 sign); duplicate RESEARCH_LOG copies (byte-identical).

**Missing but required by Batch A:** `TenDDegree6ContractionPlanning_V1.wl` — **ABSENT**. Status: **NOT RUN** / broken dependency for clean-kernel Batch A.

**Named in audit brief but absent:** `MetricContractions6D_FIXED.wl`, `MetricContractions6D_FINAL.wl`, `TensorContractionOrderingFix.wl` (axis fix absorbed into `MetricContractions6D.wl` / Gate 3 narrative).

### 2.2 Notebook

`6D_3Form_Project.nb`: Mathematica notebook (Wolfram 15.0). Heuristic parse: 6 `Cell[` markers; **0** `VerificationTest` strings; **not** a reliable stored TestReport archive. Status: **UNKNOWN** for scientific outputs. Do not infer Gate results from this notebook alone.

### 2.3 Python MIT package

Primary science: `tensor_invariants/`, `run_pipeline.py`, `outputs/6d/`, `outputs/10d/`, `reports/`.  
Legacy (ops / superseded for discovery): `src/invariants/`, `src/invariant_engine/`, `scripts/run_6d.py`.  
Do not treat `docs/invariants_78.json` as validated 10D science.

---

## 3. Chronological research log

| When | Event | Outcome |
|---|---|---|
| 2026-08-03 | Stage 1: AntisymmetricPForms | 5/5 exact tests OBSERVED |
| 2026-08-03 | Stage 2: MetricContractions; **AssociationMap** bug | Fixed to `Map[evaluate,…]`; 5/5 then 8 substantive True |
| 2026-08-03 | Stage 3: Jacobian; **0^0 Indeterminate**; then **rank-4** because \(x^{(6)}\) was \(X_1^{(6)}\) | Axis-order / RaiseTensorIndex fix; rank 5; A.2a residual 0 |
| 2026-08-03 | Stage 4: Appendix relations | 7/7; 12 integer holdouts seed 20260804 |
| 2026-08-03 | Stage 5: Graph enum; **IncidenceGraph** name collision | FIXED module; counts 1,2,6,20; ranks 1,2,3,6 |
| 2026-08-03 | Literature gate for 10D | Hilbert/Euler/81 sourced; computational 10D **not yet** |
| 2026-08-03 | Lorentzian V1→V2; Degree4 V1→V4 | Component keys; diagonal raise Dot; Transpose Ordering |
| 2026-08-03→05 | Degree6 enum/trace/N1050/batches/catalog | 12043/54/49; K6 sign corrected V2 |
| 2026-08-05→06 | Degree8 Burnside, keys, discovery A–D, basis validation, formula catalog | 1753; basis 7 directions; CSV/TXT export |
| 2026-08-06 01:00 | TenDDegree10Foundations_V1.wl | Product subspace module authored |
| 2026-08-06 ~01:12–09:07 | Python MIT package + pipeline | Blind 6D PASS outputs; 10D smoke only |

`RESEARCH_LOG.md`, `_2`, `v3`, `v4` are **byte-identical** (MD5 `431f853d…`) and stop at Stage 5 / Module 6 plan—they **do not** document 10D degree work. Provenance for 10D is filename versions + exported catalogs + module Print banners.

---

## 4. Reconstruction of the paper’s method (arXiv:2512.23750 §§2–4)

### Encoding and enumeration
Contractions of an antisymmetric \(p\)-form with the metric are encoded as **loopless weighted multigraphs** with vertex weighted degree \(p\) (for 3-forms: 3-regular). Edge weight = number of contracted index pairs. Self-loops are excluded by antisymmetry. The paper prefers **connected** graphs; disconnected graphs factorize into products (secondary / composite invariants).

### Isomorphism and evaluation
Graphs are reduced up to isomorphism (paper: VF2-style). Random tensors are sampled; contractions evaluated; **fixed-degree** linear dependence is extracted from numerical evaluation matrices (paper: floating-point **SVD** nullspaces). New primary generators are those independent of **polynomials in lower-degree invariants**. Syzygies are reconstructed from null vectors and validated on fresh samples. Stabilization over several degrees is **heuristic evidence**, not a completeness proof (§ paper discussion / project RESEARCH_LOG caution).

### Project differences from the paper
| Paper | This project |
|---|---|
| Floating-point SVD discovery | Mathematica exact/modular ranks; Python SVD + modular syzygies |
| igraph isomorphism | MMA `CanonicalGraph` incidence encoding; Python NetworkX / min-lex |
| Numerical syzygy rationalization | Exact holdouts (MMA App. A); Python CRT/Farey candidates |

---

## 5. Six-dimensional reproduction

### Definitions (paper Eqs. (4.1)–(4.4); Mathematica `MetricContractions6D.wl`)

\[
\begin{aligned}
x^{(2)} &= H_{abc}H^{abc},\\
x^{(4)}_1 &= H_{abc}H_{ade}H^{def}H^{bc}{}_{f},\\
x^{(4)}_2 &= H_{abc}H_{ade}H^{cef}H^{bd}{}_{f},\\
x^{(6)} &= H_{abc}H^{chi}H_{ghi}H^{adg}H_{def}H^{bef},\\
x^{(8)} &= H_{abc}H^{bci}H_{ghi}H^{gjk}H_{jkl}H^{fhl}H_{def}H^{ade}.
\end{aligned}
\]

(Index raising with Euclidean \(\delta\).) Mathematica stores contraction specs as paired index lists, e.g. `"x^(2)" -> {{"a","b","c"},{"a","b","c"}}`.

### Counts vs paper §4.1

| Degree | Connected graphs (paper) | Project MMA Gate5 | Project Python |
|---:|---:|---:|---:|
| 2 | 1 | 1 | 1 |
| 4 | 2 | 2 | 2 |
| 6 | 6 | 6 | 6 |
| 8 | 20 | 20 | 20 |

| Degree | Connected rank (paper) | MMA | Python |
|---:|---:|---:|---:|
| 2 | 1 | 1 | 1 |
| 4 | 2 | 2 | 2 |
| 6 | 3 | 3 | 3 |
| 8 | 6 | 6 | 6 |

| Degree | New gens after products | Python blind |
|---:|---:|---:|
| 2 | 1 | 1 |
| 4 | 2 | 2 |
| 6 | 1 | 1 |
| 8 | 1 | 1 |
| 10 | 0 (paper) | 0 on sample of 12 |

Final degrees: **\([2,4,4,6,8]\)**.

### Jacobian / modular / Appendix
- Exact Jacobian \(5\times20\) rank **5** over \(\mathbb{Q}\) and primes \(1000003,1000033,1000037\) (Gate 3) — **REPRODUCED COMPUTATIONALLY WITH EXACT ARITHMETIC** (OBSERVED RUN).
- Appendix (A.2a),(A.2b),(A.4),(A.6) exact zero on 12 holdouts (Gate 4) — **FINITE-SAMPLE EVIDENCE ONLY** (exact arithmetic on samples ≠ symbolic proof).
- Stabilization through degree **18**: stated in paper; **not executed** in RESEARCH_LOG Stages 1–5.

### Evidence labels for 6D headline
- Graph counts: **REPRODUCED COMPUTATIONALLY WITH EXACT ARITHMETIC** (MMA) + **RERUN PASSED** for N≤6 Python smoke.
- Algebraic independence of five polys: **REPRODUCED COMPUTATIONALLY WITH EXACT ARITHMETIC** (Jacobian) ⇒ independence in characteristic zero at tested point; **not** completeness.
- Python blind \(n_{\mathrm{new}}\): **SUPPORTED ONLY BY FLOATING-POINT NUMERICS** (SVD), cross-checked by tests.

---

## 6. Benchmarks

`InvariantBenchmarks_CORRECTED_V2.wl` (12 VerificationTests; OBSERVED RUN): one/two vectors under \(O(d)\); real antisymmetric 2-form in 4D under \(SO(4)\) and \(O(4)\).

**Pfaffian:** \(P=\frac18\epsilon_{abcd}F^{ab}F^{cd}\) is an \(SO(4)\) invariant. Under orientation-reversing \(O(4)\) elements, \(\epsilon\) flips sign, so \(P\) is a **pseudoscalar** (changes sign) and is **not** an \(O(4)\) invariant. The corrected module’s TestID explicitly distinguishes \(SO(4)\) from \(O(4)\). Earlier `InvariantBenchmarks.wl` had a missing `Dot` (`DiagonalMatrix[…] Reverse[…]`) and is **SUPERSEDED**.

No separate self-dual 3-form benchmark module beyond this path was identified as current.

---

## 7. Ten-dimensional mathematical formulation

### Conventions (project)
- Metric: \(\eta=\mathrm{diag}(-1,+1^{\times9})\) (mostly plus).
- Indices: \(0,\ldots,9\); time = 0.
- Orientation: \(\epsilon_{0123456789}=+1\).
- Hodge: \((*F)_{\mu_1\ldots\mu_5}=\frac1{5!}\epsilon_{\mu_1\ldots\mu_5\nu_1\ldots\nu_5}F^{\nu_1\ldots\nu_5}\).
- Chirality: \(F=*F\).

### \(\star^2\) formula
\[
\star^2 = (-1)^{p(D-p)+t}.
\]
For \((D,p,t)=(10,5,1)\): \(p(D-p)+t=25+1=26\) even ⇒ \(\star^2=+1\) ⇒ real \(\pm\) eigenspaces of dimension \(252/2=126\).  
Euclidean \(t=0\): \(\star^2=-1\) ⇒ eigenvalues \(\pm i\); **no** nonzero real self-dual 5-form.

### Group-theoretic facts
- \(\dim SO(1,9)=45\).
- \(126-45=81\) equals the Krull dimension **only if** the generic stabilizer is trivial — **STATED IN A CITED PRIMARY SOURCE** (Cederwall et al.), **UNRESOLVED** as an independent project proof.
- Orientation reversal in \(O(1,9)\) exchanges chiralities ⇒ fixed-chirality problem is naturally \(SO(1,9)\), not full \(O(1,9)\).
- Quadratic \(F_{\mu_1\ldots\mu_5}F^{\mu_1\ldots\mu_5}=0\) for self-dual odd middle forms — **ESTABLISHED ANALYTICALLY** (and cited).

### Distinctions
Chiral 4-form potential \(A_4\) ≠ field strength \(F_5=dA_4\) ≠ generic 5-form ≠ self-dual projection. Invariant Lagrangians without derivatives are polynomials in \(F_5\).

---

## 8. Representation-theory targets

From `TenDChiralFiveForm_Representation_Literature_Gate.md` and `TenDRepresentationTargets.wl` (checks series conversion; does **not** re-run LiE):

Hilbert (Cederwall Eq. (4.2)):  
\(1 + t^4 + 2t^6 + 7t^8 + 14t^{10} + 72t^{12} + \cdots\)

Euler/plethystic initial balances: \((m_4,\ldots)=(1,2,6,12,62,\ldots)\).

**Source caveats:** counts are for the complexified chiral \(126\) of \(SO(10,\mathbb{C})\) (Dynkin `(00002)`). Identifying them with **real** \(SO(1,9)\) **metric-only** graph spans requires additional hypotheses (complexification, epsilon reduction). Positive Euler coefficients are **net generator−relation balances**, not automatically raw generator counts. Sum of first five positive Euler exponents \(=83>81\) ⇒ relations must exist if the cited data hold.

---

## 9. Degree-by-degree 10D results

| Degree | Published singlets | Labeled | Canonical | Connected | Exact span rank (claimed) | Lower product rank | New quotient | Status |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 2 | 0 | — | — | — | 0 (vanishes) | 0 | 0 | Analytic + conventions |
| 4 | 1 | 21 | 5 | 4 | 1 | 0 | 1 | OBSERVED RUN V4 |
| 6 | 2 | 12043 | 54 | 49 (+5 disc.) | 2 | 0 | 2 | OBSERVED RUN; Catalog_V2 |
| 8 | 7 | 45163496 | 1753 | 1689 (+64 disc.) | 7 | 1 (\(I_4^2\)) | 6 | OBSERVED RUN; basis validation |
| 10 | 14 | — | — | — | products rank 2 claimed | 2 | target 12 | Foundations only; **no graph discovery** |

### Degree 4
Invariant \(I_4=\mathrm{tr} M^2\) with \(M_\mu{}^\nu = F_{\mu\rho_1\rho_2\rho_3\rho_4}F^{\nu\rho_1\rho_2\rho_3\rho_4}\) (factorial normalizations as in formula catalog). Graph+I4 span rank 1 claimed.

### Degree 6
Two independents: \(I_6^{(1)}=\mathrm{tr} M^3\) and \(I_6^{(2)}\) from \(N^{(1050)}\) cubic (Hutomo/Cederwall). Catalog CSV: 54 graphs; K6 coefficients corrected to \(\{-17/1152,\ 125/4\}\) in V2. Some graph relations **fitted on samples** with holdout residuals recorded—**not** symbolic proofs.

### Degree 8 — seven validated basis directions
1. \(I_4^2\)
2. Graph **3**
3. Graph **249**
4. Graph **508**
5. Graph **61**
6. Graph **376**
7. Graph **528**

Explicit keys, adjacency matrices, and Einstein/metric contractions: `TenDDegree8InvariantFormulaCatalog.txt` (copied to `supporting/`). Claimed: exact & modular rank 7 on 24 fresh tensors and on each 8-sample block. **Not all 1753 graphs** were necessarily evaluated for reduction; discovery used batched peak-rank/work filters. Matching published dimension 7 is **conditional completeness evidence**.

### Degree 10
`TenDDegree10Foundations_V1.wl` is designed to run 16 VerificationTests validating products \(I_4 I_6^{(1)}\) and \(I_4 I_6^{(2)}\) have rank 2, hence **conditional** new-direction target 12 given published dim 14. **This auditor did not observe a stored TestReport output file** proving it was run; classify as **SOURCE EXISTS / designed OBSERVED RUN unknown**. **Do not claim twelve degree-10 generators have been found.**

Python `explore-10d`: only N=2 (1 graph) and N=4 (4 graphs) 5-regular censuses + self-duality.

---

## 10. SO versus O and epsilon-tensor audit

| Layer | Status |
|---|---|
| Analytic: even number of \(\epsilon\) reduces to metrics | ESTABLISHED ANALYTICALLY (standard) |
| Analytic: saturating one \(\epsilon\) on five indices of self-dual \(F\) replaces by metric form | ESTABLISHED ANALYTICALLY in saturated case; Cederwall App. C |
| Project computational proof that **every** \(SO(1,9)\) scalar with \(\epsilon\) reduces to metric-only graphs under project conventions | **UNRESOLVED** |
| Hilbert match at deg 8 ⇒ completeness without epsilon audit | **Unsafe**; requires hypotheses that (i) cited singlets apply to the same real representation & allowed tensors, and (ii) epsilon sectors add nothing new after \(F=*F\) |

Metric-only enumeration **might omit** orientation-sensitive invariants if reduction fails. Fixed chirality is an \(SO\) problem; Pfaffian-like lessons from 4D benchmarks apply.

---

## 11. Graph canonicalization and antisymmetry-sign audit

- Topology determines a contraction **only up to sign** and slot wiring; modules assign fixed vertex index labels (see formula catalog).
- Canonicalization via incidence multigraphs aims to preserve multiplicities; **whether all odd automorphisms forcing vanishing were proved symbolically vs detected on samples** is not uniformly documented—many vanishings are sample/fit based (Catalog flags).
- `Degree8CanonicalGraphKeys.wl` SHA-256 proves **file identity**, not mathematical completeness of the orbit list.
- Python N≤8 uses exact min-lex labels; N>8 uses fingerprints (weaker).

---

## 12. Claims register

See `TenD_Project_Claims_Register.csv` (18 major claims with evidence labels).

---

## 13. Test register

See `TenD_Project_Test_Register.csv`.  
**Critical:** a green `TestReport` after loading many files into one kernel may depend on leftover `DownValues`. Modules should be retested in a **fresh kernel** with documented `Get` order. Auditor could not execute Wolfram.

---

## 14. Failures and discrepancies

| Symptom | Root cause | Corrected by | Downstream regenerated? |
|---|---|---|---|
| Module2 AssociationMap failures | Rule-wise Map over Association | `Map[evaluate, specs]` in MetricContractions | Yes (Gate2 pass) |
| Jacobian Indeterminate | \(0^0\) | Explicit degree-0 row = 1 | Yes |
| Jacobian rank 4 | Wrong \(x^{(6)}\) (= \(X_1^{(6)}\)); axis order | TensorContract axis fix; RaiseTensorIndex | Yes; Gate3 rank5 |
| GraphEnumeration load fail | `IncidenceGraph` protected | `_FIXED` rename | Yes Gate5 |
| Benchmarks matrix bug | Missing `Dot` | `_CORRECTED_V2` | Yes |
| Lorentzian missing components | Incomplete association keys | V2 Lookup fill | Yes |
| Degree4 wrong raise/transpose | Diagonal raise; Ordering | V3/V4 | Yes |
| Degree6 K6 wrong sign | Catalog V1 | Catalog V2 `-17/1152` | Catalog regenerated; confirm batches refreshed |
| Missing ContractionPlanning | File absent | **Unresolved** | Batch A cannot clean-start |
| Python initial audit: ladder omitted \(P_N\) | Design bug | `tensor_invariants` product quotient | Yes 2026-08-06 |
| Legacy docs 78/81 | Autonomous climb | Not authoritative | Do not use |

---

## 15. Reproducibility audit

| Item | Finding |
|---|---|
| Required Mathematica | Logs cite Wolfram **15.0.1** |
| Auditor OS | macOS; Wolfram **not installed** in PATH |
| Clean-kernel 6D | Load FIXED chain in order §2.1; expect Gate5 ~2–3 min enum |
| Clean-kernel 10D deg8 | Needs keys file + planning + batches; high memory/time (45M labeled class size combinatorial) |
| Python | `pip install -r requirements.txt`; `python run_pipeline.py reproduce-6d` |
| Random seeds | App.A holdouts `20260804`; D10 foundations seeds `20261601–20261606`; Python pipeline seeds in configs |
| Missing dependency | `TenDDegree6ContractionPlanning_V1.wl` |
| External packages | None beyond Wolfram / Python reqs |

---

## 16. Current scientific conclusions

### A. Established analytically
\(\star^2\) sign; real self-duality in Lorentzian middle dimension; quadratic vanishing for chiral 5-form; \(SO\) vs \(O\) chirality exchange; even-\(\epsilon\) reduction to metrics (standard).

### B. Stated in primary literature
Krull 81; Hilbert/Euler table through deg 22; uniqueness of \(I_4\); two deg-6; six new deg-8; twelve new deg-10 (as literature targets).

### C. Reproduced exactly (project computation; MMA OBSERVED / Python partial RERUN)
6D graph counts; 6D ranks; 6D Jacobian rank 5; App. A finite holdouts; 10D component counts / \(\star^2\) (Python RERUN smoke).

### D. Supported by modular checks
6D Jacobian primes; claimed 10D deg8 rank7 modular; Python syzygies on validation primes.

### E. Supported only on finite samples
App. A identities; many 10D graph-to-basis fits; Python SVD \(n_{\mathrm{new}}\).

### F. Conjectural
Legacy 78/81 JSON; any claim that metric graphs already give the full \(SO(1,9)\) ring.

### G. Unresolved
Epsilon completeness; generic stabilizer proof; deg-10 generators; full syzygies; Hironaka/HSOP; independent cross-language 10D reproduction.

---

## 17. What has not been done

- Complete reduction of all 1753 degree-8 canonical graphs onto the 7-dimensional basis  
- Degree-10 graph enumeration and quotient search  
- Higher-degree generators  
- Systematic syzygy discovery with symbolic proof  
- Generic stabilizer proof  
- Complete \(SO\)/epsilon reduction certificate  
- Complete primary/secondary classification and Hironaka decomposition  
- Proof that low-degree candidates generate the full ring  
- Full 81-parameter structure  
- Independent cross-language 10D implementation matching Mathematica  
- Formal machine-checkable proof  
- Fresh-kernel retest by this auditor (Wolfram absent)

---

## 18. Recommended next steps (gated)

1. **Fresh-kernel reproducibility** — Input: Research folder only. Module: driver notebook. Pass: all Gate1–5 + Deg4 V4 + Deg8 BasisValidation True in new kernel. Justifies: OBSERVED→RERUN. Unproved: 10D completeness.
2. **\(SO(1,9)\)/epsilon-reduction validation** — Explicit identities under project conventions. Pass: every tested single-\(\epsilon\) scalar equals a metric graph combination exactly. Justifies: metric-only census adequacy. Unproved: all degrees.
3. **Independent exact degree-8 rank certificate** — Second implementation or exact minor export. Pass: rank7 with exhibited minor. Justifies: stronger than finite-sample alone.
4. **Independent implementation (Python 10D)** — Port deg4/6 evaluations. Pass: match \(I_4\), two deg6, rank7. Justifies: cross-language evidence.
5. **Degree-10 foundations RERUN** — Pass: product rank2 exact+modular. Justifies: target 12 conditional.
6. **Degree-10 graph enumeration + quotient** — Pass: span rank14 with 12 new beyond products **or** documented obstruction. Justifies: computational match to Hilbert 14.
7. **Syzygy discovery + holdout** — Pass: relations validate on unused primes/samples. Justifies: finite-sample identities. Unproved: symbolic.

---

## 19. Draft publication claims

### Currently safer to write
- We reproduce Elamaran et al. connected 3-regular counts \((1,2,6,20)\) and ranks \((1,2,3,6)\) for the Euclidean 6D 3-form, and recover generator degrees \([2,4,4,6,8]\) by product quotienting (Python numerical; Mathematica exact ranks).
- The five paper polynomials are algebraically independent (exact Jacobian rank 5 at a tested integer point).
- Appendix A relations vanish exactly on tested integer holdouts (not a symbolic proof).
- For Lorentzian self-dual 5-forms with stated conventions, \(\star^2=+1\) and there are 126 real chiral components; the quadratic invariant vanishes.
- Literature targets (Cederwall): Hilbert coefficients and Krull dimension 81 are **adopted as cited**, not re-proved.
- Computational evidence (Mathematica, not auditor-rerun) supports dim 1,2,7 at degrees 4,6,8 for metric-only graphs, with an explicit 7-direction degree-8 basis catalogued.

### Currently unsafe / overstated
- “We proved the invariant ring is generated by five elements in 6D.”
- “We proved Krull dimension 81.”
- “Metric-only graphs are complete for \(SO(1,9)\).”
- “We found twelve degree-10 generators.”
- “Degree-8 matching Hilbert 7 proves completeness.”
- “78 of 81 invariants found” (`docs/invariants_78.json`).
- “Green TestReport ⇒ mathematical completeness.”

---

## 20. Appendices

- `TenD_Project_File_Manifest.csv`  
- `TenD_Project_Claims_Register.csv`  
- `TenD_Project_Test_Register.csv`  
- `supporting/` — logs, catalogs, MIT outputs, hashes, smoke rerun  
- Environment: Python 3.13 venv with project requirements; Wolfram absent from PATH  
- PDF engine: pure-Python text PDF writer (no TeX/pandoc installed)

---

*End of audit report.*


---

# 4. CLAIMS REGISTER

```csv
Claim,Degree,Exact_statement,Evidence_label,Source_file,Passed_tests,Logical_assumptions,Remaining_risk
Five independent 6D trace invariants (Jacobian rank 5),6,Exact 5x20 Jacobian rank 5 over Q and three primes,REPRODUCED COMPUTATIONALLY WITH EXACT ARITHMETIC,FunctionalIndependence6D.wl / RESEARCH_LOGv4 Gate 3,5/5 Gate 3,Implemented contractions match (4.1)-(4.4),Does not prove ring generation/completeness
"6D connected graph counts (1,2,6,20)",2-8,Canonical connected 3-regular multigraphs,REPRODUCED COMPUTATIONALLY WITH EXACT ARITHMETIC,GraphEnumeration6D_FIXED.wl; Python tensor_invariants,Gate5 6/6; Python RERUN N<=6 + cached N=8,Weighted multigraph model,N=10 exact census not done in Python
"6D connected ranks (1,2,3,6)",2-8,Same-degree contraction ranks,REPRODUCED COMPUTATIONALLY WITH EXACT ARITHMETIC,GraphEnumeration6D_FIXED Gate5; Python SVD match,Gate5; Python outputs/6d/ranks.json,Finite exact samples in MMA,Upper bounds not symbolic
"6D new generators (1,2,1,1,0) degrees [2,4,4,6,8]",2-10,Product-quotient new generators,SUPPORTED ONLY BY FLOATING-POINT NUMERICS,Python generator_selection + outputs/6d,test_generator_counts_6d,SVD discovery backend,Not exact-arithmetic discovery; N=10 sampled
Appendix A relations (A.2)(A.4)(A.6),"6,8",Exact residuals 0 on 12 integer holdouts,FINITE-SAMPLE EVIDENCE ONLY,AppendixRelations6D.wl Gate4,7/7,Implemented X and x match paper,Not symbolic identity proof
Python syzygies 8 candidates,"6,8",Modular nullspace + fresh validation,SUPPORTED BY MODULAR COMPUTATION,outputs/6d/syzygies.json,test_syzygy_validation,FF identities on tested samples,Not matched to paper A.4/A.6 coefficients symbolically
10D ★^2=+1; 252/126,10,Self-dual real 5-form exists Lorentzian,REPRODUCED COMPUTATIONALLY WITH EXACT ARITHMETIC / strong computational (Python),TenDLorentzianFoundations_V2; Python self_duality,MMA 15 VT claimed; Python smoke True,"Conventions η,ε",Independent of invariant counts
Krull dimension 81,—,126-45=81 generic trivial stabilizer,STATED IN A CITED PRIMARY SOURCE,Cederwall et al. arXiv:2509.14350,TenDRepresentationTargets checks series conversion,Generic stabilizer argument,Not independently proved here
"Hilbert singlets deg4=1,6=2,8=7,10=14",4-10,LiE singlet dims Sym^n(126),STATED IN A CITED PRIMARY SOURCE,Cederwall Eq (4.2); TenDRepresentationTargets,9 VT claimed,"SO(10,C) chiral 126","May differ from real SO(1,9) metric-only graphs"
10D one degree-4 invariant I4=tr M^2,4,Exact span rank 1; graphs 21/5/4,FINITE-SAMPLE EVIDENCE ONLY / OBSERVED RUN,TenDDegree4Invariants_V4.wl,16 VT claimed,Metric-only; self-dual samples,Wolfram not rerun by auditor
10D two degree-6 invariants,6,Trace + N1050; 12043/54/49 graphs,FINITE-SAMPLE EVIDENCE ONLY / OBSERVED RUN,Degree6 modules Catalog_V2,VT claimed; catalog CSV exists,Missing ContractionPlanning file risk,Fitted relations not symbolic
10D seven degree-8 directions,8,"I4^2 + graphs 3,249,508,61,376,528",EXACT FINITE-SAMPLE INDEPENDENCE CERTIFICATE (claimed),TenDDegree8BasisValidation_V1,16 VT claimed; catalog exported,Not all 1753 graphs reduced,Completeness conditional on Hilbert 7
Burnside 1753 canonical / 45163496 labeled,8,Orbit census,REPRODUCED COMPUTATIONALLY WITH EXACT ARITHMETIC (claimed),TenDDegree8GraphEnumeration_V1 + Degree8CanonicalGraphKeys.wl,13 VT claimed,Burnside conjugacy classes,Checksum proves file identity not math completeness
Degree-10 product rank 2; target 12 new,10,"I4 I6^(1,2) span rank 2",FINITE-SAMPLE EVIDENCE ONLY if module run,TenDDegree10Foundations_V1.wl,16 VT designed,Depends on D6/D8 state in kernel,Graph enumeration NOT done; 12 gens NOT found
Python 10D generators,—,None discovered,UNRESOLVED,outputs/10d/generators.json,explore-10d smoke,—,Ladder not implemented
SO/epsilon reduction after F=*F,—,All SO invariants reduce to metric graphs,UNRESOLVED,Literature gate §5,Not computationally proved,Cederwall App C identities,Matching Hilbert 7 does not prove no epsilon-only invariants
Complete 81-parameter generating structure,—,Full Hironaka/HSOP for chiral 5-form,UNRESOLVED,—,—,—,Far beyond current computation
docs/invariants_78.json 78/81 claim,10,Legacy 78 primary invariants,CONJECTURAL / inconsistent with literature low-degree balances,MIT docs/invariants_78.json,Not in tensor_invariants path,Autonomous climb,Do not treat as validated

```

---

# 5. TEST REGISTER

```csv
File,Test_ID,Expected_result,Observed_result,Run_status,Arithmetic_type,What_it_establishes,What_it_does_not_establish
AntisymmetricPForms.wl,aggregate/TestReport,all VerificationTests True / pytest pass,5/5,OBSERVED RUN,exact,Indep slots/signs,Not 6D completeness
MetricContractions6D.wl,aggregate/TestReport,all VerificationTests True / pytest pass,8/8 after fixes,OBSERVED RUN,exact,Eqs (4.1)-(4.4) + A.2a regression,Harness false fail initially
FunctionalIndependence6D.wl,aggregate/TestReport,all VerificationTests True / pytest pass,5/5,OBSERVED RUN,exact+modular,Jacobian rank 5,Not ring generation
AppendixRelations6D.wl,aggregate/TestReport,all VerificationTests True / pytest pass,7/7,OBSERVED RUN,exact,"A.2,A.4,A.6 on 12 holdouts",Not symbolic proof
GraphEnumeration6D_FIXED.wl,aggregate/TestReport,all VerificationTests True / pytest pass,6/6 twice,OBSERVED RUN,exact,"Counts 1,2,6,20 ranks 1,2,3,6",Finite-sample ranks
InvariantBenchmarks_CORRECTED_V2.wl,aggregate/TestReport,all VerificationTests True / pytest pass,12 VT,OBSERVED RUN,exact,O(4)/SO(4)/Pfaffian,Module6 only
TenDLorentzianFoundations_V2.wl,aggregate/TestReport,all VerificationTests True / pytest pass,15 VT,OBSERVED RUN,exact/float,Hodge ★^2=+1; 126,Not invariant counts
TenDRepresentationTargets.wl,aggregate/TestReport,all VerificationTests True / pytest pass,9 VT,OBSERVED RUN,exact series ops,Hilbert/Euler table match cited integers,Does not prove LiE
TenDDegree4Invariants_V4.wl,aggregate/TestReport,all VerificationTests True / pytest pass,16 VT,OBSERVED RUN,exact,I4 span rank 1,Not rerun by auditor
TenDDegree6GraphEnumeration_V1.wl,aggregate/TestReport,all VerificationTests True / pytest pass,10 VT,OBSERVED RUN,combinatorial,12043/54/49,—
TenDDegree6Catalog_V2.wl,aggregate/TestReport,all VerificationTests True / pytest pass,12 VT,OBSERVED RUN,exact fit+holdout,54 graph coeffs; K6 signs,Fitted identities
TenDDegree8GraphEnumeration_V1.wl,aggregate/TestReport,all VerificationTests True / pytest pass,13 VT,OBSERVED RUN,Burnside exact,1753/1689/64; 45163496,—
TenDDegree8BasisValidation_V1.wl,aggregate/TestReport,all VerificationTests True / pytest pass,16 VT,OBSERVED RUN,exact+modular,Rank 7 on 24 fresh,Not full 1753 reduction
TenDDegree10Foundations_V1.wl,aggregate/TestReport,all VerificationTests True / pytest pass,16 VT designed,UNKNOWN/OBSERVED RUN claimed,exact+modular,Product rank 2 target,No graph discovery
Python test_generator_counts_6d,aggregate/TestReport,all VerificationTests True / pytest pass,6 passed,RERUN PASSED (prior session),SVD+float,Blind n_new match paper,Not exact discovery
Python smoke 2026-08-06 audit,aggregate/TestReport,all VerificationTests True / pytest pass,"graphs 1,2,6; n_new 1,2,1; SD True",RERUN PASSED,float+combinatorial,Confirms Python path,N=8 not rerun this audit

```

---

# 6. FILE MANIFEST

```csv
File,Version,Purpose,Dependencies,Execution_status,Tests_VT_count,Supersedes_or_superseded_by,Outputs_produced,SHA256,Size_bytes,mtime_utc
Research/2001 (1).pdf,2001 (1).pdf,,,SOURCE EXISTS,,,,03c5d970f96bda42b6c39c38e858412c65f6d9fac315ecdd0267bed95212c24a,668076,2026-07-17T15:08:51Z
Research/6D_3Form_Project.nb,6D_3Form_Project.nb,,,UNKNOWN,,,,131de04c9e6caa03c67ba700cb312d4b7ae9cc6e543eced0539d71b8670b2b61,14155,2026-08-03T04:42:09Z
Research/AntisymmetricPForms.wl,AntisymmetricPForms.wl,Exact sparse antisym p-form representation,,OBSERVED RUN,5,,,d4b73aef9cebf1f487b58bde5c93ffeb435ca3ee31106f7b5aacea7ec5faead7,4644,2026-08-03T04:39:42Z
Research/AppendixRelations6D.wl,AppendixRelations6D.wl,Appendix A syzygies exact holdouts,,OBSERVED RUN,7,,,cae2a749a6ed6405c63651259660c30eb7e232b091213bfdd9227105028337a0,4899,2026-08-03T05:33:26Z
Research/Degree8CanonicalGraphKeys.wl,Degree8CanonicalGraphKeys.wl,1753 canonical graph keys data,,OBSERVED RUN,0,,,085e6dc3233bdafde53329fd580ed01c36742b6cf3d386a6aa1d670114d56ebe,106936,2026-08-05T22:30:41Z
Research/FunctionalIndependence6D.wl,FunctionalIndependence6D.wl,Exact Jacobian rank for five generators,,OBSERVED RUN,5,,,46cbcc18315cf9c73e300eac75103ae74d3ea8894d6f19369423b81ec0b67a76,5539,2026-08-03T04:59:42Z
Research/GraphEnumeration6D.wl,GraphEnumeration6D.wl,3-regular graph enum (broken loader),,SUPERSEDED,6,SUPERSEDED by GraphEnumeration6D_FIXED.wl,,93344630e3fb39f4c52ff84089a18838856485c4fe9adf5ffa532d2b64b2d356,9861,2026-08-03T05:40:42Z
Research/GraphEnumeration6D_FIXED.wl,GraphEnumeration6D_FIXED.wl,3-regular graph enum Gate 5,,OBSERVED RUN,6,,,a9240642de84e85633db04de4d91b97e7955064c5fcc9877c2db79985a689f2b,9862,2026-08-03T14:17:52Z
Research/InvariantBenchmarks.wl,InvariantBenchmarks.wl,O(d)/SO(4) benchmarks (Dot bug),,SUPERSEDED,12,SUPERSEDED by InvariantBenchmarks_CORRECTED_V2.wl,,21838131abcd8fae511b3fc3cb207d08cd410eb4bc1746ad363391cf7d6edc75,9311,2026-08-03T14:50:49Z
Research/InvariantBenchmarks_CORRECTED_V2.wl,InvariantBenchmarks_CORRECTED_V2.wl,Corrected O(d)/SO(4) benchmarks,,OBSERVED RUN,12,,,05b3efd51f5a7df29fe7fe7d4fdbfbf2fb462c10bf866297555e2097e8f10f98,9339,2026-08-03T14:55:03Z
Research/MetricContractions6D.wl,MetricContractions6D.wl,6D metric contractions; Eqs (4.1)-(4.4),,OBSERVED RUN,8,,,8e8248abfefc8c92dae6ee78c2bd366b3ab1d709df65b2d5bf19be9855cb9d52,9506,2026-08-03T05:25:49Z
Research/New Folder With Items/Beginner_Companion_to_Machine_Learning_Invariants_of_Tensors.pdf,Beginner_Companion_to_Machine_Learning_Invariants_of_Tensors.pdf,,,SOURCE EXISTS,,,,588249c952b11c34407b0118064e3296154407f7459524c1d5f348dddbc858a1,95701,2026-07-03T19:31:17Z
Research/New Folder With Items/Molecular_Dynamics_Math_Notes.pdf,Molecular_Dynamics_Math_Notes.pdf,,,SOURCE EXISTS,,,,516473c142f945ba2e6f3cbc9c7b94560fdb8399fc47b7d041610b21591e1d70,107945,2026-07-03T15:07:19Z
Research/New Folder With Items/Untitled document-31.pdf,Untitled document-31.pdf,,,SOURCE EXISTS,,,,61593ab31368ba310ea0ae4f7844e7c898d7ba6e76abd217017c89ea216100ce,78344,2026-07-17T23:24:15Z
Research/New Folder With Items/invariants_78.pdf,invariants_78.pdf,,,SOURCE EXISTS,,,,742b51875e2108dea7730c90039720772309cc4ace4e620949450e3181722f52,68903,2026-07-23T15:14:50Z
Research/New Folder With Items/reclaiming_attention_case_study.pdf,reclaiming_attention_case_study.pdf,,,SOURCE EXISTS,,,,7851f0c84a6d9901eb14b2731cbc5bbf717b1114be19139211510a60cd363ffb,6168710,2026-07-20T20:57:01Z
Research/New Folder With Items/reclaiming_attention_feinstein_30_day_case_study.pdf,reclaiming_attention_feinstein_30_day_case_study.pdf,,,SOURCE EXISTS,,,,ec9d7db56ed44b87b01fbdefd7e2e0788a5c82d266a25209c93e3dda833397dc,1002442,2026-07-20T22:30:52Z
Research/New Folder With Items/regents_to_tensor_invariants_guide.pdf,regents_to_tensor_invariants_guide.pdf,,,SOURCE EXISTS,,,,7725ae93466be7eba6ee1e61197176c665d7efe856da74ff176335ee140c4e19,291007,2026-07-03T21:46:00Z
Research/New Folder With Items/tensor_paper_page_paragraph_companion_v2.pdf,tensor_paper_page_paragraph_companion_v2.pdf,,,SOURCE EXISTS,,,,d34a8088bbe78839187f600ff3905fe3038b92816fd4524572973ced484a9280,1286592,2026-07-03T23:58:43Z
Research/New Folder With Items/tensor_paper_paragraph_by_paragraph_companion.pdf,tensor_paper_paragraph_by_paragraph_companion.pdf,,,SOURCE EXISTS,,,,a5f99cfe40d17cde54a1fe24f84d2381b39b2d843c340a15f68485433f6dd089,556143,2026-07-03T23:53:04Z
Research/New Folder With Items/what_i_built.pdf,what_i_built.pdf,,,SOURCE EXISTS,,,,49fa826318b4e4316761fbdd0b2bd2f7ea3fa58c52737a68fdaab8137c2fdd8d,58117,2026-07-21T21:47:43Z
Research/RESEARCH_LOG.md,RESEARCH_LOG.md,,,SOURCE EXISTS,,IDENTICAL to RESEARCH_LOGv4.md,,b385693d43cd6f8d9d07a2f8df4ca8e307f14c6a38860420ca84280648ecacee,11048,2026-08-03T14:34:42Z
Research/RESEARCH_LOG_2.md,RESEARCH_LOG_2.md,,,SOURCE EXISTS,,IDENTICAL to RESEARCH_LOGv4.md,,b385693d43cd6f8d9d07a2f8df4ca8e307f14c6a38860420ca84280648ecacee,11048,2026-08-03T15:58:26Z
Research/RESEARCH_LOGv3.md,RESEARCH_LOGv3.md,,,SOURCE EXISTS,,IDENTICAL to RESEARCH_LOGv4.md,,b385693d43cd6f8d9d07a2f8df4ca8e307f14c6a38860420ca84280648ecacee,11048,2026-08-03T16:34:07Z
Research/RESEARCH_LOGv4.md,RESEARCH_LOGv4.md,,,SOURCE EXISTS,,,,b385693d43cd6f8d9d07a2f8df4ca8e307f14c6a38860420ca84280648ecacee,11048,2026-08-03T17:29:53Z
Research/TenDChiralFiveForm_Representation_Literature_Gate.md,TenDChiralFiveForm_Representation_Literature_Gate.md,,,SOURCE EXISTS,,,,5f5b4592baf86cae66bf2d11a5b2aec7c2a1cad7155edab18a4541f9b9bb4d64,15597,2026-08-03T15:58:20Z
Research/TenDDegree10Foundations_V1.wl,TenDDegree10Foundations_V1.wl,Degree-10 product subspace foundations,,OBSERVED RUN,16,,,85f07701a770933c4995f02971df50cbe3db6b4225c94daebfbd388fb518b716,8100,2026-08-06T05:00:32Z
Research/TenDDegree4Invariants_V1.wl,TenDDegree4Invariants_V1.wl,,,SUPERSEDED,13,SUPERSEDED by V4,,186315f4bdc0049979251bbe4fc5e7a742a8ed9c60b21d7b59ec9a0e37800983,12943,2026-08-03T16:08:46Z
Research/TenDDegree4Invariants_V2.wl,TenDDegree4Invariants_V2.wl,,,SUPERSEDED,13,SUPERSEDED by V4,,ea2418526f2134a265a134acb99b643eb60d52bd1c7e448008f70c28d26188bf,12950,2026-08-03T16:13:58Z
Research/TenDDegree4Invariants_V3.wl,TenDDegree4Invariants_V3.wl,,,SUPERSEDED,15,SUPERSEDED by V4,,ec29ac78e5dd53abeb48e2aaed2e5459bdd903b2fd374771a44626d181511ea1,14111,2026-08-03T16:21:30Z
Research/TenDDegree4Invariants_V4.wl,TenDDegree4Invariants_V4.wl,Degree-4 I4=tr M^2 graph gate,,OBSERVED RUN,16,,,0b600b556c579330c32da3b8bb44829a1d76209552c30aa1fe620d6a6da5d247,14454,2026-08-03T16:28:48Z
Research/TenDDegree6Catalog.csv,TenDDegree6Catalog.csv,,,OBSERVED RUN,,,,b00cc3f037701ba89fe5815b5e87994257880922740e20baec3c124d96bf0228,4546,2026-08-05T21:41:26Z
Research/TenDDegree6Catalog_V1.wl,TenDDegree6Catalog_V1.wl,,,SUPERSEDED,12,SUPERSEDED by V2 (K6 sign),,8a4767bc3bd65ae1ed639191d11ba4d0c128234989223b6a432a8b7f27bc8b1c,6344,2026-08-05T21:27:34Z
Research/TenDDegree6Catalog_V2.wl,TenDDegree6Catalog_V2.wl,54-graph degree-6 catalog corrected signs,,OBSERVED RUN,12,,,c52f7bee266ea5e398d381e9e1205405d599782b9c3968b7a09f92d21d6ee418,6340,2026-08-05T21:41:03Z
Research/TenDDegree6GraphBasis_BatchA_V1.wl,TenDDegree6GraphBasis_BatchA_V1.wl,,,OBSERVED RUN,12,,,417c2f8ae4c4e397c5080af4d6d1993ac4641ab770fa73a70961b8f250fff652,10055,2026-08-05T16:54:25Z
Research/TenDDegree6GraphBasis_BatchB1_V1.wl,TenDDegree6GraphBasis_BatchB1_V1.wl,,,OBSERVED RUN,12,,,f18973e2b6af0dbda59aaae750c27ec0053cb6cc093143473c0b8fe64c9309d5,5133,2026-08-05T17:24:11Z
Research/TenDDegree6GraphBasis_BatchB2_V1.wl,TenDDegree6GraphBasis_BatchB2_V1.wl,,,OBSERVED RUN,12,,,e29141fd4dcb65dc9f31d82f82c802abdb374a0038d23e04952e0f55fe333c1f,5237,2026-08-05T17:52:58Z
Research/TenDDegree6GraphBasis_BatchC_V1.wl,TenDDegree6GraphBasis_BatchC_V1.wl,,,OBSERVED RUN,12,,,7c606ef1c5a328101a14e76a5e832f9445491c83d686d306ffc2320f4c8f9444,5723,2026-08-05T18:02:40Z
Research/TenDDegree6GraphBasis_FinalK6_V1.wl,TenDDegree6GraphBasis_FinalK6_V1.wl,,,SUPERSEDED,14,SUPERSEDED by V2,,7c7c18f14af35cb285b96c80285f85ede876aaab586e5774b81484caeec8da45,11973,2026-08-05T20:36:46Z
Research/TenDDegree6GraphBasis_FinalK6_V2.wl,TenDDegree6GraphBasis_FinalK6_V2.wl,,,OBSERVED RUN,14,,,b7646ebad277740960ccc796dbcf7bf76a2e5f796f82a9a0c22c5686c9ec3cff,12542,2026-08-05T20:45:54Z
Research/TenDDegree6GraphEnumeration_V1.wl,TenDDegree6GraphEnumeration_V1.wl,5-regular N=6 graph census,,OBSERVED RUN,10,,,b050f4404ac3ff2710903123c1a1d299800707ad4731947779509226d5464145,7468,2026-08-03T16:41:33Z
Research/TenDDegree6N1050Invariant_V1.wl,TenDDegree6N1050Invariant_V1.wl,,,SUPERSEDED,12,SUPERSEDED by V2,,ba677c4e9d766ba2d6fb6be3bacd82064ce7fb81a93f64bc79f1c8e6704af07c,13926,2026-08-03T17:40:54Z
Research/TenDDegree6N1050Invariant_V2.wl,TenDDegree6N1050Invariant_V2.wl,I6^(2) via N1050 corrected,,OBSERVED RUN,13,,,61ee09a71e4e0d21373d4a466a59c389c990e6e33dc94f41fb1c71da081a074c,14513,2026-08-03T18:11:58Z
Research/TenDDegree6TraceInvariant_V1.wl,TenDDegree6TraceInvariant_V1.wl,I6^(1)=Tr M^3,,OBSERVED RUN,11,,,942f8339e1f47acad8fdeeda4ba72461b8b3d9954fed1ea9feb1930f8069f155,9617,2026-08-03T17:29:22Z
Research/TenDDegree8BasisValidation_V1.wl,TenDDegree8BasisValidation_V1.wl,Validate 7 degree-8 basis directions,,OBSERVED RUN,16,,,1c88de1f589db39ae273433746d0da292a2206de830c17bce5476718c4dcb9ac,6712,2026-08-06T04:41:27Z
Research/TenDDegree8ContractionPlanning_V1.wl,TenDDegree8ContractionPlanning_V1.wl,,,OBSERVED RUN,14,,,337dcc6710da8f560775f80970cecdd54963a1e5de3e3bdc984731405a0e06d2,8994,2026-08-06T03:30:10Z
Research/TenDDegree8DiscoveryBatchA_V1.wl,TenDDegree8DiscoveryBatchA_V1.wl,,,OBSERVED RUN,13,,,e4c204193845827cc4ecc451587284061a2699173acd73d2a892572341ec4a25,11420,2026-08-06T03:53:56Z
Research/TenDDegree8DiscoveryBatchB_V1.wl,TenDDegree8DiscoveryBatchB_V1.wl,,,OBSERVED RUN,12,,,e36013c112e68cef9a61e2b08aad97762f3f7e244c1df47e63e377ec14b571f5,5137,2026-08-06T04:04:28Z
Research/TenDDegree8DiscoveryBatchC_V1.wl,TenDDegree8DiscoveryBatchC_V1.wl,,,OBSERVED RUN,12,,,ee975d55e9bc2af130231f885ef588a111cfb33f78f2529b3aa52f31e4065327,5109,2026-08-06T04:11:34Z
Research/TenDDegree8DiscoveryBatchD_V1.wl,TenDDegree8DiscoveryBatchD_V1.wl,,,OBSERVED RUN,12,,,7cf85c27a5e259a2401d403d9f7ad757176a83527147d9a38bc47b4f77feabb9,5435,2026-08-06T04:22:26Z
Research/TenDDegree8FormulaCatalog_V1.wl,TenDDegree8FormulaCatalog_V1.wl,Export degree-8 formulas,,OBSERVED RUN,15,,,5a140e9ae76419c6ee9a9d19696cf9007c8a52c1e313de4b7bc5eba2e22bbdfc,10206,2026-08-06T04:52:45Z
Research/TenDDegree8GraphEnumeration_V1.wl,TenDDegree8GraphEnumeration_V1.wl,Burnside degree-8 graph census,,OBSERVED RUN,13,,,ce701d1c652f91fb3ef9612ac5cda4e698f7068853c8195c0e5957938c43f935,7720,2026-08-05T22:30:30Z
Research/TenDDegree8InvariantFormulaCatalog.csv,TenDDegree8InvariantFormulaCatalog.csv,,,OBSERVED RUN,,,,901b6a33a822b49ba0d079be5351ed915df3d64e56f258cb33596aa77e4f12ee,20511,2026-08-06T04:53:07Z
Research/TenDDegree8InvariantFormulaCatalog.txt,TenDDegree8InvariantFormulaCatalog.txt,,,OBSERVED RUN,,,,1759a23b01543f29d05709d5c428bde14503fce69551c8dfb5089c38cd16f9a1,21538,2026-08-06T04:53:07Z
Research/TenDLorentzianFoundations_V1.wl,TenDLorentzianFoundations_V1.wl,10D Hodge/self-dual foundations V1,,SUPERSEDED,15,SUPERSEDED by TenDLorentzianFoundations_V2.wl,,93a1e9ca053117354a57f6cec92b41966c705f7624419b07ce5d9a73f83e7315,16587,2026-08-03T15:24:31Z
Research/TenDLorentzianFoundations_V2.wl,TenDLorentzianFoundations_V2.wl,10D Hodge/self-dual foundations V2,,OBSERVED RUN,15,,,c01d2dcf8ef1bd2e4c00e859052b70cf815d650ed2632efccbbc98d222eee21f,16731,2026-08-03T15:34:48Z
Research/TenDRepresentationTargets.wl,TenDRepresentationTargets.wl,Hilbert/Euler table check from Cederwall,,OBSERVED RUN,9,,,105ae4934782042ec9bf8a3712e994e6a8eb186b9da2d4fa91e9fd4c5d2d5f76,3899,2026-08-03T15:58:38Z
Research/regents_to_tensor_invariants_guide_edited.pdf,regents_to_tensor_invariants_guide_edited.pdf,,,SOURCE EXISTS,,,,4fa7e9a597bd631bda36096a20415f36f06ba11e3903f376e6fcd6476d2eff05,333956,2026-07-03T21:56:46Z
MIT/.gitattributes,.gitattributes,,,SOURCE EXISTS,,,,1a1dbe176bc233b499d35a57db7513f2941c99ab9759f177830c9149be99005b,66,2026-07-27T22:48:47Z
MIT/.gitignore,.gitignore,,,SOURCE EXISTS,,,,0188bf8452ee9938b96d46951feede7d9d70d3b6285a4ebd08bb7b2f74ec15e9,124,2026-07-27T22:48:47Z
MIT/IMPLEMENTATION_PLAN.md,IMPLEMENTATION_PLAN.md,,,SOURCE EXISTS,,,,03a7bfb6133a84cf83aeaa89e5ad1010dc53cbb47957b528399e70b38795633e,2714,2026-07-27T22:48:47Z
MIT/MIGRATION.md,MIGRATION.md,,,SOURCE EXISTS,,,,484361a1c71097abc49f9726758b6c04480d12f576559580960e3fae00c1a048,1317,2026-08-06T05:55:21Z
MIT/NOTES.md,NOTES.md,,,SOURCE EXISTS,,,,9f160f77637432ef5e4df4bba8633ef3319af2b479d75490a93033ae61a91fc6,3684,2026-07-27T22:48:47Z
MIT/Project_Audit_2026-08-06/rerun_smoke.txt,rerun_smoke.txt,,,OBSERVED RUN,,,,ade09d9d0c942f87826b4b8fde64a47279e834ad982ea9d215ba12441eab00f3,203,2026-08-06T13:22:23Z
MIT/Project_Audit_2026-08-06/sha256_all_research.txt,sha256_all_research.txt,,,OBSERVED RUN,,,,c44fce292794b00bd1da374808286af76e253c6bbb8592419c894472822bcbc0,5982,2026-08-06T13:22:23Z
MIT/Project_Audit_2026-08-06/sha256_mit_core.txt,sha256_mit_core.txt,,,OBSERVED RUN,,,,cbf13a22c96b5a764dd5cf02cfba6f4f34b3a84d0b3bd6b2f4396c5f3f01728c,6760,2026-08-06T13:22:23Z
MIT/Project_Audit_2026-08-06/sha256_research_top.txt,sha256_research_top.txt,,,OBSERVED RUN,,,,b7ba48bcd1ba45cf33a5c13d43101f92621e9e44dfe8f091e4d2a55c44093e6d,4505,2026-08-06T13:18:58Z
MIT/Project_Audit_2026-08-06/supporting/MIT_10d_explore_summary.json,MIT_10d_explore_summary.json,,,SOURCE EXISTS,,,,5a8815a59810f494dae4aa0db4eca98eb6ed15772a76516f018c3b30680b9890,3109,2026-08-06T13:23:36Z
MIT/Project_Audit_2026-08-06/supporting/MIT_10d_results.md,MIT_10d_results.md,,,SOURCE EXISTS,,,,0b0be3cc190f569d634455dce014ab5eeb7af83d6dea5c81feb891baf8db7c80,1029,2026-08-06T13:23:36Z
MIT/Project_Audit_2026-08-06/supporting/MIT_6d_generators.json,MIT_6d_generators.json,,,SOURCE EXISTS,,,,8f42d750bcf6fa6bcd2cbebe046df1516d43fc222bfbb48536223d6d59a66664,412,2026-08-06T13:23:36Z
MIT/Project_Audit_2026-08-06/supporting/MIT_6d_ranks.json,MIT_6d_ranks.json,,,SOURCE EXISTS,,,,21f2a821faafd004202053694e03c265cc59038661166f5c997f6991a8a837eb,1984,2026-08-06T13:23:36Z
MIT/Project_Audit_2026-08-06/supporting/MIT_6d_reproduction.md,MIT_6d_reproduction.md,,,SOURCE EXISTS,,,,ac5f12f24ecc8c3e113bd1204e9f56f4e6cfaac2407c87b86a51333b206f0dd4,1201,2026-08-06T13:23:36Z
MIT/Project_Audit_2026-08-06/supporting/MIT_initial_audit.md,MIT_initial_audit.md,,,SOURCE EXISTS,,,,663bac4cdb5b26d824a6593143101e1eae1f650e411347aa3b4a7fc6e9b9b77b,7651,2026-08-06T13:23:36Z
MIT/Project_Audit_2026-08-06/supporting/RESEARCH_LOGv4.md,RESEARCH_LOGv4.md,,,SOURCE EXISTS,,,,b385693d43cd6f8d9d07a2f8df4ca8e307f14c6a38860420ca84280648ecacee,11048,2026-08-06T13:23:36Z
MIT/Project_Audit_2026-08-06/supporting/TenDChiralFiveForm_Representation_Literature_Gate.md,TenDChiralFiveForm_Representation_Literature_Gate.md,,,SOURCE EXISTS,,,,5f5b4592baf86cae66bf2d11a5b2aec7c2a1cad7155edab18a4541f9b9bb4d64,15597,2026-08-06T13:23:36Z
MIT/Project_Audit_2026-08-06/supporting/TenDDegree6Catalog.csv,TenDDegree6Catalog.csv,,,OBSERVED RUN,,,,b00cc3f037701ba89fe5815b5e87994257880922740e20baec3c124d96bf0228,4546,2026-08-06T13:23:36Z
MIT/Project_Audit_2026-08-06/supporting/TenDDegree8InvariantFormulaCatalog.csv,TenDDegree8InvariantFormulaCatalog.csv,,,OBSERVED RUN,,,,901b6a33a822b49ba0d079be5351ed915df3d64e56f258cb33596aa77e4f12ee,20511,2026-08-06T13:23:36Z
MIT/Project_Audit_2026-08-06/supporting/TenDDegree8InvariantFormulaCatalog.txt,TenDDegree8InvariantFormulaCatalog.txt,,,OBSERVED RUN,,,,1759a23b01543f29d05709d5c428bde14503fce69551c8dfb5089c38cd16f9a1,21538,2026-08-06T13:23:36Z
MIT/Project_Audit_2026-08-06/supporting/rerun_smoke.txt,rerun_smoke.txt,,,OBSERVED RUN,,,,ade09d9d0c942f87826b4b8fde64a47279e834ad982ea9d215ba12441eab00f3,203,2026-08-06T13:23:36Z
MIT/Project_Audit_2026-08-06/supporting/sha256_all_research.txt,sha256_all_research.txt,,,OBSERVED RUN,,,,c44fce292794b00bd1da374808286af76e253c6bbb8592419c894472822bcbc0,5982,2026-08-06T13:23:36Z
MIT/Project_Audit_2026-08-06/supporting/sha256_mit_core.txt,sha256_mit_core.txt,,,OBSERVED RUN,,,,cbf13a22c96b5a764dd5cf02cfba6f4f34b3a84d0b3bd6b2f4396c5f3f01728c,6760,2026-08-06T13:23:36Z
MIT/README.md,README.md,,,SOURCE EXISTS,,,,1cd619a5d82206c505ed62d8680183fa44037df08c171307d33e0306506c0844,4643,2026-08-06T05:55:21Z
MIT/SYSTEM.md,SYSTEM.md,,,SOURCE EXISTS,,,,5cee81292fb8407992d7e71af93f105ac265dad1176973d88995b807e55d1437,2547,2026-07-27T22:48:47Z
MIT/benchmarks/paper_6d_expected.json,paper_6d_expected.json,,,SOURCE EXISTS,,,,0fafbc6921349df1b3ebae77473d3d8654712c6345c141131baf832a57cb7d15,413,2026-08-06T05:25:53Z
MIT/checkpoints/graphs/graphs_N10_r3.json,graphs_N10_r3.json,,,OBSERVED RUN,,,,ba1411a2ba78d7e2f6900dd0ab9099a14f36ccc902c97d7c1dcff69ad9313588,6165,2026-08-06T05:54:43Z
MIT/checkpoints/graphs/graphs_N2_r3.json,graphs_N2_r3.json,,,OBSERVED RUN,,,,cbd23a70aae6076bcafeba1b73daaeaea3fd445ab65fdf8eb83005c5fa4d6ba5,142,2026-08-06T05:44:34Z
MIT/checkpoints/graphs/graphs_N4_r3.json,graphs_N4_r3.json,,,OBSERVED RUN,,,,41808500aa93d2504725c8fb6edb0f7b1a79cebadc82f4c1f872693930df6ef6,268,2026-08-06T05:44:34Z
MIT/checkpoints/graphs/graphs_N6_r3.json,graphs_N6_r3.json,,,OBSERVED RUN,,,,ec3af4deb28954d0e075f05c5c0edeac261c24f7b760cdb6446e024d71a54db2,1064,2026-08-06T05:44:34Z
MIT/checkpoints/graphs/graphs_N8_r3.json,graphs_N8_r3.json,,,OBSERVED RUN,,,,9094adefefd245955fc7d4000ccb8408f30786a398be9d61d43a5b051dd3ae2b,5557,2026-08-06T05:44:34Z
MIT/configs/self_dual_five_form_10d.yaml,self_dual_five_form_10d.yaml,,,SOURCE EXISTS,,,,c41c5904a6a572e5d6c0d091a8db1851a43ba9ec5774cc0e47dd5608398c5f67,661,2026-08-06T05:25:21Z
MIT/configs/three_form_6d.yaml,three_form_6d.yaml,,,SOURCE EXISTS,,,,e43764895bdcdceffc2b836895762070ad8d9b97cbd9156853ceba4a622a9a0b,395,2026-08-06T05:25:19Z
MIT/docs/AUTONOMOUS_LOCAL.md,AUTONOMOUS_LOCAL.md,,,SOURCE EXISTS,,,,e4b65ccb3ab2a9912b4603a61a616cd3ac6125ea5a3317b9e0bdac093741258e,3798,2026-07-28T23:33:02Z
MIT/docs/invariants_78.json,invariants_78.json,,,SOURCE EXISTS,,,,532cadca61471847b8c2f7479de70b9a92b6448dfedd905dd14cd23243793bb5,12435,2026-07-28T23:33:02Z
MIT/docs/invariants_78.pdf,invariants_78.pdf,,,SOURCE EXISTS,,,,742b51875e2108dea7730c90039720772309cc4ace4e620949450e3181722f52,68903,2026-07-28T23:33:02Z
MIT/outputs/10d/checkpoints/graphs_N2.json,graphs_N2.json,,,OBSERVED RUN,,,,c77e0cb9f24b24d3ea7c7dfa5862afa3143e1462121482268c98e5b3a4a3ee45,337,2026-08-06T05:55:16Z
MIT/outputs/10d/checkpoints/graphs_N4.json,graphs_N4.json,,,OBSERVED RUN,,,,1948da317ae60478d904f2134010dc747b379d88ea4af726fdbac90fba56d564,412,2026-08-06T05:55:16Z
MIT/outputs/10d/checkpoints/self_duality.json,self_duality.json,,,SOURCE EXISTS,,,,bc46e6707941fdef16a7e2949ab0271cac9eca9081feaa3fbad2d26779709cdc,303,2026-08-06T13:07:05Z
MIT/outputs/10d/explore_summary.json,explore_summary.json,,,SOURCE EXISTS,,,,5a8815a59810f494dae4aa0db4eca98eb6ed15772a76516f018c3b30680b9890,3109,2026-08-06T13:07:05Z
MIT/outputs/10d/generators.json,generators.json,,,SOURCE EXISTS,,,,1195729e355fadf5d879e7967f1e0fe88cf31fd981540d6f21a29ecfca758888,156,2026-08-06T13:07:05Z
MIT/outputs/10d/graphs.json,graphs.json,,,SOURCE EXISTS,,,,8272a8a2aba428a6371a32c3ca84951fbf6f1786554d9aeb3caeac7e4af72c30,819,2026-08-06T13:07:05Z
MIT/outputs/10d/ranks.json,ranks.json,,,SOURCE EXISTS,,,,44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a,2,2026-08-06T13:07:05Z
MIT/outputs/10d/syzygies.json,syzygies.json,,,SOURCE EXISTS,,,,4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945,2,2026-08-06T13:07:05Z
MIT/outputs/6d/generators.json,generators.json,,,OBSERVED RUN,,,,8f42d750bcf6fa6bcd2cbebe046df1516d43fc222bfbb48536223d6d59a66664,412,2026-08-06T13:05:16Z
MIT/outputs/6d/graphs.json,graphs.json,,,OBSERVED RUN,,,,0d9faa652355b88fef6ebbc1db24498a418d1342b9cb776d5d7de9d03cd02dad,47067,2026-08-06T13:05:16Z
MIT/outputs/6d/ranks.json,ranks.json,,,OBSERVED RUN,,,,21f2a821faafd004202053694e03c265cc59038661166f5c997f6991a8a837eb,1984,2026-08-06T13:05:16Z
MIT/outputs/6d/syzygies.json,syzygies.json,,,OBSERVED RUN,,,,263df599295690deb285b73476c8b47c345ff984bc1bc114fe94d0bae10ff3da,16300,2026-08-06T13:05:16Z
MIT/references/machine_learning_invariants_of_tensors.pdf,machine_learning_invariants_of_tensors.pdf,,,SOURCE EXISTS,,,,03c5d970f96bda42b6c39c38e858412c65f6d9fac315ecdd0267bed95212c24a,668076,2026-08-06T05:15:44Z
MIT/reports/10d_methodology.md,10d_methodology.md,,,SOURCE EXISTS,,,,2fa7ebe481fe3c40badade3b159c93700064a28940116de2378ad830b0d8038c,1216,2026-08-06T13:07:05Z
MIT/reports/10d_results.md,10d_results.md,,,SOURCE EXISTS,,,,0b0be3cc190f569d634455dce014ab5eeb7af83d6dea5c81feb891baf8db7c80,1029,2026-08-06T13:07:05Z
MIT/reports/6d_reproduction.md,6d_reproduction.md,,,SOURCE EXISTS,,,,ac5f12f24ecc8c3e113bd1204e9f56f4e6cfaac2407c87b86a51333b206f0dd4,1201,2026-08-06T13:05:16Z
MIT/reports/initial_audit.md,initial_audit.md,,,SOURCE EXISTS,,,,663bac4cdb5b26d824a6593143101e1eae1f650e411347aa3b4a7fc6e9b9b77b,7651,2026-08-06T05:58:38Z
MIT/requirements.txt,requirements.txt,,,OBSERVED RUN,,,,c6d1e4e5e9ab4c3935d85d39d4dbcb20759b9b5d80211625e48b83bbc45b372f,89,2026-08-06T05:27:26Z
MIT/research_state/.gitignore,.gitignore,,,SOURCE EXISTS,,,,240a3e0d37d2e86b614063f5347eb02d4f99ca6c254de6b82871ff8d95532a7d,14,2026-07-27T22:48:47Z
MIT/research_state/cache/graphs_N2_r3.json,graphs_N2_r3.json,,,SOURCE EXISTS,,,,cbd23a70aae6076bcafeba1b73daaeaea3fd445ab65fdf8eb83005c5fa4d6ba5,142,2026-08-06T05:15:16Z
MIT/research_state/cache/graphs_N4_r3.json,graphs_N4_r3.json,,,SOURCE EXISTS,,,,41808500aa93d2504725c8fb6edb0f7b1a79cebadc82f4c1f872693930df6ef6,268,2026-08-06T05:15:16Z
MIT/research_state/cache/graphs_N6_r3.json,graphs_N6_r3.json,,,SOURCE EXISTS,,,,ec3af4deb28954d0e075f05c5c0edeac261c24f7b760cdb6446e024d71a54db2,1064,2026-08-06T05:18:58Z
MIT/research_state/live_progress.json,live_progress.json,,,SOURCE EXISTS,,,,f4123feaff7d7c419a8392507c9c41fd6ed11b5cbd002dc9e6e7ea3f1485ecd1,3284,2026-08-06T05:15:16Z
MIT/research_state/logs/run_5b6b16938416.log,run_5b6b16938416.log,,,SOURCE EXISTS,,,,dcaa4b280a6574dc4711cac394cf5464ac196df40f26ece8bbad27101ec2ec69,74,2026-08-06T05:15:16Z
MIT/run_pipeline.py,run_pipeline.py,,,RERUN PASSED,,,,0754863f0002859eefae42e3562dcbf7dd00a4eed200491c6d09e282156c5a89,6545,2026-08-06T06:00:42Z
MIT/scripts/brain_monitor.py,brain_monitor.py,,,SOURCE EXISTS,,,,445921e8eb1809fa5b82a47a1868b67fb35196594a395e374cb2f247cdca38a6,4006,2026-07-27T22:48:47Z
MIT/scripts/brain_tick.sh,brain_tick.sh,,,SOURCE EXISTS,,,,c340301fa383a30896be1244b3240b04cda031d6b5beb09a698d02430077f445,1097,2026-07-27T22:48:47Z
MIT/scripts/lib/autonomous_common.sh,autonomous_common.sh,,,SOURCE EXISTS,,,,08863a978bfd3938cc41028bfa5b08d8564c0d5356075c41569b9a4cb76b4d41,3037,2026-07-27T22:48:47Z
MIT/scripts/run_10d.py,run_10d.py,,,SOURCE EXISTS,,,,e73d7cebf75a10ad576e0e60cc9b21f0169eb4d2d090e7812dd35db1c8c09127,1507,2026-07-27T22:48:47Z
MIT/scripts/run_6d.py,run_6d.py,,,SOURCE EXISTS,,,,05e4729aa96edbecbc3a8f5651ae028f93c2bc16f9e708169a799e6d267bf4fa,1611,2026-07-27T22:48:47Z
MIT/scripts/run_autonomous_local.sh,run_autonomous_local.sh,,,SOURCE EXISTS,,,,a82e7b1e486b8f8bb9b13b5709e17108ade02fb9f1baa2728ff1aa06ed56c6d6,6234,2026-07-27T22:48:47Z
MIT/scripts/run_ladder.py,run_ladder.py,,,SOURCE EXISTS,,,,9bd6435dded94a55f0ecf82ab7b3cda84e1dcbb230e27b4c0b2b3bd672d5bf42,1548,2026-07-27T22:48:47Z
MIT/scripts/search_ui_server.py,search_ui_server.py,,,SOURCE EXISTS,,,,ffe58d2fff1956266130fa8e3c28c443167019da3db5136d5f6744bb2158880c,2425,2026-07-27T22:48:47Z
MIT/scripts/start_brain_monitor.sh,start_brain_monitor.sh,,,SOURCE EXISTS,,,,a8459dfedd9496b1502e50742aa022dac51f28b36f64a8f292071011694e5649,3461,2026-07-27T22:48:47Z
MIT/scripts/start_forever_daemon.sh,start_forever_daemon.sh,,,SOURCE EXISTS,,,,817b47110393153d8ac34c6121c84dac01ec3b84120fdd1017e75871cc422b28,2988,2026-07-27T22:48:47Z
MIT/scripts/status_autonomous_local.sh,status_autonomous_local.sh,,,SOURCE EXISTS,,,,4ea07c5c2cf9e8bdbc05e4d6db5b4de0ad5d142d86a7cabbb3e2b066e84136f4,1638,2026-07-27T22:48:47Z
MIT/scripts/stop_autonomous_local.sh,stop_autonomous_local.sh,,,SOURCE EXISTS,,,,3dfb7cb3a5818ebe74a73786f9c82ac251f59b8ce1091e0af014883e9421da49,1467,2026-07-27T22:48:47Z
MIT/scripts/supervise_autonomous_local.sh,supervise_autonomous_local.sh,,,SOURCE EXISTS,,,,7275de4b08183961af7b697efb9d162f39fabedd43623416cd3b327d57d0948a,2714,2026-07-27T22:48:47Z
MIT/src/invariant_engine/__init__.py,__init__.py,,,SOURCE EXISTS,,,,9b4e0392caadd99d7493c417891651449c12e4d875e7580626e8ece42fff3e54,100,2026-07-27T22:48:47Z
MIT/src/invariant_engine/__main__.py,__main__.py,,,SOURCE EXISTS,,,,307299fda7b77d22c64cb51430ec75e5f59d78e9c948786afb3b2544fe45e4b7,79,2026-07-27T22:48:47Z
MIT/src/invariant_engine/atomic_io.py,atomic_io.py,,,SOURCE EXISTS,,,,7bed08483f3ed82238d8bc808cd5ed3a7d7b18f89992082d58ece6c6908c2966,1422,2026-07-27T22:48:47Z
MIT/src/invariant_engine/autonomous.py,autonomous.py,,,SOURCE EXISTS,,,,7e40585f811f943a806da3e7c0d34317524c14503e4f78015530a9f2258b90e0,58356,2026-07-27T22:48:47Z
MIT/src/invariant_engine/brain.py,brain.py,,,SOURCE EXISTS,,,,91b251af5a9841e358fe816fce1da729979aad2aea0c38e74dd5a4098d3f89c8,4361,2026-07-27T22:48:47Z
MIT/src/invariant_engine/checkpoint.py,checkpoint.py,,,SOURCE EXISTS,,,,d65b5479f0b79795dfecd0c8e0bfc8babab56b2998c9375f9d2fb87d18aa21e8,1648,2026-07-27T22:48:47Z
MIT/src/invariant_engine/cli.py,cli.py,,,SOURCE EXISTS,,,,fad346a9a67beef5436737acc1e95527c55668197692090642363370f6e15c59,3158,2026-07-27T22:48:47Z
MIT/src/invariant_engine/compute_status.py,compute_status.py,,,SOURCE EXISTS,,,,b92689902413617dd60764d761cdbf219f7f6b2f53f4835f5aea95bf4016605e,1543,2026-07-27T22:48:47Z
MIT/src/invariant_engine/controls.py,controls.py,,,SOURCE EXISTS,,,,3be522e5543ad649d24644862c8e355ea72e9347e1150108a6edc0e855b0c593,1776,2026-07-27T22:48:47Z
MIT/src/invariant_engine/dashboard/__init__.py,__init__.py,,,SOURCE EXISTS,,,,82af92c96827fe8193ed8c8f03135a8b90fc2573d4ae16093856be9bfb79a515,115,2026-07-27T22:48:47Z
MIT/src/invariant_engine/dashboard/server.py,server.py,,,SOURCE EXISTS,,,,62a34c57f2ee17eacb0fc31781fc0029a5058c0dc082686495a3d0d915e9205f,4065,2026-07-27T22:48:47Z
MIT/src/invariant_engine/dashboard/static/app.js,app.js,,,SOURCE EXISTS,,,,c177ae590cef9d67d6ce0f2506887fa79cf4ee1a5699f91ebdc622d2cb04fc66,9721,2026-07-27T22:48:47Z
MIT/src/invariant_engine/dashboard/static/index.html,index.html,,,SOURCE EXISTS,,,,31c9e2310e4923b171a2153f54780fe437804bf52d2c37c3f8930046b623e568,3236,2026-07-27T22:48:47Z
MIT/src/invariant_engine/dashboard/static/style.css,style.css,,,SOURCE EXISTS,,,,4f9ca0f85ad008bc67ecb37b05272d66847ca321c4f53c171ee71c9b78161b27,4070,2026-07-27T22:48:47Z
MIT/src/invariant_engine/heal.py,heal.py,,,SOURCE EXISTS,,,,165e7d92410f65fe6bf70f790554792d45b7f824647f3187454fcde0303574fa,4394,2026-07-27T22:48:47Z
MIT/src/invariant_engine/ladder10d.py,ladder10d.py,,,SOURCE EXISTS,,,,2e8f718e5cc1c0aaa0af014c4f52240d432bac1542183165f27c910f544cc83e,15956,2026-07-27T22:48:47Z
MIT/src/invariant_engine/ladder6d.py,ladder6d.py,,,SOURCE EXISTS,,,,2f91a8aae6010f041ba71a3920132ce68219f2513dae500ed4be285627089835,13444,2026-07-27T22:48:47Z
MIT/src/invariant_engine/offline.py,offline.py,,,SOURCE EXISTS,,,,5fd3d9a868a6a90c2ff886d21ed989ac4a9799db7d0159d6db4793b93b6f0965,8704,2026-07-27T22:48:47Z
MIT/src/invariant_engine/paths.py,paths.py,,,SOURCE EXISTS,,,,bd46cf3c8acffed3d791121398a705a572296357eed0ade28ce6616249f67b60,969,2026-07-27T22:48:47Z
MIT/src/invariant_engine/power.py,power.py,,,SOURCE EXISTS,,,,2dcee9f055e44a61d15594e53cecdb0d3e57ef64ea6ffabc8b75075121ca6593,3196,2026-07-27T22:48:47Z
MIT/src/invariant_engine/presets.py,presets.py,,,SOURCE EXISTS,,,,a530763301c85714d86b0e014c1e47baaadc6913186d5e9ad4275eb969725053,5396,2026-07-27T22:48:47Z
MIT/src/invariant_engine/progress.py,progress.py,,,SOURCE EXISTS,,,,bbe6fd55533edd855b85eb84d433d0781a053791c78bc767bf61906641f47ffb,11721,2026-07-27T22:48:47Z
MIT/src/invariants/__init__.py,__init__.py,,,SOURCE EXISTS,,,,79dd490c95fe9e2be94285923f83c120f2fff58fba149676843907300fce3f01,670,2026-07-27T22:48:47Z
MIT/src/invariants/contraction.py,contraction.py,,,SOURCE EXISTS,,,,81989aae1869fd2805a945a1fdcd3975c1e81286a960a55deda43d0d78bab6de,4873,2026-07-27T22:48:47Z
MIT/src/invariants/discover.py,discover.py,,,SOURCE EXISTS,,,,42f542218d7c6438430387ef7ceef294f2455372c8ae2207873b08af4b85366d,4502,2026-07-27T22:48:47Z
MIT/src/invariants/five_form_10d.py,five_form_10d.py,,,SOURCE EXISTS,,,,b6b30814382bd4ff8f22f30d976c86755b5fd0664be8ba5de5d1574017db84a2,4326,2026-07-27T22:48:47Z
MIT/src/invariants/graphs.py,graphs.py,,,SOURCE EXISTS,,,,52c79adde30b1153b2f6f4841f62b9e04d6401c0615631894a86dfaf4e11f323,9405,2026-07-27T22:48:47Z
MIT/src/invariants/hodge10.py,hodge10.py,,,SOURCE EXISTS,,,,b7d982597fce5f93ec2f11399e59363efffd11d16545ff2fae9802f19ecc9375,10351,2026-07-27T22:48:47Z
MIT/src/invariants/ladder.py,ladder.py,,,SOURCE EXISTS,,,,4679c9558c41bfb703fc4583bb09ca916209fc0b37101a286bb3642f628c2349,2822,2026-07-27T22:48:47Z
MIT/src/invariants/three_form_6d.py,three_form_6d.py,,,SOURCE EXISTS,,,,d2bd15a9ae7c0984b36b2650581396073d20c2f0e449962c4217f9ec9f45a35d,7010,2026-07-27T22:48:47Z
MIT/src/invariants/timed_search.py,timed_search.py,,,SOURCE EXISTS,,,,03a559003248e45622a489a384b60c3ef583ec617f8be20a0576e4ba4c58eac9,12853,2026-07-27T22:48:47Z
MIT/src/invariants/utils.py,utils.py,,,SOURCE EXISTS,,,,3cd9c25a7b94840563d589aa75a1d9bb092857cd3735b97109a48bac6c7e71e6,1838,2026-07-27T22:48:47Z
MIT/tensor_invariants/__init__.py,__init__.py,,,SOURCE EXISTS,,,,e1bef8a168927b815dc199cf6487bfd61262740a2bb026906e365996d781789c,363,2026-08-06T05:20:34Z
MIT/tensor_invariants/antisymmetric_tensors.py,antisymmetric_tensors.py,,,SOURCE EXISTS,,,,85e7c1af8999a443159af146fe22299e261cc18cef74d789fb10fa80a07461fe,3913,2026-08-06T05:22:37Z
MIT/tensor_invariants/checkpointing.py,checkpointing.py,,,SOURCE EXISTS,,,,2064404de00e1877f25e2f375be5ee41dae78b3dee8b051fa191b0edd5324dbe,951,2026-08-06T05:25:11Z
MIT/tensor_invariants/configuration.py,configuration.py,,,SOURCE EXISTS,,,,938367758641aeceb022393b0f83b2e94728196df3912a287aca5a2e179c6ce5,4988,2026-08-06T05:33:27Z
MIT/tensor_invariants/contraction_compiler.py,contraction_compiler.py,,,SOURCE EXISTS,,,,2a50b2a39f3d0f59c34da4a1a408df082c9b8ae979b5728304e439e1c38a58ae,3065,2026-08-06T05:54:35Z
MIT/tensor_invariants/contraction_evaluator.py,contraction_evaluator.py,,,SOURCE EXISTS,,,,b5bb4e435e121c4d34e538ed3b8c05493e912746608bdfd757bd70cd8464bd6f,2072,2026-08-06T05:23:09Z
MIT/tensor_invariants/explore_10d.py,explore_10d.py,,,SOURCE EXISTS,,,,de4c3e4c55f650979da56aad2a5957131c24db1ab440d90e6303a7d88c850426,8379,2026-08-06T05:55:38Z
MIT/tensor_invariants/finite_field.py,finite_field.py,,,SOURCE EXISTS,,,,1cfc29465eab677fa4b683c6caec044b1356a37e484a8a1e671d47c8e406f44b,2339,2026-08-06T05:20:34Z
MIT/tensor_invariants/generator_selection.py,generator_selection.py,,,RERUN PASSED,,,,0ae2296de8ef1d7c908ba8ab9d1d3af0fe9b0ee3246d982ad2b7b2b0736a98d1,10844,2026-08-06T05:54:30Z
MIT/tensor_invariants/graph_canonicalization.py,graph_canonicalization.py,,,SOURCE EXISTS,,,,eedb37959f873b475c92fef064344a0364c24fc2bc96344dbcd853ffb87e5011,4777,2026-08-06T05:54:28Z
MIT/tensor_invariants/graph_enumeration.py,graph_enumeration.py,,,SOURCE EXISTS,,,,dc9e6a1b11cd87b9f9013c5d9d44e7f20f1341bd5ce431ea07f484b498e72ed5,7284,2026-08-06T05:42:42Z
MIT/tensor_invariants/monomial_basis.py,monomial_basis.py,,,SOURCE EXISTS,,,,0d720d572a6c4106b9bac4f7d909c6866cdbc21b3853e95768a87e8561d667a4,2315,2026-08-06T05:23:09Z
MIT/tensor_invariants/nullspace.py,nullspace.py,,,SOURCE EXISTS,,,,51bac4d85b3d67f60938fe9d053ca45f5d3096c9be71b787fb6732535eb91735,3922,2026-08-06T05:21:04Z
MIT/tensor_invariants/numerical_rank.py,numerical_rank.py,,,SOURCE EXISTS,,,,3cb03cb788bc6879189cc7fa657ae4485f9aeb1083d6e093300690c7364480e3,3011,2026-08-06T05:21:28Z
MIT/tensor_invariants/rational_reconstruction.py,rational_reconstruction.py,,,SOURCE EXISTS,,,,0c0baba72089d2e477dfd7ba4778684d7f47f915e4944fbfbcd391f1bd171bfe,5288,2026-08-06T05:21:28Z
MIT/tensor_invariants/reporting.py,reporting.py,,,SOURCE EXISTS,,,,c40d577481feeb0333f380cf2bba1c7aa85b3ce90bc346ca0873e8fd077fc032,6443,2026-08-06T06:00:58Z
MIT/tensor_invariants/self_duality.py,self_duality.py,,,SOURCE EXISTS,,,,e2a5c1265da49f8ce5df9d013f8b068c3ca990fd99fb9b2cfa17f9caaaa58ac5,4887,2026-08-06T05:24:42Z
MIT/tensor_invariants/syzygies.py,syzygies.py,,,SOURCE EXISTS,,,,049af7d656870b4004529af1ff0c04c0fc839e64ff10c8a33fad0c62f884dd64,6186,2026-08-06T05:24:24Z
MIT/tensor_invariants/tensor_spaces.py,tensor_spaces.py,,,SOURCE EXISTS,,,,756fb22eee8bcb299f2ac61d1c8e133b8aaabc96dda5c6ba0a92e4992c348d43,1261,2026-08-06T05:22:37Z
MIT/tensor_invariants/validation.py,validation.py,,,SOURCE EXISTS,,,,a7540cbefae703be747ff0cb297ce63ac33c307343233548f5d1c35bc2747f7c,4384,2026-08-06T05:48:41Z
MIT/tests/__init__.py,__init__.py,,,SOURCE EXISTS,,,,e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855,0,2026-07-27T22:48:47Z
MIT/tests/test_autonomous_infra.py,test_autonomous_infra.py,,,SOURCE EXISTS,,,,afaf22f7ae7f032d25e4e35074611853692dbe41d721d9c0745d228936e6c00f,5905,2026-07-27T22:48:47Z
MIT/tests/test_autonomous_smoke.py,test_autonomous_smoke.py,,,SOURCE EXISTS,,,,2c3525b640e740f3433497a1b60fa768ef7312299d08e05fc1519903ffa32afb,3941,2026-07-27T22:48:47Z
MIT/tests/test_contraction_evaluation.py,test_contraction_evaluation.py,,,SOURCE EXISTS,,,,fa36e291f5dba96f9826805903e669b95f5eebcaf20edb75beb181049099722f,1795,2026-08-06T05:48:42Z
MIT/tests/test_generator_counts_6d.py,test_generator_counts_6d.py,,,SOURCE EXISTS,,,,42f109ade9fb57ccfe8fcccb1287877466ffae08d51cd49fe132c7a74d7e48e0,1886,2026-08-06T05:48:44Z
MIT/tests/test_graph_canonicalization.py,test_graph_canonicalization.py,,,SOURCE EXISTS,,,,1677b88744777b22e22d2ecd507a70921101530e323f7ca60b1bf44a2d67466a,1335,2026-08-06T05:26:36Z
MIT/tests/test_graph_counts_6d.py,test_graph_counts_6d.py,,,SOURCE EXISTS,,,,67d071a36dfb5be6d701343c5529199e623f37ea7a2b6750ce192df429f12799,709,2026-08-06T05:26:43Z
MIT/tests/test_graph_weighted_degree.py,test_graph_weighted_degree.py,,,SOURCE EXISTS,,,,01981488cc24d6c940be4e5b1d2fc8ce175cd479eab802fd9f9a270ab1198949,1339,2026-08-06T05:26:33Z
MIT/tests/test_graphs_6d.py,test_graphs_6d.py,,,SOURCE EXISTS,,,,470bd9cd68c025b680c69e023b9429eea3eb11b8110579f11b15812a22233e5b,4730,2026-07-27T22:48:47Z
MIT/tests/test_hodge10.py,test_hodge10.py,,,SOURCE EXISTS,,,,2a9b9c5716523f88ba7eab7ac3204ab6e4478c3c0b526e92e1217ce37df2de10,2825,2026-07-27T22:48:47Z
MIT/tests/test_monomial_generation.py,test_monomial_generation.py,,,SOURCE EXISTS,,,,4fd2ddaf67b6ade523b7b682f1d7deb2caad26237220afe468c84da1a5ff0add,1340,2026-08-06T05:26:56Z
MIT/tests/test_offline_dashboard.py,test_offline_dashboard.py,,,SOURCE EXISTS,,,,b073b470c338f259091160997745300057baaaef85005bd391823b6edd4f86f6,1597,2026-07-27T22:48:47Z
MIT/tests/test_rank_backends.py,test_rank_backends.py,,,SOURCE EXISTS,,,,2a63b57fd81a22c687862900b9890f33bd16df28b57c2c0cccdd48eebb7c8057,1450,2026-08-06T05:27:04Z
MIT/tests/test_runner_power.py,test_runner_power.py,,,SOURCE EXISTS,,,,5123b46e0497a7d7234745595b1043058998a2a4bb741b7ee48dadb6d35d3979,2476,2026-07-27T22:48:47Z
MIT/tests/test_self_duality_10d.py,test_self_duality_10d.py,,,SOURCE EXISTS,,,,03844765a8df0f8182a28848ca90e250278be0ec9fde78a4b477e3d4e9974435,1254,2026-08-06T05:27:15Z
MIT/tests/test_syzygy_validation.py,test_syzygy_validation.py,,,SOURCE EXISTS,,,,7b3ace68b332dd4d67d2a4f03b5fb1b5f44da87653a8f792ea5707a2c16f03ad,1954,2026-08-06T05:27:15Z
MIT/tests/test_tensor_antisymmetry.py,test_tensor_antisymmetry.py,,,SOURCE EXISTS,,,,32c9abb3e8af8240627048c6639dd527846f050366195ce279ba67b77207e0cf,912,2026-08-06T05:26:28Z
MIT/ui/index.html,index.html,,,SOURCE EXISTS,,,,e5a85ed956207136d46d9a28ba7c22137f102e86d4981d9fba288c784a46c1fd,9002,2026-07-27T22:48:47Z
MIT/ui/progress.json,progress.json,,,SOURCE EXISTS,,,,532cadca61471847b8c2f7479de70b9a92b6448dfedd905dd14cd23243793bb5,12435,2026-07-28T23:33:02Z
Research/TenDDegree6ContractionPlanning_V1.wl,V1,Contraction plans for degree-6 graph basis batches,,NOT RUN,,REQUIRED by BatchA but FILE ABSENT from folder,,,0,

```

---

# 7. RESEARCH_LOGv4 (Mathematica Stages 1–5)

# Chiral 5-form invariant project - research log

## Stage 1 status (2026-08-03)

### Completed

- Read all 46 pages of Elamaran, Ferko, and Scarlett, *Machine Learning Invariants of Tensors*, arXiv:2512.23750v1, including Appendix A.
- Reconstructed the Sections 2-4 numerical graph/rank procedure.
- Extracted the trace-variable HSOP candidates (4.1)-(4.5) and relations (4.12), (A.2), (A.4), and (A.6).
- Implemented the first Mathematica module for exact sparse representation and integer sampling of antisymmetric p-forms.

### Formulas queued for computational reproduction

- `x^(2)`, `x_1^(4)`, `x_2^(4)`, `x^(6)`, `x^(8)` from (4.1)-(4.4).
- Dependent sixth-order contractions `X_1^(6)`, `X_2^(6)` and (A.2).
- Dependent eighth-order contractions `X_1^(8)`, `X_2^(8)` and (A.4), (A.6).
- Hodge-variable relation (4.12).

### Tests defined in Module 1

- `Binomial[6,3] == 20` independent slots.
- Correct permutation sign.
- Sign reversal under a transposition.
- Vanishing with repeated indices.
- Consistency over all permutations of a representative component.

### Discrepancies / cautions

- The paper calls (4.5) an explicit generating set and gives strong numerical evidence through total degree 18, but this computation is not by itself a proof of algebraic independence or completeness.
- Equation (4.12) is reported only to ten decimal places; Appendix A says relations were rationalized from numerical null vectors and checked on 1,000 fresh floating-point samples. Exact verification remains required.
- The trace analysis is Euclidean and metric-only (O(6)); the chiral 10D target is Lorentzian and naturally SO(1,9)-sensitive once epsilon contractions are considered.

### Unresolved mathematical questions

- Exact Hilbert series, generic stabilizer, and Krull dimension for the 10D chiral 5-form representation.
- Lowest nonzero invariant degree and the status of metric-only versus epsilon-using invariants after Lorentzian self-duality.
- A proof-quality treatment of real Lorentzian invariants via complexification and the relevant Spin(10,C) representation.

### Next computational step (blocked pending user test)

- Module 1 was run in Wolfram 15.0.1 on 2026-08-03: 5 tests passed, 0 failed.
- Run Module 2 (`MetricContractions6D.wl`) and correct any version-specific or tensor-contraction issues.

## Stage 2 implementation status (2026-08-03)

### Completed in code, awaiting independent execution

- Added exact raising of tensor indices by an arbitrary nondegenerate metric.
- Added pairwise tensor-network contraction with one inverse metric per graph edge.
- Used a greedy pairwise contraction order to avoid materializing the full outer product of all factors.
- Encoded the five trace-variable contractions from Eqs. (4.1)-(4.4).
- Added five exact verification tests, including a Lorentzian metric check.

### Validation gate

- Gate 2 passes only if all five Module 2 tests succeed in the user's Wolfram installation.

### Discrepancy found during first Module 2 run

- Wolfram 15.0.1 interpreted `AssociationMap[evaluate, specifications]` rule-wise rather than value-wise, causing four of five tests to fail before invariant evaluation.
- Corrected the construction to `Map[evaluate, specifications]`, which preserves the association keys and applies the evaluator to each contraction specification value.
- This was an association-construction bug, not evidence of a tensor-algebra mismatch.

### Gate 2 result

- After the compatibility correction, Module 2 passed 5/5 exact tests in Wolfram 15.0.1.

## Stage 3 implementation status (2026-08-03)

### Completed in code, awaiting independent execution

- Added exact Jacobian recovery by degree-bounded polynomial interpolation.
- The method evaluates each invariant along 20 independent component directions and reconstructs the derivative at the base point with exact rational weights.
- Added exact rank over the rationals and modular rank checks at three primes.
- Added homogeneity verification for degrees `(2,4,4,6,8)`.

### Interpretation gate

- An exact rank-five result at one rational/integer point proves that these five characteristic-zero polynomials are algebraically independent, assuming the implemented contractions match Eqs. (4.1)-(4.4).
- It does not prove that they generate the full invariant ring or that no additional independent invariant exists.

### Discrepancy found during first Module 3 run

- All 20 Jacobian directions and 180 exact invariant evaluations completed in 73.24 seconds.
- Mathematica evaluated the interpolation matrix entry `0^0` as `Indeterminate`, so `LinearSolve` could not construct derivative weights and the downstream rank matrix was invalid.
- Corrected the degree-zero moment row explicitly to `1`. This is an interpolation implementation edge case, not a tensor-algebra discrepancy.

### Structural discrepancy found by the exact Jacobian

- The corrected exact Jacobian had rational rank 4 and modular ranks `(4,4,4)`.
- Its left null vector was `(16584,-279,0,1,0)` at a sample with `x^(2)=558` and `x_1^(4)=70620`.
- These coefficients exactly equal the derivative of Appendix relation (A.2a), demonstrating that the intended `x^(6)` contraction had been evaluated as the dependent `X_1^(6)` contraction.
- Root cause: the pairwise `TensorContract` implementation assumed an output free-index order that was not preserved by the evaluated contraction path.
- Replaced it with explicit axis permutation, matrix reshaping and matrix multiplication, which defines the output order as `left free indices` followed by `right free indices`.
- Added exact Eq. (A.2a) and graph-distinction regression tests.
- A nonsymmetric identity-metric test then isolated the lower-level error: raising axis 3 reordered a generic rank-3 intermediate (`{True,True,False}`), while antisymmetry had hidden this in the original tensor test.
- Reimplemented single-index raising by explicitly moving the target axis to the front, multiplying its matricization by the inverse metric, reshaping, and applying the inverse permutation.
- Added a compiled nine-loop reference evaluation for `x^(6)` as an independent regression oracle.

### Gate 3 result

- Corrected axis tests: `(True,True,True)`.
- Exact Appendix (A.2a) residual: `0`.
- Network and independent nine-loop values for `x^(6)`: both `313296`; dependent `X_1^(6)` remained distinct at `359568`.
- Module 3 then passed 5/5 tests in Wolfram 15.0.1.
- The exact `5 x 20` Jacobian has rank 5 over the rationals and modulo each of `1000003`, `1000033`, and `1000037`.
- Corrected runtime for the 180 exact invariant evaluations: 1.46 seconds, down from approximately 73 seconds with the faulty intermediate-axis ordering.
- All eight Module 2 substantive diagnostics evaluated to `True`. The initial 7/8 `TestReport` was a harness-only false failure caused by referencing the private `RaiseTensorIndex` helper without its full package context after `EndPackage[]`; the test reference was qualified accordingly.

### Established by this gate

- **Reproduced computationally with exact arithmetic:** the five implemented polynomials have an exact Jacobian of rank five at the tested integer point.
- **Established analytically conditional on implementation correctness:** full Jacobian rank at one characteristic-zero point implies algebraic independence of these five polynomials.
- **Not established:** that these five generate the entire invariant ring, that the paper's graph counts have been reproduced, or that all Appendix relations hold for the corrected engine.

## Stage 4 implementation status (2026-08-03)

### Completed in code, awaiting independent execution

- Encoded dependent contractions `X_1^(6)`, `X_2^(6)`, `X_1^(8)`, and `X_2^(8)` from Eqs. (A.1), (A.3), and (A.5).
- Encoded exact residuals for Eqs. (A.2a), (A.2b), (A.4), and (A.6).
- Added 12 fresh integer holdouts drawn from `[-3,3]^20` with seed `20260804`.
- Added separate exact tests for every relation, plus sample-count, uniqueness, and exact-arithmetic checks.

### Gate 4 result

- Module 4 passed 7/7 tests in Wolfram 15.0.1 in 0.241 seconds.
- **Reproduced computationally with exact arithmetic:** Eqs. (A.2a), (A.2b), (A.4), and (A.6) vanish on all 12 fresh integer-valued holdouts.
- No machine-precision values were used; every residual was exactly zero.
- This verifies the stated identities for the implemented contractions on the tested domain. A symbolic tensor-identity proof remains separate.

## Stage 5 implementation status (2026-08-03)

### Completed in code, awaiting independent execution

- Added exact backtracking enumeration of labeled loopless 3-regular multigraph adjacency matrices.
- Added canonicalization through simple incidence graphs and `CanonicalGraph`, so parallel-edge multiplicities are preserved under isomorphism.
- Added conversion from each graph to a concrete signed tensor contraction convention.
- Added exact discovery-matrix ranks and exact nullspaces at degrees 2, 4, 6, and 8.
- Added six fresh holdouts per degree for every discovered same-degree linear relation.
- Target canonical all-graph counts: `(1,3,9,32)`; target connected counts: `(1,2,6,20)`; target exact ranks: `(1,2,3,6)`.

### First Module 5 loading failure

- The initial run did not perform graph enumeration. The private helper name
  `IncidenceGraph` collided with a protected Wolfram System symbol, and the
  optional typed argument of `ContractionGraphData` remained unevaluated in
  Wolfram 15.0.1.
- Renamed the helper to `PFormIncidenceGraph` and made the degree argument
  explicit. This was a package-loading/dispatch failure, not a discrepancy with
  the paper's graph counts.

### Gate 5 result

- The corrected Module 5 passed 6/6 tests twice in Wolfram 15.0.1.
- Labeled loopless 3-regular multigraph counts at degrees `(2,4,6,8)` were
  `(1,10,760,190050)`.
- Canonical all-graph counts were exactly `(1,3,9,32)`.
- Canonical connected-graph counts were exactly `(1,2,6,20)`.
- Exact-arithmetic sampled contraction-matrix ranks were `(1,2,3,6)`.
- Every exact nullspace relation discovered from the training samples vanished
  on the independent exact holdout samples.
- The two observed graph-enumeration/canonicalization runtimes were 119.540 and
  151.359 seconds; the corresponding exact graph-rank runtimes were 1.390 and
  1.286 seconds.

### Interpretation of Gate 5

- **Reproduced computationally:** the paper's graph counts through degree eight.
- **Supported by exact-arithmetic sampling:** the paper's reported same-degree
  contraction ranks `(1,2,3,6)`; finite exact sampling is not by itself a
  symbolic proof of every upper-bound identity.
- **Not established:** completeness of the five-generator invariant set solely
  from stabilization or finite-degree enumeration.

### Next computational step

- Build Module 6 benchmarks: one vector, two vectors, and a real antisymmetric
  2-form in four Euclidean dimensions, using exact graph ranks and Jacobian
  checks before beginning the Lorentzian 10D self-dual 5-form implementation.


---

# 8. TEN-D REPRESENTATION / LITERATURE GATE

# 10D chiral five-form: representation-theory and literature gate

Date: 2026-08-03

This note fixes the external targets that the 10D computation must reproduce. It distinguishes the Krull dimension of the invariant ring, the dimension of each homogeneous space of invariants, and the number of new degree-by-degree generators. Those are three different quantities.

## Status labels

- **Established analytically:** follows from a displayed argument given here.
- **Stated in a cited source:** reported by the cited primary source but not independently proved here.
- **Reproduced computationally:** verified by our exact implementation.
- **Supported only by numerical evidence:** finite sampling or numerical rank only.
- **Conjectural:** a proposed mathematical claim.
- **Unresolved:** not established by the sources or our computation.

## 1. Mathematical object and group

Let \(F\in\Lambda^5(\mathbb R^{1,9})^*\) be real and obey

\[
F=*F,
\qquad
(*F)_{\mu_1\ldots\mu_5}
=\frac1{5!}\epsilon_{\mu_1\ldots\mu_5\nu_1\ldots\nu_5}
F^{\nu_1\ldots\nu_5},
\]

with metric \(\eta=\mathrm{diag}(-,+,\ldots,+)\) and \(\epsilon_{01\ldots9}=+1\). These are the conventions used in our validated `TenDLorentzianFoundations_V2.wl` module and match Section 4 of Cederwall et al. up to the same almost-plus convention.

- **Established analytically and reproduced computationally:** \(*^2=(-1)^{p(D-p)+t}=+1\) for \((D,p,t)=(10,5,1)\), so real eigenspaces of chirality \(\pm1\) exist and each has \(252/2=126\) real components.
- **Established analytically and reproduced computationally:** in Euclidean 10D, \(*^2=-1\), so the middle-form eigenspaces have eigenvalues \(\pm i\); a nonzero real Euclidean self-dual 5-form does not exist.
- **Stated in a cited source:** after complexification the selected chiral module is the 126-dimensional irreducible \(D_5=\mathfrak{so}(10,\mathbb C)\) module with Dynkin label `(00002)` [Cederwall et al., Section 4](https://arxiv.org/pdf/2509.14350).
- **Established analytically and reproduced computationally:** an orientation-reversing element of \(O(1,9)\) exchanges the two chiralities. A single fixed-chirality space is therefore naturally an \(SO(1,9)\) representation, not a representation of the whole \(O(1,9)\).
- **Established analytically:** the tensor is the field strength \(F_5=dA_4\) of a chiral 4-form potential. Gauge invariants without derivatives are polynomials in \(F_5\), not in the potential \(A_4\).

## 2. Generic stabilizer and Krull dimension

Define the symmetric traceless tensor

\[
M_\mu{}^\nu=F_{\mu\rho_1\rho_2\rho_3\rho_4}
F^{\nu\rho_1\rho_2\rho_3\rho_4}.
\]

Cederwall et al. argue in Section 4, Eq. (4.1), that for generic \(F\), \(M\) has distinct eigenvalues. If an infinitesimal Lorentz transformation stabilizes \(F\), it stabilizes \(M\); the distinct-eigenvalue condition forces its Lie-algebra generator to vanish. They therefore identify the generic stabilizer as trivial and obtain

\[
\dim \mathbb C[V]^{SO(10,\mathbb C)}
=126-45=81.
\]

- **Stated in a cited source, with an analytic generic-eigenvalue argument:** the generic stabilizer is trivial and the Krull dimension is 81 [Cederwall et al., Eqs. (2.1), (4.1)](https://arxiv.org/pdf/2509.14350).
- **Important qualification:** 81 is the transcendence degree, equivalently the number of algebraically independent parameters on the generic quotient. It is not the total number of homogeneous generators. A non-free ring may need more than 81 generators and relations among them.
- **Unresolved in this project:** an independent algebraic-geometric proof that the stated diagonalization/distinct-spectrum argument covers a Zariski-open subset of the complex chiral module. Until supplied, we use 81 as a primary-source theorem target, not as a result newly proved by our code.

## 3. Lowest degrees and Hilbert-series targets

Cederwall et al. used LiE to count singlets in \(\operatorname{Sym}^n(126)\). Their Eq. (4.2) gives the truncated Hilbert series

\[
\begin{aligned}
P(t)={}&1+t^4+2t^6+7t^8+14t^{10}+72t^{12}+247t^{14}\\
&+1364t^{16}+6851t^{18}+40170t^{20}+227979t^{22}+O(t^{24}).
\end{aligned}
\]

The corresponding initial Euler-product exponents are

\[
(m_4,m_6,m_8,m_{10},m_{12},m_{14},m_{16},m_{18},m_{20},m_{22})
=(1,2,6,12,62,221,1247,6404,37896,216486).
\]

| Degree | Total singlets \(\dim(\mathrm{Sym}^n126)^{SO(10)}\) | Products forced by lower degrees | Initial new-generator balance |
|---:|---:|---:|---:|
| 2 | 0 | 0 | 0 |
| 4 | 1 | 0 | 1 |
| 6 | 2 | 0 | 2 |
| 8 | 7 | 1 | 6 |
| 10 | 14 | 2 | 12 |
| 12 | 72 | 10 | 62 |
| 14 | 247 | 26 | 221 |
| 16 | 1364 | 117 | 1247 |
| 18 | 6851 | 447 | 6404 |
| 20 | 40170 | 2274 | 37896 |
| 22 | 227979 | 11493 | 216486 |

- **Stated in a cited source:** the Hilbert coefficients and Euler-product exponents above, through degree 22 [Cederwall et al., Eq. (4.2)](https://arxiv.org/pdf/2509.14350).
- **Established analytically:** the familiar quadratic contraction vanishes. Since \(*F=F\),
  \(F\wedge *F=F\wedge F=0\) because a 5-form has odd degree; equivalently \(F_{\mu_1\ldots\mu_5}F^{\mu_1\ldots\mu_5}=0\).
- **Stated in a cited source:** no odd-degree scalar invariants occur, and the LiE series contains only even powers [Hutomo, Lechner and Sorokin, Section 2.1](https://arxiv.org/pdf/2509.14351).
- **Established analytically for the full complex \(SO(10)\):** \(-I\in SO(10,\mathbb C)\) acts as \(-1\) on \(\Lambda^5\), so an invariant polynomial must obey \(p(F)=p(-F)\); hence its odd homogeneous pieces vanish. For the identity component of the real Lorentz group, the equality of polynomial invariants is most safely understood through complexification rather than by claiming \(-I\in SO^+(1,9)\).

The first five positive Euler exponents sum to \(1+2+6+12+62=83\), already exceeding the Krull dimension 81. Therefore the ring cannot be a polynomial ring on all these candidates.

- **Established analytically conditional on the cited counts and dimension:** algebraic relations must exist among a homogeneous generating set.
- **Unresolved:** the first degree at which a minimal syzygy occurs. The positive Euler exponent at a degree is a net generator-minus-relation balance once generators and relations overlap; it cannot indefinitely be read as a raw generator count.
- **Unresolved:** a closed rational Hilbert series, a homogeneous system of parameters, a minimal generating set, and a minimal syzygy resolution.

## 4. Explicit low-degree tensor structures already known

Cederwall et al. decompose bilinears in \(F\) into irreducible tensors \(M^{(54)}\), \(N^{(1050)}\), and \(N^{(4125)}\), Eqs. (4.3)-(4.6).

At degree 4, the unique scalar is

\[
I_4=\operatorname{tr}M^2.
\]

At degree 6, a basis may be chosen as

\[
I_6^{(1)}=\operatorname{tr}M^3
\]

and the independent \(N^{(1050)}N^{(1050)}N^{(1050)}\) contraction displayed in Eq. (4.10) of Cederwall et al. and Eq. (2.14) of Hutomo et al.

At degree 8 there are seven total singlets: \(I_4^2\) plus six new independent structures. Cederwall et al. give tensor and spinor bases in Sections 4.1.3 and 4.2.3. At degree 10 there are 14 total singlets: the two products \(I_4I_6^{(1)}\), \(I_4I_6^{(2)}\), plus twelve new structures discussed in Section 4.1.4.

The nine trace invariants

\[
I_{2n}^{(1)}=\operatorname{tr}M^n,\qquad n=2,\ldots,10,
\]

are algebraically independent within the symmetric-traceless-matrix eigenvalue sector, but they are only nine members of the full 81-dimensional quotient. They do not generate the full chiral-five-form invariant ring.

- **Stated in cited sources:** uniqueness of \(I_4\), two independent degree-6 invariants, six new degree-8 invariants, and twelve new degree-10 invariants [Cederwall et al., Eqs. (4.7)-(4.20) and Section 4.1.4](https://arxiv.org/pdf/2509.14350); [Hutomo et al., Eqs. (2.11)-(2.16)](https://arxiv.org/pdf/2509.14351).
- **Not yet reproduced computationally:** every item in this subsection. These are the first targets for our graph and exact-sampling engine.

## 5. Metric contractions, epsilon contractions, and chirality

- **Established analytically:** two Levi-Civita tensors reduce to generalized Kronecker deltas, so any contraction with an even number of epsilon tensors reduces to metric contractions.
- **Established analytically in the directly saturated case:** if one epsilon tensor uses five indices of a particular \(F\), self-duality replaces that epsilon-F block with a metric-index version of \(F\).
- **Stated in a cited source:** Appendix C of Cederwall et al. systematically derives self-dual-five-form identities by Hodge replacing a form and reducing the product of two epsilon tensors.
- **Unresolved computationally:** whether our future canonicalizer proves that every scalar contraction containing a single epsilon reduces, with all signs and normalizations fixed, to the metric-only graph span. We will not identify parity-even and parity-odd graph spaces merely by assumption.
- **Established analytically:** orientation reversal swaps chirality. Thus a pseudoscalar distinction under full \(O(1,9)\) cannot be discussed inside one chiral 126 alone without adjoining the opposite chirality or specifying how reflection acts between the two spaces.

## 6. Literature table

| Source | Object studied | Signature | Group / representation | Invariant count | Degrees | Relations | Relevance |
|---|---|---|---|---:|---|---|---|
| M. Cederwall, J. Hutomo, S. M. Kuzenko, K. Lechner, D. P. Sorokin, *Some remarks on invariants*, arXiv:2509.14350v2 (2026) | Real self-dual 5-form and broader invariant theory | Lorentzian for tensor formulas; complex algebra for invariant ring | \(SO(1,9)\); complex chiral 126 `(00002)` | Krull dimension 81; singlet counts through degree 22 | First nonzero: 4; counts listed above | Relations must exist; first syzygy degree unknown | Primary representation-theory target and explicit low-degree bases. [arXiv](https://arxiv.org/abs/2509.14350) |
| J. Hutomo, K. Lechner, D. P. Sorokin, *On non-linear chiral 4-form theories in D=10*, JHEP 02 (2026) 147, arXiv:2509.14351 | Chiral 4-form potential with self-dual 5-form composite/field strength | Lorentzian, mostly-plus | \(SO(1,9)\), chiral 126 | 81 functionally independent parameters; explicit degrees 4 and 6 | Unique degree 4; two degree 6; nine trace-sector invariants at 4 through 20 | Full classification open | Physical nonlinear-theory and 10D ModMax-like context. [arXiv](https://arxiv.org/abs/2509.14351), [DOI](https://doi.org/10.1007/JHEP02(2026)147) |
| I. Bandos, K. Lechner, D. Sorokin, P. K. Townsend, *A non-linear duality-invariant conformal extension of Maxwell's equations*, Phys. Rev. D 102 (2020) 121703, arXiv:2007.09092 | ModMax nonlinear electrodynamics | 4D Lorentzian | 4D electromagnetic duality and Lorentz symmetry | Not a 10D invariant count | Quartic structure in 4D formulation | Not a 10D syzygy result | This is reference [67] of Elamaran et al.; it motivates “ModMax-type” language but does not classify 10D chiral-five-form invariants. [arXiv](https://arxiv.org/abs/2007.09092), [DOI](https://doi.org/10.1103/PhysRevD.102.121703) |
| I. Bandos, K. Lechner, D. Sorokin, P. K. Townsend, *On p-form gauge theories and their conformal limits*, JHEP 03 (2021) 022, arXiv:2012.09286 | Nonlinear duality-invariant and chiral p-form theories | Minkowski | General p-forms in \(D=4n\), chiral forms in \(D=4n+2\) | No 10D invariant-ring enumeration | Model-dependent | No invariant-ring resolution | General chiral/ModMax-type framework. [arXiv](https://arxiv.org/abs/2012.09286), [DOI](https://doi.org/10.1007/JHEP03(2021)022) |
| Z. Avetisyan, O. Evnin, K. Mkrtchyan, *Nonlinear (chiral) p-form electrodynamics*, JHEP 08 (2022) 112, arXiv:2205.02522 | Lagrangian theories for nonlinear higher forms, including 4-forms in 10D | Lorentzian | Chiral \(2k\)-forms in \(4k+2\) dimensions | No invariant-ring enumeration | Model-dependent | No invariant-ring resolution | Independent formulation of interacting 10D chiral 4-forms. [arXiv](https://arxiv.org/abs/2205.02522), [DOI](https://doi.org/10.1007/JHEP08(2022)112) |
| A. Sen, *Covariant Action for Type IIB Supergravity*, JHEP 07 (2016) 017, arXiv:1511.08220 | Type IIB supergravity with self-dual five-form sector | 10D Lorentzian | Lorentz covariant type IIB fields | No invariant-ring count | Action-level | No scalar-contraction classification | Confirms the physical chiral 4-form / self-dual 5-form setting. [arXiv](https://arxiv.org/abs/1511.08220), [DOI](https://doi.org/10.1007/JHEP07(2016)017) |
| M. F. Paulos, *Higher derivative terms including the Ramond-Ramond five-form*, JHEP 10 (2008) 047, arXiv:0804.0763 | Higher-derivative type-IIB couplings involving \(F_5\) and curvature | 10D Lorentzian | Type IIB covariance | Specialized contraction basis, not full pure-\(F_5\) ring | Eight-derivative correction sector | Schouten reductions in that sector | Shows why exact tensor-identity reduction matters in type IIB applications. [arXiv](https://arxiv.org/abs/0804.0763), [DOI](https://doi.org/10.1088/1126-6708/2008/10/047) |

### Generic unconstrained 5-form versus chiral 5-form

The table's invariant counts apply to one chiral 126, not to the full 252-dimensional \(\Lambda^5\). For an unconstrained real 5-form the quadratic norm does not vanish generically, both chiral halves are present in Lorentzian signature, and the invariant ring is a different problem.

- **Unresolved:** a complete Hilbert series, minimal generators, syzygies, or canonical generic-orbit classification for the unconstrained 252-dimensional five-form was not located in this targeted primary-source review.
- **Methodological rule:** no count for the chiral 126 may be transferred to the unconstrained 252 representation.

## 7. Computational consequences and validation gates

The next implementation must proceed in this order:

1. Reproduce exactly the Hilbert coefficient and Euler-exponent table through degree 22 from fixed integer data.
2. Enumerate degree-4 metric graphs and recover a one-dimensional nonzero span represented by \(I_4=\operatorname{tr}M^2\).
3. Enumerate degree-6 graphs and recover a two-dimensional span; verify that \(\operatorname{tr}M^3\) alone is insufficient.
4. At degree 8, recover total dimension 7 and distinguish the product \(I_4^2\) from six new directions.
5. At degree 10, recover total dimension 14 and distinguish the two products \(I_4I_6^{(1,2)}\) from twelve new directions.
6. Use exact rational and multi-prime modular ranks; verify every nullspace relation on fresh exact holdouts.
7. Treat graph stabilization only as evidence. Completeness at a degree is certified only by matching the independent representation-theoretic singlet count.

The combinatorics become severe immediately: a metric-only contraction of \(N\) five-valent vertices is a loopless 5-regular multigraph, with antisymmetry signs beyond ordinary graph isomorphism. The practical first target is degree 4, followed by degree 6. Degree 8 should not be attempted until both lower gates match the cited singlet multiplicities exactly.

## 8. Gate decision

**Gate passed at the literature/formulation level:** the target representation, generic quotient dimension, first nonzero degree, and singlet counts through degree 22 are now sourced.

**Gate not yet passed computationally:** none of the 10D invariant counts or explicit low-degree tensor structures has yet been reproduced by our own enumeration code. The next code module should implement degree-4 direct and graph evaluations and compare them with \(\operatorname{tr}M^2\).


---

# 9. DEGREE-6 CATALOG CSV

```csv
"CanonicalGraphNumber","Connected","PeakRank","PeakWorkExponent","CoefficientI6Trace","CoefficientI6N1050","VanishesOnExactFit","HoldoutResidual","GraphKey"
1,false,5,5,"0","0",true,"0","{0, 0, 0, 0, 5, 0, 0, 5, 0, 5, 0, 0, 0, 0, 0}"
2,false,5,6,"0","0",true,"0","{0, 0, 0, 0, 5, 0, 1, 4, 0, 4, 1, 0, 0, 0, 0}"
3,false,5,7,"0","0",true,"0","{0, 0, 0, 0, 5, 0, 2, 3, 0, 3, 2, 0, 0, 0, 0}"
4,false,5,7,"0","0",true,"0","{0, 0, 0, 0, 5, 1, 1, 3, 0, 3, 1, 0, 1, 0, 0}"
5,false,6,8,"0","0",true,"0","{0, 0, 0, 0, 5, 1, 2, 2, 0, 2, 2, 0, 1, 0, 0}"
6,true,5,6,"1/4","0",false,"0","{0, 0, 0, 1, 4, 0, 1, 3, 1, 4, 1, 0, 0, 0, 0}"
7,true,5,6,"1","0",false,"0","{0, 0, 0, 1, 4, 0, 1, 4, 0, 4, 0, 1, 0, 0, 0}"
8,true,5,7,"-1/8","0",false,"0","{0, 0, 0, 1, 4, 0, 2, 2, 1, 3, 2, 0, 0, 0, 0}"
9,true,5,7,"3/16","0",false,"0","{0, 0, 0, 1, 4, 0, 2, 3, 0, 3, 1, 1, 0, 0, 0}"
10,true,5,7,"-1/16","0",false,"0","{0, 0, 0, 1, 4, 1, 1, 2, 1, 3, 1, 0, 1, 0, 0}"
11,true,5,7,"-3/32","0",false,"0","{0, 0, 0, 1, 4, 1, 1, 3, 0, 3, 0, 1, 1, 0, 0}"
12,true,5,6,"0","0",true,"0","{0, 0, 0, 1, 4, 1, 1, 3, 0, 4, 0, 0, 0, 0, 1}"
13,true,6,8,"1/144","0",false,"0","{0, 0, 0, 1, 4, 1, 2, 1, 1, 2, 2, 0, 1, 0, 0}"
14,true,6,8,"1/36","0",false,"0","{0, 0, 0, 1, 4, 1, 2, 2, 0, 2, 2, 0, 0, 1, 0}"
15,true,5,7,"0","0",true,"0","{0, 0, 0, 1, 4, 1, 2, 2, 0, 3, 1, 0, 0, 0, 1}"
16,true,6,8,"0","0",true,"0","{0, 0, 0, 1, 4, 2, 2, 1, 0, 2, 1, 0, 1, 0, 1}"
17,true,5,7,"-1/16","0",false,"0","{0, 0, 0, 2, 3, 0, 2, 1, 2, 3, 2, 0, 0, 0, 0}"
18,true,5,7,"-1/64","0",false,"0","{0, 0, 0, 2, 3, 0, 2, 2, 1, 3, 1, 1, 0, 0, 0}"
19,true,5,7,"3/32","0",false,"0","{0, 0, 0, 2, 3, 0, 2, 3, 0, 3, 0, 2, 0, 0, 0}"
20,true,5,7,"-1/32","0",false,"0","{0, 0, 0, 2, 3, 1, 1, 1, 2, 3, 1, 0, 1, 0, 0}"
21,true,5,7,"1/128","0",false,"0","{0, 0, 0, 2, 3, 1, 1, 2, 1, 3, 0, 1, 1, 0, 0}"
22,true,5,7,"3/64","0",false,"0","{0, 0, 0, 2, 3, 1, 1, 3, 0, 3, 0, 1, 0, 1, 0}"
23,true,6,8,"-1/288","0",false,"0","{0, 0, 0, 2, 3, 1, 2, 0, 2, 2, 2, 0, 1, 0, 0}"
24,true,6,8,"1/288","0",false,"0","{0, 0, 0, 2, 3, 1, 2, 1, 1, 2, 1, 1, 1, 0, 0}"
25,true,6,8,"1/192","0",false,"0","{0, 0, 0, 2, 3, 1, 2, 1, 1, 2, 2, 0, 0, 1, 0}"
26,true,5,7,"0","0",true,"0","{0, 0, 0, 2, 3, 1, 2, 1, 1, 3, 1, 0, 0, 0, 1}"
27,true,5,7,"0","0",true,"0","{0, 0, 0, 2, 3, 1, 2, 2, 0, 3, 0, 1, 0, 0, 1}"
28,true,6,8,"0","0",true,"0","{0, 0, 0, 2, 3, 2, 2, 0, 1, 2, 1, 0, 1, 0, 1}"
29,true,5,7,"0","0",true,"0","{0, 0, 0, 2, 3, 2, 2, 1, 0, 3, 0, 0, 0, 0, 2}"
30,true,5,7,"7/64","0",false,"0","{0, 0, 1, 1, 3, 0, 1, 3, 1, 3, 1, 1, 0, 0, 0}"
31,true,6,8,"0","0",true,"0","{0, 0, 1, 1, 3, 0, 2, 2, 1, 2, 2, 1, 0, 0, 0}"
32,true,5,7,"11/128","0",false,"0","{0, 0, 1, 1, 3, 1, 0, 3, 1, 3, 0, 1, 1, 0, 0}"
33,true,5,7,"-3/128","0",false,"0","{0, 0, 1, 1, 3, 1, 0, 3, 1, 3, 1, 0, 0, 1, 0}"
34,true,6,8,"1/72","0",false,"0","{0, 0, 1, 1, 3, 1, 1, 2, 1, 2, 1, 1, 1, 0, 0}"
35,true,6,8,"-1/384","0",false,"0","{0, 0, 1, 1, 3, 1, 1, 2, 1, 2, 2, 0, 0, 1, 0}"
36,true,5,7,"-1/256","0",false,"0","{0, 0, 1, 1, 3, 1, 1, 2, 1, 3, 1, 0, 0, 0, 1}"
37,true,6,8,"11/288","0",false,"0","{0, 0, 1, 1, 3, 2, 0, 2, 1, 2, 0, 1, 2, 0, 0}"
38,true,6,8,"0","0",true,"0","{0, 0, 1, 1, 3, 2, 1, 1, 1, 1, 1, 1, 2, 0, 0}"
39,true,6,8,"-1/576","0",false,"0","{0, 0, 1, 1, 3, 2, 1, 1, 1, 1, 2, 0, 1, 1, 0}"
40,true,6,8,"-1/576","0",false,"0","{0, 0, 1, 1, 3, 2, 1, 2, 0, 2, 1, 0, 0, 1, 1}"
41,true,5,7,"-1/64","0",false,"0","{0, 0, 1, 1, 3, 3, 1, 1, 0, 1, 1, 0, 1, 1, 1}"
42,true,6,9,"-1/12","0",false,"0","{0, 0, 1, 2, 2, 0, 2, 1, 2, 2, 2, 1, 0, 0, 0}"
43,true,6,9,"-7/864","0",false,"0","{0, 0, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 0, 0}"
44,true,6,9,"1/288","0",false,"0","{0, 0, 1, 2, 2, 1, 1, 1, 2, 2, 2, 0, 0, 1, 0}"
45,true,6,8,"-13/432","0",false,"0","{0, 0, 1, 2, 2, 1, 2, 0, 2, 2, 2, 0, 0, 0, 1}"
46,true,6,8,"-7/432","0",false,"0","{0, 0, 1, 2, 2, 1, 2, 1, 1, 2, 1, 1, 0, 0, 1}"
47,true,6,8,"1/576","-125/3",false,"0","{0, 0, 1, 2, 2, 2, 1, 0, 2, 1, 1, 1, 2, 0, 0}"
48,true,7,9,"1/288","125/3",false,"0","{0, 0, 1, 2, 2, 2, 1, 0, 2, 1, 2, 0, 1, 1, 0}"
49,true,7,9,"0","0",true,"0","{0, 0, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0}"
50,true,6,8,"-1/864","125/6",false,"0","{0, 0, 1, 2, 2, 2, 1, 1, 1, 2, 0, 1, 1, 0, 1}"
51,true,6,8,"-5/144","250/3",false,"0","{0, 0, 1, 2, 2, 2, 2, 0, 1, 2, 1, 0, 0, 0, 2}"
52,true,7,9,"-1/144","125/12",false,"0","{0, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 0}"
53,true,6,9,"-13/2304","125/12",false,"0","{0, 1, 1, 1, 2, 1, 1, 2, 1, 2, 0, 1, 1, 0, 1}"
54,true,8,12,"-17/1152","125/4",false,"0","{1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}"

```

---

# 10. DEGREE-8 INVARIANT FORMULA CATALOG (TXT)

```
10D Lorentzian self-dual five-form: validated degree-eight basis
Metric convention: diag(-1,+1,+1,+1,+1,+1,+1,+1,+1,+1)
Orientation: +1; chirality: +1; F = HodgeStar[F]
Basis direction 1: I4^2
I4^2 where I4 = Tr[(M.gInverse)^2]
M[mu,nu] = 4! Sum[F[mu,a,b,c,d] F[nu]^raised[a,b,c,d], a<b<c<d]
The remaining six basis directions are raw connected graph contractions.
In each compact expression, every repeated i_n is contracted with g inverse.

Graph 3
Graph key: {0, 0, 0, 0, 0, 1, 4, 0, 0, 0, 1, 4, 0, 0, 1, 4, 0, 0, 4, 0, 0, 1, 0, 0, 0, 0, 0, 0}
Adjacency matrix: {{0, 0, 0, 0, 0, 0, 1, 4}, {0, 0, 0, 0, 0, 1, 4, 0}, {0, 0, 0, 0, 1, 4, 0, 0}, {0, 0, 0, 0, 4, 0, 0, 1}, {0, 0, 1, 4, 0, 0, 0, 0}, {0, 1, 4, 0, 0, 0, 0, 0}, {1, 4, 0, 0, 0, 0, 0, 0}, {4, 0, 0, 1, 0, 0, 0, 0}}
Vertex index labels: {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15}, {16, 17, 18, 19, 20}, {11, 16, 17, 18, 19}, {6, 12, 13, 14, 15}, {1, 7, 8, 9, 10}, {2, 3, 4, 5, 20}}
Compact contraction: Inactive[Times][D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 2], Subscript[i, 3], Subscript[i, 4], Subscript[i, 5]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 7], Subscript[i, 8], Subscript[i, 9], Subscript[i, 10]], D8FormulaFiveForm[Subscript[i, 11], Subscript[i, 12], Subscript[i, 13], Subscript[i, 14], Subscript[i, 15]], D8FormulaFiveForm[Subscript[i, 16], Subscript[i, 17], Subscript[i, 18], Subscript[i, 19], Subscript[i, 20]], D8FormulaFiveForm[Subscript[i, 11], Subscript[i, 16], Subscript[i, 17], Subscript[i, 18], Subscript[i, 19]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 12], Subscript[i, 13], Subscript[i, 14], Subscript[i, 15]], D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 7], Subscript[i, 8], Subscript[i, 9], Subscript[i, 10]], D8FormulaFiveForm[Subscript[i, 2], Subscript[i, 3], Subscript[i, 4], Subscript[i, 5], Subscript[i, 20]]]
Metric-explicit contraction: Inactive[Times][D8FormulaMetricInverse[Subscript[a, 1], Subscript[b, 1]], D8FormulaMetricInverse[Subscript[a, 2], Subscript[b, 2]], D8FormulaMetricInverse[Subscript[a, 3], Subscript[b, 3]], D8FormulaMetricInverse[Subscript[a, 4], Subscript[b, 4]], D8FormulaMetricInverse[Subscript[a, 5], Subscript[b, 5]], D8FormulaMetricInverse[Subscript[a, 6], Subscript[b, 6]], D8FormulaMetricInverse[Subscript[a, 7], Subscript[b, 7]], D8FormulaMetricInverse[Subscript[a, 8], Subscript[b, 8]], D8FormulaMetricInverse[Subscript[a, 9], Subscript[b, 9]], D8FormulaMetricInverse[Subscript[a, 10], Subscript[b, 10]], D8FormulaMetricInverse[Subscript[a, 11], Subscript[b, 11]], D8FormulaMetricInverse[Subscript[a, 12], Subscript[b, 12]], D8FormulaMetricInverse[Subscript[a, 13], Subscript[b, 13]], D8FormulaMetricInverse[Subscript[a, 14], Subscript[b, 14]], D8FormulaMetricInverse[Subscript[a, 15], Subscript[b, 15]], D8FormulaMetricInverse[Subscript[a, 16], Subscript[b, 16]], D8FormulaMetricInverse[Subscript[a, 17], Subscript[b, 17]], D8FormulaMetricInverse[Subscript[a, 18], Subscript[b, 18]], D8FormulaMetricInverse[Subscript[a, 19], Subscript[b, 19]], D8FormulaMetricInverse[Subscript[a, 20], Subscript[b, 20]], D8FormulaFiveForm[Subscript[a, 1], Subscript[a, 2], Subscript[a, 3], Subscript[a, 4], Subscript[a, 5]], D8FormulaFiveForm[Subscript[a, 6], Subscript[a, 7], Subscript[a, 8], Subscript[a, 9], Subscript[a, 10]], D8FormulaFiveForm[Subscript[a, 11], Subscript[a, 12], Subscript[a, 13], Subscript[a, 14], Subscript[a, 15]], D8FormulaFiveForm[Subscript[a, 16], Subscript[a, 17], Subscript[a, 18], Subscript[a, 19], Subscript[a, 20]], D8FormulaFiveForm[Subscript[b, 11], Subscript[b, 16], Subscript[b, 17], Subscript[b, 18], Subscript[b, 19]], D8FormulaFiveForm[Subscript[b, 6], Subscript[b, 12], Subscript[b, 13], Subscript[b, 14], Subscript[b, 15]], D8FormulaFiveForm[Subscript[b, 1], Subscript[b, 7], Subscript[b, 8], Subscript[b, 9], Subscript[b, 10]], D8FormulaFiveForm[Subscript[b, 2], Subscript[b, 3], Subscript[b, 4], Subscript[b, 5], Subscript[b, 20]]]
Normalization: 1

Graph 249
Graph key: {0, 0, 0, 0, 4, 0, 1, 0, 0, 4, 0, 0, 1, 4, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 2}
Adjacency matrix: {{0, 0, 0, 0, 0, 4, 0, 1}, {0, 0, 0, 0, 4, 0, 0, 1}, {0, 0, 0, 4, 0, 0, 0, 1}, {0, 0, 4, 0, 0, 0, 1, 0}, {0, 4, 0, 0, 0, 0, 1, 0}, {4, 0, 0, 0, 0, 0, 1, 0}, {0, 0, 0, 1, 1, 1, 0, 2}, {1, 1, 1, 0, 0, 0, 2, 0}}
Vertex index labels: {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15}, {11, 12, 13, 14, 16}, {6, 7, 8, 9, 17}, {1, 2, 3, 4, 18}, {16, 17, 18, 19, 20}, {5, 10, 15, 19, 20}}
Compact contraction: Inactive[Times][D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 2], Subscript[i, 3], Subscript[i, 4], Subscript[i, 5]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 7], Subscript[i, 8], Subscript[i, 9], Subscript[i, 10]], D8FormulaFiveForm[Subscript[i, 11], Subscript[i, 12], Subscript[i, 13], Subscript[i, 14], Subscript[i, 15]], D8FormulaFiveForm[Subscript[i, 11], Subscript[i, 12], Subscript[i, 13], Subscript[i, 14], Subscript[i, 16]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 7], Subscript[i, 8], Subscript[i, 9], Subscript[i, 17]], D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 2], Subscript[i, 3], Subscript[i, 4], Subscript[i, 18]], D8FormulaFiveForm[Subscript[i, 16], Subscript[i, 17], Subscript[i, 18], Subscript[i, 19], Subscript[i, 20]], D8FormulaFiveForm[Subscript[i, 5], Subscript[i, 10], Subscript[i, 15], Subscript[i, 19], Subscript[i, 20]]]
Metric-explicit contraction: Inactive[Times][D8FormulaMetricInverse[Subscript[a, 1], Subscript[b, 1]], D8FormulaMetricInverse[Subscript[a, 2], Subscript[b, 2]], D8FormulaMetricInverse[Subscript[a, 3], Subscript[b, 3]], D8FormulaMetricInverse[Subscript[a, 4], Subscript[b, 4]], D8FormulaMetricInverse[Subscript[a, 5], Subscript[b, 5]], D8FormulaMetricInverse[Subscript[a, 6], Subscript[b, 6]], D8FormulaMetricInverse[Subscript[a, 7], Subscript[b, 7]], D8FormulaMetricInverse[Subscript[a, 8], Subscript[b, 8]], D8FormulaMetricInverse[Subscript[a, 9], Subscript[b, 9]], D8FormulaMetricInverse[Subscript[a, 10], Subscript[b, 10]], D8FormulaMetricInverse[Subscript[a, 11], Subscript[b, 11]], D8FormulaMetricInverse[Subscript[a, 12], Subscript[b, 12]], D8FormulaMetricInverse[Subscript[a, 13], Subscript[b, 13]], D8FormulaMetricInverse[Subscript[a, 14], Subscript[b, 14]], D8FormulaMetricInverse[Subscript[a, 15], Subscript[b, 15]], D8FormulaMetricInverse[Subscript[a, 16], Subscript[b, 16]], D8FormulaMetricInverse[Subscript[a, 17], Subscript[b, 17]], D8FormulaMetricInverse[Subscript[a, 18], Subscript[b, 18]], D8FormulaMetricInverse[Subscript[a, 19], Subscript[b, 19]], D8FormulaMetricInverse[Subscript[a, 20], Subscript[b, 20]], D8FormulaFiveForm[Subscript[a, 1], Subscript[a, 2], Subscript[a, 3], Subscript[a, 4], Subscript[a, 5]], D8FormulaFiveForm[Subscript[a, 6], Subscript[a, 7], Subscript[a, 8], Subscript[a, 9], Subscript[a, 10]], D8FormulaFiveForm[Subscript[a, 11], Subscript[a, 12], Subscript[a, 13], Subscript[a, 14], Subscript[a, 15]], D8FormulaFiveForm[Subscript[b, 11], Subscript[b, 12], Subscript[b, 13], Subscript[b, 14], Subscript[a, 16]], D8FormulaFiveForm[Subscript[b, 6], Subscript[b, 7], Subscript[b, 8], Subscript[b, 9], Subscript[a, 17]], D8FormulaFiveForm[Subscript[b, 1], Subscript[b, 2], Subscript[b, 3], Subscript[b, 4], Subscript[a, 18]], D8FormulaFiveForm[Subscript[b, 16], Subscript[b, 17], Subscript[b, 18], Subscript[a, 19], Subscript[a, 20]], D8FormulaFiveForm[Subscript[b, 5], Subscript[b, 10], Subscript[b, 15], Subscript[b, 19], Subscript[b, 20]]]
Normalization: 1

Graph 508
Graph key: {0, 0, 3, 0, 0, 0, 2, 3, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1}
Adjacency matrix: {{0, 0, 0, 3, 0, 0, 0, 2}, {0, 0, 3, 0, 0, 0, 2, 0}, {0, 3, 0, 0, 0, 2, 0, 0}, {3, 0, 0, 0, 2, 0, 0, 0}, {0, 0, 0, 2, 0, 1, 1, 1}, {0, 0, 2, 0, 1, 0, 1, 1}, {0, 2, 0, 0, 1, 1, 0, 1}, {2, 0, 0, 0, 1, 1, 1, 0}}
Vertex index labels: {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {6, 7, 8, 11, 12}, {1, 2, 3, 13, 14}, {13, 14, 15, 16, 17}, {11, 12, 15, 18, 19}, {9, 10, 16, 18, 20}, {4, 5, 17, 19, 20}}
Compact contraction: Inactive[Times][D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 2], Subscript[i, 3], Subscript[i, 4], Subscript[i, 5]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 7], Subscript[i, 8], Subscript[i, 9], Subscript[i, 10]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 7], Subscript[i, 8], Subscript[i, 11], Subscript[i, 12]], D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 2], Subscript[i, 3], Subscript[i, 13], Subscript[i, 14]], D8FormulaFiveForm[Subscript[i, 13], Subscript[i, 14], Subscript[i, 15], Subscript[i, 16], Subscript[i, 17]], D8FormulaFiveForm[Subscript[i, 11], Subscript[i, 12], Subscript[i, 15], Subscript[i, 18], Subscript[i, 19]], D8FormulaFiveForm[Subscript[i, 9], Subscript[i, 10], Subscript[i, 16], Subscript[i, 18], Subscript[i, 20]], D8FormulaFiveForm[Subscript[i, 4], Subscript[i, 5], Subscript[i, 17], Subscript[i, 19], Subscript[i, 20]]]
Metric-explicit contraction: Inactive[Times][D8FormulaMetricInverse[Subscript[a, 1], Subscript[b, 1]], D8FormulaMetricInverse[Subscript[a, 2], Subscript[b, 2]], D8FormulaMetricInverse[Subscript[a, 3], Subscript[b, 3]], D8FormulaMetricInverse[Subscript[a, 4], Subscript[b, 4]], D8FormulaMetricInverse[Subscript[a, 5], Subscript[b, 5]], D8FormulaMetricInverse[Subscript[a, 6], Subscript[b, 6]], D8FormulaMetricInverse[Subscript[a, 7], Subscript[b, 7]], D8FormulaMetricInverse[Subscript[a, 8], Subscript[b, 8]], D8FormulaMetricInverse[Subscript[a, 9], Subscript[b, 9]], D8FormulaMetricInverse[Subscript[a, 10], Subscript[b, 10]], D8FormulaMetricInverse[Subscript[a, 11], Subscript[b, 11]], D8FormulaMetricInverse[Subscript[a, 12], Subscript[b, 12]], D8FormulaMetricInverse[Subscript[a, 13], Subscript[b, 13]], D8FormulaMetricInverse[Subscript[a, 14], Subscript[b, 14]], D8FormulaMetricInverse[Subscript[a, 15], Subscript[b, 15]], D8FormulaMetricInverse[Subscript[a, 16], Subscript[b, 16]], D8FormulaMetricInverse[Subscript[a, 17], Subscript[b, 17]], D8FormulaMetricInverse[Subscript[a, 18], Subscript[b, 18]], D8FormulaMetricInverse[Subscript[a, 19], Subscript[b, 19]], D8FormulaMetricInverse[Subscript[a, 20], Subscript[b, 20]], D8FormulaFiveForm[Subscript[a, 1], Subscript[a, 2], Subscript[a, 3], Subscript[a, 4], Subscript[a, 5]], D8FormulaFiveForm[Subscript[a, 6], Subscript[a, 7], Subscript[a, 8], Subscript[a, 9], Subscript[a, 10]], D8FormulaFiveForm[Subscript[b, 6], Subscript[b, 7], Subscript[b, 8], Subscript[a, 11], Subscript[a, 12]], D8FormulaFiveForm[Subscript[b, 1], Subscript[b, 2], Subscript[b, 3], Subscript[a, 13], Subscript[a, 14]], D8FormulaFiveForm[Subscript[b, 13], Subscript[b, 14], Subscript[a, 15], Subscript[a, 16], Subscript[a, 17]], D8FormulaFiveForm[Subscript[b, 11], Subscript[b, 12], Subscript[b, 15], Subscript[a, 18], Subscript[a, 19]], D8FormulaFiveForm[Subscript[b, 9], Subscript[b, 10], Subscript[b, 16], Subscript[b, 18], Subscript[a, 20]], D8FormulaFiveForm[Subscript[b, 4], Subscript[b, 5], Subscript[b, 17], Subscript[b, 19], Subscript[b, 20]]]
Normalization: 1

Graph 61
Graph key: {0, 0, 0, 0, 1, 2, 2, 0, 2, 0, 2, 0, 1, 2, 2, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1}
Adjacency matrix: {{0, 0, 0, 0, 0, 1, 2, 2}, {0, 0, 0, 2, 0, 2, 0, 1}, {0, 0, 0, 2, 2, 0, 1, 0}, {0, 2, 2, 0, 1, 0, 0, 0}, {0, 0, 2, 1, 0, 1, 1, 0}, {1, 2, 0, 0, 1, 0, 0, 1}, {2, 0, 1, 0, 1, 0, 0, 1}, {2, 1, 0, 0, 0, 1, 1, 0}}
Vertex index labels: {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15}, {6, 7, 11, 12, 16}, {13, 14, 16, 17, 18}, {1, 8, 9, 17, 19}, {2, 3, 15, 18, 20}, {4, 5, 10, 19, 20}}
Compact contraction: Inactive[Times][D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 2], Subscript[i, 3], Subscript[i, 4], Subscript[i, 5]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 7], Subscript[i, 8], Subscript[i, 9], Subscript[i, 10]], D8FormulaFiveForm[Subscript[i, 11], Subscript[i, 12], Subscript[i, 13], Subscript[i, 14], Subscript[i, 15]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 7], Subscript[i, 11], Subscript[i, 12], Subscript[i, 16]], D8FormulaFiveForm[Subscript[i, 13], Subscript[i, 14], Subscript[i, 16], Subscript[i, 17], Subscript[i, 18]], D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 8], Subscript[i, 9], Subscript[i, 17], Subscript[i, 19]], D8FormulaFiveForm[Subscript[i, 2], Subscript[i, 3], Subscript[i, 15], Subscript[i, 18], Subscript[i, 20]], D8FormulaFiveForm[Subscript[i, 4], Subscript[i, 5], Subscript[i, 10], Subscript[i, 19], Subscript[i, 20]]]
Metric-explicit contraction: Inactive[Times][D8FormulaMetricInverse[Subscript[a, 1], Subscript[b, 1]], D8FormulaMetricInverse[Subscript[a, 2], Subscript[b, 2]], D8FormulaMetricInverse[Subscript[a, 3], Subscript[b, 3]], D8FormulaMetricInverse[Subscript[a, 4], Subscript[b, 4]], D8FormulaMetricInverse[Subscript[a, 5], Subscript[b, 5]], D8FormulaMetricInverse[Subscript[a, 6], Subscript[b, 6]], D8FormulaMetricInverse[Subscript[a, 7], Subscript[b, 7]], D8FormulaMetricInverse[Subscript[a, 8], Subscript[b, 8]], D8FormulaMetricInverse[Subscript[a, 9], Subscript[b, 9]], D8FormulaMetricInverse[Subscript[a, 10], Subscript[b, 10]], D8FormulaMetricInverse[Subscript[a, 11], Subscript[b, 11]], D8FormulaMetricInverse[Subscript[a, 12], Subscript[b, 12]], D8FormulaMetricInverse[Subscript[a, 13], Subscript[b, 13]], D8FormulaMetricInverse[Subscript[a, 14], Subscript[b, 14]], D8FormulaMetricInverse[Subscript[a, 15], Subscript[b, 15]], D8FormulaMetricInverse[Subscript[a, 16], Subscript[b, 16]], D8FormulaMetricInverse[Subscript[a, 17], Subscript[b, 17]], D8FormulaMetricInverse[Subscript[a, 18], Subscript[b, 18]], D8FormulaMetricInverse[Subscript[a, 19], Subscript[b, 19]], D8FormulaMetricInverse[Subscript[a, 20], Subscript[b, 20]], D8FormulaFiveForm[Subscript[a, 1], Subscript[a, 2], Subscript[a, 3], Subscript[a, 4], Subscript[a, 5]], D8FormulaFiveForm[Subscript[a, 6], Subscript[a, 7], Subscript[a, 8], Subscript[a, 9], Subscript[a, 10]], D8FormulaFiveForm[Subscript[a, 11], Subscript[a, 12], Subscript[a, 13], Subscript[a, 14], Subscript[a, 15]], D8FormulaFiveForm[Subscript[b, 6], Subscript[b, 7], Subscript[b, 11], Subscript[b, 12], Subscript[a, 16]], D8FormulaFiveForm[Subscript[b, 13], Subscript[b, 14], Subscript[b, 16], Subscript[a, 17], Subscript[a, 18]], D8FormulaFiveForm[Subscript[b, 1], Subscript[b, 8], Subscript[b, 9], Subscript[b, 17], Subscript[a, 19]], D8FormulaFiveForm[Subscript[b, 2], Subscript[b, 3], Subscript[b, 15], Subscript[b, 18], Subscript[a, 20]], D8FormulaFiveForm[Subscript[b, 4], Subscript[b, 5], Subscript[b, 10], Subscript[b, 19], Subscript[b, 20]]]
Normalization: 1

Graph 376
Graph key: {0, 0, 0, 2, 2, 0, 1, 2, 2, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1}
Adjacency matrix: {{0, 0, 0, 0, 2, 2, 0, 1}, {0, 0, 2, 2, 0, 0, 1, 0}, {0, 2, 0, 1, 0, 0, 1, 1}, {0, 2, 1, 0, 0, 1, 1, 0}, {2, 0, 0, 0, 0, 1, 1, 1}, {2, 0, 0, 1, 1, 0, 0, 1}, {0, 1, 1, 1, 1, 0, 0, 1}, {1, 0, 1, 0, 1, 1, 1, 0}}
Vertex index labels: {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {6, 7, 11, 12, 13}, {8, 9, 11, 14, 15}, {1, 2, 16, 17, 18}, {3, 4, 14, 16, 19}, {10, 12, 15, 17, 20}, {5, 13, 18, 19, 20}}
Compact contraction: Inactive[Times][D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 2], Subscript[i, 3], Subscript[i, 4], Subscript[i, 5]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 7], Subscript[i, 8], Subscript[i, 9], Subscript[i, 10]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 7], Subscript[i, 11], Subscript[i, 12], Subscript[i, 13]], D8FormulaFiveForm[Subscript[i, 8], Subscript[i, 9], Subscript[i, 11], Subscript[i, 14], Subscript[i, 15]], D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 2], Subscript[i, 16], Subscript[i, 17], Subscript[i, 18]], D8FormulaFiveForm[Subscript[i, 3], Subscript[i, 4], Subscript[i, 14], Subscript[i, 16], Subscript[i, 19]], D8FormulaFiveForm[Subscript[i, 10], Subscript[i, 12], Subscript[i, 15], Subscript[i, 17], Subscript[i, 20]], D8FormulaFiveForm[Subscript[i, 5], Subscript[i, 13], Subscript[i, 18], Subscript[i, 19], Subscript[i, 20]]]
Metric-explicit contraction: Inactive[Times][D8FormulaMetricInverse[Subscript[a, 1], Subscript[b, 1]], D8FormulaMetricInverse[Subscript[a, 2], Subscript[b, 2]], D8FormulaMetricInverse[Subscript[a, 3], Subscript[b, 3]], D8FormulaMetricInverse[Subscript[a, 4], Subscript[b, 4]], D8FormulaMetricInverse[Subscript[a, 5], Subscript[b, 5]], D8FormulaMetricInverse[Subscript[a, 6], Subscript[b, 6]], D8FormulaMetricInverse[Subscript[a, 7], Subscript[b, 7]], D8FormulaMetricInverse[Subscript[a, 8], Subscript[b, 8]], D8FormulaMetricInverse[Subscript[a, 9], Subscript[b, 9]], D8FormulaMetricInverse[Subscript[a, 10], Subscript[b, 10]], D8FormulaMetricInverse[Subscript[a, 11], Subscript[b, 11]], D8FormulaMetricInverse[Subscript[a, 12], Subscript[b, 12]], D8FormulaMetricInverse[Subscript[a, 13], Subscript[b, 13]], D8FormulaMetricInverse[Subscript[a, 14], Subscript[b, 14]], D8FormulaMetricInverse[Subscript[a, 15], Subscript[b, 15]], D8FormulaMetricInverse[Subscript[a, 16], Subscript[b, 16]], D8FormulaMetricInverse[Subscript[a, 17], Subscript[b, 17]], D8FormulaMetricInverse[Subscript[a, 18], Subscript[b, 18]], D8FormulaMetricInverse[Subscript[a, 19], Subscript[b, 19]], D8FormulaMetricInverse[Subscript[a, 20], Subscript[b, 20]], D8FormulaFiveForm[Subscript[a, 1], Subscript[a, 2], Subscript[a, 3], Subscript[a, 4], Subscript[a, 5]], D8FormulaFiveForm[Subscript[a, 6], Subscript[a, 7], Subscript[a, 8], Subscript[a, 9], Subscript[a, 10]], D8FormulaFiveForm[Subscript[b, 6], Subscript[b, 7], Subscript[a, 11], Subscript[a, 12], Subscript[a, 13]], D8FormulaFiveForm[Subscript[b, 8], Subscript[b, 9], Subscript[b, 11], Subscript[a, 14], Subscript[a, 15]], D8FormulaFiveForm[Subscript[b, 1], Subscript[b, 2], Subscript[a, 16], Subscript[a, 17], Subscript[a, 18]], D8FormulaFiveForm[Subscript[b, 3], Subscript[b, 4], Subscript[b, 14], Subscript[b, 16], Subscript[a, 19]], D8FormulaFiveForm[Subscript[b, 10], Subscript[b, 12], Subscript[b, 15], Subscript[b, 17], Subscript[a, 20]], D8FormulaFiveForm[Subscript[b, 5], Subscript[b, 13], Subscript[b, 18], Subscript[b, 19], Subscript[b, 20]]]
Normalization: 1

Graph 528
Graph key: {0, 0, 3, 0, 0, 0, 2, 3, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 2, 2, 1, 0, 1, 1}
Adjacency matrix: {{0, 0, 0, 3, 0, 0, 0, 2}, {0, 0, 3, 0, 0, 1, 1, 0}, {0, 3, 0, 1, 0, 0, 1, 0}, {3, 0, 1, 0, 0, 1, 0, 0}, {0, 0, 0, 0, 0, 2, 2, 1}, {0, 1, 0, 1, 2, 0, 0, 1}, {0, 1, 1, 0, 2, 0, 0, 1}, {2, 0, 0, 0, 1, 1, 1, 0}}
Vertex index labels: {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {6, 7, 8, 11, 12}, {1, 2, 3, 11, 13}, {14, 15, 16, 17, 18}, {9, 13, 14, 15, 19}, {10, 12, 16, 17, 20}, {4, 5, 18, 19, 20}}
Compact contraction: Inactive[Times][D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 2], Subscript[i, 3], Subscript[i, 4], Subscript[i, 5]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 7], Subscript[i, 8], Subscript[i, 9], Subscript[i, 10]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 7], Subscript[i, 8], Subscript[i, 11], Subscript[i, 12]], D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 2], Subscript[i, 3], Subscript[i, 11], Subscript[i, 13]], D8FormulaFiveForm[Subscript[i, 14], Subscript[i, 15], Subscript[i, 16], Subscript[i, 17], Subscript[i, 18]], D8FormulaFiveForm[Subscript[i, 9], Subscript[i, 13], Subscript[i, 14], Subscript[i, 15], Subscript[i, 19]], D8FormulaFiveForm[Subscript[i, 10], Subscript[i, 12], Subscript[i, 16], Subscript[i, 17], Subscript[i, 20]], D8FormulaFiveForm[Subscript[i, 4], Subscript[i, 5], Subscript[i, 18], Subscript[i, 19], Subscript[i, 20]]]
Metric-explicit contraction: Inactive[Times][D8FormulaMetricInverse[Subscript[a, 1], Subscript[b, 1]], D8FormulaMetricInverse[Subscript[a, 2], Subscript[b, 2]], D8FormulaMetricInverse[Subscript[a, 3], Subscript[b, 3]], D8FormulaMetricInverse[Subscript[a, 4], Subscript[b, 4]], D8FormulaMetricInverse[Subscript[a, 5], Subscript[b, 5]], D8FormulaMetricInverse[Subscript[a, 6], Subscript[b, 6]], D8FormulaMetricInverse[Subscript[a, 7], Subscript[b, 7]], D8FormulaMetricInverse[Subscript[a, 8], Subscript[b, 8]], D8FormulaMetricInverse[Subscript[a, 9], Subscript[b, 9]], D8FormulaMetricInverse[Subscript[a, 10], Subscript[b, 10]], D8FormulaMetricInverse[Subscript[a, 11], Subscript[b, 11]], D8FormulaMetricInverse[Subscript[a, 12], Subscript[b, 12]], D8FormulaMetricInverse[Subscript[a, 13], Subscript[b, 13]], D8FormulaMetricInverse[Subscript[a, 14], Subscript[b, 14]], D8FormulaMetricInverse[Subscript[a, 15], Subscript[b, 15]], D8FormulaMetricInverse[Subscript[a, 16], Subscript[b, 16]], D8FormulaMetricInverse[Subscript[a, 17], Subscript[b, 17]], D8FormulaMetricInverse[Subscript[a, 18], Subscript[b, 18]], D8FormulaMetricInverse[Subscript[a, 19], Subscript[b, 19]], D8FormulaMetricInverse[Subscript[a, 20], Subscript[b, 20]], D8FormulaFiveForm[Subscript[a, 1], Subscript[a, 2], Subscript[a, 3], Subscript[a, 4], Subscript[a, 5]], D8FormulaFiveForm[Subscript[a, 6], Subscript[a, 7], Subscript[a, 8], Subscript[a, 9], Subscript[a, 10]], D8FormulaFiveForm[Subscript[b, 6], Subscript[b, 7], Subscript[b, 8], Subscript[a, 11], Subscript[a, 12]], D8FormulaFiveForm[Subscript[b, 1], Subscript[b, 2], Subscript[b, 3], Subscript[b, 11], Subscript[a, 13]], D8FormulaFiveForm[Subscript[a, 14], Subscript[a, 15], Subscript[a, 16], Subscript[a, 17], Subscript[a, 18]], D8FormulaFiveForm[Subscript[b, 9], Subscript[b, 13], Subscript[b, 14], Subscript[b, 15], Subscript[a, 19]], D8FormulaFiveForm[Subscript[b, 10], Subscript[b, 12], Subscript[b, 16], Subscript[b, 17], Subscript[a, 20]], D8FormulaFiveForm[Subscript[b, 4], Subscript[b, 5], Subscript[b, 18], Subscript[b, 19], Subscript[b, 20]]]
Normalization: 1

Evidence status: exact and modular finite-sample validation; not symbolic proof.
```

---

# 11. DEGREE-8 FORMULA CATALOG CSV

```csv
"GraphNumber","GraphKey","AdjacencyMatrix","VertexIndexLabels","CompactEinsteinExpression","MetricExplicitExpression","Normalization","PolynomialDegreeInF"
3,"{0, 0, 0, 0, 0, 1, 4, 0, 0, 0, 1, 4, 0, 0, 1, 4, 0, 0, 4, 0, 0, 1, 0, 0, 0, 0, 0, 0}","{{0, 0, 0, 0, 0, 0, 1, 4}, {0, 0, 0, 0, 0, 1, 4, 0}, {0, 0, 0, 0, 1, 4, 0, 0}, {0, 0, 0, 0, 4, 0, 0, 1}, {0, 0, 1, 4, 0, 0, 0, 0}, {0, 1, 4, 0, 0, 0, 0, 0}, {1, 4, 0, 0, 0, 0, 0, 0}, {4, 0, 0, 1, 0, 0, 0, 0}}","{{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15}, {16, 17, 18, 19, 20}, {11, 16, 17, 18, 19}, {6, 12, 13, 14, 15}, {1, 7, 8, 9, 10}, {2, 3, 4, 5, 20}}","Inactive[Times][D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 2], Subscript[i, 3], Subscript[i, 4], Subscript[i, 5]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 7], Subscript[i, 8], Subscript[i, 9], Subscript[i, 10]], D8FormulaFiveForm[Subscript[i, 11], Subscript[i, 12], Subscript[i, 13], Subscript[i, 14], Subscript[i, 15]], D8FormulaFiveForm[Subscript[i, 16], Subscript[i, 17], Subscript[i, 18], Subscript[i, 19], Subscript[i, 20]], D8FormulaFiveForm[Subscript[i, 11], Subscript[i, 16], Subscript[i, 17], Subscript[i, 18], Subscript[i, 19]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 12], Subscript[i, 13], Subscript[i, 14], Subscript[i, 15]], D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 7], Subscript[i, 8], Subscript[i, 9], Subscript[i, 10]], D8FormulaFiveForm[Subscript[i, 2], Subscript[i, 3], Subscript[i, 4], Subscript[i, 5], Subscript[i, 20]]]","Inactive[Times][D8FormulaMetricInverse[Subscript[a, 1], Subscript[b, 1]], D8FormulaMetricInverse[Subscript[a, 2], Subscript[b, 2]], D8FormulaMetricInverse[Subscript[a, 3], Subscript[b, 3]], D8FormulaMetricInverse[Subscript[a, 4], Subscript[b, 4]], D8FormulaMetricInverse[Subscript[a, 5], Subscript[b, 5]], D8FormulaMetricInverse[Subscript[a, 6], Subscript[b, 6]], D8FormulaMetricInverse[Subscript[a, 7], Subscript[b, 7]], D8FormulaMetricInverse[Subscript[a, 8], Subscript[b, 8]], D8FormulaMetricInverse[Subscript[a, 9], Subscript[b, 9]], D8FormulaMetricInverse[Subscript[a, 10], Subscript[b, 10]], D8FormulaMetricInverse[Subscript[a, 11], Subscript[b, 11]], D8FormulaMetricInverse[Subscript[a, 12], Subscript[b, 12]], D8FormulaMetricInverse[Subscript[a, 13], Subscript[b, 13]], D8FormulaMetricInverse[Subscript[a, 14], Subscript[b, 14]], D8FormulaMetricInverse[Subscript[a, 15], Subscript[b, 15]], D8FormulaMetricInverse[Subscript[a, 16], Subscript[b, 16]], D8FormulaMetricInverse[Subscript[a, 17], Subscript[b, 17]], D8FormulaMetricInverse[Subscript[a, 18], Subscript[b, 18]], D8FormulaMetricInverse[Subscript[a, 19], Subscript[b, 19]], D8FormulaMetricInverse[Subscript[a, 20], Subscript[b, 20]], D8FormulaFiveForm[Subscript[a, 1], Subscript[a, 2], Subscript[a, 3], Subscript[a, 4], Subscript[a, 5]], D8FormulaFiveForm[Subscript[a, 6], Subscript[a, 7], Subscript[a, 8], Subscript[a, 9], Subscript[a, 10]], D8FormulaFiveForm[Subscript[a, 11], Subscript[a, 12], Subscript[a, 13], Subscript[a, 14], Subscript[a, 15]], D8FormulaFiveForm[Subscript[a, 16], Subscript[a, 17], Subscript[a, 18], Subscript[a, 19], Subscript[a, 20]], D8FormulaFiveForm[Subscript[b, 11], Subscript[b, 16], Subscript[b, 17], Subscript[b, 18], Subscript[b, 19]], D8FormulaFiveForm[Subscript[b, 6], Subscript[b, 12], Subscript[b, 13], Subscript[b, 14], Subscript[b, 15]], D8FormulaFiveForm[Subscript[b, 1], Subscript[b, 7], Subscript[b, 8], Subscript[b, 9], Subscript[b, 10]], D8FormulaFiveForm[Subscript[b, 2], Subscript[b, 3], Subscript[b, 4], Subscript[b, 5], Subscript[b, 20]]]",1,8
249,"{0, 0, 0, 0, 4, 0, 1, 0, 0, 4, 0, 0, 1, 4, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 2}","{{0, 0, 0, 0, 0, 4, 0, 1}, {0, 0, 0, 0, 4, 0, 0, 1}, {0, 0, 0, 4, 0, 0, 0, 1}, {0, 0, 4, 0, 0, 0, 1, 0}, {0, 4, 0, 0, 0, 0, 1, 0}, {4, 0, 0, 0, 0, 0, 1, 0}, {0, 0, 0, 1, 1, 1, 0, 2}, {1, 1, 1, 0, 0, 0, 2, 0}}","{{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15}, {11, 12, 13, 14, 16}, {6, 7, 8, 9, 17}, {1, 2, 3, 4, 18}, {16, 17, 18, 19, 20}, {5, 10, 15, 19, 20}}","Inactive[Times][D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 2], Subscript[i, 3], Subscript[i, 4], Subscript[i, 5]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 7], Subscript[i, 8], Subscript[i, 9], Subscript[i, 10]], D8FormulaFiveForm[Subscript[i, 11], Subscript[i, 12], Subscript[i, 13], Subscript[i, 14], Subscript[i, 15]], D8FormulaFiveForm[Subscript[i, 11], Subscript[i, 12], Subscript[i, 13], Subscript[i, 14], Subscript[i, 16]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 7], Subscript[i, 8], Subscript[i, 9], Subscript[i, 17]], D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 2], Subscript[i, 3], Subscript[i, 4], Subscript[i, 18]], D8FormulaFiveForm[Subscript[i, 16], Subscript[i, 17], Subscript[i, 18], Subscript[i, 19], Subscript[i, 20]], D8FormulaFiveForm[Subscript[i, 5], Subscript[i, 10], Subscript[i, 15], Subscript[i, 19], Subscript[i, 20]]]","Inactive[Times][D8FormulaMetricInverse[Subscript[a, 1], Subscript[b, 1]], D8FormulaMetricInverse[Subscript[a, 2], Subscript[b, 2]], D8FormulaMetricInverse[Subscript[a, 3], Subscript[b, 3]], D8FormulaMetricInverse[Subscript[a, 4], Subscript[b, 4]], D8FormulaMetricInverse[Subscript[a, 5], Subscript[b, 5]], D8FormulaMetricInverse[Subscript[a, 6], Subscript[b, 6]], D8FormulaMetricInverse[Subscript[a, 7], Subscript[b, 7]], D8FormulaMetricInverse[Subscript[a, 8], Subscript[b, 8]], D8FormulaMetricInverse[Subscript[a, 9], Subscript[b, 9]], D8FormulaMetricInverse[Subscript[a, 10], Subscript[b, 10]], D8FormulaMetricInverse[Subscript[a, 11], Subscript[b, 11]], D8FormulaMetricInverse[Subscript[a, 12], Subscript[b, 12]], D8FormulaMetricInverse[Subscript[a, 13], Subscript[b, 13]], D8FormulaMetricInverse[Subscript[a, 14], Subscript[b, 14]], D8FormulaMetricInverse[Subscript[a, 15], Subscript[b, 15]], D8FormulaMetricInverse[Subscript[a, 16], Subscript[b, 16]], D8FormulaMetricInverse[Subscript[a, 17], Subscript[b, 17]], D8FormulaMetricInverse[Subscript[a, 18], Subscript[b, 18]], D8FormulaMetricInverse[Subscript[a, 19], Subscript[b, 19]], D8FormulaMetricInverse[Subscript[a, 20], Subscript[b, 20]], D8FormulaFiveForm[Subscript[a, 1], Subscript[a, 2], Subscript[a, 3], Subscript[a, 4], Subscript[a, 5]], D8FormulaFiveForm[Subscript[a, 6], Subscript[a, 7], Subscript[a, 8], Subscript[a, 9], Subscript[a, 10]], D8FormulaFiveForm[Subscript[a, 11], Subscript[a, 12], Subscript[a, 13], Subscript[a, 14], Subscript[a, 15]], D8FormulaFiveForm[Subscript[b, 11], Subscript[b, 12], Subscript[b, 13], Subscript[b, 14], Subscript[a, 16]], D8FormulaFiveForm[Subscript[b, 6], Subscript[b, 7], Subscript[b, 8], Subscript[b, 9], Subscript[a, 17]], D8FormulaFiveForm[Subscript[b, 1], Subscript[b, 2], Subscript[b, 3], Subscript[b, 4], Subscript[a, 18]], D8FormulaFiveForm[Subscript[b, 16], Subscript[b, 17], Subscript[b, 18], Subscript[a, 19], Subscript[a, 20]], D8FormulaFiveForm[Subscript[b, 5], Subscript[b, 10], Subscript[b, 15], Subscript[b, 19], Subscript[b, 20]]]",1,8
508,"{0, 0, 3, 0, 0, 0, 2, 3, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1}","{{0, 0, 0, 3, 0, 0, 0, 2}, {0, 0, 3, 0, 0, 0, 2, 0}, {0, 3, 0, 0, 0, 2, 0, 0}, {3, 0, 0, 0, 2, 0, 0, 0}, {0, 0, 0, 2, 0, 1, 1, 1}, {0, 0, 2, 0, 1, 0, 1, 1}, {0, 2, 0, 0, 1, 1, 0, 1}, {2, 0, 0, 0, 1, 1, 1, 0}}","{{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {6, 7, 8, 11, 12}, {1, 2, 3, 13, 14}, {13, 14, 15, 16, 17}, {11, 12, 15, 18, 19}, {9, 10, 16, 18, 20}, {4, 5, 17, 19, 20}}","Inactive[Times][D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 2], Subscript[i, 3], Subscript[i, 4], Subscript[i, 5]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 7], Subscript[i, 8], Subscript[i, 9], Subscript[i, 10]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 7], Subscript[i, 8], Subscript[i, 11], Subscript[i, 12]], D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 2], Subscript[i, 3], Subscript[i, 13], Subscript[i, 14]], D8FormulaFiveForm[Subscript[i, 13], Subscript[i, 14], Subscript[i, 15], Subscript[i, 16], Subscript[i, 17]], D8FormulaFiveForm[Subscript[i, 11], Subscript[i, 12], Subscript[i, 15], Subscript[i, 18], Subscript[i, 19]], D8FormulaFiveForm[Subscript[i, 9], Subscript[i, 10], Subscript[i, 16], Subscript[i, 18], Subscript[i, 20]], D8FormulaFiveForm[Subscript[i, 4], Subscript[i, 5], Subscript[i, 17], Subscript[i, 19], Subscript[i, 20]]]","Inactive[Times][D8FormulaMetricInverse[Subscript[a, 1], Subscript[b, 1]], D8FormulaMetricInverse[Subscript[a, 2], Subscript[b, 2]], D8FormulaMetricInverse[Subscript[a, 3], Subscript[b, 3]], D8FormulaMetricInverse[Subscript[a, 4], Subscript[b, 4]], D8FormulaMetricInverse[Subscript[a, 5], Subscript[b, 5]], D8FormulaMetricInverse[Subscript[a, 6], Subscript[b, 6]], D8FormulaMetricInverse[Subscript[a, 7], Subscript[b, 7]], D8FormulaMetricInverse[Subscript[a, 8], Subscript[b, 8]], D8FormulaMetricInverse[Subscript[a, 9], Subscript[b, 9]], D8FormulaMetricInverse[Subscript[a, 10], Subscript[b, 10]], D8FormulaMetricInverse[Subscript[a, 11], Subscript[b, 11]], D8FormulaMetricInverse[Subscript[a, 12], Subscript[b, 12]], D8FormulaMetricInverse[Subscript[a, 13], Subscript[b, 13]], D8FormulaMetricInverse[Subscript[a, 14], Subscript[b, 14]], D8FormulaMetricInverse[Subscript[a, 15], Subscript[b, 15]], D8FormulaMetricInverse[Subscript[a, 16], Subscript[b, 16]], D8FormulaMetricInverse[Subscript[a, 17], Subscript[b, 17]], D8FormulaMetricInverse[Subscript[a, 18], Subscript[b, 18]], D8FormulaMetricInverse[Subscript[a, 19], Subscript[b, 19]], D8FormulaMetricInverse[Subscript[a, 20], Subscript[b, 20]], D8FormulaFiveForm[Subscript[a, 1], Subscript[a, 2], Subscript[a, 3], Subscript[a, 4], Subscript[a, 5]], D8FormulaFiveForm[Subscript[a, 6], Subscript[a, 7], Subscript[a, 8], Subscript[a, 9], Subscript[a, 10]], D8FormulaFiveForm[Subscript[b, 6], Subscript[b, 7], Subscript[b, 8], Subscript[a, 11], Subscript[a, 12]], D8FormulaFiveForm[Subscript[b, 1], Subscript[b, 2], Subscript[b, 3], Subscript[a, 13], Subscript[a, 14]], D8FormulaFiveForm[Subscript[b, 13], Subscript[b, 14], Subscript[a, 15], Subscript[a, 16], Subscript[a, 17]], D8FormulaFiveForm[Subscript[b, 11], Subscript[b, 12], Subscript[b, 15], Subscript[a, 18], Subscript[a, 19]], D8FormulaFiveForm[Subscript[b, 9], Subscript[b, 10], Subscript[b, 16], Subscript[b, 18], Subscript[a, 20]], D8FormulaFiveForm[Subscript[b, 4], Subscript[b, 5], Subscript[b, 17], Subscript[b, 19], Subscript[b, 20]]]",1,8
61,"{0, 0, 0, 0, 1, 2, 2, 0, 2, 0, 2, 0, 1, 2, 2, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1}","{{0, 0, 0, 0, 0, 1, 2, 2}, {0, 0, 0, 2, 0, 2, 0, 1}, {0, 0, 0, 2, 2, 0, 1, 0}, {0, 2, 2, 0, 1, 0, 0, 0}, {0, 0, 2, 1, 0, 1, 1, 0}, {1, 2, 0, 0, 1, 0, 0, 1}, {2, 0, 1, 0, 1, 0, 0, 1}, {2, 1, 0, 0, 0, 1, 1, 0}}","{{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15}, {6, 7, 11, 12, 16}, {13, 14, 16, 17, 18}, {1, 8, 9, 17, 19}, {2, 3, 15, 18, 20}, {4, 5, 10, 19, 20}}","Inactive[Times][D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 2], Subscript[i, 3], Subscript[i, 4], Subscript[i, 5]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 7], Subscript[i, 8], Subscript[i, 9], Subscript[i, 10]], D8FormulaFiveForm[Subscript[i, 11], Subscript[i, 12], Subscript[i, 13], Subscript[i, 14], Subscript[i, 15]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 7], Subscript[i, 11], Subscript[i, 12], Subscript[i, 16]], D8FormulaFiveForm[Subscript[i, 13], Subscript[i, 14], Subscript[i, 16], Subscript[i, 17], Subscript[i, 18]], D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 8], Subscript[i, 9], Subscript[i, 17], Subscript[i, 19]], D8FormulaFiveForm[Subscript[i, 2], Subscript[i, 3], Subscript[i, 15], Subscript[i, 18], Subscript[i, 20]], D8FormulaFiveForm[Subscript[i, 4], Subscript[i, 5], Subscript[i, 10], Subscript[i, 19], Subscript[i, 20]]]","Inactive[Times][D8FormulaMetricInverse[Subscript[a, 1], Subscript[b, 1]], D8FormulaMetricInverse[Subscript[a, 2], Subscript[b, 2]], D8FormulaMetricInverse[Subscript[a, 3], Subscript[b, 3]], D8FormulaMetricInverse[Subscript[a, 4], Subscript[b, 4]], D8FormulaMetricInverse[Subscript[a, 5], Subscript[b, 5]], D8FormulaMetricInverse[Subscript[a, 6], Subscript[b, 6]], D8FormulaMetricInverse[Subscript[a, 7], Subscript[b, 7]], D8FormulaMetricInverse[Subscript[a, 8], Subscript[b, 8]], D8FormulaMetricInverse[Subscript[a, 9], Subscript[b, 9]], D8FormulaMetricInverse[Subscript[a, 10], Subscript[b, 10]], D8FormulaMetricInverse[Subscript[a, 11], Subscript[b, 11]], D8FormulaMetricInverse[Subscript[a, 12], Subscript[b, 12]], D8FormulaMetricInverse[Subscript[a, 13], Subscript[b, 13]], D8FormulaMetricInverse[Subscript[a, 14], Subscript[b, 14]], D8FormulaMetricInverse[Subscript[a, 15], Subscript[b, 15]], D8FormulaMetricInverse[Subscript[a, 16], Subscript[b, 16]], D8FormulaMetricInverse[Subscript[a, 17], Subscript[b, 17]], D8FormulaMetricInverse[Subscript[a, 18], Subscript[b, 18]], D8FormulaMetricInverse[Subscript[a, 19], Subscript[b, 19]], D8FormulaMetricInverse[Subscript[a, 20], Subscript[b, 20]], D8FormulaFiveForm[Subscript[a, 1], Subscript[a, 2], Subscript[a, 3], Subscript[a, 4], Subscript[a, 5]], D8FormulaFiveForm[Subscript[a, 6], Subscript[a, 7], Subscript[a, 8], Subscript[a, 9], Subscript[a, 10]], D8FormulaFiveForm[Subscript[a, 11], Subscript[a, 12], Subscript[a, 13], Subscript[a, 14], Subscript[a, 15]], D8FormulaFiveForm[Subscript[b, 6], Subscript[b, 7], Subscript[b, 11], Subscript[b, 12], Subscript[a, 16]], D8FormulaFiveForm[Subscript[b, 13], Subscript[b, 14], Subscript[b, 16], Subscript[a, 17], Subscript[a, 18]], D8FormulaFiveForm[Subscript[b, 1], Subscript[b, 8], Subscript[b, 9], Subscript[b, 17], Subscript[a, 19]], D8FormulaFiveForm[Subscript[b, 2], Subscript[b, 3], Subscript[b, 15], Subscript[b, 18], Subscript[a, 20]], D8FormulaFiveForm[Subscript[b, 4], Subscript[b, 5], Subscript[b, 10], Subscript[b, 19], Subscript[b, 20]]]",1,8
376,"{0, 0, 0, 2, 2, 0, 1, 2, 2, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1}","{{0, 0, 0, 0, 2, 2, 0, 1}, {0, 0, 2, 2, 0, 0, 1, 0}, {0, 2, 0, 1, 0, 0, 1, 1}, {0, 2, 1, 0, 0, 1, 1, 0}, {2, 0, 0, 0, 0, 1, 1, 1}, {2, 0, 0, 1, 1, 0, 0, 1}, {0, 1, 1, 1, 1, 0, 0, 1}, {1, 0, 1, 0, 1, 1, 1, 0}}","{{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {6, 7, 11, 12, 13}, {8, 9, 11, 14, 15}, {1, 2, 16, 17, 18}, {3, 4, 14, 16, 19}, {10, 12, 15, 17, 20}, {5, 13, 18, 19, 20}}","Inactive[Times][D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 2], Subscript[i, 3], Subscript[i, 4], Subscript[i, 5]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 7], Subscript[i, 8], Subscript[i, 9], Subscript[i, 10]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 7], Subscript[i, 11], Subscript[i, 12], Subscript[i, 13]], D8FormulaFiveForm[Subscript[i, 8], Subscript[i, 9], Subscript[i, 11], Subscript[i, 14], Subscript[i, 15]], D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 2], Subscript[i, 16], Subscript[i, 17], Subscript[i, 18]], D8FormulaFiveForm[Subscript[i, 3], Subscript[i, 4], Subscript[i, 14], Subscript[i, 16], Subscript[i, 19]], D8FormulaFiveForm[Subscript[i, 10], Subscript[i, 12], Subscript[i, 15], Subscript[i, 17], Subscript[i, 20]], D8FormulaFiveForm[Subscript[i, 5], Subscript[i, 13], Subscript[i, 18], Subscript[i, 19], Subscript[i, 20]]]","Inactive[Times][D8FormulaMetricInverse[Subscript[a, 1], Subscript[b, 1]], D8FormulaMetricInverse[Subscript[a, 2], Subscript[b, 2]], D8FormulaMetricInverse[Subscript[a, 3], Subscript[b, 3]], D8FormulaMetricInverse[Subscript[a, 4], Subscript[b, 4]], D8FormulaMetricInverse[Subscript[a, 5], Subscript[b, 5]], D8FormulaMetricInverse[Subscript[a, 6], Subscript[b, 6]], D8FormulaMetricInverse[Subscript[a, 7], Subscript[b, 7]], D8FormulaMetricInverse[Subscript[a, 8], Subscript[b, 8]], D8FormulaMetricInverse[Subscript[a, 9], Subscript[b, 9]], D8FormulaMetricInverse[Subscript[a, 10], Subscript[b, 10]], D8FormulaMetricInverse[Subscript[a, 11], Subscript[b, 11]], D8FormulaMetricInverse[Subscript[a, 12], Subscript[b, 12]], D8FormulaMetricInverse[Subscript[a, 13], Subscript[b, 13]], D8FormulaMetricInverse[Subscript[a, 14], Subscript[b, 14]], D8FormulaMetricInverse[Subscript[a, 15], Subscript[b, 15]], D8FormulaMetricInverse[Subscript[a, 16], Subscript[b, 16]], D8FormulaMetricInverse[Subscript[a, 17], Subscript[b, 17]], D8FormulaMetricInverse[Subscript[a, 18], Subscript[b, 18]], D8FormulaMetricInverse[Subscript[a, 19], Subscript[b, 19]], D8FormulaMetricInverse[Subscript[a, 20], Subscript[b, 20]], D8FormulaFiveForm[Subscript[a, 1], Subscript[a, 2], Subscript[a, 3], Subscript[a, 4], Subscript[a, 5]], D8FormulaFiveForm[Subscript[a, 6], Subscript[a, 7], Subscript[a, 8], Subscript[a, 9], Subscript[a, 10]], D8FormulaFiveForm[Subscript[b, 6], Subscript[b, 7], Subscript[a, 11], Subscript[a, 12], Subscript[a, 13]], D8FormulaFiveForm[Subscript[b, 8], Subscript[b, 9], Subscript[b, 11], Subscript[a, 14], Subscript[a, 15]], D8FormulaFiveForm[Subscript[b, 1], Subscript[b, 2], Subscript[a, 16], Subscript[a, 17], Subscript[a, 18]], D8FormulaFiveForm[Subscript[b, 3], Subscript[b, 4], Subscript[b, 14], Subscript[b, 16], Subscript[a, 19]], D8FormulaFiveForm[Subscript[b, 10], Subscript[b, 12], Subscript[b, 15], Subscript[b, 17], Subscript[a, 20]], D8FormulaFiveForm[Subscript[b, 5], Subscript[b, 13], Subscript[b, 18], Subscript[b, 19], Subscript[b, 20]]]",1,8
528,"{0, 0, 3, 0, 0, 0, 2, 3, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 2, 2, 1, 0, 1, 1}","{{0, 0, 0, 3, 0, 0, 0, 2}, {0, 0, 3, 0, 0, 1, 1, 0}, {0, 3, 0, 1, 0, 0, 1, 0}, {3, 0, 1, 0, 0, 1, 0, 0}, {0, 0, 0, 0, 0, 2, 2, 1}, {0, 1, 0, 1, 2, 0, 0, 1}, {0, 1, 1, 0, 2, 0, 0, 1}, {2, 0, 0, 0, 1, 1, 1, 0}}","{{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {6, 7, 8, 11, 12}, {1, 2, 3, 11, 13}, {14, 15, 16, 17, 18}, {9, 13, 14, 15, 19}, {10, 12, 16, 17, 20}, {4, 5, 18, 19, 20}}","Inactive[Times][D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 2], Subscript[i, 3], Subscript[i, 4], Subscript[i, 5]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 7], Subscript[i, 8], Subscript[i, 9], Subscript[i, 10]], D8FormulaFiveForm[Subscript[i, 6], Subscript[i, 7], Subscript[i, 8], Subscript[i, 11], Subscript[i, 12]], D8FormulaFiveForm[Subscript[i, 1], Subscript[i, 2], Subscript[i, 3], Subscript[i, 11], Subscript[i, 13]], D8FormulaFiveForm[Subscript[i, 14], Subscript[i, 15], Subscript[i, 16], Subscript[i, 17], Subscript[i, 18]], D8FormulaFiveForm[Subscript[i, 9], Subscript[i, 13], Subscript[i, 14], Subscript[i, 15], Subscript[i, 19]], D8FormulaFiveForm[Subscript[i, 10], Subscript[i, 12], Subscript[i, 16], Subscript[i, 17], Subscript[i, 20]], D8FormulaFiveForm[Subscript[i, 4], Subscript[i, 5], Subscript[i, 18], Subscript[i, 19], Subscript[i, 20]]]","Inactive[Times][D8FormulaMetricInverse[Subscript[a, 1], Subscript[b, 1]], D8FormulaMetricInverse[Subscript[a, 2], Subscript[b, 2]], D8FormulaMetricInverse[Subscript[a, 3], Subscript[b, 3]], D8FormulaMetricInverse[Subscript[a, 4], Subscript[b, 4]], D8FormulaMetricInverse[Subscript[a, 5], Subscript[b, 5]], D8FormulaMetricInverse[Subscript[a, 6], Subscript[b, 6]], D8FormulaMetricInverse[Subscript[a, 7], Subscript[b, 7]], D8FormulaMetricInverse[Subscript[a, 8], Subscript[b, 8]], D8FormulaMetricInverse[Subscript[a, 9], Subscript[b, 9]], D8FormulaMetricInverse[Subscript[a, 10], Subscript[b, 10]], D8FormulaMetricInverse[Subscript[a, 11], Subscript[b, 11]], D8FormulaMetricInverse[Subscript[a, 12], Subscript[b, 12]], D8FormulaMetricInverse[Subscript[a, 13], Subscript[b, 13]], D8FormulaMetricInverse[Subscript[a, 14], Subscript[b, 14]], D8FormulaMetricInverse[Subscript[a, 15], Subscript[b, 15]], D8FormulaMetricInverse[Subscript[a, 16], Subscript[b, 16]], D8FormulaMetricInverse[Subscript[a, 17], Subscript[b, 17]], D8FormulaMetricInverse[Subscript[a, 18], Subscript[b, 18]], D8FormulaMetricInverse[Subscript[a, 19], Subscript[b, 19]], D8FormulaMetricInverse[Subscript[a, 20], Subscript[b, 20]], D8FormulaFiveForm[Subscript[a, 1], Subscript[a, 2], Subscript[a, 3], Subscript[a, 4], Subscript[a, 5]], D8FormulaFiveForm[Subscript[a, 6], Subscript[a, 7], Subscript[a, 8], Subscript[a, 9], Subscript[a, 10]], D8FormulaFiveForm[Subscript[b, 6], Subscript[b, 7], Subscript[b, 8], Subscript[a, 11], Subscript[a, 12]], D8FormulaFiveForm[Subscript[b, 1], Subscript[b, 2], Subscript[b, 3], Subscript[b, 11], Subscript[a, 13]], D8FormulaFiveForm[Subscript[a, 14], Subscript[a, 15], Subscript[a, 16], Subscript[a, 17], Subscript[a, 18]], D8FormulaFiveForm[Subscript[b, 9], Subscript[b, 13], Subscript[b, 14], Subscript[b, 15], Subscript[a, 19]], D8FormulaFiveForm[Subscript[b, 10], Subscript[b, 12], Subscript[b, 16], Subscript[b, 17], Subscript[a, 20]], D8FormulaFiveForm[Subscript[b, 4], Subscript[b, 5], Subscript[b, 18], Subscript[b, 19], Subscript[b, 20]]]",1,8

```

---

# 12. PYTHON 6D OUTPUTS

## generators.json

```json
{
  "degrees": [
    2,
    4,
    4,
    6,
    8
  ],
  "names": [
    "g^(2)",
    "g^(4)_1",
    "g^(4)_2",
    "g^(6)",
    "g^(8)"
  ],
  "selected_graph_ids": {
    "2": [
      "M[3]"
    ],
    "4": [
      "M[0,1,2,2,1,0]",
      "M[1,1,1,1,1,1]"
    ],
    "6": [
      "M[0,0,0,1,2,0,1,1,1,2,1,0,0,0,0]"
    ],
    "8": [
      "M[0,0,0,0,0,1,2,0,0,0,1,1,1,0,1,1,1,0,2,1,0,0,0,0,0,0,0,0]"
    ]
  }
}
```

## ranks.json

```json
{
  "2": {
    "n_graphs": 1,
    "connected_rank": 1,
    "n_lower_monomials": 0,
    "rank_P": 0,
    "rank_PC": 1,
    "n_new": 1,
    "monomial_names": [],
    "backend": "svd",
    "proof_status": "strong computational evidence",
    "elapsed_sec": 0.05684018135070801
  },
  "4": {
    "n_graphs": 2,
    "connected_rank": 2,
    "n_lower_monomials": 1,
    "rank_P": 1,
    "rank_PC": 3,
    "n_new": 2,
    "monomial_names": [
      "g^(2)*g^(2)"
    ],
    "backend": "svd",
    "proof_status": "strong computational evidence",
    "elapsed_sec": 0.02994990348815918
  },
  "6": {
    "n_graphs": 6,
    "connected_rank": 3,
    "n_lower_monomials": 3,
    "rank_P": 3,
    "rank_PC": 4,
    "n_new": 1,
    "monomial_names": [
      "g^(2)*g^(2)*g^(2)",
      "g^(2)*g^(4)_1",
      "g^(2)*g^(4)_2"
    ],
    "backend": "svd",
    "proof_status": "strong computational evidence",
    "elapsed_sec": 0.14102816581726074
  },
  "8": {
    "n_graphs": 20,
    "connected_rank": 6,
    "n_lower_monomials": 7,
    "rank_P": 7,
    "rank_PC": 8,
    "n_new": 1,
    "monomial_names": [
      "g^(2)*g^(2)*g^(2)*g^(2)",
      "g^(2)*g^(2)*g^(4)_1",
      "g^(2)*g^(2)*g^(4)_2",
      "g^(2)*g^(6)",
      "g^(4)_1*g^(4)_1",
      "g^(4)_1*g^(4)_2",
      "g^(4)_2*g^(4)_2"
    ],
    "backend": "svd",
    "proof_status": "strong computational evidence",
    "elapsed_sec": 7.054863214492798
  },
  "10": {
    "n_graphs": 12,
    "connected_rank": 8,
    "n_lower_monomials": 10,
    "rank_P": 10,
    "rank_PC": 10,
    "n_new": 0,
    "monomial_names": [
      "g^(2)*g^(2)*g^(2)*g^(2)*g^(2)",
      "g^(2)*g^(2)*g^(2)*g^(4)_1",
      "g^(2)*g^(2)*g^(2)*g^(4)_2",
      "g^(2)*g^(2)*g^(6)",
      "g^(2)*g^(4)_1*g^(4)_1",
      "g^(2)*g^(4)_1*g^(4)_2",
      "g^(2)*g^(4)_2*g^(4)_2",
      "g^(2)*g^(8)",
      "g^(4)_1*g^(6)",
      "g^(4)_2*g^(6)"
    ],
    "backend": "svd",
    "proof_status": "strong computational evidence",
    "elapsed_sec": 0.09046506881713867
  }
}
```

## syzygies.json (may be long)

```json
[
  {
    "degree": 6,
    "column_names": [
      "g^(2)*g^(2)*g^(2)",
      "g^(2)*g^(4)_1",
      "g^(2)*g^(4)_2",
      "C[M[0,0,0,1,2,0,1,1,1,2,1,0,0,0,0]]",
      "C[M[0,0,0,1,2,0,1,2,0,2,0,1,0,0,0]]",
      "C[M[0,0,0,1,2,1,1,0,1,1,1,0,1,0,0]]",
      "C[M[0,0,0,1,2,1,1,1,0,2,0,0,0,0,1]]",
      "C[M[0,0,1,1,1,0,1,1,1,1,1,1,0,0,0]]",
      "C[M[0,0,1,1,1,1,0,1,1,1,0,1,1,0,0]]"
    ],
    "coefficients": [
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      0,
      0
    ],
    "discovery_primes": [
      1000003,
      1000033,
      1000037
    ],
    "validation_primes": [
      1000039,
      1000081,
      1000151
    ],
    "n_validation_samples": 40,
    "max_abs_residual": 1.4698697335563384e-30,
    "mean_abs_residual": 2.7712687452274033e-31,
    "proof_status": "exact finite-field identity on tested samples",
    "notes": "nullity_est=5; float residuals are scale-dependent",
    "extra": {
      "mod_ok": true
    }
  },
  {
    "degree": 6,
    "column_names": [
      "g^(2)*g^(2)*g^(2)",
      "g^(2)*g^(4)_1",
      "g^(2)*g^(4)_2",
      "C[M[0,0,0,1,2,0,1,1,1,2,1,0,0,0,0]]",
      "C[M[0,0,0,1,2,0,1,2,0,2,0,1,0,0,0]]",
      "C[M[0,0,0,1,2,1,1,0,1,1,1,0,1,0,0]]",
      "C[M[0,0,0,1,2,1,1,1,0,2,0,0,0,0,1]]",
      "C[M[0,0,1,1,1,0,1,1,1,1,1,1,0,0,0]]",
      "C[M[0,0,1,1,1,1,0,1,1,1,0,1,1,0,0]]"
    ],
    "coefficients": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      0
    ],
    "discovery_primes": [
      1000003,
      1000033,
      1000037
    ],
    "validation_primes": [
      1000039,
      1000081,
      1000151
    ],
    "n_validation_samples": 40,
    "max_abs_residual": 1.3518048906188483e-13,
    "mean_abs_residual": 2.385580956237576e-14,
    "proof_status": "exact finite-field identity on tested samples",
    "notes": "nullity_est=5; float residuals are scale-dependent",
    "extra": {
      "mod_ok": true
    }
  },
  {
    "degree": 8,
    "column_names": [
      "g^(2)*g^(2)*g^(2)*g^(2)",
      "g^(2)*g^(2)*g^(4)_1",
      "g^(2)*g^(2)*g^(4)_2",
      "g^(2)*g^(6)",
      "g^(4)_1*g^(4)_1",
      "g^(4)_1*g^(4)_2",
      "g^(4)_2*g^(4)_2",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,0,1,1,1,0,2,1,0,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,0,1,2,0,0,2,0,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,1,1,0,1,0,1,1,0,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,1,1,1,0,0,2,0,0,0,0,0,0,1,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,2,0,0,1,2,0,0,2,0,0,1,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,2,0,1,1,0,0,1,1,1,0,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,2,0,1,1,1,0,0,2,0,0,0,0,0,0,0,1,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,2,1,0,0,1,1,0,1,2,0,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,2,1,0,1,1,0,0,1,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,2,1,0,1,1,0,0,1,2,0,0,0,0,0,0,1,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,0,1,1,1,0,1,1,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,2,0,1,0,0,1,0,0,0,0,1,0,1,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1]]",
      "C[M[0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,0,0,1,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,1,0,1,0,1,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1]]"
    ],
    "coefficients": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    "discovery_primes": [
      1000003,
      1000033,
      1000037
    ],
    "validation_primes": [
      1000039,
      1000081,
      1000151
    ],
    "n_validation_samples": 40,
    "max_abs_residual": 3.6287601640166543e-29,
    "mean_abs_residual": 3.436475318369033e-30,
    "proof_status": "exact finite-field identity on tested samples",
    "notes": "nullity_est=19; float residuals are scale-dependent",
    "extra": {
      "mod_ok": true
    }
  },
  {
    "degree": 8,
    "column_names": [
      "g^(2)*g^(2)*g^(2)*g^(2)",
      "g^(2)*g^(2)*g^(4)_1",
      "g^(2)*g^(2)*g^(4)_2",
      "g^(2)*g^(6)",
      "g^(4)_1*g^(4)_1",
      "g^(4)_1*g^(4)_2",
      "g^(4)_2*g^(4)_2",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,0,1,1,1,0,2,1,0,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,0,1,2,0,0,2,0,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,1,1,0,1,0,1,1,0,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,1,1,1,0,0,2,0,0,0,0,0,0,1,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,2,0,0,1,2,0,0,2,0,0,1,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,2,0,1,1,0,0,1,1,1,0,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,2,0,1,1,1,0,0,2,0,0,0,0,0,0,0,1,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,2,1,0,0,1,1,0,1,2,0,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,2,1,0,1,1,0,0,1,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,2,1,0,1,1,0,0,1,2,0,0,0,0,0,0,1,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,0,1,1,1,0,1,1,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,2,0,1,0,0,1,0,0,0,0,1,0,1,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1]]",
      "C[M[0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,0,0,1,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,1,0,1,0,1,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1]]"
    ],
    "coefficients": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    "discovery_primes": [
      1000003,
      1000033,
      1000037
    ],
    "validation_primes": [
      1000039,
      1000081,
      1000151
    ],
    "n_validation_samples": 40,
    "max_abs_residual": 1.262177448353619e-29,
    "mean_abs_residual": 3.1110701949653654e-30,
    "proof_status": "exact finite-field identity on tested samples",
    "notes": "nullity_est=19; float residuals are scale-dependent",
    "extra": {
      "mod_ok": true
    }
  },
  {
    "degree": 8,
    "column_names": [
      "g^(2)*g^(2)*g^(2)*g^(2)",
      "g^(2)*g^(2)*g^(4)_1",
      "g^(2)*g^(2)*g^(4)_2",
      "g^(2)*g^(6)",
      "g^(4)_1*g^(4)_1",
      "g^(4)_1*g^(4)_2",
      "g^(4)_2*g^(4)_2",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,0,1,1,1,0,2,1,0,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,0,1,2,0,0,2,0,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,1,1,0,1,0,1,1,0,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,1,1,1,0,0,2,0,0,0,0,0,0,1,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,2,0,0,1,2,0,0,2,0,0,1,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,2,0,1,1,0,0,1,1,1,0,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,2,0,1,1,1,0,0,2,0,0,0,0,0,0,0,1,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,2,1,0,0,1,1,0,1,2,0,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,2,1,0,1,1,0,0,1,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,2,1,0,1,1,0,0,1,2,0,0,0,0,0,0,1,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,0,1,1,1,0,1,1,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,2,0,1,0,0,1,0,0,0,0,1,0,1,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1]]",
      "C[M[0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,0,0,1,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,1,0,1,0,1,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1]]"
    ],
    "coefficients": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    "discovery_primes": [
      1000003,
      1000033,
      1000037
    ],
    "validation_primes": [
      1000039,
      1000081,
      1000151
    ],
    "n_validation_samples": 40,
    "max_abs_residual": 1.264920208379687e-29,
    "mean_abs_residual": 1.4417363665879358e-30,
    "proof_status": "exact finite-field identity on tested samples",
    "notes": "nullity_est=19; float residuals are scale-dependent",
    "extra": {
      "mod_ok": true
    }
  },
  {
    "degree": 8,
    "column_names": [
      "g^(2)*g^(2)*g^(2)*g^(2)",
      "g^(2)*g^(2)*g^(4)_1",
      "g^(2)*g^(2)*g^(4)_2",
      "g^(2)*g^(6)",
      "g^(4)_1*g^(4)_1",
      "g^(4)_1*g^(4)_2",
      "g^(4)_2*g^(4)_2",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,0,1,1,1,0,2,1,0,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,0,1,2,0,0,2,0,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,1,1,0,1,0,1,1,0,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,1,1,1,0,0,2,0,0,0,0,0,0,1,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,2,0,0,1,2,0,0,2,0,0,1,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,2,0,1,1,0,0,1,1,1,0,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,2,0,1,1,1,0,0,2,0,0,0,0,0,0,0,1,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,2,1,0,0,1,1,0,1,2,0,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,2,1,0,1,1,0,0,1,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,2,1,0,1,1,0,0,1,2,0,0,0,0,0,0,1,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,0,1,1,1,0,1,1,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,2,0,1,0,0,1,0,0,0,0,1,0,1,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1]]",
      "C[M[0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,0,0,1,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,1,0,1,0,1,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1]]"
    ],
    "coefficients": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    "discovery_primes": [
      1000003,
      1000033,
      1000037
    ],
    "validation_primes": [
      1000039,
      1000081,
      1000151
    ],
    "n_validation_samples": 40,
    "max_abs_residual": 1.6136764375371294e-12,
    "mean_abs_residual": 1.6824754973421223e-13,
    "proof_status": "exact finite-field identity on tested samples",
    "notes": "nullity_est=19; float residuals are scale-dependent",
    "extra": {
      "mod_ok": true
    }
  },
  {
    "degree": 8,
    "column_names": [
      "g^(2)*g^(2)*g^(2)*g^(2)",
      "g^(2)*g^(2)*g^(4)_1",
      "g^(2)*g^(2)*g^(4)_2",
      "g^(2)*g^(6)",
      "g^(4)_1*g^(4)_1",
      "g^(4)_1*g^(4)_2",
      "g^(4)_2*g^(4)_2",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,0,1,1,1,0,2,1,0,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,0,1,2,0,0,2,0,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,1,1,0,1,0,1,1,0,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,1,1,1,0,0,2,0,0,0,0,0,0,1,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,2,0,0,1,2,0,0,2,0,0,1,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,2,0,1,1,0,0,1,1,1,0,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,2,0,1,1,1,0,0,2,0,0,0,0,0,0,0,1,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,2,1,0,0,1,1,0,1,2,0,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,2,1,0,1,1,0,0,1,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,2,1,0,1,1,0,0,1,2,0,0,0,0,0,0,1,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,0,1,1,1,0,1,1,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,2,0,1,0,0,1,0,0,0,0,1,0,1,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1]]",
      "C[M[0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,0,0,1,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,1,0,1,0,1,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1]]"
    ],
    "coefficients": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      0,
      0,
      0,
      0,
      0
    ],
    "discovery_primes": [
      1000003,
      1000033,
      1000037
    ],
    "validation_primes": [
      1000039,
      1000081,
      1000151
    ],
    "n_validation_samples": 40,
    "max_abs_residual": 1.262177448353619e-29,
    "mean_abs_residual": 1.633034518444825e-30,
    "proof_status": "exact finite-field identity on tested samples",
    "notes": "nullity_est=19; float residuals are scale-dependent",
    "extra": {
      "mod_ok": true
    }
  },
  {
    "degree": 8,
    "column_names": [
      "g^(2)*g^(2)*g^(2)*g^(2)",
      "g^(2)*g^(2)*g^(4)_1",
      "g^(2)*g^(2)*g^(4)_2",
      "g^(2)*g^(6)",
      "g^(4)_1*g^(4)_1",
      "g^(4)_1*g^(4)_2",
      "g^(4)_2*g^(4)_2",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,0,1,1,1,0,2,1,0,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,0,1,2,0,0,2,0,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,1,1,0,1,0,1,1,0,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,1,1,1,1,1,0,0,2,0,0,0,0,0,0,1,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,2,0,0,1,2,0,0,2,0,0,1,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,2,0,1,1,0,0,1,1,1,0,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,1,2,0,1,1,1,0,0,2,0,0,0,0,0,0,0,1,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,2,1,0,0,1,1,0,1,2,0,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,2,1,0,1,1,0,0,1,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,0,2,1,0,1,1,0,0,1,2,0,0,0,0,0,0,1,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,0,1,1,1,0,1,1,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,0,1,2,0,1,0,0,1,0,0,0,0,1,0,1,0,0]]",
      "C[M[0,0,0,0,0,1,2,0,0,1,1,1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1]]",
      "C[M[0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,0,0,1,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,1,0,1,0,1,1,0,1,0,1,0,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0]]",
      "C[M[0,0,0,0,1,1,1,0,0,1,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1]]"
    ],
    "coefficients": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      0,
      0,
      0,
      0
    ],
    "discovery_primes": [
      1000003,
      1000033,
      1000037
    ],
    "validation_primes": [
      1000039,
      1000081,
      1000151
    ],
    "n_validation_samples": 40,
    "max_abs_residual": 5.751878624649688e-13,
    "mean_abs_residual": 7.706299854063163e-14,
    "proof_status": "exact finite-field identity on tested samples",
    "notes": "nullity_est=19; float residuals are scale-dependent",
    "extra": {
      "mod_ok": true
    }
  }
]
```

---

# 12b. PYTHON 10D EXPLORE SUMMARY

```json
{
  "conventions": {
    "name": "self_dual_five_form_10d",
    "dim": 10,
    "form_degree": 5,
    "signature": "lorentzian",
    "number_field": "real",
    "metric_signature": [
      -1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1
    ],
    "allow_epsilon": true,
    "self_dual": true,
    "hodge_star_squared": 1,
    "epsilon_012_plus": true,
    "symmetry_group": "SO(1,9)",
    "seed": 2,
    "discovery_primes": [
      1000003,
      1000033,
      1000037
    ],
    "validation_primes": [
      1000039,
      1000081,
      1000151
    ],
    "n_discovery_samples": 32,
    "n_validation_samples": 32,
    "max_degree": 6,
    "notes": "Chiral self-dual 5-form in ten Lorentzian dimensions. Conventions: \u03b7=diag(-1,+1\u00d79), \u03b5_0123456789=+1, **=+1 on 5-forms. Literature hypothesis ~81 primary invariants is external \u2014 not a computed target used as an answer key. All claims must carry proof-status labels.",
    "extra": {}
  },
  "self_duality": {
    "passed": true,
    "n_generic_components": 252,
    "n_self_dual_dof": 126,
    "star_squared": 1,
    "signature": "lorentzian \u03b7=diag(-1,+1\u00d79)",
    "proof_status": "strong computational evidence"
  },
  "graphs": {
    "2": {
      "n_vertices": 2,
      "form_rank": 5,
      "nonisomorphic_count": 1,
      "canonical_ids": [
        "M[5]"
      ],
      "elapsed_sec": 0.0005028247833251953,
      "proof_status": "exact combinatorial enumeration",
      "note": "5-regular loopless connected multigraphs; not yet quotiented by self-duality identities",
      "_saved_at": "2026-08-06T05:55:16Z"
    },
    "4": {
      "n_vertices": 4,
      "form_rank": 5,
      "nonisomorphic_count": 4,
      "canonical_ids": [
        "M[0,1,4,4,1,0]",
        "M[0,2,3,3,2,0]",
        "M[1,1,3,3,1,1]",
        "M[1,2,2,2,2,1]"
      ],
      "elapsed_sec": 0.002611875534057617,
      "proof_status": "exact combinatorial enumeration",
      "note": "5-regular loopless connected multigraphs; not yet quotiented by self-duality identities",
      "_saved_at": "2026-08-06T05:55:16Z"
    }
  },
  "smoke": {
    "euclidean_style_raw_contraction_F_F": 4710.284830741138,
    "note": "Raw Kronecker contraction of lowered self-dual 5-form; Lorentzian raised contraction differs.",
    "proof_status": "strong computational evidence"
  },
  "literature": {
    "hypothesis_primary_invariants": 81,
    "status": "external literature hypothesis \u2014 not independently re-derived here",
    "proof_status": "unresolved"
  },
  "ranks": {},
  "generators": {
    "degrees": [],
    "names": [],
    "note": "No generators claimed yet beyond convention checks and small-graph censuses.",
    "proof_status": "unresolved"
  },
  "syzygies": [],
  "elapsed_sec": 0.12986207008361816,
  "limitations": [
    "Full degree ladder toward ~81 invariants requires large 5-regular graph censuses and self-duality reductions.",
    "N>=6 exact enumeration for 5-forms is expensive; use sampling + checkpointing.",
    "Do not treat the literature count 81 as an answer key for discovery."
  ]
}
```

---

# 13. PYTHON / MIT REPORTS

## initial_audit.md

# Initial Repository Audit

**Date:** 2026-08-06  
**Auditor role:** lead research scientist / principal software architect  
**Reference:** Elamaran–Ferko–Scarlett, *Machine Learning Invariants of Tensors* (arXiv:2512.23750), copied to `references/machine_learning_invariants_of_tensors.pdf`

---

## 1. Repository inventory

| Area | Location | Status |
|------|----------|--------|
| Graph enumeration | `src/invariants/graphs.py` | Present; weighted multigraphs |
| Tensor generation | `src/invariants/three_form_6d.py`, `hodge10.py` | Present; float-only for 6D |
| Contraction evaluation | `src/invariants/contraction.py` | Present; einsum via opt_einsum |
| Numerical rank | `src/invariants/utils.py` | SVD only |
| Finite-field arithmetic | — | **Missing** |
| Invariant selection (blind) | `src/invariants/discover.py`, `src/invariant_engine/ladder6d.py` | Partial; see §4 |
| Syzygy detection | `three_form_6d.verify_appendix_syzygies` | Hardcoded A.2 only |
| Rational reconstruction | — | **Missing** |
| Reporting / CLI | `scripts/run_6d.py`, `invariant_engine` | Fragmented |
| Reference PDF | was absent under `references/` | **Copied** from Downloads |
| Required package layout `tensor_invariants/` | — | **Missing** |
| Required CLI `run_pipeline.py` | — | **Missing** |

---

## 2. Commands run and outputs

### 2.1 Graph enumeration (`form_rank=3`)

```
N=2: connected_raw=1,   noniso=1,   raw=1
N=4: connected_raw=7,   noniso=2,   raw=10
N=6: connected_raw=640, noniso=6,   raw=760
N=8: connected_raw=168840, noniso=20, raw=190050
```

**Verdict:** counts match the paper (`1, 2, 6, 20`). Edge multiplicities are retained. Degree-2 triple edge `M[3]` is present.

### 2.2 Hardcoded generator verification (`scripts/run_6d.py`)

```
New independents by order: {2: 1, 4: 2, 6: 1, 8: 1, 10: 0, 12: 0}
Appendix A.2 residuals ~ 1e-12
VERDICT: PASS
```

**Verdict:** verifying the *paper’s named formulas* works. This is **not** blind discovery from graphs.

### 2.3 Blind ladder (`discover_at_degree`)

```
N=2: graphs=1, linear_rank=1, expected_new=1
N=4: graphs=2, linear_rank=2, expected_new=2
N=6: graphs=6, linear_rank=3, expected_new=1
```

**Verdict:** correctly recovers **connected linear ranks**, but **never computes**

\[
\mathrm{new}(N) = \mathrm{rank}([P_N \mid C_N]) - \mathrm{rank}(P_N).
\]

At N=6 the code stores `expected_new_generators=1` but reports `linear_rank=3` and does not form the lower-product matrix \(P_N\).

---

## 3. Failure-mode checklist (required)

| Suspected error | Present? | Evidence |
|-----------------|----------|----------|
| Treating weighted graphs as simple graphs | **No** | Multiplicity matrix; N=2 is triple edge |
| Discarding the degree-2 triple edge | **No** | Canonical id `M[3]` |
| Requiring three distinct neighbors instead of weighted degree 3 | **No** | Degree = sum of multiplicities |
| Merging non-isomorphic weighted degree-4 contractions | **No** | Two non-iso graphs at N=4 |
| Ignoring edge multiplicities during isomorphism | **Partial risk** | Exact min-lex for \(n\le 6\); for \(n>6\) falls back to WL / edge-multiset hash (count luckily 20) |
| Failing to generate all lower-degree product monomials | **Yes (blind path)** | `discover_at_degree` omits \(P_N\); hardcoded path in `three_form_6d` does generate them |
| Counting fixed-degree linear rank as new algebra generators | **Yes (blind path)** | N=6: reports 3, not 1 |
| Insufficient random samples | **Risk** | Ladder uses ~48 draws; no modular cross-check |
| Unstable floating-point rank thresholds | **Risk** | SVD-only final truth |
| Incorrect antisymmetric tensor signs | **No (smoke)** | Quadratic matches \(H_{abc}H^{abc}\); A.2 holds |
| Incorrect contraction index assignments | **Low** | Quartics span paper space numerically |
| Using discovery data for validation | **Yes** | Syzygies checked on fresh draws, but no discovery/validation split for reconstructed nullspaces |
| Accidental inclusion of disconnected product graphs among primitives | **No** | Connected-only enumeration |

---

## 4. Root causes of scientific disagreement / incompleteness

Even where numbers “pass,” the repository does **not** meet the research-grade acceptance criteria:

1. **Answer-key verification ≠ discovery.** `run_6d.py` evaluates the five paper formulas and checks independence. The discovery algorithm must not hard-code those generators.
2. **Missing product quotient in the graph ladder.** New generators must be \(\mathrm{rank}([P_N|C_N])-\mathrm{rank}(P_N)\). Current blind code only ranks \(C_N\).
3. **Floating-point SVD is the sole rank backend.** No exact rational, finite-field, or CRT/rational-reconstruction path.
4. **Incomplete syzygy pipeline.** Only Appendix (A.2) is hardcoded; (A.4)/(A.6) and automatic nullspace reconstruction are absent.
5. **N≥8 canonicalization is not exact.** WL/edge-hash can in principle merge non-isomorphic weighted graphs (did not for N=8 here, but is not a proof).
6. **Architecture mismatch.** Required modular package, configs, benchmarks JSON, `run_pipeline.py`, and labeled 10D reporting are absent.
7. **6D tensors are float-uniform antisymmetrizations**, not independent-component integer / \(\mathbb{F}_p\) draws as required for exact methods.
8. **10D path exists** (`hodge10.py`) with Lorentzian conventions and self-dual projection, but is not integrated into the required evidence-labeled research package.

---

## 5. Correct targets (from paper + Mathematica Gate 5)

| Degree \(N\) | Connected graphs | Connected rank | New generators after products |
|--------------|------------------|----------------|-------------------------------|
| 2 | 1 | 1 | 1 |
| 4 | 2 | 2 | 2 |
| 6 | 6 | 3 | 1 |
| 8 | 20 | 6 | 1 |
| 10 | (enumerate) | — | 0 |

Final generator degrees: **`[2, 4, 4, 6, 8]`**.

Degree-8 lower monomials that must appear in \(P_8\):

- \((x^{(2)})^4\)
- \((x^{(2)})^2 x^{(4)}_1\)
- \((x^{(2)})^2 x^{(4)}_2\)
- \((x^{(4)}_1)^2\)
- \(x^{(4)}_1 x^{(4)}_2\)
- \((x^{(4)}_2)^2\)
- \(x^{(2)} x^{(6)}\)

---

## 6. Remediation plan (executed next)

1. Create `tensor_invariants/` package with exact/modular backends.
2. Blind discovery: enumerate graphs → evaluate \(C_N\) → build \(P_N\) → select new generators.
3. Syzygy recovery with discovery/validation split and multi-prime checks.
4. Full test suite + `run_pipeline.py` CLI.
5. Only after Phase I green: checkpointed 10D exploration with proof-status labels.

---

## 8. Corrections applied after audit

| Issue | Fix |
|-------|-----|
| Blind ladder omitted \(P_N\) | `generator_selection.select_new_columns` computes \(\mathrm{rank}([P_N\|C_N])-\mathrm{rank}(P_N)\) |
| Answer-key verification as “discovery” | New CLI discovers generators from graphs without hard-coding formulas |
| SVD-only ranks | Added `nullspace.py`, `numerical_rank.py`, modular cross-checks |
| No CRT / rational reconstruction | `rational_reconstruction.py` + `syzygies.py` with fresh validation primes |
| N>6 WL-only IDs | Exact min-lex canonical labels for \(n\le 8\); fingerprint IDs for \(n>8\) |
| Missing package / CLI | `tensor_invariants/`, `run_pipeline.py`, configs, benchmarks |
| Reference PDF absent | Copied to `references/machine_learning_invariants_of_tensors.pdf` |

## 9. Final validated 6D outputs (this session)

```
N=2: graphs=1 connected_rank=1 n_new=1
N=4: graphs=2 connected_rank=2 n_new=2
N=6: graphs=6 connected_rank=3 n_new=1
N=8: graphs=20 connected_rank=6 n_new=1
N=10 (sampled): n_new=0
Generator degrees: [2, 4, 4, 6, 8]
VERDICT: PASS
```

Tests: scientific suite green (`test_generator_counts_6d`: 6 passed; core suite: 24 passed).


## 6d_reproduction.md

# Six-dimensional reproduction report

Blind discovery of polynomial invariants of a generic antisymmetric 3-form
in six Euclidean dimensions, compared to Elamaran–Ferko–Scarlett
(*Machine Learning Invariants of Tensors*, arXiv:2512.23750).

## Generator degrees

- Obtained: `[2, 4, 4, 6, 8]`
- Expected: `[2, 4, 4, 6, 8]`
- Match: **True**

## Graph counts / connected ranks / new generators

| Degree | Graphs (got/exp) | Connected rank (got/exp) | New gens (got/exp) |
|--------|------------------|---------------------------|---------------------|
| 2 | 1/1 | 1/1 | 1/1 |
| 4 | 2/2 | 2/2 | 2/2 |
| 6 | 6/6 | 3/3 | 1/1 |
| 8 | 20/20 | 6/6 | 1/1 |
| 10 | 12/None | 8/None | 0/0 |

## Proof-status labels

- Graph enumeration counts: exact combinatorial enumeration.
- Ranks / new generators: strong computational evidence (numerical SVD),
  cross-checked with finite-field ranks in the test suite.
- Syzygies: rationally reconstructed / finite-field identities on tested samples
  — **not** claimed as symbolic proofs unless separately established.

## Machine-readable outputs

- `outputs/6d/graphs.json`
- `outputs/6d/ranks.json`
- `outputs/6d/generators.json`
- `outputs/6d/syzygies.json`


## 10d_methodology.md

# Ten-dimensional methodology

## Object

Chiral (self-dual) 5-form \(F^+_{\mu_1\ldots\mu_5}\) in \(d=10\).

## Conventions (explicit)

- Signature: **Lorentzian** \(\eta=\mathrm{diag}(-1,+1^{\times 9})\).
- Levi-Civita: \(\varepsilon_{0123456789}=+1\).
- Hodge star on lowered 5-forms as in `self_duality.py`.
- On 5-forms in this signature: \(\star^2 = +1\), enabling real self-dual forms.
- Independent generic components: \(C(10,5)=252\); self-dual projection → 126 real DOF.
- Epsilon contractions: allowed by configuration (`allow_epsilon: true`) but not yet used in the low-degree census.

Do **not** mix Euclidean and Lorentzian conventions.

## Strategy

1. Validate Hodge / self-duality numerically.
2. Enumerate small connected 5-regular loopless multigraphs (exact for tiny N).
3. Degree-by-degree evaluation with product quotienting (same algebra as 6D).
4. Checkpoint after each degree; resume safely.
5. Label every scientific claim with proof-status.

## Proof-status vocabulary

- independently reproduced established result
- exact finite-field computation
- exact combinatorial enumeration
- rationally reconstructed identity
- strong computational evidence
- conjectural generator
- unresolved


## 10d_results.md

# Ten-dimensional results

## Self-duality validation

- Passed: **True**
- Generic components: 252
- Self-dual DOF: 126
- ★²: 1
- Signature: lorentzian η=diag(-1,+1×9)
- Proof-status: `strong computational evidence`

## Graph censuses (5-regular)

- N=2: 1 non-isomorphic connected graphs (exact combinatorial enumeration)
- N=4: 4 non-isomorphic connected graphs (exact combinatorial enumeration)

## Generators

- {'degrees': [], 'names': [], 'note': 'No generators claimed yet beyond convention checks and small-graph censuses.', 'proof_status': 'unresolved'}

## Literature comparison

- {'hypothesis_primary_invariants': 81, 'status': 'external literature hypothesis — not independently re-derived here', 'proof_status': 'unresolved'}

## Limitations

- Full degree ladder toward ~81 invariants requires large 5-regular graph censuses and self-duality reductions.
- N>=6 exact enumeration for 5-forms is expensive; use sampling + checkpointing.
- Do not treat the literature count 81 as an answer key for discovery.


## README.md

# Scalar Invariants of Tensors

Computational invariant theory for antisymmetric \(p\)-forms: blind discovery of
independent polynomial scalar invariants, linear relations, and polynomial
syzygies, with floating-point, exact rational, and finite-field validation.

Reference: Elamaran–Ferko–Scarlett, *Machine Learning Invariants of Tensors*
(arXiv:2512.23750) — local copy at
[`references/machine_learning_invariants_of_tensors.pdf`](references/machine_learning_invariants_of_tensors.pdf).

---

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## One-command interface

```bash
python run_pipeline.py reproduce-6d    # blind 6D paper reproduction
python run_pipeline.py verify-6d       # unit + regression tests
python run_pipeline.py explore-10d     # checkpointed 10D self-dual exploration
python run_pipeline.py verify-all      # tests + 6D + 10D smoke
```

Useful flags:

```bash
python run_pipeline.py reproduce-6d --samples 40 --seed 1 --no-syzygies
python run_pipeline.py explore-10d --max-degree 4
python run_pipeline.py verify-all --quick
```

---

## Phase I expected outputs (6D)

Blind discovery (no answer key inside the algorithm) must recover:

| Degree | Connected graphs | Connected rank | New generators |
|--------|------------------|----------------|----------------|
| 2 | 1 | 1 | 1 |
| 4 | 2 | 2 | 2 |
| 6 | 6 | 3 | 1 |
| 8 | 20 | 6 | 1 |
| 10 | (sampled) | — | 0 |

Final generator degrees: **`[2, 4, 4, 6, 8]`**.

Machine-readable results:

- `outputs/6d/graphs.json`
- `outputs/6d/ranks.json`
- `outputs/6d/generators.json`
- `outputs/6d/syzygies.json`
- `reports/6d_reproduction.md`
- `reports/initial_audit.md`

---

## Phase II (10D chiral 5-form)

```bash
python run_pipeline.py explore-10d
```

Writes:

- `reports/10d_methodology.md`
- `reports/10d_results.md`
- `outputs/10d/*.json`
- `outputs/10d/checkpoints/`

Every scientific claim carries an explicit **proof-status** label
(exact / strong computational evidence / conjectural / unresolved).
The literature count ~81 primary invariants is treated as an **external
hypothesis**, not an answer key.

---

## Package layout

```
tensor_invariants/     # mathematical core (required architecture)
configs/               # YAML convention files
benchmarks/            # paper_6d_expected.json
tests/                 # scientific regression suite
run_pipeline.py        # CLI
references/            # paper PDF
reports/ outputs/ checkpoints/
src/                   # legacy autonomous engine (retained; see MIGRATION.md)
```

---

## Methodology (6D)

At each even degree \(N\):

1. Enumerate connected loopless **weighted** multigraphs of degree 3 on \(N\) vertices.
2. Build \(C_N\) by evaluating contractions on random antisymmetric 3-forms
   generated from the \(C(6,3)=20\) independent components only.
3. Build \(P_N\) from **all** weighted-degree-\(N\) monomials in previously
   accepted generators.
4. Report
   \[
   n_{\mathrm{new}} = \operatorname{rank}([P_N\mid C_N]) - \operatorname{rank}(P_N).
   \]

Do not confuse graph counts, connected ranks, product ranks, new generators, or syzygies.

---

## Limitations

- Floating-point SVD is used for primary discovery ranks; modular ranks are
  cross-checked in tests. SVD alone is not treated as symbolic proof.
- Degree-10 graph census is **sampled** (exact enumeration is expensive);
  \(n_{\mathrm{new}}=0\) is strong computational evidence on the sample.
- Rationally reconstructed syzygies are validated on fresh samples and unused
  primes, but are **not** claimed as symbolic identities unless separately proved.
- 10D exploration is checkpointed and incomplete relative to the ~81 literature count.

## Proof-status vocabulary

| Label | Meaning |
|-------|---------|
| exact combinatorial enumeration | Graph census by exhaustive search |
| exact finite-field computation | Rank/nullspace over \(\mathbb{F}_p\) |
| rationally reconstructed identity | CRT + Farey reconstruction + fresh validation |
| strong computational evidence | Stable numerical / multi-seed / multi-prime evidence |
| conjectural generator | Suggested by computation, not proved complete |
| unresolved | Not established in this repository |

---

## Tests

```bash
python -m pytest tests/test_tensor_antisymmetry.py tests/test_graph_*.py \
  tests/test_contraction_evaluation.py tests/test_monomial_generation.py \
  tests/test_rank_backends.py tests/test_self_duality_10d.py -q

# Full scientific suite (includes N=8 enumeration / discovery; slower)
python -m pytest tests/test_generator_counts_6d.py tests/test_syzygy_validation.py -q
```


## MIGRATION.md

# Migration note

## What changed (2026-08-06)

The research-grade package `tensor_invariants/` replaces the previous
answer-key-centric 6D verification path as the primary scientific interface.

| Before (`src/invariants`, `src/invariant_engine`) | After (`tensor_invariants`, `run_pipeline.py`) |
|--------------------------------------------------|-----------------------------------------------|
| `run_6d.py` verifies hardcoded paper formulas | Blind discovery from weighted graphs + \(P_N\mid C_N\) |
| Ladder reported connected linear rank only | Separates graph count, connected rank, and new generators |
| SVD-only ranks | SVD + rational + modular backends |
| No CRT / rational reconstruction | Syzygy pipeline with discovery/validation split |
| No `references/` PDF | Paper copied to `references/` |
| Fragmented CLIs | `python run_pipeline.py …` |

## Preserved legacy code

`src/invariants/` and `src/invariant_engine/` are **retained** (autonomous
overnight runner, dashboard, caffeinate launcher). They are not deleted until
equivalent operational tests pass for any workflows that still depend on them.

New scientific work should import `tensor_invariants` and use `run_pipeline.py`.

## Audit trail

See `reports/initial_audit.md` for the pre-fix failure-mode checklist and
root-cause analysis.


---

# 14. PYTHON SMOKE RERUN (2026-08-06 AUDIT)

```
=== graph counts ===
2 1
4 2
6 6
=== self-duality ===
True 0.0 0.0
=== blind 6D through deg 6 ===
2 graphs 1 crank 1 new 1
4 graphs 2 crank 2 new 2
6 graphs 6 crank 3 new 1
degrees [2, 4, 4, 6]
SMOKE_OK

```

---

# 15. SHA-256 DIGESTS (Research top-level files)

```
131de04c9e6caa03c67ba700cb312d4b7ae9cc6e543eced0539d71b8670b2b61  ./6D_3Form_Project.nb
d4b73aef9cebf1f487b58bde5c93ffeb435ca3ee31106f7b5aacea7ec5faead7  ./AntisymmetricPForms.wl
cae2a749a6ed6405c63651259660c30eb7e232b091213bfdd9227105028337a0  ./AppendixRelations6D.wl
085e6dc3233bdafde53329fd580ed01c36742b6cf3d386a6aa1d670114d56ebe  ./Degree8CanonicalGraphKeys.wl
46cbcc18315cf9c73e300eac75103ae74d3ea8894d6f19369423b81ec0b67a76  ./FunctionalIndependence6D.wl
93344630e3fb39f4c52ff84089a18838856485c4fe9adf5ffa532d2b64b2d356  ./GraphEnumeration6D.wl
a9240642de84e85633db04de4d91b97e7955064c5fcc9877c2db79985a689f2b  ./GraphEnumeration6D_FIXED.wl
21838131abcd8fae511b3fc3cb207d08cd410eb4bc1746ad363391cf7d6edc75  ./InvariantBenchmarks.wl
05b3efd51f5a7df29fe7fe7d4fdbfbf2fb462c10bf866297555e2097e8f10f98  ./InvariantBenchmarks_CORRECTED_V2.wl
8e8248abfefc8c92dae6ee78c2bd366b3ab1d709df65b2d5bf19be9855cb9d52  ./MetricContractions6D.wl
b385693d43cd6f8d9d07a2f8df4ca8e307f14c6a38860420ca84280648ecacee  ./RESEARCH_LOG.md
b385693d43cd6f8d9d07a2f8df4ca8e307f14c6a38860420ca84280648ecacee  ./RESEARCH_LOG_2.md
b385693d43cd6f8d9d07a2f8df4ca8e307f14c6a38860420ca84280648ecacee  ./RESEARCH_LOGv3.md
b385693d43cd6f8d9d07a2f8df4ca8e307f14c6a38860420ca84280648ecacee  ./RESEARCH_LOGv4.md
5f5b4592baf86cae66bf2d11a5b2aec7c2a1cad7155edab18a4541f9b9bb4d64  ./TenDChiralFiveForm_Representation_Literature_Gate.md
85f07701a770933c4995f02971df50cbe3db6b4225c94daebfbd388fb518b716  ./TenDDegree10Foundations_V1.wl
186315f4bdc0049979251bbe4fc5e7a742a8ed9c60b21d7b59ec9a0e37800983  ./TenDDegree4Invariants_V1.wl
ea2418526f2134a265a134acb99b643eb60d52bd1c7e448008f70c28d26188bf  ./TenDDegree4Invariants_V2.wl
ec29ac78e5dd53abeb48e2aaed2e5459bdd903b2fd374771a44626d181511ea1  ./TenDDegree4Invariants_V3.wl
0b600b556c579330c32da3b8bb44829a1d76209552c30aa1fe620d6a6da5d247  ./TenDDegree4Invariants_V4.wl
b00cc3f037701ba89fe5815b5e87994257880922740e20baec3c124d96bf0228  ./TenDDegree6Catalog.csv
8a4767bc3bd65ae1ed639191d11ba4d0c128234989223b6a432a8b7f27bc8b1c  ./TenDDegree6Catalog_V1.wl
c52f7bee266ea5e398d381e9e1205405d599782b9c3968b7a09f92d21d6ee418  ./TenDDegree6Catalog_V2.wl
417c2f8ae4c4e397c5080af4d6d1993ac4641ab770fa73a70961b8f250fff652  ./TenDDegree6GraphBasis_BatchA_V1.wl
f18973e2b6af0dbda59aaae750c27ec0053cb6cc093143473c0b8fe64c9309d5  ./TenDDegree6GraphBasis_BatchB1_V1.wl
e29141fd4dcb65dc9f31d82f82c802abdb374a0038d23e04952e0f55fe333c1f  ./TenDDegree6GraphBasis_BatchB2_V1.wl
7c606ef1c5a328101a14e76a5e832f9445491c83d686d306ffc2320f4c8f9444  ./TenDDegree6GraphBasis_BatchC_V1.wl
7c7c18f14af35cb285b96c80285f85ede876aaab586e5774b81484caeec8da45  ./TenDDegree6GraphBasis_FinalK6_V1.wl
b7646ebad277740960ccc796dbcf7bf76a2e5f796f82a9a0c22c5686c9ec3cff  ./TenDDegree6GraphBasis_FinalK6_V2.wl
b050f4404ac3ff2710903123c1a1d299800707ad4731947779509226d5464145  ./TenDDegree6GraphEnumeration_V1.wl
ba677c4e9d766ba2d6fb6be3bacd82064ce7fb81a93f64bc79f1c8e6704af07c  ./TenDDegree6N1050Invariant_V1.wl
61ee09a71e4e0d21373d4a466a59c389c990e6e33dc94f41fb1c71da081a074c  ./TenDDegree6N1050Invariant_V2.wl
942f8339e1f47acad8fdeeda4ba72461b8b3d9954fed1ea9feb1930f8069f155  ./TenDDegree6TraceInvariant_V1.wl
1c88de1f589db39ae273433746d0da292a2206de830c17bce5476718c4dcb9ac  ./TenDDegree8BasisValidation_V1.wl
337dcc6710da8f560775f80970cecdd54963a1e5de3e3bdc984731405a0e06d2  ./TenDDegree8ContractionPlanning_V1.wl
e4c204193845827cc4ecc451587284061a2699173acd73d2a892572341ec4a25  ./TenDDegree8DiscoveryBatchA_V1.wl
e36013c112e68cef9a61e2b08aad97762f3f7e244c1df47e63e377ec14b571f5  ./TenDDegree8DiscoveryBatchB_V1.wl
ee975d55e9bc2af130231f885ef588a111cfb33f78f2529b3aa52f31e4065327  ./TenDDegree8DiscoveryBatchC_V1.wl
7cf85c27a5e259a2401d403d9f7ad757176a83527147d9a38bc47b4f77feabb9  ./TenDDegree8DiscoveryBatchD_V1.wl
5a140e9ae76419c6ee9a9d19696cf9007c8a52c1e313de4b7bc5eba2e22bbdfc  ./TenDDegree8FormulaCatalog_V1.wl
ce701d1c652f91fb3ef9612ac5cda4e698f7068853c8195c0e5957938c43f935  ./TenDDegree8GraphEnumeration_V1.wl
901b6a33a822b49ba0d079be5351ed915df3d64e56f258cb33596aa77e4f12ee  ./TenDDegree8InvariantFormulaCatalog.csv
1759a23b01543f29d05709d5c428bde14503fce69551c8dfb5089c38cd16f9a1  ./TenDDegree8InvariantFormulaCatalog.txt
93a1e9ca053117354a57f6cec92b41966c705f7624419b07ce5d9a73f83e7315  ./TenDLorentzianFoundations_V1.wl
c01d2dcf8ef1bd2e4c00e859052b70cf815d650ed2632efccbbc98d222eee21f  ./TenDLorentzianFoundations_V2.wl
105ae4934782042ec9bf8a3712e994e6a8eb186b9da2d4fa91e9fd4c5d2d5f76  ./TenDRepresentationTargets.wl

```

---

# 16. KEY MATHEMATICA MODULE HEADERS / EXCERPTS

## AntisymmetricPForms.wl

```mathematica
(* ::Package:: *)

BeginPackage["AntisymmetricPForms`"];

IndependentPFormComponents::usage =
  "IndependentPFormComponents[d,p] returns the increasing p-tuples indexing independent components of a p-form in d dimensions.";
PermutationSignToSortedTuple::usage =
  "PermutationSignToSortedTuple[indices] returns {sign,sorted}; repeated indices give {0,sorted}.";
CreatePFormData::usage =
  "CreatePFormData[d,p,values] creates a validated Association representation. values may be an Association or a list in IndependentPFormComponents order.";
AntisymmetricTensorValue::usage =
  "AntisymmetricTensorValue[form,indices] returns the antisymmetrically extended component, exactly.";
RandomPForm::usage =
  "RandomPForm[d,p,{min,max}] samples the independent components uniformly from integers min through max.";
PFormDenseArray::usage =
  "PFormDenseArray[form] materializes the full rank-p array (intended only for small d^p).";

Begin["`Private`"];

ClearAll[IndependentPFormComponents];
IndependentPFormComponents::args = "Require integers d >= 1 and 0 <= p <= d; received d=`1`, p=`2`.";
IndependentPFormComponents[d_Integer?Positive, p_Integer?NonNegative] /; p <= d :=
  Subsets[Range[d], {p}];
IndependentPFormComponents[d_, p_] :=
  (Message[IndependentPFormComponents::args, d, p]; $Failed);

ClearAll[PermutationSignToSortedTuple];
PermutationSignToSortedTuple[indices_List] := Module[{sorted = Sort[indices]},
  If[DuplicateFreeQ[indices], {Signature[indices], sorted}, {0, sorted}]
];

ClearAll[CreatePFormData];
CreatePFormData::length = "Expected `1` independent values but received `2`.";
CreatePFormData::keys = "Association keys must be exactly the increasing p-tuples for d=`1`, p=`2`.";
CreatePFormData[d_Integer?Positive, p_Integer?NonNegative, values_List] /; p <= d :=
 Module[{keys = IndependentPFormComponents[d, p]},
  If[Length[values] =!= Length[keys],
    Message[CreatePFormData::length, Length[keys], Length[values]]; Return[$Failed]
  ];
  <|"Dimension" -> d, "Degree" -> p, "Components" -> AssociationThread[keys, values]|>
 ];
CreatePFormData[d_Integer?Positive, p_Integer?NonNegative, values_Association] /; p <= d :=
 Module[{keys = IndependentPFormComponents[d, p]},
  If[Sort[Keys[values]] =!= keys,
    Message[CreatePFormData::keys, d, p]; Return[$Failed]
  ];
  <|"Dimension" -> d, "Degree" -> p, "Components" -> values|>
 ];
CreatePFormData[d_, p_, _] :=
  (Message[IndependentPFormComponents::args, d, p]; $Failed);

ClearAll[AntisymmetricTensorValue];
AntisymmetricTensorValue::rank = "Expected `1` indices but received `2`.";
AntisymmetricTensorValue::range = "Every index must lie in 1 through `1`; received `2`.";
AntisymmetricTensorValue[form_Association, indices_List] := Module[
  {d = form["Dimension"], p = form["Degree"], sign, sorted},
  If[Length[indices] =!= p,
    Message[AntisymmetricTensorValue::rank, p, Length[indices]]; Return[$Failed]
  ];
  If[!AllTrue[indices, IntegerQ[#] && 1 <= # <= d &],
    Message[AntisymmetricTensorValue::range, d, indices]; Return[$Failed]
  ];
  {sign, sorted} = PermutationSignToSortedTuple[indices];
  If[sign == 0, 0, sign form["Components"][sorted]]
];

ClearAll[RandomPForm];
RandomPForm::range = "The sampling range must be two integers {min,max} with min <= max.";
RandomPForm[d_Integer?Positive, p_Integer?NonNegative, range : {min_Integer, max_Integer}] /; p <= d && min <= max :=
  CreatePFormData[d, p, RandomInteger[range, Binomial[d, p]]];
RandomPForm[_, _, range_] := (Message[RandomPForm::range]; $Failed);

ClearAll[PFormDenseArray];
PFormDenseArray[form_Association] := Module[
  {d = form["Dimension"], p = form["Degree"]},
  Array[AntisymmetricTensorValue[form, {##}] &, ConstantArray[d, p]]
];

End[];
EndPackage[];

(* Minimal working example and verification tests *)
Needs["AntisymmetricPForms`"];
SeedRandom[20260803];
h = RandomPForm[6, 3, {-3, 3}];

tests = {
VerificationTest[
  Length[IndependentPFormComponents[6, 3]],
  20,
  TestID -> "six-dimensional three-form has 20 independe

[... TRUNCATED FOR SIZE; full file at /Users/davidrabinow/Downloads/26-27 Prep/Stux Technologies/Research/AntisymmetricPForms.wl ...]

```

## MetricContractions6D.wl

```mathematica
(* ::Package:: *)

(* Load Module 1 automatically when both files are stored together. *)
If[!MemberQ[$Packages, "AntisymmetricPForms`"],
  Module[{module1 = FileNameJoin[{DirectoryName[$InputFileName], "AntisymmetricPForms.wl"}]},
    If[FileExistsQ[module1], Get[module1],
      Print["Place AntisymmetricPForms.wl in the same folder as MetricContractions6D.wl."];
      Abort[]
    ]
  ]
];

BeginPackage["PFormContractions`", {"AntisymmetricPForms`"}];

RaiseAllTensorIndices::usage =
  "RaiseAllTensorIndices[array,metric] raises every index of a covariant tensor using Inverse[metric].";
ContractTensorNetwork::usage =
  "ContractTensorNetwork[arrays,labels,metric] contracts covariant tensor arrays according to repeated labels, inserting one inverse metric per contraction edge.";
SixDTraceInvariants::usage =
  "SixDTraceInvariants[form,metric] returns the five trace-variable contractions in Eqs. (4.1)-(4.4) of Elamaran-Ferko-Scarlett.";

Begin["`Private`"];

ClearAll[RaiseTensorIndex];
RaiseTensorIndex[array_, inverseMetric_, axis_Integer] := Module[
  {rank = ArrayDepth[array], dimension, forwardPermutation,
   inversePermutation, ordered, matrix, raisedOrdered},
  dimension = Length[inverseMetric];
  forwardPermutation = Join[{axis}, DeleteCases[Range[rank], axis]];
  inversePermutation = Ordering[forwardPermutation];
  ordered = If[forwardPermutation === Range[rank],
    array, Transpose[array, forwardPermutation]];
  matrix = ArrayReshape[ordered, {dimension, dimension^(rank - 1)}];
  raisedOrdered = ArrayReshape[
    inverseMetric . matrix,
    ConstantArray[dimension, rank]
  ];
  If[inversePermutation === Range[rank],
    raisedOrdered, Transpose[raisedOrdered, inversePermutation]]
];

ClearAll[RaiseAllTensorIndices];
RaiseAllTensorIndices::metric = "Metric dimensions `1` do not match tensor dimension `2`.";
RaiseAllTensorIndices[array_, metric_?MatrixQ] := Module[
  {rank = ArrayDepth[array], dimension = Length[array], inverseMetric},
  If[Dimensions[metric] =!= {dimension, dimension},
    Message[RaiseAllTensorIndices::metric, Dimensions[metric], dimension]; Return[$Failed]
  ];
  inverseMetric = Inverse[metric];
  Fold[RaiseTensorIndex[#1, inverseMetric, #2] &, array, Range[rank]]
];

ClearAll[ContractPair];
ContractPair[left_, leftLabels_, right_, rightLabels_, inverseMetric_] := Module[
  {common, leftFree, rightFree, rightRaised, rightAxes, leftPermutation,
   rightPermutation, leftOrdered, rightOrdered, dimension, commonRank,
   outputRank, leftMatrix, rightMatrix, product, result, resultLabels},
  common = Intersection[leftLabels, rightLabels];
  If[common === {},
    Return[{TensorProduct[left, right], Join[leftLabels, rightLabels]}]
  ];
  leftFree = Select[leftLabels, !MemberQ[common, #] &];
  rightFree = Select[rightLabels, !MemberQ[common, #] &];
  rightAxes = (First@FirstPosition[rightLabels, #]) & /@ common;
  rightRaised = Fold[RaiseTensorIndex[#1, inverseMetric, #2] &, right, rightAxes];
  leftPermutation = (First@FirstPosition[leftLabels, #]) & /@ Join[leftFree, common];
  rightPermutation = (First@FirstPosition[rightLabels, #]) & /@ Join[common, rightFree];
  leftOrdered = If[leftPermutation === Range[Length[leftLabels]],
    left, Transpose[left, leftPermutation]];
  rightOrdered = If[rightPermutation === Range[Length[rightLabels]],
    rightRaised, Transpose[rightRaised, rightPermutation]];
  dimension = Length[inverseMetric];
  commonRank = Length[common];
  outputRank = Length[leftFree] + Length[rightFree];
  leftMatrix = ArrayReshape[leftOrdered,
    {dimension^Length[leftFree], dimension^commonRank}];
  rightMatrix = ArrayReshape[rightOrdered,
    {dimension^commonRank, dimension^Length[rightFree]}];
  product = leftMatrix . rightMatrix;
  result = If[outputRank == 0,
    product[[1, 1]],
    ArrayReshape[product, ConstantArray[dimension, outputRank]]
  ];
  resultLabels = Join[leftFree, rightFree];
  {result, resultLabels}
];

ClearAll[ContractTensorNetwork];
ContractTensorNetwork::count = "The n

[... TRUNCATED FOR SIZE; full file at /Users/davidrabinow/Downloads/26-27 Prep/Stux Technologies/Research/MetricContractions6D.wl ...]

```

## FunctionalIndependence6D.wl

```mathematica
(* ::Package:: *)

(* Load Modules 1 and 2 automatically when all files are stored together. *)
If[!MemberQ[$Packages, "PFormContractions`"],
  Module[{module2 = FileNameJoin[{DirectoryName[$InputFileName], "MetricContractions6D.wl"}]},
    If[FileExistsQ[module2], Get[module2],
      Print["Place MetricContractions6D.wl in the same folder as FunctionalIndependence6D.wl."];
      Abort[]
    ]
  ]
];

BeginPackage[
  "PFormIndependence`",
  {"AntisymmetricPForms`", "PFormContractions`"}
];

ExactJacobianByInterpolation::usage =
  "ExactJacobianByInterpolation[f,form,maxDegree] computes the Jacobian of polynomial invariants f with respect to the independent p-form components, using exact univariate interpolation rather than symbolic expansion or finite-precision differences.";
ModularRank::usage =
  "ModularRank[matrix,prime] computes MatrixRank over the finite field with the specified prime modulus.";

Begin["`Private`"];

ClearAll[DerivativeWeightsAtZero];
DerivativeWeightsAtZero[maximumDegree_Integer?NonNegative] := Module[
  {nodes, momentMatrix, derivativeMoments},
  nodes = Range[0, maximumDegree];
  momentMatrix = Table[
    If[power == 0, 1, nodes[[column]]^power],
    {power, 0, maximumDegree},
    {column, 1, maximumDegree + 1}
  ];
  derivativeMoments = UnitVector[maximumDegree + 1, 2];
  LinearSolve[momentMatrix, derivativeMoments]
];

ClearAll[ExactJacobianByInterpolation];
Options[ExactJacobianByInterpolation] = {"Progress" -> True};
ExactJacobianByInterpolation::degree = "maximumDegree must be a positive integer.";
ExactJacobianByInterpolation::output = "The invariant function must return an Association with a consistent ordered set of keys.";

ExactJacobianByInterpolation[
  invariantFunction_, form_Association, maximumDegree_Integer?Positive,
  OptionsPattern[]
] := Module[
  {dimension, formDegree, componentKeys, baseValues, componentCount,
   nodes, weights, baseOutput, invariantNames, columns, samples,
   variedForm, output, jacobian},

  dimension = form["Dimension"];
  formDegree = form["Degree"];
  componentKeys = Keys[form["Components"]];
  baseValues = Values[form["Components"]];
  componentCount = Length[baseValues];
  nodes = Range[0, maximumDegree];
  weights = DerivativeWeightsAtZero[maximumDegree];

  baseOutput = invariantFunction[form];
  If[!AssociationQ[baseOutput],
    Message[ExactJacobianByInterpolation::output]; Return[$Failed]
  ];
  invariantNames = Keys[baseOutput];

  columns = Table[
    If[TrueQ[OptionValue["Progress"]],
      Print["Computing exact Jacobian column ", componentIndex,
            " of ", componentCount, " for component ", componentKeys[[componentIndex]], "."]
    ];
    samples = Table[
      variedForm = CreatePFormData[
        dimension,
        formDegree,
        baseValues + node UnitVector[componentCount, componentIndex]
      ];
      output = invariantFunction[variedForm];
      If[!AssociationQ[output] || Keys[output] =!= invariantNames,
        Message[ExactJacobianByInterpolation::output]; Return[$Failed]
      ];
      Values[output],
      {node, nodes}
    ];
    weights . samples,
    {componentIndex, 1, componentCount}
  ];

  If[MemberQ[columns, $Failed, Infinity], Return[$Failed]];
  jacobian = Transpose[columns];
  <|
    "InvariantNames" -> invariantNames,
    "ComponentOrder" -> componentKeys,
    "EvaluationPoint" -> baseValues,
    "Jacobian" -> jacobian,
    "RankOverRationals" -> MatrixRank[jacobian]
  |>
];

ClearAll[ModularRank];
ModularRank::prime = "The modulus `1` must be prime.";
ModularRank[matrix_?MatrixQ, prime_Integer?Positive] := Module[{},
  If[!PrimeQ[prime], Message[ModularRank::prime, prime]; Return[$Failed]];
  MatrixRank[Mod[matrix, prime], Modulus -> prime]
];

End[];
EndPackage[];

(* Exact 6D Jacobian experiment and verification tests. *)
Needs["PFormIndependence`"];

SeedRandom[20260803];
jacobianSample = RandomPForm[6, 3, {-3, 3}];
euclideanMetric3 = IdentityMatrix[6];
invariantFunction6D = SixDTraceInvariants[#, euclidea

[... TRUNCATED FOR SIZE; full file at /Users/davidrabinow/Downloads/26-27 Prep/Stux Technologies/Research/FunctionalIndependence6D.wl ...]

```

## AppendixRelations6D.wl

```mathematica
(* ::Package:: *)

(* Load the validated contraction module automatically when stored together. *)
If[!MemberQ[$Packages, "PFormContractions`"],
  Module[{module2 = FileNameJoin[{DirectoryName[$InputFileName], "MetricContractions6D.wl"}]},
    If[FileExistsQ[module2], Get[module2],
      Print["Place MetricContractions6D.wl in the same folder as AppendixRelations6D.wl."];
      Abort[]
    ]
  ]
];

BeginPackage[
  "PFormAppendixRelations`",
  {"AntisymmetricPForms`", "PFormContractions`"}
];

DependentTraceContractions6D::usage =
  "DependentTraceContractions6D[form,metric] evaluates X_1^(6), X_2^(6), X_1^(8), and X_2^(8) from Eqs. (A.1), (A.3), and (A.5).";
AppendixRelationResiduals6D::usage =
  "AppendixRelationResiduals6D[form,metric] returns the exact left-hand sides of Eqs. (A.2a), (A.2b), (A.4), and (A.6).";

Begin["`Private`"];

ClearAll[DependentTraceContractions6D];
DependentTraceContractions6D::form = "Expected a 3-form in dimension 6.";
DependentTraceContractions6D[
  form_Association,
  metric_: IdentityMatrix[6]
] := Module[{h, specifications, evaluate},
  If[form["Dimension"] =!= 6 || form["Degree"] =!= 3,
    Message[DependentTraceContractions6D::form]; Return[$Failed]
  ];
  h = PFormDenseArray[form];
  specifications = <|
    "X_1^(6)" -> {
      {"a", "b", "c"}, {"b", "c", "i"}, {"g", "h", "i"},
      {"f", "g", "h"}, {"d", "e", "f"}, {"a", "d", "e"}
    },
    "X_2^(6)" -> {
      {"a", "b", "c"}, {"c", "f", "h"}, {"d", "e", "f"},
      {"b", "e", "i"}, {"d", "g", "i"}, {"a", "g", "h"}
    },
    "X_1^(8)" -> {
      {"a", "b", "c"}, {"b", "h", "l"}, {"j", "k", "l"},
      {"g", "j", "k"}, {"g", "h", "i"}, {"c", "f", "i"},
      {"d", "e", "f"}, {"a", "d", "e"}
    },
    "X_2^(8)" -> {
      {"a", "b", "c"}, {"c", "k", "l"}, {"j", "k", "l"},
      {"b", "h", "i"}, {"g", "h", "i"}, {"f", "g", "j"},
      {"d", "e", "f"}, {"a", "d", "e"}
    }
  |>;
  evaluate[labelLists_] := ContractTensorNetwork[
    ConstantArray[h, Length[labelLists]],
    labelLists,
    metric
  ];
  Map[evaluate, specifications]
];

ClearAll[AppendixRelationResiduals6D];
AppendixRelationResiduals6D[
  form_Association,
  metric_: IdentityMatrix[6]
] := Module[
  {x, capitalX, x2, x14, x24, x6, x8, X16, X26, X18, X28},
  x = SixDTraceInvariants[form, metric];
  capitalX = DependentTraceContractions6D[form, metric];
  If[x === $Failed || capitalX === $Failed, Return[$Failed]];

  x2 = x["x^(2)"];
  x14 = x["x_1^(4)"];
  x24 = x["x_2^(4)"];
  x6 = x["x^(6)"];
  x8 = x["x^(8)"];
  X16 = capitalX["X_1^(6)"];
  X26 = capitalX["X_2^(6)"];
  X18 = capitalX["X_1^(8)"];
  X28 = capitalX["X_2^(8)"];

  <|
    "(A.2a)" ->
      X16 - (1/2) x2 x14 + (1/18) x2^3,

    "(A.2b)" ->
      X26 + (1/2) x6 + (1/12) x2 x24
        - (1/6) x2 x14 + (1/72) x2^3,

    "(A.4)" ->
      X18 + (5/2) x8 + (3/2) x6 x2 + x14 x24
        - (2/3) x24^2 + (1/4) x14^2
        - (1/9) x24 x2^2 - (11/36) x14 x2^2
        + (1/54) x2^4,

    "(A.6)" ->
      X28 + 3 x8 + (2/3) x6 x2 + x14 x24
        - (2/3) x24^2 - (1/9) x24 x2^2
        - (1/18) x14 x2^2
  |>
];

End[];
EndPackage[];

(* Twelve fresh exact holdout samples, not used in earlier modules. *)
Needs["PFormAppendixRelations`"];
SeedRandom[20260804];
appendixHoldoutCount = 12;
appendixHoldouts = Table[
  RandomPForm[6, 3, {-3, 3}],
  {appendixHoldoutCount}
];

Print[
  "Evaluating four Appendix A relations on ",
  appendixHoldoutCount,
  " fresh exact integer tensors."
];
{appendixSeconds, appendixResidualAssociations} = AbsoluteTiming[
  AppendixRelationResiduals6D[#, IdentityMatrix[6]] & /@ appendixHoldouts
];
appendixResidualMatrix = Values /@ appendixResidualAssociations;
Print[
  "Appendix relation checks finished in ",
  NumberForm[appendixSeconds, {Infinity, 3}],
  " seconds."
];

testsModule4 = {
  VerificationTest[
    Dimensions[appendixResidualMatrix],
    {12, 4},
    TestID -> "twelve holdouts times four Appendix relations"
  ],
  VerificationTest[
    FreeQ[appendixResidualMatrix, _Real],
    Tru

[... TRUNCATED FOR SIZE; full file at /Users/davidrabinow/Downloads/26-27 Prep/Stux Technologies/Research/AppendixRelations6D.wl ...]

```

## GraphEnumeration6D_FIXED.wl

```mathematica
(* ::Package:: *)

If[!MemberQ[$Packages, "PFormContractions`"],
  Module[{module2 = FileNameJoin[{DirectoryName[$InputFileName], "MetricContractions6D.wl"}]},
    If[FileExistsQ[module2], Get[module2],
      Print["Place MetricContractions6D.wl in the same folder as GraphEnumeration6D_FIXED.wl."];
      Abort[]
    ]
  ]
];

BeginPackage[
  "PFormGraphEnumeration`",
  {"AntisymmetricPForms`", "PFormContractions`"}
];

ContractionGraphData::usage =
  "ContractionGraphData[n,degree] enumerates labeled loopless regular multigraph adjacency matrices and quotients them by graph isomorphism.";
ContractionLabelsFromMatrix::usage =
  "ContractionLabelsFromMatrix[matrix] converts a weighted adjacency matrix into one three-index label list per tensor vertex.";
GraphInvariantRankExperiment::usage =
  "GraphInvariantRankExperiment[matrices] evaluates graph contractions on exact discovery and holdout samples and returns ranks and nullspace verification data.";

Begin["`Private`"];

ClearAll[BoundedCompositions];
BoundedCompositions[total_Integer?NonNegative, bounds_List] :=
  Select[Tuples[Range[0, #] & /@ bounds], Total[#] == total &];

ClearAll[LabeledRegularMultigraphMatrices];
LabeledRegularMultigraphMatrices::args =
  "Require an even positive vertex count and a positive integer degree.";
LabeledRegularMultigraphMatrices[
  vertexCount_Integer?Positive,
  degree_Integer?Positive
] /; EvenQ[vertexCount degree] := Module[
  {results, recurse, initialMatrix, initialRemaining},
  initialMatrix = ConstantArray[0, {vertexCount, vertexCount}];
  initialRemaining = ConstantArray[degree, vertexCount];

  results = Reap[
    recurse[vertex_, remaining_, matrix_] := Module[
      {need, bounds, assignments, newRemaining, newMatrix, targets},
      If[vertex == vertexCount,
        If[remaining[[vertexCount]] == 0, Sow[matrix]];
        Return[]
      ];
      need = remaining[[vertex]];
      bounds = remaining[[vertex + 1 ;; vertexCount]];
      If[need > Total[bounds], Return[]];
      assignments = BoundedCompositions[need, bounds];
      targets = Range[vertex + 1, vertexCount];
      Do[
        newRemaining = remaining;
        newRemaining[[vertex]] = 0;
        newRemaining[[targets]] = newRemaining[[targets]] - assignment;
        If[Min[newRemaining] < 0, Continue[]];
        newMatrix = matrix;
        Do[
          newMatrix[[vertex, targets[[k]]]] = assignment[[k]];
          newMatrix[[targets[[k]], vertex]] = assignment[[k]],
          {k, Length[targets]}
        ];
        recurse[vertex + 1, newRemaining, newMatrix],
        {assignment, assignments}
      ]
    ];
    recurse[1, initialRemaining, initialMatrix]
  ][[2]];
  If[results === {}, {}, First[results]]
];
LabeledRegularMultigraphMatrices[___] :=
  (Message[LabeledRegularMultigraphMatrices::args]; $Failed);

ClearAll[MatrixConnectedQ];
MatrixConnectedQ[matrix_?MatrixQ] :=
  ConnectedGraphQ[AdjacencyGraph[Unitize[matrix]]];

ClearAll[PFormIncidenceGraph];
PFormIncidenceGraph[matrix_?MatrixQ] := Module[
  {vertexCount = Length[matrix], tensorVertices, edgeVertices = {},
   incidenceEdges = {}, edgeNumber = 0, edgeVertex},
  tensorVertices = Table[{"T", i}, {i, vertexCount}];
  Do[
    Do[
      edgeNumber++;
      edgeVertex = {"E", edgeNumber};
      AppendTo[edgeVertices, edgeVertex];
      AppendTo[incidenceEdges, UndirectedEdge[tensorVertices[[i]], edgeVertex]];
      AppendTo[incidenceEdges, UndirectedEdge[tensorVertices[[j]], edgeVertex]],
      {matrix[[i, j]]}
    ],
    {i, 1, vertexCount - 1}, {j, i + 1, vertexCount}
  ];
  Graph[Join[tensorVertices, edgeVertices], incidenceEdges]
];

ClearAll[CanonicalIncidenceKey];
CanonicalIncidenceKey[matrix_?MatrixQ] := Module[{canonical},
  canonical = CanonicalGraph[PFormIncidenceGraph[matrix]];
  Flatten[Normal[AdjacencyMatrix[canonical]]]
];

ClearAll[ContractionGraphData];
ContractionGraphData[
  vertexCount_Integer?Positive,
  degree_Integer?Positive
] := Module[{labeled, connectedLabeled, canonicalAll, canonicalCon

[... TRUNCATED FOR SIZE; full file at /Users/davidrabinow/Downloads/26-27 Prep/Stux Technologies/Research/GraphEnumeration6D_FIXED.wl ...]

```

## TenDLorentzianFoundations_V2.wl

```mathematica
(* ::Package:: *)

(*
  Module 7: foundations for a real chiral five-form in D=10 Lorentzian
  signature.

  Conventions
  -----------
  Mathematica index 1 represents the physical time index 0.
  Lorentz metric: eta = DiagonalMatrix[{-1,1,1,1,1,1,1,1,1,1}].
  Orientation: epsilon_{1...10}=+1, corresponding to epsilon_{0...9}=+1.

  For a covariant p-form F,

    star(F)_{mu_1...mu_(D-p)} = (1/p!) epsilon_{mu_1...mu_(D-p) nu_1...nu_p}
                              F^{nu_1...nu_p}.

  The implementation stores only increasing index tuples.  Consequently the
  p! permutation sum is already included and no explicit factorial appears in
  the ordered-component formula.

  Scope and complexity
  --------------------
  HodgeStarPForm currently accepts exact, nondegenerate diagonal metrics. This
  covers the Euclidean and Cartesian Lorentzian conventions needed here and
  avoids a dense 10^5 tensor. For a diagonal metric the cost is
  O[Binomial[D,p] p] time and O[Binomial[D,p]] storage. At D=10,p=5 this means
  252 stored components. A fixed-chirality form is generated from 126 freely
  specified components.
*)

If[!MemberQ[$Packages, "AntisymmetricPForms`"],
  Module[{module1 = FileNameJoin[{DirectoryName[$InputFileName], "AntisymmetricPForms.wl"}]},
    If[FileExistsQ[module1], Get[module1],
      Print["Place AntisymmetricPForms.wl in the same folder as TenDLorentzianFoundations_V2.wl."];
      Abort[]
    ]
  ]
];

BeginPackage["TenDLorentzianForms`", {"AntisymmetricPForms`"}];

HodgeStarSquareSign::usage =
  "HodgeStarSquareSign[d,p,t] returns (-1)^(p(d-p)+t), where t is the number of timelike/negative metric directions.";
HodgeStarPForm::usage =
  "HodgeStarPForm[form,metric,orientation] computes the Hodge dual for an exact nondegenerate diagonal metric and orientation +1 or -1.";
HodgeEigenProjection::usage =
  "HodgeEigenProjection[form,eigenvalue,metric,orientation] projects a middle-degree form to the stated Hodge-star eigenvalue when eigenvalue^2 equals the Hodge-star-square sign.";
ChiralProjection::usage =
  "ChiralProjection[form,chirality,metric,orientation] projects a real middle-degree form to chirality +1 or -1 when star^2=+1.";
IndependentChiralPFormComponents::usage =
  "IndependentChiralPFormComponents[d,p] returns one increasing tuple from each complementary pair, requiring d=2p.";
CreateChiralPFormData::usage =
  "CreateChiralPFormData[d,p,values,metric,orientation,chirality] constructs an exact fixed-chirality middle-degree form from one value per complementary pair.";
PFormInnerProduct::usage =
  "PFormInnerProduct[f,g,metric] returns (1/p!) f_{a1...ap} g^{a1...ap} for an exact diagonal metric.";
MiddleFormWedgeCoefficient::usage =
  "MiddleFormWedgeCoefficient[f,g] returns the coefficient of dx^1 wedge ... wedge dx^D in f wedge g, requiring equal middle degree.";
TransformDiagonalPForm::usage =
  "TransformDiagonalPForm[form,signs] applies the diagonal transformation diag(signs) to every covariant form index.";
ScalePFormData::usage =
  "ScalePFormData[scalar,form] multiplies every independent component by scalar.";
AddPFormData::usage =
  "AddPFormData[left,right] adds two p-forms with matching dimension and degree.";

Begin["`Private`"];

ClearAll[ExactDiagonalMetricData];
ExactDiagonalMetricData::metric =
  "The metric must be a square, exact, nondegenerate diagonal matrix.";
ExactDiagonalMetricData[metric_?MatrixQ] := Module[
  {dimensions = Dimensions[metric], diagonal},
  If[Length[dimensions] =!= 2 || dimensions[[1]] =!= dimensions[[2]],
    Message[ExactDiagonalMetricData::metric]; Return[$Failed]
  ];
  diagonal = Diagonal[metric];
  If[metric =!= DiagonalMatrix[diagonal] || MemberQ[diagonal, 0] ||
     !FreeQ[diagonal, _Real],
    Message[ExactDiagonalMetricData::metric]; Return[$Failed]
  ];
  <|
    "Dimension" -> Length[diagonal],
    "Diagonal" -> diagonal,
    "InverseDiagonal" -> 1/diagonal,
    "VolumeFactor" -> Sqrt[Abs[Times @@ diagonal]],
    "NegativeDirections" -> Count[diagonal, entry

[... TRUNCATED FOR SIZE; full file at /Users/davidrabinow/Downloads/26-27 Prep/Stux Technologies/Research/TenDLorentzianFoundations_V2.wl ...]

```

## TenDRepresentationTargets.wl

```mathematica
(* ::Package:: *)

(*
  TenDRepresentationTargets.wl

  Exact bookkeeping checks for the published Hilbert-series targets of one
  chiral 126-dimensional five-form representation of SO(10).

  This module does not discover or prove the representation-theory counts.
  It records Eq. (4.2) of Cederwall et al., arXiv:2509.14350v2, and verifies
  its Euler-product conversion exactly through degree 22.
*)

ClearAll["Global`*"];

Print["Running 10D REPRESENTATION TARGETS V1 with exact series arithmetic."];

maxTargetDegree = 22;

publishedHilbertCoefficients = <|
  0 -> 1,
  2 -> 0,
  4 -> 1,
  6 -> 2,
  8 -> 7,
  10 -> 14,
  12 -> 72,
  14 -> 247,
  16 -> 1364,
  18 -> 6851,
  20 -> 40170,
  22 -> 227979
|>;

publishedEulerExponents = <|
  4 -> 1,
  6 -> 2,
  8 -> 6,
  10 -> 12,
  12 -> 62,
  14 -> 221,
  16 -> 1247,
  18 -> 6404,
  20 -> 37896,
  22 -> 216486
|>;

hilbertPolynomial = Sum[
  Lookup[publishedHilbertCoefficients, degree, 0] t^degree,
  {degree, 0, maxTargetDegree}
];

(* The plethystic logarithm of Product[(1-t^n)^(-m_n),n] is Sum[m_n t^n,n]. *)
plethysticLogTruncated[series_, variable_, maximumDegree_Integer] :=
  Normal @ Series[
    Sum[
      MoebiusMu[k]/k Log[series /. variable -> variable^k],
      {k, 1, maximumDegree}
    ],
    {variable, 0, maximumDegree}
  ];

computedPlethysticLog =
  Expand[plethysticLogTruncated[hilbertPolynomial, t, maxTargetDegree]];

computedEulerExponents = Association @ Table[
  degree -> Coefficient[computedPlethysticLog, t, degree],
  {degree, Keys[publishedEulerExponents]}
];

(* Product counts are the total Hilbert coefficient minus the initial
   Euler-product balance. At degrees where generators and relations overlap,
   the latter is only a net balance, not automatically a raw generator count. *)
lowerDegreeProductBalances = Association @ Table[
  degree -> (
    publishedHilbertCoefficients[degree] - publishedEulerExponents[degree]
  ),
  {degree, Keys[publishedEulerExponents]}
];

targetSummary = <|
  "GenericFiveFormComponents" -> Binomial[10, 5],
  "ChiralFiveFormComponents" -> Binomial[10, 5]/2,
  "LorentzGroupDimension" -> 10 9/2,
  "KrullDimensionTarget" -> Binomial[10, 5]/2 - 10 9/2,
  "HilbertCoefficients" -> publishedHilbertCoefficients,
  "EulerExponents" -> computedEulerExponents,
  "ProductBalances" -> lowerDegreeProductBalances,
  "CumulativeInitialBalanceThrough12" -> Total[
    Lookup[computedEulerExponents, {4, 6, 8, 10, 12}]
  ]
|>;

Print[targetSummary];

representationTargetTests = TestReport[{
  VerificationTest[
    targetSummary["GenericFiveFormComponents"],
    252,
    TestID -> "Generic five-form has 252 components"
  ],
  VerificationTest[
    targetSummary["ChiralFiveFormComponents"],
    126,
    TestID -> "Chiral five-form has 126 components"
  ],
  VerificationTest[
    targetSummary["LorentzGroupDimension"],
    45,
    TestID -> "SO(1,9) has dimension 45"
  ],
  VerificationTest[
    targetSummary["KrullDimensionTarget"],
    81,
    TestID -> "Published generic-quotient dimension target is 81"
  ],
  VerificationTest[
    computedEulerExponents,
    publishedEulerExponents,
    TestID -> "Exact plethystic logarithm reproduces Eq. (4.2) exponents"
  ],
  VerificationTest[
    Lookup[lowerDegreeProductBalances, {4, 6, 8, 10, 12}],
    {0, 0, 1, 2, 10},
    TestID -> "Low-degree product balances are 0,0,1,2,10"
  ],
  VerificationTest[
    targetSummary["CumulativeInitialBalanceThrough12"],
    83,
    TestID -> "Initial balances through degree 12 sum to 83"
  ],
  VerificationTest[
    And @@ Table[
      Coefficient[hilbertPolynomial, t, oddDegree] == 0,
      {oddDegree, 1, maxTargetDegree, 2}
    ],
    True,
    TestID -> "Published truncation has no odd-degree singlets"
  ],
  VerificationTest[
    Coefficient[hilbertPolynomial, t, 2],
    0,
    TestID -> "Published truncation has no quadratic singlet"
  ]
}];

representationTargetTests

```

## TenDDegree4Invariants_V4.wl

```mathematica
(* ::Package:: *)

(*
  TenDDegree4Invariants_V4.wl

  First 10D invariant-enumeration gate for one real self-dual five-form in
  Lorentzian signature (-,+,...,+), epsilon_(0...9)=+1.

  Scope
  -----
  1. Enumerate loopless 5-regular multigraphs on four identical vertices.
  2. Canonicalize under permutations of the four form vertices.
  3. Evaluate every canonical metric contraction on exact chiral samples.
  4. Compare their span with I4 = Tr[M^2], the unique degree-four singlet
     reported in Eq. (4.8) of Cederwall et al., arXiv:2509.14350v2.

  Evidence level
  --------------
  Exact finite sampling supplies computational evidence for the contraction
  rank. Matching the published representation-theory singlet multiplicity is
  the independent completeness certificate at degree four.

  Complexity
  ----------
  There are 21 labeled adjacency matrices and 5 canonical multigraphs, of
  which 4 are connected. The most expensive topology has edge multiplicities
  (2,2,1) and creates rank-six intermediates of size 10^6. The code never
  creates an outer product of four rank-five tensors.
*)

If[!MemberQ[$Packages, "AntisymmetricPForms`"],
  Module[{dependency = FileNameJoin[{DirectoryName[$InputFileName],
      "AntisymmetricPForms.wl"}]},
    If[FileExistsQ[dependency], Get[dependency],
      Print["Place AntisymmetricPForms.wl in the same folder as this file."];
      Abort[]
    ]
  ]
];

If[!MemberQ[$Packages, "TenDLorentzianForms`"],
  Module[{dependency = FileNameJoin[{DirectoryName[$InputFileName],
      "TenDLorentzianFoundations_V2.wl"}]},
    If[FileExistsQ[dependency], Get[dependency],
      Print["Place TenDLorentzianFoundations_V2.wl in the same folder as this file."];
      Abort[]
    ]
  ]
];

Needs["AntisymmetricPForms`"];
Needs["TenDLorentzianForms`"];

ClearAll[
  DegreeFourAdjacencyMatrix, DegreeFourLabeledGraphs,
  DegreeFourGraphKey, DegreeFourCanonicalMatrix,
  DegreeFourCanonicalGraphs, DegreeFourConnectedQ,
  DegreeFourContractionLabels, RaiseArrayAxisDiagonal,
  ContractArrayPairDiagonal, ContractNetworkDiagonal,
  DegreeFourMetricContractions, FiveFormMMatrix, FiveFormI4,
  ExactChiralSample
];

degreeFourEdgePositions = Subsets[Range[4], {2}];

DegreeFourAdjacencyMatrix[edgeMultiplicities_List] := Module[{matrix},
  matrix = ConstantArray[0, {4, 4}];
  MapThread[
    Function[{edge, multiplicity},
      matrix[[edge[[1]], edge[[2]]]] = multiplicity;
      matrix[[edge[[2]], edge[[1]]]] = multiplicity
    ],
    {degreeFourEdgePositions, edgeMultiplicities}
  ];
  matrix
];

DegreeFourLabeledGraphs[] :=
  DegreeFourAdjacencyMatrix /@ Select[
    Tuples[Range[0, 5], Length[degreeFourEdgePositions]],
    Total /@ DegreeFourAdjacencyMatrix[#] == ConstantArray[5, 4] &
  ];

DegreeFourGraphKey[matrix_?MatrixQ] :=
  Flatten @ Table[matrix[[i, j]], {i, 1, 3}, {j, i + 1, 4}];

DegreeFourCanonicalMatrix[matrix_?MatrixQ] := First @ MinimalBy[
  (matrix[[#, #]] &) /@ Permutations[Range[4]],
  DegreeFourGraphKey
];

DegreeFourCanonicalGraphs[] :=
  SortBy[
    DeleteDuplicatesBy[
      DegreeFourCanonicalMatrix /@ DegreeFourLabeledGraphs[],
      DegreeFourGraphKey
    ],
    DegreeFourGraphKey
  ];

DegreeFourConnectedQ[matrix_?MatrixQ] :=
  ConnectedGraphQ[AdjacencyGraph[Unitize[matrix]]];

(* Give each metric edge its own label. The order of slots at a vertex is
   deterministic. Antisymmetry signs are therefore included by evaluation,
   not inferred from unsigned graph isomorphism alone. *)
DegreeFourContractionLabels[matrix_?MatrixQ] := Module[
  {labels = ConstantArray[{}, 4], edge, multiplicity, edgeLabels},
  Do[
    edge = degreeFourEdgePositions[[edgeIndex]];
    multiplicity = matrix[[edge[[1]], edge[[2]]]];
    edgeLabels = Table[
      "e" <> ToString[edge[[1]]] <> ToString[edge[[2]]] <>
        "_" <> ToString[k],
      {k, multiplicity}
    ];
    labels[[edge[[1]]]] = Join[labels[[edge[[1]]]], edgeLabels];
    labels[[edge[[2]]]] = Join[labels[[edge[[2]]]], edgeLabels],
    {edgeIndex, Length

[... TRUNCATED FOR SIZE; full file at /Users/davidrabinow/Downloads/26-27 Prep/Stux Technologies/Research/TenDDegree4Invariants_V4.wl ...]

```

## TenDDegree6GraphEnumeration_V1.wl

```mathematica
(* ::Package:: *)

(*
  TenDDegree6GraphEnumeration_V1.wl

  Combinatorial gate for metric contractions of six identical five-forms.
  Each tensor is a vertex of valency five; every metric contraction is an
  edge, and parallel edges are allowed. Self-edges are excluded because a
  metric contraction of two indices on one antisymmetric form vanishes.

  This module does not evaluate tensor contractions. It enumerates labeled
  loopless 5-regular multigraphs on six vertices and quotients them by all
  permutations of the six identical tensor vertices.

  Independent reference check used while preparing this module:
    labeled keys = 12043, canonical keys = 54, connected keys = 49.
  The reference calculation used a separate Python implementation. The
  Mathematica tests below recompute these values from scratch.

  Expected bottleneck: canonicalization compares 720 relabelings for each of
  12043 labeled keys (about 8.7 million short integer-list permutations).
*)

ClearAll[
  D6BoundedCompositions, D6AdjacencyFromKey, D6GraphKey,
  D6LabeledGraphKeys, D6CanonicalKey, D6ConnectedQ,
  D6ComponentSizes, D6OrbitSize
];

d6VertexCount = 6;
d6Valency = 5;
d6EdgePositions = Subsets[Range[d6VertexCount], {2}];
d6VertexPermutations = Permutations[Range[d6VertexCount]];

(* For each vertex permutation, this gives the old edge-key positions that
   appear in the new standard upper-triangular order. Precomputing these maps
   avoids millions of temporary 6 x 6 matrices during canonicalization. *)
d6EdgePositionIndex = AssociationThread[d6EdgePositions, Range[Length[d6EdgePositions]]];
d6PermutationEdgeMaps = Function[permutation,
    Lookup[
      d6EdgePositionIndex,
      Sort /@ ({permutation[[#[[1]]]], permutation[[#[[2]]]]} & /@
        d6EdgePositions)
    ]
  ] /@ d6VertexPermutations;

D6BoundedCompositions[total_Integer?NonNegative, bounds_List] := Module[
  {recurse},
  recurse[remaining_, {}] := If[remaining == 0, {{}}, {}];
  recurse[remaining_, {bound_, rest___}] := Flatten[
    Table[
      Prepend[#, value] & /@ recurse[remaining - value, {rest}],
      {value, 0, Min[bound, remaining]}
    ],
    1
  ];
  recurse[total, bounds]
];

D6GraphKey[matrix_?MatrixQ] :=
  Extract[matrix, d6EdgePositions];

D6AdjacencyFromKey[key_List] /; Length[key] == Length[d6EdgePositions] :=
  Module[{matrix = ConstantArray[0, {d6VertexCount, d6VertexCount}]},
    MapThread[
      Function[{edge, multiplicity},
        matrix[[edge[[1]], edge[[2]]]] = multiplicity;
        matrix[[edge[[2]], edge[[1]]]] = multiplicity
      ],
      {d6EdgePositions, key}
    ];
    matrix
  ];

(* Recursive degree-sequence completion. At vertex v, all edges to earlier
   vertices are already fixed; only the bounded composition among later
   vertices remains. The output contains one 15-entry upper-triangle key per
   labeled graph. *)
D6LabeledGraphKeys[] := Module[
  {matrix, collected, recurse},
  matrix = ConstantArray[0, {d6VertexCount, d6VertexCount}];
  collected = Reap[
    recurse[vertex_, remaining_List] := Module[
      {need, targets, assignments, nextRemaining},
      If[vertex == d6VertexCount,
        If[remaining[[vertex]] == 0, Sow[D6GraphKey[matrix], "D6Key"]];
        Return[]
      ];
      need = remaining[[vertex]];
      targets = Range[vertex + 1, d6VertexCount];
      If[need > Total[remaining[[targets]]], Return[]];
      assignments = D6BoundedCompositions[need, remaining[[targets]]];
      Do[
        nextRemaining = remaining;
        nextRemaining[[vertex]] = 0;
        nextRemaining[[targets]] = nextRemaining[[targets]] - assignment;
        If[Min[nextRemaining] >= 0,
          Do[
            matrix[[vertex, targets[[k]]]] = assignment[[k]];
            matrix[[targets[[k]], vertex]] = assignment[[k]],
            {k, Length[targets]}
          ];
          recurse[vertex + 1, nextRemaining];
          Do[
            matrix[[vertex, target]] = 0;
            matrix[[target, vertex]] = 0,
            {target, targets}
        

[... TRUNCATED FOR SIZE; full file at /Users/davidrabinow/Downloads/26-27 Prep/Stux Technologies/Research/TenDDegree6GraphEnumeration_V1.wl ...]

```

## TenDDegree6Catalog_V2.wl

```mathematica
(* ::Package:: *)

(*
  TenDDegree6Catalog_V2.wl

  Consolidates the exact finite-sample coefficient records for all 54
  canonical metric-contraction graphs of six real Lorentzian self-dual
  five-forms.  Every graph is expressed in the fixed basis

      I6^(1) = Tr[M^3],        I6^(2) = I6[N^(1050)].

  The graph reductions were obtained from exact discovery samples and checked
  on exact holdouts.  This catalog is reproducible computational evidence; it
  is not a symbolic proof that the displayed identities hold identically.

  Required file in the same folder:
    TenDDegree6GraphBasis_FinalK6_V2.wl

  Output written beside this module:
    TenDDegree6Catalog.csv
*)

If[
  !(AssociationQ[d6kCoefficientRecord] &&
    NumberQ[d6kCoefficientRecord["CoefficientI6Trace"]] &&
    NumberQ[d6kCoefficientRecord["CoefficientI6N1050"]] &&
    d6kCoefficientRecord["HoldoutResidual"] === 0),
  Module[{dependency = FileNameJoin[{DirectoryName[$InputFileName],
      "TenDDegree6GraphBasis_FinalK6_V2.wl"}]},
    If[FileExistsQ[dependency], Get[dependency],
      Print[
        "Place TenDDegree6GraphBasis_FinalK6_V2.wl in the same folder as this file."
      ];
      Abort[]
    ]
  ]
];

ClearAll[D6CatalogRow, D6CatalogCSVRow];

D6CatalogRow[record_Association] := Module[
  {number, plan, traceCoefficient, n1050Coefficient},
  number = record["CanonicalGraphNumber"];
  plan = d6pPlanTable[[number]];
  traceCoefficient = record["CoefficientI6Trace"];
  n1050Coefficient = record["CoefficientI6N1050"];
  <|
    "CanonicalGraphNumber" -> number,
    "Connected" -> plan["Connected"],
    "PeakRank" -> plan["PeakRank"],
    "PeakWorkExponent" -> plan["PeakWorkExponent"],
    "CoefficientI6Trace" -> traceCoefficient,
    "CoefficientI6N1050" -> n1050Coefficient,
    "VanishesOnExactFit" -> ({traceCoefficient, n1050Coefficient} === {0, 0}),
    "HoldoutResidual" -> record["HoldoutResidual"],
    "GraphKey" -> plan["GraphKey"]
  |>
];

D6CatalogCSVRow[row_Association] := {
  row["CanonicalGraphNumber"],
  row["Connected"],
  row["PeakRank"],
  row["PeakWorkExponent"],
  ToString[row["CoefficientI6Trace"], InputForm],
  ToString[row["CoefficientI6N1050"], InputForm],
  row["VanishesOnExactFit"],
  ToString[row["HoldoutResidual"], InputForm],
  ToString[row["GraphKey"], InputForm]
};

Print[
  "Running 10D DEGREE-6 CATALOG V2: corrected K6 trace-coefficient sign."
];

d6catalogSourceRecords = Join[
  d6eCoefficientTable,
  d6bCoefficientTable,
  d6cCoefficientTable,
  d6dCoefficientTable,
  {d6kCoefficientRecord}
];

d6catalogRows = SortBy[
  D6CatalogRow /@ d6catalogSourceRecords,
  #1["CanonicalGraphNumber"] &
];
d6catalogNumbers = #1["CanonicalGraphNumber"] & /@ d6catalogRows;
d6catalogCoefficientPairs = {
  #1["CoefficientI6Trace"], #1["CoefficientI6N1050"]
} & /@ d6catalogRows;
d6catalogZeroNumbers = Cases[
  d6catalogRows,
  row_ /; row["VanishesOnExactFit"] :> row["CanonicalGraphNumber"]
];
d6catalogNonzeroNumbers = Complement[Range[54], d6catalogZeroNumbers];
d6catalogHoldoutResiduals = #1["HoldoutResidual"] & /@ d6catalogRows;

d6catalogCSVHeader = {
  "CanonicalGraphNumber", "Connected", "PeakRank", "PeakWorkExponent",
  "CoefficientI6Trace", "CoefficientI6N1050", "VanishesOnExactFit",
  "HoldoutResidual", "GraphKey"
};
d6catalogCSVPath = FileNameJoin[{
  DirectoryName[$InputFileName], "TenDDegree6Catalog.csv"
}];
Export[
  d6catalogCSVPath,
  Prepend[D6CatalogCSVRow /@ d6catalogRows, d6catalogCSVHeader],
  "CSV"
];

d6catalogSummary = <|
  "LabeledGraphs" -> Length[d6LabeledKeys],
  "CanonicalGraphs" -> Length[d6catalogRows],
  "ConnectedGraphs" -> Count[d6catalogRows, row_ /; TrueQ[row["Connected"]]],
  "DisconnectedGraphs" -> Count[d6catalogRows, row_ /; !TrueQ[row["Connected"]]],
  "ZeroGraphsOnExactFit" -> Length[d6catalogZeroNumbers],
  "NonzeroGraphsOnExactFit" -> Length[d6catalogNonzeroNumbers],
  "CoefficientSpanRank" -> MatrixRank[d6catalogCoefficientPairs],
  "K6CoefficientPair" -> {
    d6kCoefficientRecord["CoefficientI6Tra

[... TRUNCATED FOR SIZE; full file at /Users/davidrabinow/Downloads/26-27 Prep/Stux Technologies/Research/TenDDegree6Catalog_V2.wl ...]

```

## TenDDegree8GraphEnumeration_V1.wl

```mathematica
(* ::Package:: *)

(*
  TenDDegree8GraphEnumeration_V1.wl

  Combinatorial and representation-target gate for contractions of eight
  identical real Lorentzian self-dual five-forms.  Metric-only contractions
  correspond to loopless 5-regular multigraphs on eight vertices.

  Direct labeled generation contains 45,163,496 graphs.  The companion file
  Degree8CanonicalGraphKeys.wl stores one exact 28-edge key for each
  isomorphism class, generated by an independent compiled orderly procedure.

  The orbit count is independently certified here by Burnside's lemma using
  all 22 conjugacy classes of S8.  The fixed-graph counts in the certificate
  were produced by an exact degree-vector dynamic program.  That program also
  reproduced the already validated degree-six counts 12,043 labeled and 54
  canonical before being used at degree eight.

  Representation target: Cederwall et al., arXiv:2509.14350v2, Eq. (4.2),
  gives Hilbert coefficient 7 and Euler exponent 6 at degree eight.  Since the
  one degree-four invariant supplies the product (I4)^2, the target quotient
  dimension modulo lower-degree products is six.

  This module enumerates candidate contraction topologies.  It does not yet
  evaluate the tensor contractions or prove that their span attains the
  representation-theory target.

  Required companion file in the same folder:
    Degree8CanonicalGraphKeys.wl
*)

ClearAll[
  D8EAdjacencyFromKey, D8EValidKeyQ, D8EConnectedQ,
  D8EComponentSizes, D8EPermutationClassSize
];

d8eVertexCount = 8;
d8eValency = 5;
d8eEdgePositions = Subsets[Range[d8eVertexCount], {2}];

D8EAdjacencyFromKey[key_List] /; Length[key] == Length[d8eEdgePositions] :=
  Module[{matrix = ConstantArray[0, {d8eVertexCount, d8eVertexCount}]},
    MapThread[
      Function[{edge, multiplicity},
        matrix[[edge[[1]], edge[[2]]]] = multiplicity;
        matrix[[edge[[2]], edge[[1]]]] = multiplicity
      ],
      {d8eEdgePositions, key}
    ];
    matrix
  ];

D8EValidKeyQ[key_List] := Module[{matrix},
  If[Length[key] =!= 28 ||
      !VectorQ[key, IntegerQ[#] && 0 <= # <= d8eValency &],
    Return[False]
  ];
  matrix = D8EAdjacencyFromKey[key];
  Diagonal[matrix] === ConstantArray[0, d8eVertexCount] &&
    Total[matrix, {2}] === ConstantArray[d8eValency, d8eVertexCount]
];

D8EComponentSizes[key_List] := Module[{matrix, graph},
  matrix = Unitize[D8EAdjacencyFromKey[key]];
  graph = AdjacencyGraph[matrix];
  Sort[Length /@ ConnectedComponents[graph]]
];

D8EConnectedQ[key_List] := Length[D8EComponentSizes[key]] == 1;

D8EPermutationClassSize[partition_List] := Module[{multiplicities},
  multiplicities = Tally[partition];
  8!/(Times @@ (
    Function[pair, pair[[1]]^pair[[2]] pair[[2]]!] /@ multiplicities
  ))
];

d8eKeyFile = FileNameJoin[{
  DirectoryName[$InputFileName], "Degree8CanonicalGraphKeys.wl"
}];
If[!FileExistsQ[d8eKeyFile],
  Print[
    "Place Degree8CanonicalGraphKeys.wl in the same folder as this module."
  ];
  Abort[]
];

Print[
  "Running 10D DEGREE-8 GRAPH ENUMERATION V1 with Burnside certification."
];

d8eCanonicalKeys = Get[d8eKeyFile];
d8eKeyFileSHA256 = FileHash[d8eKeyFile, "SHA256"];

(* {cycle partition, conjugacy-class size, fixed graph count,
    unordered-edge orbit count}. *)
d8eBurnsideCertificate = {
  {{8}, 5040, 10, 4},
  {{7, 1}, 5760, 0, 4},
  {{6, 2}, 3360, 18, 6},
  {{6, 1, 1}, 3360, 6, 6},
  {{5, 3}, 2688, 2, 4},
  {{5, 2, 1}, 4032, 5, 6},
  {{5, 1, 1, 1}, 1344, 11, 8},
  {{4, 4}, 1260, 256, 8},
  {{4, 3, 1}, 3360, 0, 6},
  {{4, 2, 2}, 1260, 398, 10},
  {{4, 2, 1, 1}, 2520, 50, 10},
  {{4, 1, 1, 1, 1}, 420, 138, 12},
  {{3, 3, 2}, 1120, 60, 8},
  {{3, 3, 1, 1}, 1120, 104, 10},
  {{3, 2, 2, 1}, 1680, 54, 10},
  {{3, 2, 1, 1, 1}, 1120, 54, 12},
  {{3, 1, 1, 1, 1, 1}, 112, 962, 16},
  {{2, 2, 2, 2}, 105, 76896, 16},
  {{2, 2, 2, 1, 1}, 420, 10980, 16},
  {{2, 2, 1, 1, 1, 1}, 210, 18852, 18},
  {{2, 1, 1, 1, 1, 1, 1}, 28, 258960, 22},
  {{1, 1, 1, 1, 1, 1, 1, 1}, 1, 45163496, 28}
};

d8eBurnsideWeightedSum = Tota

[... TRUNCATED FOR SIZE; full file at /Users/davidrabinow/Downloads/26-27 Prep/Stux Technologies/Research/TenDDegree8GraphEnumeration_V1.wl ...]

```

## TenDDegree8BasisValidation_V1.wl

```mathematica
(* ::Package:: *)

(*
  TenDDegree8BasisValidation_V1.wl

  Independent exact validation of the seven degree-eight invariant directions
  discovered for one real Lorentzian self-dual five-form in ten dimensions.

  The candidate basis is
    (I4)^2, Graph 3, Graph 249, Graph 508,
    Graph 61, Graph 376, Graph 528.

  Twenty-four fresh exact tensors, disjoint from all discovery samples, are
  divided into three blocks of eight.  Exact rational ranks, modular ranks,
  chirality, the null quadratic contraction, and degree-eight homogeneity are
  checked.  Passing these tests is reproducible finite-sample evidence, not a
  symbolic proof of completeness or algebraic independence.

  Required files in the same folder:
    TenDDegree8DiscoveryBatchD_V1.wl
    TenDDegree8DiscoveryBatchC_V1.wl
    TenDDegree8DiscoveryBatchB_V1.wl
    TenDDegree8DiscoveryBatchA_V1.wl
    TenDDegree8ContractionPlanning_V1.wl
    TenDDegree8GraphEnumeration_V1.wl
    Degree8CanonicalGraphKeys.wl
    TenDLorentzianFoundations_V2.wl
    AntisymmetricPForms.wl
*)

If[!ValueQ[d8d2CombinedEvaluationMatrix] ||
    Dimensions[d8d2CombinedEvaluationMatrix] =!= {8, 348} ||
    !ValueQ[d8d2CombinedRank] || d8d2CombinedRank =!= 7,
  Module[{dependency = FileNameJoin[{
      DirectoryName[$InputFileName],
      "TenDDegree8DiscoveryBatchD_V1.wl"
    }]},
    If[FileExistsQ[dependency], Get[dependency],
      Print[
        "Place TenDDegree8DiscoveryBatchD_V1.wl and all of its " <>
        "dependencies in the same folder as this file."
      ];
      Abort[]
    ]
  ]
];

Print[
  "Running 10D DEGREE-8 BASIS VALIDATION V1 on 24 fresh exact tensors."
];

d8vBasisGraphNumbers = {3, 249, 508, 61, 376, 528};
d8vBasisLabels = Prepend[
  ("Graph " <> ToString[#]) & /@ d8vBasisGraphNumbers,
  "I4^2"
];
d8vBasisPlans = d8pPlans[[d8vBasisGraphNumbers]];
d8vSeeds = Range[20261401, 20261424];

D8VInvariantVector[form_Association] := Module[
  {dense, i4Squared, graphValues},
  dense = Developer`ToPackedArray[PFormDenseArray[form]];
  i4Squared = D8DI4[form]^2;
  graphValues = D8DEvaluateGraph[dense, #] & /@ d8vBasisPlans;
  Prepend[graphValues, i4Squared]
];

D8VModularEntry[value_, prime_Integer] := Module[
  {rational = Together[value]},
  Mod[
    Numerator[rational] PowerMod[Denominator[rational], -1, prime],
    prime
  ]
];

D8VModularRank[matrix_?MatrixQ, prime_Integer] := MatrixRank[
  Map[D8VModularEntry[#, prime] &, matrix, {2}],
  Modulus -> prime
];

{d8vBuildSeconds, d8vForms} = AbsoluteTiming[
  D8DExactChiralSample /@ d8vSeeds
];

Print[
  "Evaluating seven candidate degree-eight directions on three fresh " <>
  "eight-sample blocks."
];

{d8vEvaluationSeconds, d8vEvaluationMatrix} = AbsoluteTiming[
  D8VInvariantVector /@ d8vForms
];

d8vExactRank = MatrixRank[d8vEvaluationMatrix];
d8vBlockMatrices = Partition[d8vEvaluationMatrix, 8];
d8vBlockExactRanks = MatrixRank /@ d8vBlockMatrices;
d8vPrimes = NextPrime /@ {10^6, 10^6 + 1000, 10^6 + 2000};
d8vModularRanks = D8VModularRank[d8vEvaluationMatrix, #] & /@ d8vPrimes;
d8vBlockModularRanks = Table[
  D8VModularRank[block, prime],
  {block, d8vBlockMatrices},
  {prime, d8vPrimes}
];

d8vScaledForm = ScalePFormData[2, First[d8vForms]];
d8vNegatedForm = ScalePFormData[-1, First[d8vForms]];
d8vBaseVector = First[d8vEvaluationMatrix];
d8vScaledVector = D8VInvariantVector[d8vScaledForm];
d8vNegatedVector = D8VInvariantVector[d8vNegatedForm];

d8vSummary = <|
  "CandidateBasisLabels" -> d8vBasisLabels,
  "FreshExactSampleCount" -> Length[d8vForms],
  "EvaluationMatrixDimensions" -> Dimensions[d8vEvaluationMatrix],
  "ExactRank" -> d8vExactRank,
  "ThreeFreshBlockExactRanks" -> d8vBlockExactRanks,
  "ModularPrimes" -> d8vPrimes,
  "FullMatrixModularRanks" -> d8vModularRanks,
  "ThreeBlockModularRanks" -> d8vBlockModularRanks,
  "PublishedDegree8SingletTarget" -> 7,
  "TargetConfirmedOnFreshSamples" ->
    (d8vExactRank == 7 && d8vBlockExactRanks === {7, 7, 7}),
  "SampleBuildSeconds" -> d8vBuildSeconds,
  "EvaluationSec

[... TRUNCATED FOR SIZE; full file at /Users/davidrabinow/Downloads/26-27 Prep/Stux Technologies/Research/TenDDegree8BasisValidation_V1.wl ...]

```

## TenDDegree10Foundations_V1.wl

```mathematica
(* ::Package:: *)

(*
  TenDDegree10Foundations_V1.wl

  Establishes the degree-ten search target and validates the complete product
  subspace generated from lower degrees for one real Lorentzian self-dual
  five-form in ten dimensions.

  Published representation-theory targets (Cederwall et al.,
  arXiv:2509.14350v2, Eq. (4.2)):
    dim R_10 = 14,
    initial Euler/plethystic balance at degree 10 = 12.

  Since there is no degree-two invariant, the only partition of ten using
  positive lower invariant degrees is 10 = 4 + 6.  The validated degree-four
  space has dimension one and the degree-six space has dimension two, giving
  the two product candidates
    I4 I6^(1), I4 I6^(2).

  This module validates that these products have exact rank two on fresh
  tensors.  Therefore the target quotient dimension at degree ten is 12,
  conditional on the cited singlet multiplicity 14.  This is not a graph
  enumeration and does not prove that twelve new generators have been found.

  Required files in the same folder:
    TenDDegree8FormulaCatalog_V1.wl
    TenDDegree6N1050Invariant_V2.wl
    and their dependencies.
*)

If[!ValueQ[d8fCatalog] || !ValueQ[d8vExactRank] || d8vExactRank =!= 7,
  Module[{dependency = FileNameJoin[{
      DirectoryName[$InputFileName],
      "TenDDegree8FormulaCatalog_V1.wl"
    }]},
    If[FileExistsQ[dependency], Get[dependency],
      Print[
        "Place TenDDegree8FormulaCatalog_V1.wl and all dependencies " <>
        "in the same folder as this file."
      ];
      Abort[]
    ]
  ]
];

If[!ValueQ[d6nEvaluationMatrix] || MatrixRank[d6nEvaluationMatrix] =!= 2 ||
    DownValues[D6NBuildNumeratorData] === {},
  Module[{dependency = FileNameJoin[{
      DirectoryName[$InputFileName],
      "TenDDegree6N1050Invariant_V2.wl"
    }]},
    If[FileExistsQ[dependency], Get[dependency],
      Print[
        "Place TenDDegree6N1050Invariant_V2.wl and its dependencies " <>
        "in the same folder as this file."
      ];
      Abort[]
    ]
  ]
];

Print[
  "Running 10D DEGREE-10 FOUNDATIONS V1: exact lower-degree product basis."
];

ClearAll[
  D10FTraceInvariants, D10FN1050Invariant, D10FProductVector,
  D10FModularEntry, D10FModularRank
];

d10fMetric = DiagonalMatrix[Join[{-1}, ConstantArray[1, 9]]];
d10fPublishedSingletDimension = 14;
d10fPublishedInitialBalance = 12;
d10fAvailablePositiveLowerDegrees = {4, 6, 8};
d10fLowerDegreePartitions = Select[
  IntegerPartitions[10],
  AllTrue[#, MemberQ[d10fAvailablePositiveLowerDegrees, #] &] &
];
d10fProductLabels = {"I4 I6^(1)", "I4 I6^(2)"};
d10fSeeds = Range[20261601, 20261606];

D10FTraceInvariants[form_Association] := Module[{mMixed},
  mMixed = D6NFiveFormMMatrix[form] . Inverse[d10fMetric];
  {Tr[MatrixPower[mMixed, 2]], Tr[MatrixPower[mMixed, 3]]}
];

D10FN1050Invariant[form_Association] := Module[
  {numeratorData, numeratorArray},
  numeratorData = D6NBuildNumeratorData[form];
  numeratorArray = D6NBuildSparseArray[numeratorData];
  D6NCubicNumerator[numeratorArray]/1000
];

D10FProductVector[form_Association] := Module[
  {traceInvariants, n1050},
  traceInvariants = D10FTraceInvariants[form];
  n1050 = D10FN1050Invariant[form];
  {
    traceInvariants[[1]] traceInvariants[[2]],
    traceInvariants[[1]] n1050
  }
];

D10FModularEntry[value_, prime_Integer] := Module[
  {rational = Together[value]},
  Mod[
    Numerator[rational] PowerMod[Denominator[rational], -1, prime],
    prime
  ]
];

D10FModularRank[matrix_?MatrixQ, prime_Integer] := MatrixRank[
  Map[D10FModularEntry[#, prime] &, matrix, {2}],
  Modulus -> prime
];

d10fForms = D8DExactChiralSample /@ d10fSeeds;

Print[
  "Evaluating I4 I6^(1) and I4 I6^(2) on six fresh exact tensors."
];

{d10fEvaluationSeconds, d10fProductMatrix} = AbsoluteTiming[
  D10FProductVector /@ d10fForms
];

d10fExactProductRank = MatrixRank[d10fProductMatrix];
d10fBlockMatrices = {
  d10fProductMatrix[[1 ;; 3]],
  d10fProductMatrix[[4 ;; 6]]
};
d10fBlockExactRanks = MatrixRank /@ d10fBlockMatrices;
d10fPrimes = N

[... TRUNCATED FOR SIZE; full file at /Users/davidrabinow/Downloads/26-27 Prep/Stux Technologies/Research/TenDDegree10Foundations_V1.wl ...]

```

---

# 17. PAPER EQUATION REMINDERS (6D TRACE GENERATORS)


From Elamaran–Ferko–Scarlett, arXiv:2512.23750, Eqs. (4.1)–(4.4):

x^(2) = H_abc H^abc

x_1^(4) = H_abc H_ade H^def H^bc_f

x_2^(4) = H_abc H_ade H^cef H^bd_f

x^(6) = H_abc H^chi H_ghi H^adg H_def H^bef

x^(8) = H_abc H^bci H_ghi H^gjk H_jkl H^fhl H_def H^ade

Expected connected graph counts: 1, 2, 6, 20 at degrees 2,4,6,8  
Expected connected ranks: 1, 2, 3, 6  
Expected new generators: 1, 2, 1, 1 (then 0)  
Final degrees: [2, 4, 4, 6, 8]

10D literature (Cederwall et al.): Hilbert 1 + t^4 + 2 t^6 + 7 t^8 + 14 t^10 + ...  
Krull dimension target 81 = 126 - 45 (generic trivial stabilizer; cited, not independently proved here).

Degree-8 validated basis directions (Mathematica catalog):
1. I4^2
2. Graph 3
3. Graph 249
4. Graph 508
5. Graph 61
6. Graph 376
7. Graph 528


---

# END OF MASTER DOCUMENT

File written to: `/Users/davidrabinow/Downloads/26-27 Prep/Stux Technologies/Research/MIT_Code_And_Audit_Bundle_2026-08-06/EVERYTHING_MASTER_DOCUMENT.md`
Separate audit PDF/CSV/zip and original `.wl` files remain in place.

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

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

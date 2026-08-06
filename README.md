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

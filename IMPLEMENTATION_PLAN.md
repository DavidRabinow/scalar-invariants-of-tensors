# Implementation plan — credible 10D invariant search

Tied to existing repo layout. Work order matches the staged brief.

## Existing assets to keep

| Path | Role after refactor |
|------|---------------------|
| `src/invariants/five_form_10d.py` | Combo-basis storage, projection, dense expand; Hodge audited in Stage 1 |
| `src/invariants/three_form_6d.py` | Known generators for Stage 9 / Stage 3 regression |
| `src/invariants/utils.py` | SVD rank / nullspace helpers |
| `src/invariants/timed_search.py` | Demote to `catalog` comparison mode only |
| `ui/` + `scripts/search_ui_server.py` | Preserve; Stage 8 rewires metrics |

## New modules

| Path | Stage |
|------|-------|
| `src/invariants/hodge10.py` | 1 — Levi-Civita reference + validation |
| `tests/test_hodge10.py` | 1 — ≥1000-sample foundation tests |
| `src/invariants/graphs.py` | 2 — weighted multigraph enumeration |
| `src/invariants/contraction.py` | 3 — graph → einsum compiler |
| `tests/test_graphs_6d.py` | 3 — paper regression (N=2,4 counts) |
| `src/invariants/rank_pipeline.py` | 4–6 — samples, rank, monomials, syzygies |
| `src/invariants/lorentz.py` | 7 — SO(1,9) tests |
| `ui/` updates | 8 — honest progress metrics |

## Gate rule

Do not present 10D generator lists as credible until Stage 1 tests and Stage 3 6D regression pass.

## Status log

### Stage 1 — PASS (2026-07-20)
- Files: `src/invariants/hodge10.py`, `tests/test_hodge10.py`, `five_form_10d.py` rewired
- 1000-sample validation: `max|**F-F|=0`, `max|*Fp-Fp|=0`, antisym=0, fast-vs-ref≈3e-15, free=126
- Command: `PYTHONPATH=src python3 -m unittest tests.test_hodge10 -v`

### Stage 2–3 — PASS (2026-07-20)
- Files: `src/invariants/graphs.py`, `src/invariants/contraction.py`, `tests/test_graphs_6d.py`
- 3-regular connected non-iso counts: N=2→1, N=4→2, N=6→6, N=8→20 (matches paper)
- Quadratic graph evaluates to paper `x^(2)`; two N=4 graphs lie in span of paper quartics + `(x2)^2`
- 5-regular N=2 exists (unique quintuple edge) for 10D path
- Command: `PYTHONPATH=src python3 -m unittest tests.test_graphs_6d -v`

### Remaining
- Stage 4: rank pipeline on auto graphs (6D then 10D)
- Stage 5–7: monomials, syzygies, Lorentz tests
- Stage 8: UI honest metrics
- Stage 9–10: full 6D generator recovery + report JSON


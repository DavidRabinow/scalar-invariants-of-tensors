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

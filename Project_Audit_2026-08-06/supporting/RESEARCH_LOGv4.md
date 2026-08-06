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

# Ten-dimensional results

## Ultimate goal

Independent Lorentz-scalar polynomial invariants of a real self-dual 5-form in 10D (generating set + syzygies). Literature Krull dimension ≈ 81 (Cederwall et al.) — **not achieved in this run**.

## Self-duality validation

- Passed: **True**
- Generic components: 252
- Self-dual DOF: 126
- ★²: 1
- Signature: lorentzian η=diag(-1,+1×9)
- Proof-status: `strong computational evidence`

## Degree ladder (computed this run)

| N | graphs | connected_rank | n_new | lit singlets | lit new | match? |
|---|--------|----------------|-------|--------------|---------|--------|
| 2 | 1 | 0 | 0 | 0 | 0 | yes |
| 4 | 4 | 1 | 1 | 1 | 1 | yes |
| 6 | 49 | 2 | 2 | 2 | 2 | yes |

## Generators (blind discovery)

- Degrees: `[4, 6, 6]`
- Names: `['g^(4)', 'g^(6)_1', 'g^(6)_2']`
- Graph IDs: `{'4': ['M[0,1,4,4,1,0]'], '6': ['M[0,0,0,1,4,0,1,3,1,4,1,0,0,0,0]', 'M[0,0,1,2,2,2,1,0,2,1,1,1,2,0,0]']}`
- Proof-status: `strong computational evidence`
- Note: Blind metric-graph discovery on self-dual samples. Not a complete classification of the invariant ring.

## I4 cross-check

- {'ratios_graph_over_I4': [0.9999999999999929, 0.9999999999999848, 1.000000000000004, 0.999999999999999, 1.0000000000000075, 0.9999999999999897, 0.9999999999999967, 0.999999999999995], 'ratio_mean': 0.9999999999999962, 'ratio_std': 6.917322045583247e-15, 'proof_status': 'strong computational evidence', 'note': 'Constant ratio ⇒ selected degree-4 graph spans the I4=tr(M^2) line.'}

## Degree 8 basis validation (not full census)

Independent Python check of the Mathematica degree-8 basis
\(I_4^2\) + graphs `{3,249,508,61,376,528}` on 40 self-dual samples:

- rank(\(I_4^2\) + 6 graphs) = **7** (matches literature singlet dimension)
- rank(6 graphs) = 6; rank(\(I_4^2\)) = 1
- Proof-status: `strong computational evidence`
- Artifact: `outputs/10d/degree8_basis_validation.json`
- Caveat: validates this 7-dimensional span; does **not** reduce all 1753 canonical degree-8 graphs.

## Established this run

- Degree 2: connected_rank=0, n_new=0 (matches cited Hilbert / Euler balance)
- Degree 4: connected_rank=1, n_new=1 (matches cited Hilbert / Euler balance); selected graph `M[0,1,4,4,1,0]` **equals** \(I_4=\mathrm{tr}M^2\) (ratio 1)
- Degree 6: connected_rank=2, n_new=2 (matches cited Hilbert / Euler balance)
- Degree 8: literature 7-basis independently has rank 7 on self-dual samples

## Unresolved

- Full ~81-parameter generating set / Hironaka decomposition
- Degree ≥8 complete connected census + blind new-generator extraction
- Degree ≥10 discovery
- Epsilon-tensor reduction certificate (metric-only completeness)
- Minimal syzygy resolution

## Limitations

- Results are finite-sample SVD ranks on self-dual draws — strong computational evidence, not symbolic proof.
- Metric-only graphs; epsilon completeness unresolved.
- Do not treat the literature count 81 as an answer key for discovery.
- Blind discovery completed through degree 6; degree 8 is basis validation only.

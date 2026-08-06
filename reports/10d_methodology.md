# Ten-dimensional methodology

## Object

Chiral (self-dual) 5-form \(F^+_{\mu_1\ldots\mu_5}\) in \(d=10\).

## Conventions (explicit)

- Signature: **Lorentzian** \(\eta=\mathrm{diag}(-1,+1^{\times 9})\).
- Levi-Civita: \(\varepsilon_{0123456789}=+1\).
- Hodge star on lowered 5-forms as in `self_duality.py`.
- On 5-forms in this signature: \(\star^2 = +1\), enabling real self-dual forms.
- Independent generic components: \(C(10,5)=252\); self-dual projection → 126 real DOF.
- Contractions: metric \(\eta\) on every identified index pair (not Kronecker).

## Strategy

1. Validate Hodge / self-duality numerically.
2. Enumerate connected 5-regular loopless multigraphs (exact through N=6).
3. Blind degree-by-degree rank / new-generator selection on self-dual samples.
4. Compare afterward to Cederwall et al. Hilbert targets — never as answer key.
5. Label every scientific claim with proof-status.

## Proof-status vocabulary

- independently reproduced established result
- exact finite-field computation
- exact combinatorial enumeration
- rationally reconstructed identity
- strong computational evidence
- conjectural generator
- unresolved

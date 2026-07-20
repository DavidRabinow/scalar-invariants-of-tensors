# What we are trying to figure out

## The one-sentence question

Given a tensor field with a fixed index symmetry (here: an antisymmetric *p*-form), **how many independent Lorentz scalars can you build from it**, and **what are explicit formulas + algebraic relations (syzygies) among them?**

That number is the number of free arguments of the most general Lagrangian that depends on the field strength but not on derivatives:

\[
\mathcal{L} = \mathcal{L}(I_1,\ldots,I_k).
\]

## Toy analogy (4D Maxwell)

For \(F_{\mu\nu}\) in 4D there are **2** independent invariants, e.g.

- traces: \(\mathrm{tr}(F^2),\ \mathrm{tr}(F^4)\)
- or Hodge: \(S \sim F\cdot F,\ P \sim F\cdot\tilde F\)

So nonlinear electrodynamics is \(\mathcal{L}(S,P)\).

## What the base paper already did (6D)

Object: generic (non-chiral) 3-form \(H_{\mu\nu\rho}\) in **6** dimensions.

Result: **5** independent invariants. Three equivalent presentations:

| Language | Generators (orders) |
|----------|---------------------|
| Trace / Kronecker only | \(x^{(2)}, x^{(4)}_1, x^{(4)}_2, x^{(6)}, x^{(8)}\) |
| Hodge dual | \(y^{(2)}, y^{(4)}_1, y^{(4)}_2, y^{(4)}_3, y^{(6)}\) |
| Spinors (\(M^{\alpha\beta}, N_{\alpha\beta}\)) | \(z^{(2)}, z^{(4)}_1, z^{(4)}_2, z^{(4)}_3, z^{(6)}\) |

Method: enumerate contraction graphs → evaluate on random tensors → SVD nullspaces find linear/polynomial relations.

We reproduced the trace HSOP numerically: independence pattern `1,2,1,1` at orders `2,4,6,8`, and verified Appendix A syzygies to ~1e-12.

## What we are extending to (10D chiral)

Object: **self-dual (chiral) 5-form** \(F^+_{\mu_1\ldots\mu_5}\) in **10** dimensions  
(field strength of a chiral 4-form \(A_4\), as in Type IIB / nonlinear chiral *p*-form theories).

Why this is the natural sequel (Utsav’s target, and §5 of the ML paper):

1. Same structural ladder: 2-form in 4D → 3-form in 6D → **5-form in 10D**.
2. For a *chiral* form in 6D there is only **1** invariant (the quartic). In 10D the story explodes: analytical work (Cederwall–Hutomo–Kuzenko–Lechner–Sorokin; Hutomo–Lechner–Sorokin) finds on the order of **~81 primary invariants**.
3. Physics: general nonlinear / ModMax-type / \(T\bar T\)-like theories for chiral 4-forms need an explicit basis of those scalars and the relations among candidate contractions—not just a count from a Hilbert series.

### What “figuring it out” means operationally

1. **Reproduce 6D** (done as checkpoint) — trust the pipeline.
2. **Implement 10D self-dual 5-form** numerical tensors (126 → 126 independent real components for a real self-dual 5-form in Euclidean/Lorentz with \(\star^2=+1\) appropriately; careful with signature).
3. **Enumerate / sample contractions** at orders 4, 6, 8, … (order 2 vanishes for chiral forms in many conventions; leading invariant is typically quartic).
4. **Extract**:
   - a conjectural generating set \(\{I_a\}\) of independent scalars;
   - syzygies expressing other graphs as polynomials in the \(I_a\);
   - ideally maps between tensor-index and spinor presentations.
5. **Cross-check** against the known partition function / count (~81) from the analytical papers.

## Status in this repo

- `scripts/run_6d.py` — **PASS**: 5 generators independent; Appendix A relations hold.
- `scripts/run_ladder.py` — **PASS**: blind rediscovery of 1 then 2 on easy levels.
- `scripts/run_10d.py` — **PASS engine**: chiral 5-form on your Mac; starter discovery found **2** independent order-4 ingredients (quadratic vanishes). Full ~81 needs a bigger auto-generated candidate list.
- Next code milestone: auto-generate many more 10D contractions so discovery can climb toward ~81.

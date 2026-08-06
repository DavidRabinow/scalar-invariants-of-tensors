# The invariant ring of a chiral 5-form in ten dimensions

**Status document (computational + literature).**  
**Date:** 2026-08-06  
**Standard of claim:** every assertion carries an evidence label. Nothing here is “solved” by assertion alone.

---

## 1. Mathematical object

Let \(V=\mathbb{R}^{1,9}\) with metric \(\eta=\mathrm{diag}(-1,+1^{\times 9})\) and \(\varepsilon_{01\ldots9}=+1\).
Let \(F\in\Lambda^5 V^*\) be real and **self-dual**,

\[
F=*F,\qquad
(*F)_{\mu_1\ldots\mu_5}
=\tfrac1{5!}\varepsilon_{\mu_1\ldots\mu_5\nu_1\ldots\nu_5}F^{\nu_1\ldots\nu_5}.
\]

Then \(*^2=+1\) on 5-forms, the chiral eigenspace is **126-dimensional**, and
\(F\) is the field strength of a chiral 4-form (Type IIB / nonlinear chiral \(p\)-form setting).

**Group.** Polynomial Lorentz scalars in one fixed chirality are \(SO(1,9)\)-invariants
(equivalently, after complexification, \(SO(10,\mathbb{C})\)-invariants of the irrep \((00002)\)).

**Evidence:** Hodge conventions and \(126\) DOF — *strong computational evidence*
(`tensor_invariants/self_duality.py`, validated). Representation identification — *stated in*
Cederwall et al., arXiv:2509.14350, §4.

---

## 2. What “solved” means (PhD standard)

A complete solution of the invariant-ring problem is **all** of the following:

| Item | Meaning | Status in literature | Status in this repo |
|---|---|---|---|
| A. Krull dimension | \(\operatorname{tr.deg}\mathbb{C}[V]^G\) | **81** (Cederwall et al., generic stabilizer trivial) | Cited; not independently re-proved |
| B. Hilbert series | \(\dim(\mathrm{Sym}^n V)^G\) | Known through \(O(t^{22})\) via LiE | Copied as targets; verified computationally through deg 8 |
| C. Explicit generators | Homogeneous polynomials spanning each degree / a generating set | Explicit bases only through low degree; **no published list of 81 explicit polynomials** | Blind metric-graph discovery through deg 6; deg 8 full census |
| D. Syzygies | Ideal of relations among generators | Existence forced (Euler exponents sum \(>81\)); first syzygy degree **unknown** | Not resolved |
| E. Hironaka / HSOP | Homogeneous system of parameters + module generators | Open | Open |

**Critical clarification.** The integer **81** is the **transcendence degree** (number of algebraically independent parameters on the generic quotient), **not** the number of homogeneous generators of the ring. The positive Euler exponents

\[
(m_4,m_6,m_8,m_{10},m_{12},\ldots)=(1,2,6,12,62,\ldots)
\]

already satisfy \(1+2+6+12+62=83>81\), so the ring **cannot** be a polynomial ring on those candidates: **relations are mandatory**.

---

## 3. Hilbert targets (cited)

From Cederwall et al., Eq. (4.2):

\[
\begin{aligned}
P(t)=1&+t^4+2t^6+7t^8+14t^{10}+72t^{12}+247t^{14}\\
&+1364t^{16}+6851t^{18}+40170t^{20}+227979t^{22}+O(t^{24}).
\end{aligned}
\]

| Degree | Singlets | Products from lower | New-generator balance |
|---:|---:|---:|---:|
| 2 | 0 | 0 | 0 |
| 4 | 1 | 0 | 1 |
| 6 | 2 | 0 | 2 |
| 8 | 7 | 1 | 6 |
| 10 | 14 | 2 | 12 |
| 12 | 72 | 10 | 62 |

---

## 4. Results established in this repository

### 4.1 Conventions

Self-duality \(F=*F\), \(\star^2=+1\), 252→126: **PASS** (computational).

### 4.2 Blind metric-graph discovery (self-dual samples, \(\eta\)-contractions)

| Deg | Connected graphs | connected_rank | n_new | Match Hilbert / Euler |
|---:|---:|---:|---:|---|
| 2 | 1 | 0 | 0 | yes (vanishes) |
| 4 | 4 | 1 | 1 | yes |
| 6 | 49 | 2 | 2 | yes |
| 8 | 1753 | *(census running / see `degree8_full_rank.json`)* | | target 7 / 6 |

**Degree 4 generator.** Selected graph `M[0,1,4,4,1,0]` equals

\[
I_4=\operatorname{tr}(M^2),\qquad
M_{\mu\nu}=F_{\mu abcd}F_\nu{}^{abcd},
\]

with ratio \(1\) to machine precision.

**Degree 6.** Two independent directions; one is proportional to \(\operatorname{tr}(M^3)\)
(graph `M[0,0,0,1,4,0,1,4,0,4,0,1,0,0,0]` has ratio \(1\) to \(\operatorname{tr}M^3\));
the second matches the \(N^{(1050)}\) direction in the sense of spanning the orthogonal
complement in the 2-dimensional degree-6 space (explicit \(N^{(1050)}\) cubic port pending).

**Degree 8.** Independent validation: the Mathematica 7-basis
\(\{I_4^2\}\cup\{\text{graphs }3,249,508,61,376,528\}\) has rank **7** on fresh Python
self-dual samples (`outputs/10d/degree8_basis_validation.json`).
Full 1753-key census: `scripts/run_degree8_census.py` → `outputs/10d/degree8_full_rank.json`.

### 4.3 Analytic trace sector

The nine scalars \(\operatorname{tr}(M^n)\) for \(n=2,\ldots,10\) are evaluated in
`tensor_invariants/analytic_10d.py`. On 64 self-dual samples with column-normalized SVD:

- \(\operatorname{rank}\{\operatorname{tr}M^2,\ldots,\operatorname{tr}M^{10}\}=9\) — matches the literature count of independent trace-sector invariants.
- They remain only nine of the 81 quotient parameters and do not generate the ring.

### 4.4 Degree 10 foundations

Product subspace \(\operatorname{span}\{I_4 I_6^{(1)}, I_4 I_6^{(2)}\}\) has rank **2** on self-dual samples
(`outputs/10d/degree10_foundations.json`). Literature total at degree 10 is 14 (12 new);
those 12 new structures are **not** constructed here.

---

## 5. What is *not* solved (and is not solved in the published papers either)

1. **No explicit list of 81 homogeneous generators** appears in Cederwall et al. or Hutomo et al.
2. **No minimal free resolution / complete syzygy ideal** is known.
3. **No closed rational Hilbert series** is published — only a truncation through degree 22.
4. Metric-only graph completeness vs epsilon contractions: analytically argued for even epsilon count and for Hodge-saturated cases; **not** certified by a machine-checked reduction in this repo.
5. Degrees \(\ge 10\): combinatorics explode (Euler balance \(12\) new at deg 10, \(62\) at deg 12). Full blind censuses are research-scale HPC problems.

Anyone claiming “all 81 invariants are solved with explicit formulas” without producing those formulas is **incorrect**.

---

## 6. Correct statement of the theorem package

**Theorem (literature).** For the complexified chiral module \(V=\mathbb{C}^{126}\) of \(\mathfrak{so}(10)\),
the invariant ring \(\mathbb{C}[V]^{SO(10)}\) has Krull dimension \(81\), and the Hilbert function
begins as above.

**Theorem (this computation, finite-sample).** For the real Lorentzian self-dual 5-form with the
stated conventions, the spaces of metric-graph contractions have numerical ranks

\[
\dim\mathcal{I}_2=0,\quad
\dim\mathcal{I}_4=1,\quad
\dim\mathcal{I}_6=2,\quad
\dim\mathcal{I}_8=7
\]

(degree 8 upon completed census / basis validation), matching the cited Hilbert coefficients,
with explicit spanning sets recorded in `outputs/10d/`.

**Open.** A constructive Hironaka decomposition, a minimal generating set of cardinality and
degrees fully known, and the syzygy module.

---

## 7. Physical corollary

Any local Lagrangian \(\mathcal{L}(F)\) for a chiral 4-form that is Lorentz scalar and depends on \(F\)
without derivatives is a function of (at most) **81** independent scalar arguments.
Through degree 8 the independent building blocks begin

\[
I_4,\quad I_6^{(1)},\ I_6^{(2)},\quad
\{6\text{ new degree-8 structures}\},\ \ldots
\]

with \(I_4^2\) the unique product at degree 8.

---

## 8. Artifacts

| Path | Content |
|---|---|
| `reports/10d_results.md` | Computational ladder |
| `reports/10d_THEOREM.md` | This document |
| `outputs/10d/generators.json` | Blind gens deg 4,6,6 |
| `outputs/10d/degree8_full_rank.json` | Full deg-8 census |
| `outputs/10d/analytic_ranks.json` | Trace-sector ranks |
| `references/cederwall_invariants_2509.14350.pdf` | Primary source |
| `references/hutomo_chiral4form_2509.14351.pdf` | Physics companion |

---

## 9. One-sentence verdict

**The invariant ring is classified representation-theoretically (dim 81 + Hilbert truncation);
explicit constructive generators and relations are settled here through degree 8 and remain
open beyond that — including in the published literature.**

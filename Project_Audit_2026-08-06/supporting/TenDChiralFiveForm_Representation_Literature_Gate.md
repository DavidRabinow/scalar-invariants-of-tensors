# 10D chiral five-form: representation-theory and literature gate

Date: 2026-08-03

This note fixes the external targets that the 10D computation must reproduce. It distinguishes the Krull dimension of the invariant ring, the dimension of each homogeneous space of invariants, and the number of new degree-by-degree generators. Those are three different quantities.

## Status labels

- **Established analytically:** follows from a displayed argument given here.
- **Stated in a cited source:** reported by the cited primary source but not independently proved here.
- **Reproduced computationally:** verified by our exact implementation.
- **Supported only by numerical evidence:** finite sampling or numerical rank only.
- **Conjectural:** a proposed mathematical claim.
- **Unresolved:** not established by the sources or our computation.

## 1. Mathematical object and group

Let \(F\in\Lambda^5(\mathbb R^{1,9})^*\) be real and obey

\[
F=*F,
\qquad
(*F)_{\mu_1\ldots\mu_5}
=\frac1{5!}\epsilon_{\mu_1\ldots\mu_5\nu_1\ldots\nu_5}
F^{\nu_1\ldots\nu_5},
\]

with metric \(\eta=\mathrm{diag}(-,+,\ldots,+)\) and \(\epsilon_{01\ldots9}=+1\). These are the conventions used in our validated `TenDLorentzianFoundations_V2.wl` module and match Section 4 of Cederwall et al. up to the same almost-plus convention.

- **Established analytically and reproduced computationally:** \(*^2=(-1)^{p(D-p)+t}=+1\) for \((D,p,t)=(10,5,1)\), so real eigenspaces of chirality \(\pm1\) exist and each has \(252/2=126\) real components.
- **Established analytically and reproduced computationally:** in Euclidean 10D, \(*^2=-1\), so the middle-form eigenspaces have eigenvalues \(\pm i\); a nonzero real Euclidean self-dual 5-form does not exist.
- **Stated in a cited source:** after complexification the selected chiral module is the 126-dimensional irreducible \(D_5=\mathfrak{so}(10,\mathbb C)\) module with Dynkin label `(00002)` [Cederwall et al., Section 4](https://arxiv.org/pdf/2509.14350).
- **Established analytically and reproduced computationally:** an orientation-reversing element of \(O(1,9)\) exchanges the two chiralities. A single fixed-chirality space is therefore naturally an \(SO(1,9)\) representation, not a representation of the whole \(O(1,9)\).
- **Established analytically:** the tensor is the field strength \(F_5=dA_4\) of a chiral 4-form potential. Gauge invariants without derivatives are polynomials in \(F_5\), not in the potential \(A_4\).

## 2. Generic stabilizer and Krull dimension

Define the symmetric traceless tensor

\[
M_\mu{}^\nu=F_{\mu\rho_1\rho_2\rho_3\rho_4}
F^{\nu\rho_1\rho_2\rho_3\rho_4}.
\]

Cederwall et al. argue in Section 4, Eq. (4.1), that for generic \(F\), \(M\) has distinct eigenvalues. If an infinitesimal Lorentz transformation stabilizes \(F\), it stabilizes \(M\); the distinct-eigenvalue condition forces its Lie-algebra generator to vanish. They therefore identify the generic stabilizer as trivial and obtain

\[
\dim \mathbb C[V]^{SO(10,\mathbb C)}
=126-45=81.
\]

- **Stated in a cited source, with an analytic generic-eigenvalue argument:** the generic stabilizer is trivial and the Krull dimension is 81 [Cederwall et al., Eqs. (2.1), (4.1)](https://arxiv.org/pdf/2509.14350).
- **Important qualification:** 81 is the transcendence degree, equivalently the number of algebraically independent parameters on the generic quotient. It is not the total number of homogeneous generators. A non-free ring may need more than 81 generators and relations among them.
- **Unresolved in this project:** an independent algebraic-geometric proof that the stated diagonalization/distinct-spectrum argument covers a Zariski-open subset of the complex chiral module. Until supplied, we use 81 as a primary-source theorem target, not as a result newly proved by our code.

## 3. Lowest degrees and Hilbert-series targets

Cederwall et al. used LiE to count singlets in \(\operatorname{Sym}^n(126)\). Their Eq. (4.2) gives the truncated Hilbert series

\[
\begin{aligned}
P(t)={}&1+t^4+2t^6+7t^8+14t^{10}+72t^{12}+247t^{14}\\
&+1364t^{16}+6851t^{18}+40170t^{20}+227979t^{22}+O(t^{24}).
\end{aligned}
\]

The corresponding initial Euler-product exponents are

\[
(m_4,m_6,m_8,m_{10},m_{12},m_{14},m_{16},m_{18},m_{20},m_{22})
=(1,2,6,12,62,221,1247,6404,37896,216486).
\]

| Degree | Total singlets \(\dim(\mathrm{Sym}^n126)^{SO(10)}\) | Products forced by lower degrees | Initial new-generator balance |
|---:|---:|---:|---:|
| 2 | 0 | 0 | 0 |
| 4 | 1 | 0 | 1 |
| 6 | 2 | 0 | 2 |
| 8 | 7 | 1 | 6 |
| 10 | 14 | 2 | 12 |
| 12 | 72 | 10 | 62 |
| 14 | 247 | 26 | 221 |
| 16 | 1364 | 117 | 1247 |
| 18 | 6851 | 447 | 6404 |
| 20 | 40170 | 2274 | 37896 |
| 22 | 227979 | 11493 | 216486 |

- **Stated in a cited source:** the Hilbert coefficients and Euler-product exponents above, through degree 22 [Cederwall et al., Eq. (4.2)](https://arxiv.org/pdf/2509.14350).
- **Established analytically:** the familiar quadratic contraction vanishes. Since \(*F=F\),
  \(F\wedge *F=F\wedge F=0\) because a 5-form has odd degree; equivalently \(F_{\mu_1\ldots\mu_5}F^{\mu_1\ldots\mu_5}=0\).
- **Stated in a cited source:** no odd-degree scalar invariants occur, and the LiE series contains only even powers [Hutomo, Lechner and Sorokin, Section 2.1](https://arxiv.org/pdf/2509.14351).
- **Established analytically for the full complex \(SO(10)\):** \(-I\in SO(10,\mathbb C)\) acts as \(-1\) on \(\Lambda^5\), so an invariant polynomial must obey \(p(F)=p(-F)\); hence its odd homogeneous pieces vanish. For the identity component of the real Lorentz group, the equality of polynomial invariants is most safely understood through complexification rather than by claiming \(-I\in SO^+(1,9)\).

The first five positive Euler exponents sum to \(1+2+6+12+62=83\), already exceeding the Krull dimension 81. Therefore the ring cannot be a polynomial ring on all these candidates.

- **Established analytically conditional on the cited counts and dimension:** algebraic relations must exist among a homogeneous generating set.
- **Unresolved:** the first degree at which a minimal syzygy occurs. The positive Euler exponent at a degree is a net generator-minus-relation balance once generators and relations overlap; it cannot indefinitely be read as a raw generator count.
- **Unresolved:** a closed rational Hilbert series, a homogeneous system of parameters, a minimal generating set, and a minimal syzygy resolution.

## 4. Explicit low-degree tensor structures already known

Cederwall et al. decompose bilinears in \(F\) into irreducible tensors \(M^{(54)}\), \(N^{(1050)}\), and \(N^{(4125)}\), Eqs. (4.3)-(4.6).

At degree 4, the unique scalar is

\[
I_4=\operatorname{tr}M^2.
\]

At degree 6, a basis may be chosen as

\[
I_6^{(1)}=\operatorname{tr}M^3
\]

and the independent \(N^{(1050)}N^{(1050)}N^{(1050)}\) contraction displayed in Eq. (4.10) of Cederwall et al. and Eq. (2.14) of Hutomo et al.

At degree 8 there are seven total singlets: \(I_4^2\) plus six new independent structures. Cederwall et al. give tensor and spinor bases in Sections 4.1.3 and 4.2.3. At degree 10 there are 14 total singlets: the two products \(I_4I_6^{(1)}\), \(I_4I_6^{(2)}\), plus twelve new structures discussed in Section 4.1.4.

The nine trace invariants

\[
I_{2n}^{(1)}=\operatorname{tr}M^n,\qquad n=2,\ldots,10,
\]

are algebraically independent within the symmetric-traceless-matrix eigenvalue sector, but they are only nine members of the full 81-dimensional quotient. They do not generate the full chiral-five-form invariant ring.

- **Stated in cited sources:** uniqueness of \(I_4\), two independent degree-6 invariants, six new degree-8 invariants, and twelve new degree-10 invariants [Cederwall et al., Eqs. (4.7)-(4.20) and Section 4.1.4](https://arxiv.org/pdf/2509.14350); [Hutomo et al., Eqs. (2.11)-(2.16)](https://arxiv.org/pdf/2509.14351).
- **Not yet reproduced computationally:** every item in this subsection. These are the first targets for our graph and exact-sampling engine.

## 5. Metric contractions, epsilon contractions, and chirality

- **Established analytically:** two Levi-Civita tensors reduce to generalized Kronecker deltas, so any contraction with an even number of epsilon tensors reduces to metric contractions.
- **Established analytically in the directly saturated case:** if one epsilon tensor uses five indices of a particular \(F\), self-duality replaces that epsilon-F block with a metric-index version of \(F\).
- **Stated in a cited source:** Appendix C of Cederwall et al. systematically derives self-dual-five-form identities by Hodge replacing a form and reducing the product of two epsilon tensors.
- **Unresolved computationally:** whether our future canonicalizer proves that every scalar contraction containing a single epsilon reduces, with all signs and normalizations fixed, to the metric-only graph span. We will not identify parity-even and parity-odd graph spaces merely by assumption.
- **Established analytically:** orientation reversal swaps chirality. Thus a pseudoscalar distinction under full \(O(1,9)\) cannot be discussed inside one chiral 126 alone without adjoining the opposite chirality or specifying how reflection acts between the two spaces.

## 6. Literature table

| Source | Object studied | Signature | Group / representation | Invariant count | Degrees | Relations | Relevance |
|---|---|---|---|---:|---|---|---|
| M. Cederwall, J. Hutomo, S. M. Kuzenko, K. Lechner, D. P. Sorokin, *Some remarks on invariants*, arXiv:2509.14350v2 (2026) | Real self-dual 5-form and broader invariant theory | Lorentzian for tensor formulas; complex algebra for invariant ring | \(SO(1,9)\); complex chiral 126 `(00002)` | Krull dimension 81; singlet counts through degree 22 | First nonzero: 4; counts listed above | Relations must exist; first syzygy degree unknown | Primary representation-theory target and explicit low-degree bases. [arXiv](https://arxiv.org/abs/2509.14350) |
| J. Hutomo, K. Lechner, D. P. Sorokin, *On non-linear chiral 4-form theories in D=10*, JHEP 02 (2026) 147, arXiv:2509.14351 | Chiral 4-form potential with self-dual 5-form composite/field strength | Lorentzian, mostly-plus | \(SO(1,9)\), chiral 126 | 81 functionally independent parameters; explicit degrees 4 and 6 | Unique degree 4; two degree 6; nine trace-sector invariants at 4 through 20 | Full classification open | Physical nonlinear-theory and 10D ModMax-like context. [arXiv](https://arxiv.org/abs/2509.14351), [DOI](https://doi.org/10.1007/JHEP02(2026)147) |
| I. Bandos, K. Lechner, D. Sorokin, P. K. Townsend, *A non-linear duality-invariant conformal extension of Maxwell's equations*, Phys. Rev. D 102 (2020) 121703, arXiv:2007.09092 | ModMax nonlinear electrodynamics | 4D Lorentzian | 4D electromagnetic duality and Lorentz symmetry | Not a 10D invariant count | Quartic structure in 4D formulation | Not a 10D syzygy result | This is reference [67] of Elamaran et al.; it motivates “ModMax-type” language but does not classify 10D chiral-five-form invariants. [arXiv](https://arxiv.org/abs/2007.09092), [DOI](https://doi.org/10.1103/PhysRevD.102.121703) |
| I. Bandos, K. Lechner, D. Sorokin, P. K. Townsend, *On p-form gauge theories and their conformal limits*, JHEP 03 (2021) 022, arXiv:2012.09286 | Nonlinear duality-invariant and chiral p-form theories | Minkowski | General p-forms in \(D=4n\), chiral forms in \(D=4n+2\) | No 10D invariant-ring enumeration | Model-dependent | No invariant-ring resolution | General chiral/ModMax-type framework. [arXiv](https://arxiv.org/abs/2012.09286), [DOI](https://doi.org/10.1007/JHEP03(2021)022) |
| Z. Avetisyan, O. Evnin, K. Mkrtchyan, *Nonlinear (chiral) p-form electrodynamics*, JHEP 08 (2022) 112, arXiv:2205.02522 | Lagrangian theories for nonlinear higher forms, including 4-forms in 10D | Lorentzian | Chiral \(2k\)-forms in \(4k+2\) dimensions | No invariant-ring enumeration | Model-dependent | No invariant-ring resolution | Independent formulation of interacting 10D chiral 4-forms. [arXiv](https://arxiv.org/abs/2205.02522), [DOI](https://doi.org/10.1007/JHEP08(2022)112) |
| A. Sen, *Covariant Action for Type IIB Supergravity*, JHEP 07 (2016) 017, arXiv:1511.08220 | Type IIB supergravity with self-dual five-form sector | 10D Lorentzian | Lorentz covariant type IIB fields | No invariant-ring count | Action-level | No scalar-contraction classification | Confirms the physical chiral 4-form / self-dual 5-form setting. [arXiv](https://arxiv.org/abs/1511.08220), [DOI](https://doi.org/10.1007/JHEP07(2016)017) |
| M. F. Paulos, *Higher derivative terms including the Ramond-Ramond five-form*, JHEP 10 (2008) 047, arXiv:0804.0763 | Higher-derivative type-IIB couplings involving \(F_5\) and curvature | 10D Lorentzian | Type IIB covariance | Specialized contraction basis, not full pure-\(F_5\) ring | Eight-derivative correction sector | Schouten reductions in that sector | Shows why exact tensor-identity reduction matters in type IIB applications. [arXiv](https://arxiv.org/abs/0804.0763), [DOI](https://doi.org/10.1088/1126-6708/2008/10/047) |

### Generic unconstrained 5-form versus chiral 5-form

The table's invariant counts apply to one chiral 126, not to the full 252-dimensional \(\Lambda^5\). For an unconstrained real 5-form the quadratic norm does not vanish generically, both chiral halves are present in Lorentzian signature, and the invariant ring is a different problem.

- **Unresolved:** a complete Hilbert series, minimal generators, syzygies, or canonical generic-orbit classification for the unconstrained 252-dimensional five-form was not located in this targeted primary-source review.
- **Methodological rule:** no count for the chiral 126 may be transferred to the unconstrained 252 representation.

## 7. Computational consequences and validation gates

The next implementation must proceed in this order:

1. Reproduce exactly the Hilbert coefficient and Euler-exponent table through degree 22 from fixed integer data.
2. Enumerate degree-4 metric graphs and recover a one-dimensional nonzero span represented by \(I_4=\operatorname{tr}M^2\).
3. Enumerate degree-6 graphs and recover a two-dimensional span; verify that \(\operatorname{tr}M^3\) alone is insufficient.
4. At degree 8, recover total dimension 7 and distinguish the product \(I_4^2\) from six new directions.
5. At degree 10, recover total dimension 14 and distinguish the two products \(I_4I_6^{(1,2)}\) from twelve new directions.
6. Use exact rational and multi-prime modular ranks; verify every nullspace relation on fresh exact holdouts.
7. Treat graph stabilization only as evidence. Completeness at a degree is certified only by matching the independent representation-theoretic singlet count.

The combinatorics become severe immediately: a metric-only contraction of \(N\) five-valent vertices is a loopless 5-regular multigraph, with antisymmetry signs beyond ordinary graph isomorphism. The practical first target is degree 4, followed by degree 6. Degree 8 should not be attempted until both lower gates match the cited singlet multiplicities exactly.

## 8. Gate decision

**Gate passed at the literature/formulation level:** the target representation, generic quotient dimension, first nonzero degree, and singlet counts through degree 22 are now sourced.

**Gate not yet passed computationally:** none of the 10D invariant counts or explicit low-degree tensor structures has yet been reproduced by our own enumeration code. The next code module should implement degree-4 direct and graph evaluations and compare them with \(\operatorname{tr}M^2\).

"""Chinese remainder theorem and rational reconstruction for syzygies."""

from __future__ import annotations

from fractions import Fraction
from math import gcd
from typing import Mapping, Sequence


def crt_combine(residues: Sequence[int], moduli: Sequence[int]) -> int:
    """
    Combine residues modulo pairwise-coprime moduli into a unique class mod Π m_i.

    Returns the representative in ``[0, M)``.
    """
    if len(residues) != len(moduli):
        raise ValueError("residues/moduli length mismatch")
    if not moduli:
        return 0
    x, M = int(residues[0]) % int(moduli[0]), int(moduli[0])
    for a, m in zip(residues[1:], moduli[1:]):
        a = int(a) % int(m)
        m = int(m)
        # solve x + M t ≡ a (mod m)
        # t ≡ (a - x) * M^{-1} (mod m)
        inv = pow(M % m, -1, m)
        t = ((a - x) * inv) % m
        x = x + M * t
        M *= m
    return x % M


def rational_reconstruct(a: int, m: int, max_den: int | None = None) -> Fraction:
    """
    Reconstruct a rational ``n/d`` with ``gcd(n,d)=1``, ``0 < d <= max_den``,
    such that ``n/d ≡ a (mod m)``, via continued fractions / Farey method.

    Default ``max_den = floor(sqrt(m/2))``.
    """
    a = a % m
    if max_den is None:
        max_den = int((m // 2) ** 0.5)

    # Extended continued fraction
    v0_n, v0_d = m, 0  # (m, 0) conceptually for remainder tracking
    # Standard Wang rational reconstruction:
    r0, r1 = m, a
    s0, s1 = 0, 1
    t0, t1 = 1, 0  # unused but kept for clarity
    while r1 != 0 and r1 > max_den:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    if abs(s1) > max_den or s1 == 0:
        # Fall back: treat as integer in centered range
        centered = a if a <= m // 2 else a - m
        return Fraction(centered, 1)
    n, d = r1, s1
    if d < 0:
        n, d = -n, -d
    g = gcd(abs(n), abs(d))
    return Fraction(n // g, d // g)


def normalize_integer_vector(coeffs: Sequence[int]) -> list[int]:
    """Clear content (gcd) and fix sign so the first nonzero entry is positive."""
    vals = [int(c) for c in coeffs]
    if not vals or all(v == 0 for v in vals):
        return vals
    g = 0
    for v in vals:
        g = gcd(g, abs(v))
    vals = [v // g for v in vals]
    for v in vals:
        if v != 0:
            if v < 0:
                vals = [-x for x in vals]
            break
    return vals


def reconstruct_integer_vector_from_primes(
    vecs_by_prime: Mapping[int, Sequence[int]],
    moduli: Sequence[int] | None = None,
) -> list[int]:
    """
    Reconstruct an integer nullvector from modular images via CRT + rational reconstruction.

    ``vecs_by_prime[p]`` must be residue vectors of equal length. Result is normalized.
    """
    primes = list(moduli) if moduli is not None else list(vecs_by_prime.keys())
    if not primes:
        return []
    length = len(next(iter(vecs_by_prime.values())))
    M = 1
    for p in primes:
        M *= int(p)
    max_den = int((M // 2) ** 0.5) or 1
    out_frac: list[Fraction] = []
    for i in range(length):
        residues = [int(vecs_by_prime[p][i]) % int(p) for p in primes]
        combined = crt_combine(residues, primes)
        out_frac.append(rational_reconstruct(combined, M, max_den=max_den))
    # Clear denominators
    dens = [f.denominator for f in out_frac]
    lcm = 1
    for d in dens:
        lcm = lcm * d // gcd(lcm, d)
    ints = [int(f.numerator * (lcm // f.denominator)) for f in out_frac]
    return normalize_integer_vector(ints)


def match_nullspace_vectors(
    bases: Mapping[int, np_ndarray_like],
    *,
    scale_normalize: bool = True,
) -> list[dict]:
    """
    Attempt to match nullspace basis vectors across primes by projective scaling.

    ``bases[p]`` is shape (n_cols, nullity_p). Returns candidate matched families.
    This is a heuristic matching for small nullities.
    """
    # Deferred import typing without requiring numpy at type time
    primes = sorted(bases.keys())
    if not primes:
        return []
    # Represent each column as a tuple of ints mod p, normalized so first nonzero is 1
    def norm_col(col, p: int) -> tuple[int, ...]:
        vals = [int(x) % p for x in col]
        for v in vals:
            if v != 0:
                inv = pow(v, -1, p)
                return tuple((x * inv) % p for x in vals)
        return tuple(vals)

    ref_p = primes[0]
    ref = bases[ref_p]
    n_cols = ref.shape[0]
    nullity = ref.shape[1]
    matched = []
    for j in range(nullity):
        family = {ref_p: [int(x) % ref_p for x in ref[:, j]]}
        ref_norm = norm_col(ref[:, j], ref_p)
        ok = True
        for p in primes[1:]:
            B = bases[p]
            found = None
            for k in range(B.shape[1]):
                if norm_col(B[:, k], p) == ref_norm:
                    found = [int(x) % p for x in B[:, k]]
                    break
            if found is None:
                ok = False
                break
            family[p] = found
        if ok:
            matched.append({"primes": primes, "vectors_mod": family, "length": n_cols})
    return matched


# Alias for type checkers without importing numpy at module import for match signature
np_ndarray_like = object

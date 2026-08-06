"""
Canonical labeling of weighted loopless multigraphs.

Isomorphism must preserve edge multiplicities. For n <= 8 we use exact
min-lex search over vertex permutations (8! = 40320 is acceptable).
"""

from __future__ import annotations

from itertools import permutations
from typing import Sequence

import numpy as np


Multiplicity = tuple[tuple[int, ...], ...]


def _as_array(mult: Sequence[Sequence[int]] | np.ndarray) -> np.ndarray:
    return np.asarray(mult, dtype=int)


def upper_tri_tuple(M: np.ndarray) -> tuple[int, ...]:
    n = M.shape[0]
    return tuple(int(M[i, j]) for i in range(n) for j in range(i + 1, n))


def weighted_degrees(mult: Sequence[Sequence[int]] | np.ndarray) -> list[int]:
    M = _as_array(mult)
    n = M.shape[0]
    return [int(sum(M[i, j] for j in range(n) if j != i)) for i in range(n)]


def is_connected(mult: Sequence[Sequence[int]] | np.ndarray) -> bool:
    """BFS connectivity treating positive multiplicity as an edge."""
    M = _as_array(mult)
    n = M.shape[0]
    if n <= 1:
        return True
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in range(n):
            if v not in seen and M[u, v] > 0:
                seen.add(v)
                stack.append(v)
    return len(seen) == n


def brute_force_canonical(mult: Sequence[Sequence[int]] | np.ndarray) -> Multiplicity:
    """Exact canonical representative: min-lex upper-triangular under Aut=S_n."""
    M = _as_array(mult)
    n = M.shape[0]
    best_tri: tuple[int, ...] | None = None
    best_M: np.ndarray | None = None
    for perm in permutations(range(n)):
        P = M[np.ix_(perm, perm)]
        tri = upper_tri_tuple(P)
        if best_tri is None or tri < best_tri:
            best_tri = tri
            best_M = P
    assert best_M is not None
    return tuple(tuple(int(x) for x in row) for row in best_M)


def canonical_multiplicity(mult: Sequence[Sequence[int]] | np.ndarray) -> Multiplicity:
    """
    Exact canonical multiplicity matrix for n <= 8 (min-lex / degree refinement).

    For n > 8, returns the input matrix unchanged as a representative; use
    ``canonical_label`` which falls back to a deterministic hash id.
    """
    M = _as_array(mult)
    n = M.shape[0]
    if n == 0:
        return tuple()
    if n == 1:
        return ((0,),)
    if n > 8:
        return tuple(tuple(int(x) for x in row) for row in M)

    degs = weighted_degrees(M)
    from collections import defaultdict

    buckets: dict[int, list[int]] = defaultdict(list)
    for v, d in enumerate(degs):
        buckets[d].append(v)

    sizes = [len(buckets[d]) for d in buckets]
    from math import prod

    if prod(math_factorial(s) for s in sizes) <= 40320 or n <= 8:
        verts_by_deg = [buckets[d] for d in sorted(buckets)]
        best_tri: tuple[int, ...] | None = None
        best_M: np.ndarray | None = None

        def rec(i: int, acc: list[int]) -> None:
            nonlocal best_tri, best_M
            if i == len(verts_by_deg):
                perm = tuple(acc)
                P = M[np.ix_(perm, perm)]
                tri = upper_tri_tuple(P)
                if best_tri is None or tri < best_tri:
                    best_tri = tri
                    best_M = P
                return
            for p in permutations(verts_by_deg[i]):
                acc.extend(p)
                rec(i + 1, acc)
                del acc[-len(p) :]

        rec(0, [])
        assert best_M is not None
        return tuple(tuple(int(x) for x in row) for row in best_M)

    return brute_force_canonical(M)


def math_factorial(k: int) -> int:
    r = 1
    for i in range(2, k + 1):
        r *= i
    return r


def canonical_label(mult: Sequence[Sequence[int]] | np.ndarray) -> str:
    """
    Stable string id.

    Exact min-lex upper triangle for n <= 8; for larger n a deterministic
    multiplicity fingerprint (sorted degrees + sorted edge multiset + local
    incident weights) — sufficient for caching keys, not a full Aut certificate.
    """
    M = _as_array(mult)
    n = M.shape[0]
    if n <= 8:
        C = canonical_multiplicity(M)
        tri = upper_tri_tuple(np.asarray(C, dtype=int))
        return "M[" + ",".join(str(x) for x in tri) + "]"

    degs = tuple(sorted(weighted_degrees(M)))
    weights = tuple(
        sorted(int(M[i, j]) for i in range(n) for j in range(i + 1, n) if M[i, j])
    )
    local = tuple(
        sorted(
            tuple(sorted(int(M[i, j]) for j in range(n) if j != i and M[i, j]))
            for i in range(n)
        )
    )
    return f"F[{degs}|{weights}|{local}]"


def are_isomorphic(
    m1: Sequence[Sequence[int]] | np.ndarray,
    m2: Sequence[Sequence[int]] | np.ndarray,
) -> bool:
    return canonical_label(m1) == canonical_label(m2)

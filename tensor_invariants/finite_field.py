"""Finite-field arithmetic helpers for modular invariant discovery."""

from __future__ import annotations

import math
from typing import Iterable

# Large primes for discovery (disjoint from validation set).
DEFAULT_DISCOVERY_PRIMES: tuple[int, ...] = (
    1_000_003,
    1_000_033,
    1_000_037,
)

# Validation primes — at least one never used in discovery.
DEFAULT_VALIDATION_PRIMES: tuple[int, ...] = (
    1_000_039,
    1_000_081,
    1_000_151,
)


def is_prime(n: int) -> bool:
    """Deterministic Miller–Rabin-free trial division (sufficient for our sizes)."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def mod_inv(a: int, p: int) -> int:
    """Multiplicative inverse of ``a`` modulo prime ``p``."""
    a %= p
    if a == 0:
        raise ZeroDivisionError(f"no inverse of 0 mod {p}")
    # Extended Euclidean algorithm
    t, new_t = 0, 1
    r, new_r = p, a
    while new_r != 0:
        q = r // new_r
        t, new_t = new_t, t - q * new_t
        r, new_r = new_r, r - q * new_r
    if r > 1:
        raise ZeroDivisionError(f"{a} not invertible mod {p}")
    return t % p


def mod_pow(base: int, exp: int, p: int) -> int:
    return pow(base % p, exp, p)


def reduce_matrix(matrix: Iterable[Iterable[int]], p: int) -> list[list[int]]:
    """Reduce an integer matrix modulo ``p`` into nested lists."""
    return [[int(x) % p for x in row] for row in matrix]


def assert_primes_disjoint(
    discovery: Iterable[int] = DEFAULT_DISCOVERY_PRIMES,
    validation: Iterable[int] = DEFAULT_VALIDATION_PRIMES,
) -> None:
    d, v = set(discovery), set(validation)
    overlap = d & v
    if overlap:
        raise ValueError(f"discovery/validation primes overlap: {sorted(overlap)}")
    for q in d | v:
        if not is_prime(q):
            raise ValueError(f"non-prime in prime list: {q}")


def next_prime(n: int) -> int:
    """Smallest prime strictly greater than ``n``."""
    cand = n + 1 + (n % 2 == 0)
    if cand < 2:
        cand = 2
    while not is_prime(cand):
        cand += 1 if cand == 2 else 2
    return cand


def gcd_int(a: int, b: int) -> int:
    return math.gcd(a, b)

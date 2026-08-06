"""
Weighted-degree monomial bases in previously accepted generators.

At degree N, every monomial whose generator-degree weights sum to N must appear
in P_N. Example before degree 8 with generators of degrees 2,4,4,6:

  (x2)^4, (x2)^2 x4_1, (x2)^2 x4_2, (x4_1)^2, x4_1 x4_2, (x4_2)^2, x2 x6
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Sequence


@dataclass(frozen=True)
class NamedGenerator:
    name: str
    degree: int
    evaluate: Callable[[object], float]


@dataclass(frozen=True)
class Monomial:
    """Multiset of generator indices (nondecreasing)."""

    factors: tuple[int, ...]
    degree: int
    name: str

    def evaluate(self, values: Sequence[float]) -> float:
        p = 1.0
        for i in self.factors:
            p *= float(values[i])
        return p


def weighted_monomials(generators: Sequence[NamedGenerator], target_degree: int) -> list[Monomial]:
    """All products of generators whose degrees sum to ``target_degree``."""
    out: list[Monomial] = []
    n = len(generators)

    def rec(start: int, rem: int, acc: list[int]) -> None:
        if rem == 0:
            factors = tuple(acc)
            parts = [generators[i].name for i in factors]
            # Compact name: count repeats
            name = "*".join(parts) if parts else "1"
            out.append(Monomial(factors=factors, degree=target_degree, name=name))
            return
        for i in range(start, n):
            d = generators[i].degree
            if d > rem:
                continue
            acc.append(i)
            rec(i, rem - d, acc)
            acc.pop()

    if generators:
        rec(0, target_degree, [])
    return out


def evaluate_monomial_row(
    generators: Sequence[NamedGenerator],
    monomials: Sequence[Monomial],
    tensor: object,
) -> list[float]:
    values = [g.evaluate(tensor) for g in generators]
    return [m.evaluate(values) for m in monomials]


def expected_degree8_monomial_names() -> list[str]:
    """Paper / requirements checklist for P_8 with gens {x2, x4_1, x4_2, x6}."""
    return [
        "x^(2)*x^(2)*x^(2)*x^(2)",
        "x^(2)*x^(2)*x^(4)_1",
        "x^(2)*x^(2)*x^(4)_2",
        "x^(4)_1*x^(4)_1",
        "x^(4)_1*x^(4)_2",
        "x^(4)_2*x^(4)_2",
        "x^(2)*x^(6)",
    ]

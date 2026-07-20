"""
Practice ladder: blind rediscovery of known ingredient counts.

Curriculum (your idea):
  Level 1 — vector length²          → expect 1
  Level 2 — antisymmetric 2-form 4D → expect 2
  Level 3 — will later plug in 6D 3-form discovery

No neural net yet. This is the search+redundancy engine AlphaGo-style systems
need underneath a future "policy network."
"""

from __future__ import annotations

import numpy as np

from .discover import Candidate, discover_independent, grade


# ---------------------------------------------------------------------------
# Level 1: vector in 3D — only ingredient is v·v
# ---------------------------------------------------------------------------


def random_vector(rng: np.random.Generator, dim: int = 3) -> np.ndarray:
    return rng.uniform(-1.0, 1.0, size=(dim,))


def vector_candidates() -> list[Candidate]:
    # Include a rewrite so discovery must prune duplicates.
    def q(v):
        return float(np.dot(v, v))

    def q2(v):
        return float(np.dot(v, v) ** 2)

    return [
        Candidate("v·v", 2, q),
        Candidate("(v·v)^2", 4, q2),  # should be dropped (= product of v·v)
    ]


# ---------------------------------------------------------------------------
# Level 2: antisymmetric 2-form in 4D — expect floor(4/2)=2 ingredients
#   classic: tr(F^2), tr(F^4)  (same spirit as Maxwell invariants)
# ---------------------------------------------------------------------------


def random_two_form(rng: np.random.Generator, dim: int = 4) -> np.ndarray:
    raw = rng.uniform(-1.0, 1.0, size=(dim, dim))
    F = raw - raw.T  # antisymmetrize
    return F


def two_form_candidates() -> list[Candidate]:
    def tr2(F):
        return float(np.trace(F @ F))

    def tr4(F):
        return float(np.trace(F @ F @ F @ F))

    def tr6(F):
        return float(np.trace(F @ F @ F @ F @ F @ F))

    def tr2_sq(F):
        t = float(np.trace(F @ F))
        return t * t

    def tr8(F):
        M = F
        for _ in range(7):
            M = M @ F
        return float(np.trace(M))

    return [
        Candidate("tr(F^2)", 2, tr2),
        Candidate("tr(F^4)", 4, tr4),
        Candidate("tr(F^6)", 6, tr6),
        Candidate("[tr(F^2)]^2", 4, tr2_sq),
        Candidate("tr(F^8)", 8, tr8),
    ]


def run_ladder(seed: int = 0) -> list[dict]:
    reports = []

    # Level 1
    r1 = discover_independent(
        vector_candidates(), random_vector, max_order=4, seed=seed
    )
    r1 = grade(r1, expected_count=1, name="L1: vector (expect 1)")
    reports.append(r1.__dict__)

    # Level 2
    r2 = discover_independent(
        two_form_candidates(), random_two_form, max_order=8, seed=seed + 17
    )
    r2 = grade(r2, expected_count=2, name="L2: 2-form in 4D (expect 2)")
    reports.append(r2.__dict__)

    return reports

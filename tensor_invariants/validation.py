"""Scientific validation helpers with discovery/validation data separation."""

from __future__ import annotations

from typing import Callable, Sequence

import numpy as np

from .antisymmetric_tensors import (
    antisymmetry_error,
    random_antisymmetric_form,
    transform_orthogonal,
)
from .finite_field import DEFAULT_VALIDATION_PRIMES
from .graph_canonicalization import brute_force_canonical, canonical_multiplicity
from .graph_enumeration import ContractionGraph, enumerate_contraction_graphs
from .nullspace import rank_mod_p
from .numerical_rank import rational_rank, svd_rank
from .contraction_compiler import make_evaluator
from .contraction_evaluator import evaluate_nested_loops


def check_antisymmetry(dim: int = 6, p: int = 3, seed: int = 0) -> dict:
    rng = np.random.default_rng(seed)
    H = random_antisymmetric_form(dim, p, rng, mode="float")
    return {"max_error": antisymmetry_error(H), "pass": antisymmetry_error(H) < 1e-12}


def check_graph_relabeling_invariance(
    graph: ContractionGraph, tensor: np.ndarray, n_perms: int = 5, seed: int = 0
) -> dict:
    """Permuting vertex labels must not change the contraction value."""
    from itertools import permutations
    import random as pyrandom

    rng = pyrandom.Random(seed)
    _, ev0 = make_evaluator(graph)
    base = float(ev0(tensor))
    n = graph.n_vertices
    M = np.asarray(graph.multiplicity, dtype=int)
    errs = []
    all_perms = list(permutations(range(n)))
    for perm in rng.sample(all_perms, min(n_perms, len(all_perms))):
        P = M[np.ix_(perm, perm)]
        g2 = ContractionGraph(
            multiplicity=tuple(tuple(int(x) for x in row) for row in P),
            form_rank=graph.form_rank,
        )
        _, ev = make_evaluator(g2)
        errs.append(abs(float(ev(tensor)) - base))
    return {"max_error": max(errs) if errs else 0.0, "pass": all(e < 1e-8 for e in errs)}


def check_canonicalizers_agree(max_n: int = 6, form_rank: int = 3) -> dict:
    mismatches = []
    for n in range(2, max_n + 1, 2):
        enum = enumerate_contraction_graphs(n, form_rank)
        for g in enum["graphs"]:
            a = canonical_multiplicity(g.multiplicity)
            b = brute_force_canonical(g.multiplicity)
            if a != b:
                mismatches.append({"n": n, "id": g.canonical_id})
    return {"mismatches": mismatches, "pass": len(mismatches) == 0}


def check_einsum_vs_loops(seed: int = 0) -> dict:
    rng = np.random.default_rng(seed)
    H = random_antisymmetric_form(6, 3, rng)
    enum = enumerate_contraction_graphs(2, 3)
    g = enum["graphs"][0]
    v1 = make_evaluator(g)[1](H)
    v2 = evaluate_nested_loops(g, H)
    return {"einsum": v1, "loops": v2, "pass": abs(v1 - v2) < 1e-8}


def check_rank_backends() -> dict:
    M = np.array([[1, 2, 3], [2, 4, 6], [1, 0, 1]], dtype=object)
    svd = svd_rank(np.asarray(M, dtype=float))
    rat = rational_rank(M)
    mods = {p: rank_mod_p(M, p) for p in (97, 101, 100003)}
    return {
        "svd": svd,
        "rational": rat,
        "mod": mods,
        "pass": rat == 2 and svd == 2 and all(v == 2 for v in mods.values()),
    }


def check_orthogonal_invariance(seed: int = 0, n_graphs: int = 3) -> dict:
    rng = np.random.default_rng(seed)
    # Random orthogonal Q via QR
    A = rng.normal(size=(6, 6))
    Q, _ = np.linalg.qr(A)
    H = random_antisymmetric_form(6, 3, rng)
    Hp = transform_orthogonal(H, Q)
    enum = enumerate_contraction_graphs(4, 3)
    errs = []
    for g in enum["graphs"][:n_graphs]:
        ev = make_evaluator(g)[1]
        errs.append(abs(float(ev(H)) - float(ev(Hp))))
    return {"max_error": max(errs) if errs else 0.0, "pass": all(e < 1e-7 for e in errs)}


def check_fresh_sample_relation(
    discover_fn: Callable[[], np.ndarray],
    validate_fn: Callable[[np.ndarray], float],
) -> dict:
    """
    discover_fn returns a coefficient vector from discovery data;
    validate_fn evaluates residual on a fresh tensor.
    """
    coeffs = discover_fn()
    # Caller supplies validation — placeholder API
    return {"coeffs": coeffs.tolist() if hasattr(coeffs, "tolist") else list(coeffs)}


def check_prime_consistency(matrix: np.ndarray, primes: Sequence[int] = DEFAULT_VALIDATION_PRIMES) -> dict:
    ranks = {int(p): rank_mod_p(matrix, int(p)) for p in primes}
    return {"ranks": ranks, "pass": len(set(ranks.values())) == 1}

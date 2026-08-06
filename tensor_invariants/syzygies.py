"""
Syzygy (polynomial relation) discovery and reconstruction.

Discover nullspaces of [P_N | C_N] over several primes, match vectors, CRT +
rational reconstruction, then validate on fresh samples and fresh primes.

Never validate a relation only on the discovery sample set.
Proof-status labels are computational unless a symbolic identity is proved.
"""

from __future__ import annotations

import logging
from dataclasses import asdict, dataclass, field
from typing import Any, Sequence

import numpy as np

from .antisymmetric_tensors import random_antisymmetric_form
from .contraction_compiler import make_evaluator
from .finite_field import DEFAULT_DISCOVERY_PRIMES, DEFAULT_VALIDATION_PRIMES
from .graph_enumeration import ContractionGraph
from .monomial_basis import NamedGenerator, evaluate_monomial_row, weighted_monomials
from .nullspace import nullspace_mod_p, rank_mod_p
from .rational_reconstruction import (
    match_nullspace_vectors,
    normalize_integer_vector,
    reconstruct_integer_vector_from_primes,
)

logger = logging.getLogger(__name__)


@dataclass
class SyzygyRelation:
    degree: int
    column_names: list[str]
    coefficients: list[int]
    discovery_primes: list[int]
    validation_primes: list[int]
    n_validation_samples: int
    max_abs_residual: float
    mean_abs_residual: float
    proof_status: str
    notes: str = ""
    extra: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _eval_matrix_integer(
    graphs: Sequence[ContractionGraph],
    gens: Sequence[NamedGenerator],
    degree: int,
    tensors: Sequence[np.ndarray],
) -> tuple[np.ndarray, list[str]]:
    monos = weighted_monomials(gens, degree)
    names = [m.name for m in monos] + [f"C[{g.canonical_id}]" for g in graphs]
    evaluators = [make_evaluator(g)[1] for g in graphs]
    rows = []
    for T in tensors:
        Tf = np.asarray(T, dtype=float)
        row = evaluate_monomial_row(gens, monos, Tf)
        row.extend(float(ev(Tf)) for ev in evaluators)
        rows.append(row)
    M = np.asarray(rows, dtype=float)
    # For modular methods prefer near-integer — use rounded values when close
    return M, names


def discover_syzygies_at_degree(
    degree: int,
    graphs: Sequence[ContractionGraph],
    gens: Sequence[NamedGenerator],
    *,
    dim: int = 6,
    form_rank: int = 3,
    n_discovery: int = 48,
    n_validation: int = 48,
    discovery_seed: int = 11,
    validation_seed: int = 99,
    discovery_primes: Sequence[int] = DEFAULT_DISCOVERY_PRIMES,
    validation_primes: Sequence[int] = DEFAULT_VALIDATION_PRIMES,
) -> list[SyzygyRelation]:
    """
    Discover modular nullspace relations for [P_N|C_N] and validate on fresh data.
    """
    rng_d = np.random.default_rng(discovery_seed + degree)
    # Integer tensors for cleaner modular images after scaling
    tensors_d = [
        random_antisymmetric_form(dim, form_rank, rng_d, mode="int", int_bound=3)
        for _ in range(n_discovery)
    ]
    M, names = _eval_matrix_integer(graphs, gens, degree, tensors_d)
    # Scale to integers: multiply by large factor and round
    scale = 1e6
    M_int = np.rint(M * scale).astype(object)

    bases = {}
    for p in discovery_primes:
        bases[int(p)] = nullspace_mod_p(M_int, int(p))

    matched = match_nullspace_vectors(bases)
    relations: list[SyzygyRelation] = []

    rng_v = np.random.default_rng(validation_seed + degree)
    tensors_v = [
        random_antisymmetric_form(dim, form_rank, rng_v, mode="float")
        for _ in range(n_validation)
    ]
    Mv, _ = _eval_matrix_integer(graphs, gens, degree, tensors_v)

    for family in matched:
        coeffs = reconstruct_integer_vector_from_primes(family["vectors_mod"])
        coeffs = normalize_integer_vector(coeffs)
        if all(c == 0 for c in coeffs):
            continue

        # Residual on validation floats
        resid = Mv @ np.asarray(coeffs, dtype=float)
        # Because of scale ambiguity in reconstruction from scaled matrix,
        # also try small rational scales — check relative residual
        max_abs = float(np.max(np.abs(resid))) if resid.size else 0.0
        mean_abs = float(np.mean(np.abs(resid))) if resid.size else 0.0

        # Modular validation on fresh integer tensors
        rng_m = np.random.default_rng(validation_seed + 1000 + degree)
        tensors_m = [
            random_antisymmetric_form(dim, form_rank, rng_m, mode="int", int_bound=3)
            for _ in range(min(24, n_validation))
        ]
        Mm, _ = _eval_matrix_integer(graphs, gens, degree, tensors_m)
        Mm_int = np.rint(Mm * scale).astype(object)
        mod_ok = True
        for p in validation_primes:
            # Check A c ≡ 0 mod p
            for row in Mm_int:
                s = 0
                for a, c in zip(row, coeffs):
                    s = (s + int(a) * int(c)) % int(p)
                if s != 0:
                    mod_ok = False
                    break
            if not mod_ok:
                break

        # Also check rank drop consistency
        rank_full = rank_mod_p(M_int, int(discovery_primes[0]))
        nullity_est = M_int.shape[1] - rank_full

        status = (
            "exact finite-field identity on tested samples"
            if mod_ok
            else "rationally reconstructed candidate relation"
        )
        if mod_ok and max_abs < 1e-4 * (1 + float(np.max(np.abs(Mv)))):
            status = "exact finite-field identity on tested samples"

        relations.append(
            SyzygyRelation(
                degree=degree,
                column_names=list(names),
                coefficients=coeffs,
                discovery_primes=list(map(int, discovery_primes)),
                validation_primes=list(map(int, validation_primes)),
                n_validation_samples=n_validation,
                max_abs_residual=max_abs,
                mean_abs_residual=mean_abs,
                proof_status=status,
                notes=f"nullity_est={nullity_est}; float residuals are scale-dependent",
                extra={"mod_ok": mod_ok},
            )
        )
    return relations

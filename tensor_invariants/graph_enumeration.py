"""
Enumeration of connected loopless weighted multigraphs for p-form contractions.

Each vertex is one copy of an antisymmetric rank-``form_rank`` tensor.
Edge weight A_ij = number of contracted index pairs between tensors i and j.
Every vertex satisfies weighted degree form_rank:

    sum_{j != i} A_ij = form_rank,   A_ii = 0,   A_ij = A_ji >= 0.

For a 3-form the expected connected non-isomorphic counts are:
N=2 → 1, N=4 → 2, N=6 → 6, N=8 → 20.

Deduplication during search uses a multiplicity fingerprint + NetworkX
weighted-multigraph isomorphism (edge keys = parallel edges). Exact min-lex
canonical labels are computed only for the retained unique graphs.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Any

import networkx as nx
import numpy as np

from .graph_canonicalization import canonical_label, is_connected, weighted_degrees


@dataclass(frozen=True)
class ContractionGraph:
    """Undirected weighted multigraph encoded by a symmetric multiplicity matrix."""

    multiplicity: tuple[tuple[int, ...], ...]
    form_rank: int

    @property
    def n_vertices(self) -> int:
        return len(self.multiplicity)

    @property
    def canonical_id(self) -> str:
        return canonical_label(self.multiplicity)

    def edge_list(self) -> list[tuple[int, int, int]]:
        edges: list[tuple[int, int, int]] = []
        n = self.n_vertices
        for i in range(n):
            for j in range(i + 1, n):
                w = self.multiplicity[i][j]
                if w:
                    edges.append((i, j, w))
        return edges

    def degrees(self) -> list[int]:
        return weighted_degrees(self.multiplicity)

    def to_networkx(self) -> nx.MultiGraph:
        return _as_nx([list(row) for row in self.multiplicity])


def _fingerprint(mult: list[list[int]]) -> tuple:
    n = len(mult)
    degs = tuple(sorted(weighted_degrees(mult)))
    weights = tuple(
        sorted(mult[i][j] for i in range(n) for j in range(i + 1, n) if mult[i][j])
    )
    local = []
    for i in range(n):
        local.append(tuple(sorted(mult[i][j] for j in range(n) if j != i and mult[i][j])))
    return degs, weights, tuple(sorted(local))


def _as_nx(mult: list[list[int]]) -> nx.MultiGraph:
    n = len(mult)
    G = nx.MultiGraph()
    G.add_nodes_from(range(n))
    for i, j in combinations(range(n), 2):
        for _ in range(mult[i][j]):
            G.add_edge(i, j)
    return G


def enumerate_contraction_graphs(
    n_vertices: int,
    form_rank: int,
    *,
    connected_only: bool = True,
) -> dict[str, Any]:
    """
    Exact backtracking enumeration with isomorphism deduplication.

    Edge multiplicities are never discarded.
    """
    empty: dict[str, Any] = {
        "n_vertices": n_vertices,
        "form_rank": form_rank,
        "raw_assignments": 0,
        "connected_count": 0,
        "nonisomorphic_count": 0,
        "graphs": [],
        "canonical_ids": [],
    }
    if n_vertices < 1:
        return empty
    if (n_vertices * form_rank) % 2 != 0:
        empty["note"] = "impossible by handshaking lemma"
        return empty

    n = n_vertices
    mult = [[0] * n for _ in range(n)]
    raw = 0
    connected_count = 0
    unique: list[ContractionGraph] = []
    unique_nx: list[nx.MultiGraph] = []
    unique_fp: list[tuple] = []

    def consider() -> None:
        nonlocal connected_count
        degs = weighted_degrees(mult)
        if any(d != form_rank for d in degs):
            return
        if connected_only and n > 1 and not is_connected(mult):
            return
        connected_count += 1
        fp = _fingerprint(mult)
        Gnx = _as_nx(mult)
        for H, hfp in zip(unique_nx, unique_fp):
            if hfp != fp:
                continue
            if nx.is_isomorphic(Gnx, H):
                return
        M = tuple(tuple(row) for row in mult)
        unique.append(ContractionGraph(multiplicity=M, form_rank=form_rank))
        unique_nx.append(Gnx)
        unique_fp.append(fp)

    def rec(v: int) -> None:
        nonlocal raw
        if v == n:
            raw += 1
            consider()
            return

        need = form_rank - sum(mult[v][u] for u in range(v))
        if need < 0:
            return
        partners = list(range(v + 1, n))

        def assign(k: int, left: int) -> None:
            if left == 0:
                rec(v + 1)
                return
            if k == len(partners):
                return
            j = partners[k]
            used_j = sum(mult[j][u] for u in range(j))
            max_m = min(left, form_rank - used_j, form_rank)
            for m in range(max_m + 1):
                if m:
                    mult[v][j] = mult[j][v] = m
                assign(k + 1, left - m)
                if m:
                    mult[v][j] = mult[j][v] = 0

        if need == 0:
            rec(v + 1)
        elif not partners:
            return
        else:
            assign(0, need)

    rec(0)
    # Exact canonical ids only for survivors (n<=8 exact min-lex)
    ids = [g.canonical_id for g in unique]
    return {
        "n_vertices": n_vertices,
        "form_rank": form_rank,
        "raw_assignments": raw,
        "connected_count": connected_count,
        "nonisomorphic_count": len(unique),
        "graphs": unique,
        "canonical_ids": ids,
    }


def sample_contraction_graphs(
    n_vertices: int,
    form_rank: int,
    *,
    target: int = 60,
    seed: int = 0,
    max_attempts: int = 100_000,
    connected_only: bool = True,
) -> list[ContractionGraph]:
    """Random stub-matching search for distinct form_rank-regular multigraphs."""
    rng = np.random.default_rng(seed)
    n = n_vertices
    unique: list[ContractionGraph] = []
    unique_nx: list[nx.MultiGraph] = []
    unique_fp: list[tuple] = []
    attempts = 0
    while len(unique) < target and attempts < max_attempts:
        attempts += 1
        stubs: list[int] = []
        for v in range(n):
            stubs.extend([v] * form_rank)
        rng.shuffle(stubs)
        mult = [[0] * n for _ in range(n)]
        ok = True
        for a in range(0, len(stubs), 2):
            u, v = stubs[a], stubs[a + 1]
            if u == v:
                ok = False
                break
            i, j = (u, v) if u < v else (v, u)
            mult[i][j] += 1
            mult[j][i] += 1
            if mult[i][j] > form_rank:
                ok = False
                break
        if not ok:
            continue
        if any(d != form_rank for d in weighted_degrees(mult)):
            continue
        if connected_only and n > 1 and not is_connected(mult):
            continue
        fp = _fingerprint(mult)
        Gnx = _as_nx(mult)
        dup = False
        for H, hfp in zip(unique_nx, unique_fp):
            if hfp != fp:
                continue
            if nx.is_isomorphic(Gnx, H):
                dup = True
                break
        if dup:
            continue
        M = tuple(tuple(row) for row in mult)
        unique.append(ContractionGraph(multiplicity=M, form_rank=form_rank))
        unique_nx.append(Gnx)
        unique_fp.append(fp)
    return unique


EXPECTED_CONNECTED_COUNTS_3FORM = {2: 1, 4: 2, 6: 6, 8: 20}

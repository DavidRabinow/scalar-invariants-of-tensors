"""
6D degree ladder discovery: evaluate contraction graphs and extract independent
invariants (numerical SVD), with live progress — the work that actually "finds
answers" beyond mere graph counting.
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Callable

import numpy as np

from invariants.contraction import make_evaluator
from invariants.graphs import ContractionGraph, enumerate_contraction_graphs
from invariants.three_form_6d import paper_generators, random_three_form
from invariants.utils import numerical_rank

from .paths import RESEARCH_STATE, ensure_state_dirs


EXPECTED_GRAPH_COUNTS = {2: 1, 4: 2, 6: 6, 8: 20}
# Paper HSOP independence pattern at orders 2,4,6,8
EXPECTED_NEW_GENERATORS = {2: 1, 4: 2, 6: 1, 8: 1}

CACHE_DIR = RESEARCH_STATE / "cache"


def _cache_path(n_vertices: int, form_rank: int) -> Path:
    return CACHE_DIR / f"graphs_N{n_vertices}_r{form_rank}.json"


def load_or_enumerate_graphs(
    n_vertices: int,
    form_rank: int = 3,
    *,
    progress: Callable[[str, dict[str, Any]], None] | None = None,
    force: bool = False,
    allow_sample: bool = False,
    sample_target: int = 120,
) -> dict[str, Any]:
    """Enumerate graphs, caching multiplicity matrices so N=8 is only computed once."""
    ensure_state_dirs()
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path = _cache_path(n_vertices, form_rank)
    if path.exists() and not force:
        data = json.loads(path.read_text(encoding="utf-8"))
        graphs = [
            ContractionGraph(
                multiplicity=tuple(tuple(row) for row in m),
                form_rank=form_rank,
            )
            for m in data["multiplicities"]
        ]
        if progress:
            progress(
                f"Loaded {len(graphs)} cached graphs for N={n_vertices}"
                + (" (sampled)" if data.get("sampled") else ""),
                {"stage": "cache_hit", "degree": n_vertices, "graph_count": len(graphs)},
            )
        return {
            "n_vertices": n_vertices,
            "form_rank": form_rank,
            "nonisomorphic_count": len(graphs),
            "graphs": graphs,
            "canonical_ids": [g.canonical_id for g in graphs],
            "from_cache": True,
            "sampled": bool(data.get("sampled")),
        }

    # For hard cases (5-regular N>=8), prefer sampling over exact enum that can
    # run for many hours with no cache output.
    if allow_sample or (form_rank >= 5 and n_vertices >= 8):
        from invariants.graphs import sample_contraction_graphs

        if progress:
            progress(
                f"Sampling graphs at N={n_vertices} (exact enum too slow)…",
                {"stage": "sample", "degree": n_vertices},
            )
        enum = sample_contraction_graphs(
            n_vertices,
            form_rank,
            target=sample_target,
            seed=n_vertices * 17 + form_rank,
            progress=progress,
        )
        payload = {
            "n_vertices": n_vertices,
            "form_rank": form_rank,
            "nonisomorphic_count": enum["nonisomorphic_count"],
            "multiplicities": [g.multiplicity for g in enum["graphs"]],
            "canonical_ids": enum.get("canonical_ids", [g.canonical_id for g in enum["graphs"]]),
            "sampled": True,
            "attempts": enum.get("attempts"),
        }
        path.write_text(json.dumps(payload), encoding="utf-8")
        enum["from_cache"] = False
        return enum

    if progress:
        progress(
            f"Enumerating graphs at N={n_vertices} (will cache)…",
            {"stage": "enum", "degree": n_vertices},
        )
    enum = enumerate_contraction_graphs(n_vertices, form_rank=form_rank)
    payload = {
        "n_vertices": n_vertices,
        "form_rank": form_rank,
        "nonisomorphic_count": enum["nonisomorphic_count"],
        "multiplicities": [g.multiplicity for g in enum["graphs"]],
        "canonical_ids": enum.get("canonical_ids", [g.canonical_id for g in enum["graphs"]]),
        "sampled": False,
    }
    path.write_text(json.dumps(payload), encoding="utf-8")
    enum["from_cache"] = False
    return enum


def discover_at_degree(
    n_vertices: int,
    *,
    n_draws: int = 48,
    seed: int = 0,
    form_rank: int = 3,
    progress: Callable[[str, dict[str, Any]], None] | None = None,
    cancel: Callable[[], bool] | None = None,
    use_cache: bool = True,
) -> dict[str, Any]:
    """
    Enumerate (or load cached) graphs at N=n_vertices, evaluate on random 3-forms,
    and greedily keep columns that increase numerical rank.
    """
    if cancel and cancel():
        return {"cancelled": True}

    t0 = time.time()
    if use_cache:
        enum = load_or_enumerate_graphs(
            n_vertices, form_rank, progress=progress
        )
    else:
        if progress:
            progress(
                f"Enumerating graphs at N={n_vertices}",
                {"stage": "enum", "degree": n_vertices},
            )
        enum = enumerate_contraction_graphs(n_vertices, form_rank=form_rank)
        enum["from_cache"] = False

    graphs = enum["graphs"]
    if progress:
        progress(
            f"N={n_vertices}: {enum['nonisomorphic_count']} canonical graphs; evaluating…",
            {
                "stage": "eval",
                "degree": n_vertices,
                "graph_count": enum["nonisomorphic_count"],
                "from_cache": enum.get("from_cache"),
            },
        )

    rng = np.random.default_rng(seed + n_vertices)
    evaluators = []
    ids = []
    max_graphs = None
    # Cap N=8 evaluators if requested (full 20 × many draws can OOM/SIGKILL).
    if n_vertices >= 8:
        # Prefer evaluating all 20 with very few draws; caller sets n_draws small.
        max_graphs = None

    for gi, g in enumerate(graphs):
        if cancel and cancel():
            return {"cancelled": True}
        if max_graphs is not None and gi >= max_graphs:
            break
        try:
            if progress and n_vertices >= 8:
                progress(
                    f"N={n_vertices}: compile graph {gi + 1}/{len(graphs)}",
                    {"stage": "compile", "degree": n_vertices, "completed": gi + 1, "total": len(graphs)},
                )
            _, ev = make_evaluator(g)
            evaluators.append(ev)
            ids.append(g.canonical_id)
        except Exception as exc:  # noqa: BLE001
            if progress:
                progress(f"Skip graph {g.canonical_id}: {exc}", {"stage": "eval_skip"})

    n_g = len(evaluators)
    mat = np.zeros((n_draws, n_g), dtype=float)
    for i in range(n_draws):
        if cancel and cancel():
            return {"cancelled": True}
        H = random_three_form(rng)
        for j, ev in enumerate(evaluators):
            try:
                mat[i, j] = float(ev(H))
            except Exception:
                mat[i, j] = 0.0
            if progress and n_vertices >= 8 and (j + 1) % 5 == 0:
                progress(
                    f"N={n_vertices}: draw {i + 1}/{n_draws}, graph {j + 1}/{n_g}",
                    {
                        "stage": "sample",
                        "degree": n_vertices,
                        "completed": i * n_g + j + 1,
                        "total": n_draws * n_g,
                    },
                )
        if progress and (i + 1) % max(1, n_draws // 4) == 0:
            progress(
                f"N={n_vertices}: sample {i + 1}/{n_draws}",
                {
                    "stage": "sample",
                    "degree": n_vertices,
                    "completed": i + 1,
                    "total": n_draws,
                },
            )

    # Greedy column selection by order (all graphs at this N share order = n_vertices
    # for a 3-form? Actually each vertex is one H, so polynomial degree in H is N.
    order = n_vertices
    # Without lower products first: linear independence among graph columns
    kept_idx: list[int] = []
    for j in range(n_g):
        cols = [mat[:, k] for k in kept_idx] + [mat[:, j]]
        base = np.column_stack([mat[:, k] for k in kept_idx]) if kept_idx else np.zeros((n_draws, 0))
        trial = np.column_stack(cols)
        if numerical_rank(trial, tol=None) > numerical_rank(base, tol=None):
            kept_idx.append(j)

    singular = []
    if mat.size:
        try:
            singular = np.linalg.svd(mat, compute_uv=False).tolist()[:12]
        except Exception:
            singular = []

    elapsed = time.time() - t0
    return {
        "n_vertices": n_vertices,
        "order": order,
        "graph_count": enum["nonisomorphic_count"],
        "expected_graph_count": EXPECTED_GRAPH_COUNTS.get(n_vertices),
        "graph_count_ok": enum["nonisomorphic_count"] == EXPECTED_GRAPH_COUNTS.get(n_vertices),
        "evaluated": n_g,
        "n_draws": n_draws,
        "linear_rank": len(kept_idx),
        "selected_ids": [ids[j] for j in kept_idx],
        "all_ids": ids[:40],
        "singular_values": [float(x) for x in singular],
        "elapsed_sec": elapsed,
        "expected_new_generators": EXPECTED_NEW_GENERATORS.get(n_vertices),
    }


def verify_paper_generators(
    *, n_draws: int = 40, seed: int = 1
) -> dict[str, Any]:
    """Confirm the known 5 paper generators are independent (6D answer key check)."""
    gens = paper_generators()
    rng = np.random.default_rng(seed)
    mat = np.zeros((n_draws, len(gens)))
    for i in range(n_draws):
        H = random_three_form(rng)
        for j, g in enumerate(gens):
            mat[i, j] = g.fn(H)
    rank = numerical_rank(mat, tol=None)
    return {
        "names": [g.name for g in gens],
        "orders": [g.order for g in gens],
        "rank": int(rank),
        "expected_rank": 5,
        "ok": int(rank) >= 5,
    }

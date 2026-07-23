"""
10D chiral 5-form discovery stages for the autonomous engine.

Climb path:
  sanity → optional light low-order → N=2 enum → automatic graph discovery
  at N=4 then N=6 (Lorentzian einsum, intermediate cap) → chunked catalog fill.
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Callable

import numpy as np

from invariants.contraction import (
    LORENTZ_MODES,
    estimate_largest_intermediate,
    make_evaluator_lorentz,
)
from invariants.five_form_10d import (
    run_low_order_discovery,
    sanity_checks,
)
from invariants.hodge10 import (
    combo_to_dense,
    raise_dense,
    random_chiral_five_form_combo as random_chiral_five_form,
)
from invariants.timed_search import (
    _build_T_and_G,
    candidate_catalog,
    run_timed_search,
)
from invariants.utils import numerical_rank

from .ladder6d import load_or_enumerate_graphs


LITERATURE_TARGET = 81
DEFAULT_MAX_INTERMEDIATE = 5.0e7  # ~400 MB float64 peak; skips K6-scale graphs


def run_sanity(progress: Callable[[str, dict[str, Any]], None] | None = None) -> dict[str, Any]:
    if progress:
        progress("10D: chiral 5-form sanity checks…", {"stage": "sanity"})
    t0 = time.time()
    out = sanity_checks(seed=0)
    out["elapsed_sec"] = time.time() - t0
    return out


def run_low_order(
    *,
    n_draws: int = 8,
    seed: int = 1,
    progress: Callable[[str, dict[str, Any]], None] | None = None,
) -> dict[str, Any]:
    n_draws = max(2, min(int(n_draws), 12))
    if progress:
        progress(
            f"10D: light low-order discovery (n_draws={n_draws})…",
            {"stage": "low_order", "total": n_draws},
        )
    t0 = time.time()
    out = run_low_order_discovery(seed=seed, n_draws=n_draws)
    out["elapsed_sec"] = time.time() - t0
    return out


def enumerate_5regular(
    n_vertices: int,
    *,
    progress: Callable[[str, dict[str, Any]], None] | None = None,
) -> dict[str, Any]:
    if progress:
        progress(
            f"10D: enumerating 5-regular graphs at N={n_vertices}…",
            {"stage": "enum5", "degree": n_vertices},
        )
    t0 = time.time()
    enum = load_or_enumerate_graphs(n_vertices, form_rank=5, progress=progress)
    return {
        "n_vertices": n_vertices,
        "form_rank": 5,
        "nonisomorphic_count": enum["nonisomorphic_count"],
        "connected_count": enum.get("connected_count", enum["nonisomorphic_count"]),
        "canonical_ids": enum.get("canonical_ids", [])[:40],
        "elapsed_sec": time.time() - t0,
        "from_cache": enum.get("from_cache"),
    }


def run_catalog_search(
    *,
    duration_sec: float,
    progress_path: Path,
    n_draws: int = 24,
    seed: int = 7,
    progress: Callable[[str, dict[str, Any]], None] | None = None,
) -> dict[str, Any]:
    duration_sec = max(30.0, float(duration_sec))
    if progress:
        progress(
            f"10D: catalog timed search for {duration_sec:.0f}s…",
            {"stage": "catalog", "total": int(duration_sec)},
        )
    result = run_timed_search(
        duration_sec=duration_sec,
        progress_path=progress_path,
        n_draws=n_draws,
        seed=seed,
    )
    return {
        "found_count": result.found_count,
        "found": [
            {"name": f.name, "order": f.order, "id": f.id} for f in result.found
        ],
        "draws_used": result.draws_used,
        "elapsed_sec": result.elapsed_sec,
        "by_order": result.by_order,
        "target": LITERATURE_TARGET,
        "catalog_size": len(candidate_catalog()),
        "status": result.status,
        "message": result.message,
    }


def merge_catalog_best(prev: dict[str, Any] | None, new: dict[str, Any]) -> dict[str, Any]:
    if not prev:
        return dict(new)
    if int(new.get("found_count") or 0) >= int(prev.get("found_count") or 0):
        out = dict(new)
        out["chunks"] = int(prev.get("chunks") or 0) + 1
        out["total_draws"] = int(prev.get("total_draws") or 0) + int(new.get("draws_used") or 0)
        return out
    prev = dict(prev)
    prev["chunks"] = int(prev.get("chunks") or 0) + 1
    prev["total_draws"] = int(prev.get("total_draws") or 0) + int(new.get("draws_used") or 0)
    return prev


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _greedy_keep(
    values: np.ndarray,
    orders: list[int],
    names: list[str],
    *,
    tol: float = 1e-5,
) -> list[int]:
    """Keep columns that increase rank, processing low order first; include products."""
    n_cand = values.shape[1]
    order_sorted = sorted(range(n_cand), key=lambda i: (orders[i], i))
    kept: list[int] = []
    for j in order_sorted:
        col = values[:, j]
        if float(np.max(np.abs(col))) < tol:
            continue
        cols = [values[:, k] for k in kept]
        for a in range(len(kept)):
            for b in range(a, len(kept)):
                if orders[kept[a]] + orders[kept[b]] == orders[j]:
                    cols.append(values[:, kept[a]] * values[:, kept[b]])
        for a in range(len(kept)):
            for b in range(a, len(kept)):
                for c in range(b, len(kept)):
                    if (
                        orders[kept[a]] + orders[kept[b]] + orders[kept[c]]
                        == orders[j]
                    ):
                        cols.append(
                            values[:, kept[a]]
                            * values[:, kept[b]]
                            * values[:, kept[c]]
                        )
        base = np.column_stack(cols) if cols else np.zeros((values.shape[0], 0))
        trial = np.column_stack([base, col]) if base.size else col.reshape(-1, 1)
        if numerical_rank(trial, tol=None) > numerical_rank(base, tol=None):
            kept.append(j)
    return kept


def prefer_higher_count(
    prev: dict[str, Any] | None, new: dict[str, Any]
) -> dict[str, Any]:
    """Keep the stronger climb result so weak redraws cannot erase a best score."""
    if not prev:
        return dict(new)
    if int(new.get("found_count") or 0) >= int(prev.get("found_count") or 0):
        out = dict(new)
        out["prior_best_count"] = int(prev.get("found_count") or 0)
        return out
    held = dict(prev)
    held["stale_redraw_count"] = int(new.get("found_count") or 0)
    held["held_best"] = True
    return held


def discover_10d_graphs(
    *,
    degrees: list[int] | None = None,
    n_draws: int = 12,
    seed: int = 3,
    max_intermediate: float = DEFAULT_MAX_INTERMEDIATE,
    include_catalog: bool = True,
    lorentz_modes: list[str] | None = None,
    slot_policies: list[str] | None = None,
    sample_targets: dict[int, int] | dict[str, int] | None = None,
    dense_variants: bool = False,
    progress: Callable[[str, dict[str, Any]], None] | None = None,
    cancel: Callable[[], bool] | None = None,
) -> dict[str, Any]:
    """
    Automatic climb: catalog features + 5-regular graph scalars at given N,
    ranked jointly with product filtering.

    Uses multiple Lorentz raise-patterns and slot wirings to grow past a
    single-convention plateau.
    """
    degrees = list(degrees or [4, 6])
    # Default: richer modes for higher N where we plateaued.
    if lorentz_modes is None:
        lorentz_modes = ["alt", "half", "first", "last"]
    if slot_policies is None:
        slot_policies = ["pop", "pop0", "reverse"]
    targets: dict[int, int] = {}
    if sample_targets:
        targets = {int(k): int(v) for k, v in sample_targets.items()}
    t0 = time.time()
    names: list[str] = []
    orders: list[int] = []
    kinds: list[tuple[str, Any]] = []

    if include_catalog:
        for name, order, fn in candidate_catalog():
            names.append(f"cat:{name}")
            orders.append(int(order))
            kinds.append(("catalog", fn))

    skipped: list[dict[str, Any]] = []
    per_degree: dict[str, Any] = {}

    rng_probe = np.random.default_rng(seed)
    Td_probe = combo_to_dense(random_chiral_five_form(rng_probe))
    Tu_probe = raise_dense(Td_probe)

    for n in degrees:
        if cancel and cancel():
            return {"cancelled": True, "elapsed_sec": time.time() - t0}
        if progress:
            progress(
                f"10D: prepare graphs at N={n}…",
                {"stage": "graph_prep", "degree": n},
            )
        expand_to = targets.get(n)
        enum = load_or_enumerate_graphs(
            n,
            form_rank=5,
            progress=progress,
            expand_to=expand_to,
            sample_target=int(expand_to or 120),
        )
        graphs = enum["graphs"]
        kept_here = 0
        skipped_here = 0
        # Don't explode candidate count: richer variants only where they help.
        if n <= 4:
            modes, policies = ["alt"], ["pop"]
        elif n == 6:
            modes, policies = ["alt", "half", "first"], ["pop", "pop0"]
        elif n == 8:
            modes, policies = list(lorentz_modes), list(slot_policies)
        elif n == 10:
            modes, policies = ["alt", "half", "first"], ["pop", "pop0"]
        else:
            modes, policies = ["alt", "half"], ["pop", "pop0"]
        if dense_variants:
            modes = list(lorentz_modes)
            policies = list(slot_policies)
        for gi, g in enumerate(graphs):
            if cancel and cancel():
                return {"cancelled": True, "elapsed_sec": time.time() - t0}
            for mode in modes:
                for policy in policies:
                    # Mild thinning only — denser than the old plateau pass.
                    if not dense_variants:
                        if n >= 8 and policy != "pop" and (gi % 2) != 0:
                            continue
                        if n >= 8 and mode not in ("alt", "half") and (gi % 3) != 0:
                            continue
                        if n >= 12 and mode != "alt" and (gi % 2) != 0:
                            continue
                        if n >= 14 and (gi % 2) != 0:
                            continue
                    try:
                        li = estimate_largest_intermediate(
                            g, Td_probe, Tu_probe, mode=mode, slot_policy=policy
                        )
                    except Exception as exc:  # noqa: BLE001
                        skipped.append(
                            {
                                "id": g.canonical_id,
                                "reason": str(exc),
                                "n": n,
                                "mode": mode,
                                "policy": policy,
                            }
                        )
                        skipped_here += 1
                        continue
                    if li > max_intermediate:
                        skipped.append(
                            {
                                "id": g.canonical_id,
                                "reason": "intermediate_cap",
                                "largest_intermediate": li,
                                "n": n,
                                "mode": mode,
                                "policy": policy,
                            }
                        )
                        skipped_here += 1
                        continue
                    try:
                        _, ev = make_evaluator_lorentz(
                            g, mode=mode, slot_policy=policy
                        )
                    except Exception as exc:  # noqa: BLE001
                        skipped.append(
                            {
                                "id": g.canonical_id,
                                "reason": str(exc),
                                "n": n,
                                "mode": mode,
                                "policy": policy,
                            }
                        )
                        skipped_here += 1
                        continue
                    tag = f"G{n}:{g.canonical_id}:{mode}:{policy}"
                    names.append(tag)
                    orders.append(int(n))
                    kinds.append(("graph", ev))
                    kept_here += 1
            if progress and (gi + 1) % 10 == 0:
                progress(
                    f"10D: N={n} compiled {gi + 1}/{len(graphs)} "
                    f"(kept {kept_here}, skip {skipped_here})",
                    {
                        "stage": "graph_compile",
                        "degree": n,
                        "completed": gi + 1,
                        "total": len(graphs),
                    },
                )
        per_degree[str(n)] = {
            "graph_count": enum["nonisomorphic_count"],
            "evaluated": kept_here,
            "skipped": skipped_here,
            "from_cache": enum.get("from_cache"),
            "modes": modes,
            "policies": policies,
            "expanded": enum.get("expanded"),
        }

    n_cand = len(kinds)
    if n_cand == 0:
        return {
            "found_count": 0,
            "found": [],
            "n_draws": 0,
            "n_candidates": 0,
            "per_degree": per_degree,
            "skipped": skipped,
            "elapsed_sec": time.time() - t0,
            "target": LITERATURE_TARGET,
        }

    if progress:
        progress(
            f"10D: sampling {n_draws} chiral forms × {n_cand} candidates…",
            {"stage": "graph_sample", "total": n_draws},
        )

    rng = np.random.default_rng(seed + 17)
    values = np.zeros((n_draws, n_cand), dtype=float)
    for i in range(n_draws):
        if cancel and cancel():
            return {"cancelled": True, "elapsed_sec": time.time() - t0}
        F = random_chiral_five_form(rng)
        Td = combo_to_dense(F)
        Tu = raise_dense(Td)
        T, G, q = _build_T_and_G(F)
        for j, (kind, fn) in enumerate(kinds):
            try:
                if kind == "catalog":
                    values[i, j] = float(fn(T, G, q))
                else:
                    values[i, j] = float(fn(Td, Tu))
            except Exception:
                values[i, j] = 0.0
        values[i, :] = np.nan_to_num(values[i, :], nan=0.0, posinf=0.0, neginf=0.0)
        if progress and ((i + 1) % max(1, n_draws // 16) == 0 or i + 1 == n_draws or i == 0):
            progress(
                f"10D: sample {i + 1}/{n_draws}",
                {
                    "stage": "graph_sample",
                    "completed": i + 1,
                    "total": n_draws,
                },
            )

    kept_idx = _greedy_keep(values, orders, names)
    found = [
        {
            "name": names[j],
            "order": orders[j],
            "id": k + 1,
            "source": "catalog" if names[j].startswith("cat:") else "graph",
        }
        for k, j in enumerate(kept_idx)
    ]
    by_order: dict[str, int] = {}
    by_source = {"catalog": 0, "graph": 0}
    for item in found:
        by_order[str(item["order"])] = by_order.get(str(item["order"]), 0) + 1
        by_source[item["source"]] = by_source.get(item["source"], 0) + 1

    return {
        "found_count": len(found),
        "found": found,
        "by_order": by_order,
        "by_source": by_source,
        "n_draws": n_draws,
        "n_candidates": n_cand,
        "per_degree": per_degree,
        "skipped": skipped[:30],
        "skipped_total": len(skipped),
        "elapsed_sec": time.time() - t0,
        "target": LITERATURE_TARGET,
        "max_intermediate": max_intermediate,
        "message": (
            f"Graph+catalog climb kept {len(found)} / ~{LITERATURE_TARGET} "
            f"({by_source.get('graph', 0)} from graphs, "
            f"{by_source.get('catalog', 0)} from catalog)."
        ),
    }

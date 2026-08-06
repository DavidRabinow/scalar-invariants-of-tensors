"""Configuration for tensor-invariant experiments."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from dataclasses import field as dc_field
from pathlib import Path
from typing import Any, Literal


SignatureName = Literal["euclidean", "lorentzian"]
FieldName = Literal["real", "complex", "finite"]


@dataclass
class TensorConfig:
    """
    Explicit conventions for a p-form invariant calculation.

    Do not silently mix Euclidean and Lorentzian conventions.
    """

    name: str
    dim: int
    form_degree: int
    signature: SignatureName = "euclidean"
    number_field: FieldName = "real"
    metric_signature: tuple[int, ...] = ()
    allow_epsilon: bool = False
    self_dual: bool = False
    hodge_star_squared: int | None = None  # +1 or -1 when applicable
    epsilon_012_plus: bool = True
    symmetry_group: str = "SO(d)"
    seed: int = 0
    discovery_primes: tuple[int, ...] = (1_000_003, 1_000_033, 1_000_037)
    validation_primes: tuple[int, ...] = (1_000_039, 1_000_081, 1_000_151)
    n_discovery_samples: int = 64
    n_validation_samples: int = 64
    max_degree: int = 10
    notes: str = ""
    extra: dict[str, Any] = dc_field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.metric_signature:
            if self.signature == "euclidean":
                self.metric_signature = tuple(1 for _ in range(self.dim))
            elif self.signature == "lorentzian":
                self.metric_signature = (-1,) + tuple(1 for _ in range(self.dim - 1))
            else:
                raise ValueError(f"unknown signature {self.signature}")
        if len(self.metric_signature) != self.dim:
            raise ValueError("metric_signature length must equal dim")

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["metric_signature"] = list(self.metric_signature)
        d["discovery_primes"] = list(self.discovery_primes)
        d["validation_primes"] = list(self.validation_primes)
        return d


def load_config(path: str | Path | dict[str, Any]) -> TensorConfig:
    """Load a TensorConfig from a YAML/JSON path or a dict."""
    if isinstance(path, dict):
        data = path
    else:
        p = Path(path)
        text = p.read_text(encoding="utf-8")
        if p.suffix.lower() in {".yaml", ".yml"}:
            try:
                import yaml  # type: ignore

                data = yaml.safe_load(text)
            except ImportError:
                # Minimal YAML subset: key: value lines and nested via json-like
                data = _minimal_yaml(text)
        else:
            data = json.loads(text)
    return _from_mapping(data)


def _from_mapping(data: dict[str, Any]) -> TensorConfig:
    known = {f.name for f in TensorConfig.__dataclass_fields__.values()}  # type: ignore[attr-defined]
    kwargs = {}
    extra = {}
    for k, v in data.items():
        # Accept legacy YAML key "field" as number_field
        if k == "field":
            k = "number_field"
        if k in known:
            if k in {"metric_signature", "discovery_primes", "validation_primes"} and v is not None:
                kwargs[k] = tuple(v)
            else:
                kwargs[k] = v
        else:
            extra[k] = v
    if extra:
        kwargs["extra"] = {**kwargs.get("extra", {}), **extra}
    return TensorConfig(**kwargs)


def _minimal_yaml(text: str) -> dict[str, Any]:
    """Tiny YAML subset for flat configs (no nested structures beyond lists)."""
    out: dict[str, Any] = {}
    current_list_key: str | None = None
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        if line.strip().startswith("- ") and current_list_key:
            item = line.strip()[2:].strip().strip("\"'")
            try:
                item_v: Any = int(item)
            except ValueError:
                try:
                    item_v = float(item)
                except ValueError:
                    if item.lower() in {"true", "false"}:
                        item_v = item.lower() == "true"
                    else:
                        item_v = item
            out.setdefault(current_list_key, []).append(item_v)
            continue
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()
        if val == "":
            current_list_key = key
            out[key] = []
            continue
        current_list_key = None
        if val.lower() in {"true", "false"}:
            out[key] = val.lower() == "true"
        elif val.lower() in {"null", "none", "~"}:
            out[key] = None
        else:
            try:
                out[key] = int(val)
            except ValueError:
                try:
                    out[key] = float(val)
                except ValueError:
                    out[key] = val.strip("\"'")
    return out

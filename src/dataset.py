"""Load the official frame-coordinate representation and labels."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


def load_sequence(path: str | Path) -> list[np.ndarray]:
    """Load one coordinate JSON file in chronological frame order."""
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    return [np.asarray(payload[key], dtype=np.float64) for key in sorted(payload)]


def load_target(path: str | Path) -> list[int]:
    return [int(value) for value in json.loads(Path(path).read_text(encoding="utf-8"))]


def iter_split(level_dir: str | Path):
    """Yield ``(name, frames, target)`` from an official validation level."""
    root = Path(level_dir)
    for coordinate_path in sorted((root / "coordinates").glob("coordinates_*.json")):
        target_name = coordinate_path.name.replace("coordinates_", "target_")
        yield coordinate_path.stem, load_sequence(coordinate_path), load_target(root / "target" / target_name)

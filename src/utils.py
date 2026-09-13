"""Small reproducibility utilities."""

from __future__ import annotations

import random

import numpy as np


def seed_everything(seed: int = 42) -> None:
    random.seed(seed)
    np.random.seed(seed)

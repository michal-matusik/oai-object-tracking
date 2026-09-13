"""Evaluate the tracker on one published validation level."""

from __future__ import annotations

import argparse

from .dataset import iter_split
from .metrics import exact_match
from .model import CupTracker


def evaluate(level_dir: str) -> dict[str, float | int]:
    tracker = CupTracker()
    scores = [exact_match(tracker.predict(frames), target) for _, frames, target in iter_split(level_dir)]
    return {"correct": int(sum(scores)), "sequences": len(scores), "accuracy": sum(scores) / len(scores)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("level_dir")
    args = parser.parse_args()
    print(evaluate(args.level_dir))

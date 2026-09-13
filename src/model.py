"""Constant-velocity tracker for the three-cup shell-game videos."""

from __future__ import annotations

from itertools import permutations

import numpy as np


def box_centers(boxes: np.ndarray) -> np.ndarray:
    boxes = np.asarray(boxes, dtype=np.float64)
    if boxes.ndim != 2 or boxes.shape[1] != 4:
        raise ValueError("boxes must have shape [objects, 4]")
    return (boxes[:, :2] + boxes[:, 2:]) / 2.0


def optimal_assignment(predicted: np.ndarray, detections: np.ndarray) -> np.ndarray:
    """Solve the small assignment problem exactly by enumerating permutations."""
    cost = np.linalg.norm(predicted[:, None, :] - box_centers(detections)[None, :, :], axis=-1)
    permutation = min(
        permutations(range(len(detections))),
        key=lambda candidate: sum(cost[row, column] for row, column in enumerate(candidate)),
    )
    return np.asarray(permutation, dtype=np.int64)


class CupTracker:
    """Track identities initialized from the required left-to-right ordering."""

    def predict(self, frames: list[np.ndarray]) -> list[int]:
        if not frames:
            raise ValueError("at least one frame is required")
        tracks = np.asarray(frames[0], dtype=np.float64)
        tracks = tracks[np.argsort(box_centers(tracks)[:, 0])]
        velocity = np.zeros((len(tracks), 2), dtype=np.float64)
        for detections in frames[1:]:
            detections = np.asarray(detections, dtype=np.float64)
            if len(detections) != len(tracks):
                raise ValueError("this reconstruction expects one detection per cup in every frame")
            match = optimal_assignment(box_centers(tracks) + velocity, detections)
            updated = detections[match]
            velocity = box_centers(updated) - box_centers(tracks)
            tracks = updated
        return np.argsort(box_centers(tracks)[:, 0]).astype(int).tolist()

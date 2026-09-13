"""Motion-aware association for the three-cup tracking task."""
from __future__ import annotations
from itertools import permutations
import numpy as np

def centers(boxes: np.ndarray) -> np.ndarray:
    boxes = np.asarray(boxes, dtype=float)
    return (boxes[:, :2] + boxes[:, 2:]) / 2

def assign_tracks(previous: np.ndarray, current: np.ndarray, velocity: np.ndarray | None = None) -> np.ndarray:
    """Return indices of current detections matched to previous track order."""
    p, c = centers(previous), centers(current)
    predicted = p if velocity is None else p + velocity
    cost = np.linalg.norm(predicted[:, None, :] - c[None, :, :], axis=-1)
    return np.array(min(permutations(range(len(c))), key=lambda perm: sum(cost[i, j] for i, j in enumerate(perm))))

def final_order(frames: list[np.ndarray]) -> list[int]:
    """Track initial identities and return their left-to-right order in the final frame."""
    if not frames:
        raise ValueError("at least one frame is required")
    tracks = np.asarray(frames[0], dtype=float).copy()
    identities = np.arange(len(tracks))
    velocity = None
    for detections in frames[1:]:
        match = assign_tracks(tracks, detections, velocity)
        updated = np.asarray(detections, dtype=float)[match]
        velocity = centers(updated) - centers(tracks)
        tracks = updated
    return identities[np.argsort(centers(tracks)[:, 0])].tolist()

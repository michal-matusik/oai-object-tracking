"""Backward-compatible imports for the initial reconstruction."""

from .model import CupTracker, box_centers

centers = box_centers


def final_order(frames):
    return CupTracker().predict(frames)

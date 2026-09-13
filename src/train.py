"""Training entry point retained for a consistent research-repository layout.

The tracker is analytical and has no learned parameters.
"""

from .model import CupTracker


def train() -> CupTracker:
    return CupTracker()

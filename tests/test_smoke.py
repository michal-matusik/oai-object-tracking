import unittest

import numpy as np

from src.model import CupTracker


class TrackingSmokeTest(unittest.TestCase):
    def test_crossing_keeps_identity(self):
        box = lambda x: [x, 0, x + 1, 1]
        frames = [
            np.array([box(10), box(0), box(5)]),
            np.array([box(7), box(3), box(5)]),
            np.array([box(2), box(8), box(5)]),
        ]
        self.assertEqual(CupTracker().predict(frames), [2, 1, 0])


if __name__ == "__main__":
    unittest.main()

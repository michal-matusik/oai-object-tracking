import sys, unittest
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).parents[1] / 'src'))
from tracking import final_order

class TrackingSmokeTest(unittest.TestCase):
    def test_crossing_keeps_identity(self):
        box = lambda x: [x, 0, x + 1, 1]
        frames = [np.array([box(0), box(5), box(10)]), np.array([box(3), box(5), box(7)]), np.array([box(8), box(5), box(2)])]
        self.assertEqual(final_order(frames), [2, 1, 0])

if __name__ == '__main__': unittest.main()

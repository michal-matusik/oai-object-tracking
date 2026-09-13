# Reconstructed Object Tracking - Polish AI Olympiad I

This repository is a reconstructed reference solution for the first-stage Object Tracking task in the Polish Artificial Intelligence Olympiad.

The task supplied detected cup bounding boxes for every frame and asked for the final left-to-right identity order after a sequence of swaps.
The implementation uses motion-aware bipartite association: it predicts each track's next center from its velocity, assigns detections globally with an exhaustive minimum-cost permutation for three objects, and reports track identities ordered by final horizontal position.

![Three-cup tracking task illustration](assets/task-cup-tracking.png)

*Task illustration from the official Polish AI Olympiad I notebook.*

## Quick start

```bash
python scripts/download_data.py
python -m src.evaluate data/valid_data/level_1
python -m unittest discover -s tests -v
```

## Validation

The reconstructed tracker correctly solves 50 of 50 sequences in the official public level 1 validation set.
That is 100% exact-match accuracy on the published validation data.
No hidden-test or leaderboard result is claimed.
See `SOLUTION.md` for the algorithm and evaluation protocol.

## Provenance

The original Polish task notebook is retained as `notebooks/original_submission.ipynb`.
`docs/task_en.md` is an English task summary.

# Reconstructed Object Tracking - Polish AI Olympiad I

This repository is a reconstructed reference solution for the first-stage Object Tracking task in the Polish Artificial Intelligence Olympiad.
It is not the author's original competition submission.

The task supplied detected cup bounding boxes for every frame and asked for the final left-to-right identity order after a sequence of swaps.
The implementation uses motion-aware bipartite association: it predicts each track's next center from its velocity, assigns detections globally with an exhaustive minimum-cost permutation for three objects, and reports track identities ordered by final horizontal position.

## Quick start

`python -m unittest discover -s tests -v`

## Validation

The included synthetic crossing-sequence test validates that identity is preserved through a swap using bounding boxes alone.
It is a smoke test, not an Olympiad or hidden-test score.

## Provenance

The original Polish task notebook is retained as `notebooks/original_submission.ipynb`.
`docs/task_en.md` is an English task summary.

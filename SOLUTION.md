# Solution notes

This repository contains a retrospective reconstruction and not the original competition submission.

The task defines cup identities by their left-to-right order in the first frame.
The tracker therefore sorts the initial detections before association.
For each later frame, it extrapolates every center with a constant-velocity model and solves the three-object assignment problem exactly by enumerating all six permutations.
The final answer is the tracked identity order after sorting final centers horizontally.

The published level 1 validation split contains 50 videos with 110 coordinate frames and three detections in every frame.
The reconstructed tracker returns the exact target permutation for all 50 videos.
This is a public validation result and does not imply a hidden-test or leaderboard score.

The validation command completes in under one second on an Apple Silicon CPU:

```bash
python -m src.evaluate data/valid_data/level_1
```

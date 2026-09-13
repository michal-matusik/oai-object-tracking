"""Official task-level exact-match metric."""


def exact_match(prediction: list[int], target: list[int]) -> float:
    return float(prediction == target)

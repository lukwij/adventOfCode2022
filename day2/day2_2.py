from day2_1 import get_next_strategy, calculate_round_score

SCORE_MAPPING = {
    ("A", "X"): 0 + 3,
    ("A", "Y"): 3 + 1,
    ("A", "Z"): 6 + 2,
    ("B", "X"): 0 + 1,
    ("B", "Y"): 3 + 2,
    ("B", "Z"): 6 + 3,
    ("C", "X"): 0 + 2,
    ("C", "Y"): 3 + 3,
    ("C", "Z"): 6 + 1,
}

if __name__ == "__main__":
    score = 0
    for strategy in get_next_strategy("input.txt"):
        score += calculate_round_score(SCORE_MAPPING, strategy)
    print(f"Total score: {score}")

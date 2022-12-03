# day2_1.py

def get_next_strategy(filename: str) -> list:
    with open(filename, mode='r') as f:
        for line in f:
            yield tuple(line.strip().split())


SCORE_MAPPING = {
    ("A", "X"): 4,
    ("A", "Y"): 8,
    ("A", "Z"): 3,
    ("B", "X"): 1,
    ("B", "Y"): 5,
    ("B", "Z"): 9,
    ("C", "X"): 7,
    ("C", "Y"): 2,
    ("C", "Z"): 6,
}


def calculate_round_score(mapping, round_strategy: tuple) -> int:
    return mapping[round_strategy]


if __name__ == "__main__":
    score = 0
    for strategy in get_next_strategy("input.txt"):
        score += calculate_round_score(SCORE_MAPPING, strategy)
    print(f"Total score: {score}")

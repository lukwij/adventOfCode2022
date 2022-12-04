# day3_2.py

from day3_1 import get_next_rucksack
from string import ascii_lowercase


def get_group_badge_priority(rucksacks_gen):
    rucksack1 = next(rucksacks_gen)
    rucksack2 = next(rucksacks_gen)
    rucksack3 = next(rucksacks_gen)

    for item in rucksack1:
        if item in rucksack2:
            if item in rucksack3:
                modifier = 1
                if item.isupper():
                    item = item.lower()
                    modifier = 27
                return ascii_lowercase.index(item) + modifier


if __name__ == "__main__":
    rucksacks = get_next_rucksack("input.txt")
    priority_sum = 0
    while True:
        try:
            priority_sum += get_group_badge_priority(rucksacks)
        except StopIteration:
            break
    print(f"Total score: {priority_sum}")

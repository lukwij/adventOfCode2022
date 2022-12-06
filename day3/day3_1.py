# day3_1.py

from string import ascii_lowercase


def get_next_rucksack(filename: str) -> list:
    with open(filename, mode='r') as f:
        for line in f:
            yield line.strip()


def get_compartments(rucksack: str) -> tuple:
    return rucksack[:int(len(rucksack) / 2)], rucksack[int(len(rucksack) / 2):]


def get_backpack_priority(compartment_1, compartment_2) -> int:
    modifier = 1
    for item in compartment_1:
        if item in compartment_2:
            if item.isupper():
                item = item.lower()
                modifier = 27
            return ascii_lowercase.index(item) + modifier


if __name__ == "__main__":
    priority_sum = 0
    for rucksack in get_next_rucksack("input.txt"):
        part1, part2 = get_compartments(rucksack)
        priority_sum += get_backpack_priority(part1, part2)
    print(f"Total score: {priority_sum}")

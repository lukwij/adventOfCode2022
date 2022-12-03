# day1.py

def create_food_list(filename: str) -> list:
    with open(filename) as f:
        food_list = []
        elf_load = []
        for line in f:
            if line.strip() == '':
                food_list.append(elf_load)
                elf_load = []
            else:
                elf_load.append(int(line.strip()))
        food_list.append(elf_load)
    return food_list


def find_max_calories(totals_list: list) -> int:
    return max(totals_list)


def create_totals_list(food_list: list) -> list:
    return [sum(elf) for elf in food_list]


def sum_top_three(totals_list: list) -> int:
    return sum(sorted(totals_list)[-3:])


if __name__ == "__main__":
    elf_list = create_food_list("input.txt")
    print(sum_top_three(create_totals_list(elf_list)))

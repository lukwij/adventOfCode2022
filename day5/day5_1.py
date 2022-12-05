# day5_1.py

from string import ascii_uppercase
import re


def get_stacks_and_operations(filename: str) -> tuple:
    with open(filename, mode='r') as f:
        stacks = []
        operations = []
        for line in f:
            if "[" in line:
                stacks.append(line)
            if "move" in line:
                operations.append(line)
            if line.startswith(" 1"):
                stack_no = int(line.strip()[-1])
        return stacks, stack_no, operations


def convert_stacks(stacks: list, stack_no: int) -> dict:
    stacks_dict = {}
    for i in range(stack_no):
        stacks_dict[i + 1] = []
    for line in stacks:
        line_length = len(line)
        stack_number = 0
        modifier = 1
        spot_check = stack_number * 4 + modifier
        while spot_check < line_length:
            if line[spot_check] in ascii_uppercase:
                stacks_dict[stack_number + 1].insert(0, line[spot_check])
            stack_number += 1
            spot_check = stack_number * 4 + modifier
    return stacks_dict


def get_operations(operations: list) -> list:
    operations_list = []
    for line in operations:
        result = re.search(r"move (\d+) from (\d+) to (\d+)", line)
        operation = {"amount": int(result[1]),
                     "from": int(result[2]),
                     "to": int(result[3])}
        operations_list.append(operation)
    return operations_list


def apply_crane(initial_stacks: dict, operation_list: list) -> dict:
    for instruction in operation_list:
        for _ in range(instruction["amount"]):
            initial_stacks[instruction["to"]].append(initial_stacks[instruction["from"]].pop())
    return initial_stacks


def show_result(final_stacks: dict, stack_amnt: int):
    print("".join([final_stacks[i + 1][-1] for i in range(stack_amnt)]))


if __name__ == "__main__":
    stacks_raw, stack_amount, operations_raw = get_stacks_and_operations("input.txt")
    stack_dict = convert_stacks(stacks_raw, stack_amount)
    op_list = get_operations(operations_raw)
    end_stacks = apply_crane(stack_dict, op_list)
    show_result(end_stacks, stack_amount)

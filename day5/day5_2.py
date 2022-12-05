# day5_2.py

from day5_1 import get_stacks_and_operations, convert_stacks, get_operations, show_result


def apply_crane(initial_stacks: dict, operation_list: list) -> dict:
    for instruction in operation_list:
        initial_stacks[instruction["to"]] = initial_stacks[instruction["to"]] + initial_stacks[instruction["from"]][-instruction["amount"]:]
        del initial_stacks[instruction["from"]][-instruction["amount"]:]
    return initial_stacks


if __name__ == "__main__":
    stacks_raw, stack_amount, operations_raw = get_stacks_and_operations("input.txt")
    stack_dict = convert_stacks(stacks_raw, stack_amount)
    op_list = get_operations(operations_raw)
    end_stacks = apply_crane(stack_dict, op_list)
    show_result(end_stacks, stack_amount)

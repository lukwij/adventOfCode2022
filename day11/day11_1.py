# day11_1.py

import re
import numpy

MONKEY_LIST = []
MONKEY_PRODUCT = None


class Monkey:
    def __init__(self, items, operation_type, operation_value, test, true_outcome, false_outcome):
        self.items = items
        self.operation_type = operation_type
        self.operation_value = operation_value
        self.test = test
        self.true_monkey = true_outcome
        self.false_monkey = false_outcome
        self.activity_counter = 0

    def take_turn(self, mode):
        for item in self.items:
            self.handle_item(item, mode)
        self.items = []

    def handle_item(self, item, mode):
        item = self.change_worry_level(item)
        print(f"new worry level: {item}")
        if mode == "day1":
            item = int(item / 3)
        test_passed = self.test_item(item)
        self.throw_item(item, mode, test_passed)
        self.activity_counter += 1

    def change_worry_level(self, item):
        print(f"old worry level: {item}, operation value: {self.operation_value}")
        value = item if self.operation_value == "old" else int(self.operation_value)
        if self.operation_type == "*":
            return item * value
        else:
            return item + value

    def test_item(self, item):
        test_passed = not item % self.test
        return test_passed

    def throw_item(self, item, mode, test_passed):
        if mode != "day1":
            print(f"item before: {item}")
            item = item % MONKEY_PRODUCT
            print(f"item after: {item}")
        if test_passed:
            MONKEY_LIST[self.true_monkey].items.append(item)
        else:
            MONKEY_LIST[self.false_monkey].items.append(item)


def get_monkeys(filename: str):
    with open(filename, mode='r') as f:
        items = []
        operation_type = None
        operation_value = None
        test = None
        true_m = None
        false_m = None
        for line in f:
            line = line.strip()
            if line.startswith("Starting"):
                result = re.findall(r"\d+", line)
                for match_no in range(len(result)):
                    items.append(int(result[match_no]))
                result = []
            elif line.startswith("Operation"):
                operation_type = line.split()[-2]
                operation_value = line.split()[-1]
            elif line.startswith("Test"):
                test = int(line.split()[-1])
            elif line.startswith("If true"):
                true_m = int(line.split()[-1])
            elif line.startswith("If false"):
                false_m = int(line.split()[-1])
            if false_m is not None:
                mon = Monkey(items, operation_type, operation_value, test, true_m, false_m)
                MONKEY_LIST.append(mon)
                items = []
                false_m = None


def do_monkey_business(filename="input.txt", turn_no=20, mode="day1"):
    get_monkeys(filename)
    global MONKEY_PRODUCT
    MONKEY_PRODUCT = numpy.prod([monkey.test for monkey in MONKEY_LIST])
    print(f"monkey product: {MONKEY_PRODUCT}")
    for round_no in range(turn_no):
        for monkey in MONKEY_LIST:
            monkey.take_turn(mode)
    print([monkey.activity_counter for monkey in MONKEY_LIST])
    most_active_monkeys = sorted([monkey.activity_counter for monkey in MONKEY_LIST])[-2:]
    print(most_active_monkeys)
    return most_active_monkeys[0] * most_active_monkeys[1]


if __name__ == "__main__":
    print(do_monkey_business())

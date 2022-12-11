# day10_2.py
from day10_1 import get_instructions, process_instructions


def draw_crt(process_gen) -> list:
    line = []
    for cycle_no, register_value in process_gen:
        row_position = (cycle_no - 1) % 40
        if row_position in range(register_value - 1, register_value + 2):
            line.append("#")
        else:
            line.append(".")
    for i in range(6):
        print("".join(line[i * 40: (i + 1) * 40]))
    return line


if __name__ == "__main__":
    inst = get_instructions("input.txt")
    proc_gen = process_instructions(inst)
    print(draw_crt(proc_gen))

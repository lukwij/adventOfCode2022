# day10_1.py


def get_instructions(filename: str) -> int:
    with open(filename, mode='r') as f:
        for line in f:
            if line.startswith("add"):
                instruction = int(line.strip().split()[1])
            else:
                instruction = 0
            yield instruction


def process_instructions(inst_gen) -> tuple:
    register_value = 1
    sum_of_strengths = 0
    cycle = 0
    register_bump = 0
    processing_time = 1
    while True:
        cycle += 1
        processing_time -= 1
        if processing_time == 0:
            register_value += register_bump
            register_bump = 0
            instruction = next(inst_gen)
            if instruction == 0:
                processing_time = 1
            else:
                processing_time = 2
                register_bump = instruction
        yield cycle, register_value
        if cycle == 240:
            break
    return sum_of_strengths


def get_sum_of_signal_strengths(process_gen) -> int:
    sum_of_strengths = 0
    for cycle_no, register_value in process_gen:
        if cycle_no in [20, 60, 100, 140, 180, 220]:
            signal_strength = register_value * cycle_no
            sum_of_strengths += signal_strength
    return sum_of_strengths


if __name__ == "__main__":
    inst = get_instructions("input.txt")
    proc_gen = process_instructions(inst)
    print(get_sum_of_signal_strengths(proc_gen))

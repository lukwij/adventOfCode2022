# day14_1.py

from collections import defaultdict


def get_cave(filename: str) -> defaultdict:
    cave = defaultdict(int)
    with open(filename, mode='r') as f:
        for line in f:
            line_stripped = line.strip()
            coordinates = line_stripped.split(" -> ")
            for i in range(len(coordinates) - 1):
                from_x, from_y = eval(coordinates[i])
                to_x, to_y = eval(coordinates[i + 1])
                if from_x == to_x:
                    for y in range(from_y if from_y <= to_y else to_y, (to_y if from_y <= to_y else from_y) + 1):
                        cave[from_x, y] = 1
                else:
                    for x in range(from_x if from_x <= to_x else to_x, (to_x if from_x <= to_x else from_x) + 1):
                        cave[x, from_y] = 1
    return cave

def simulate_sand_fall(cave_layout, sand_entrance) -> int:
    sand_units_rested = 0
    falling_to_abyss = False
    while not falling_to_abyss:
        sand_unit_position = sand_entrance
        turn_falling_straight_down = 0
        while True:
            if not cave_layout[sand_unit_position[0], sand_unit_position[1] + 1]:
                sand_unit_position = (sand_unit_position[0], sand_unit_position[1] + 1)
                turn_falling_straight_down += 1
                if turn_falling_straight_down > 100:
                    falling_to_abyss = True
                    break
                continue
            if not cave_layout[sand_unit_position[0] - 1, sand_unit_position[1] + 1]:
                sand_unit_position = (sand_unit_position[0] - 1, sand_unit_position[1] + 1)
                turn_falling_straight_down = 0
                continue
            if not cave_layout[sand_unit_position[0] + 1, sand_unit_position[1] + 1]:
                sand_unit_position = (sand_unit_position[0] + 1, sand_unit_position[1] + 1)
                turn_falling_straight_down = 0
                continue
            cave_layout[sand_unit_position] = 2
            sand_units_rested += 1
            break
    return sand_units_rested



if __name__ == "__main__":
    sand_entry_coordinates = (500 ,0)
    my_cave = get_cave("input.txt")
    print(simulate_sand_fall(my_cave, sand_entry_coordinates))

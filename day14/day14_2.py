# day14_2.py


from day14_1 import get_cave


def simulate_sand_fall(cave_layout, sand_entrance) -> int:
    sand_units_rested = 0
    floor_coordinates = max([key[1] for key in cave_layout.keys()]) + 2
    inlet_clogged = False
    while not inlet_clogged:
        sand_unit_position = sand_entrance
        while True:
            if sand_unit_position[1] == floor_coordinates - 1:
                cave_layout[sand_unit_position] = 2
                sand_units_rested += 1
                break
            if not cave_layout[sand_unit_position[0], sand_unit_position[1] + 1]:
                sand_unit_position = (sand_unit_position[0], sand_unit_position[1] + 1)
                continue
            if not cave_layout[sand_unit_position[0] - 1, sand_unit_position[1] + 1]:
                sand_unit_position = (sand_unit_position[0] - 1, sand_unit_position[1] + 1)
                continue
            if not cave_layout[sand_unit_position[0] + 1, sand_unit_position[1] + 1]:
                sand_unit_position = (sand_unit_position[0] + 1, sand_unit_position[1] + 1)
                continue
            cave_layout[sand_unit_position] = 2
            sand_units_rested += 1
            if sand_unit_position == sand_entrance:
                inlet_clogged = True
            break
    return sand_units_rested


if __name__ == "__main__":
    sand_entry_coordinates = (500, 0)
    my_cave = get_cave("input.txt")
    print(simulate_sand_fall(my_cave, sand_entry_coordinates))

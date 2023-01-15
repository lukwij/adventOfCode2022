# day15_1.py

import re


def get_sensors_and_beacons(filename: str) -> list:
    sensors_and_beacons = []
    with open(filename, mode='r') as f:
        for line in f:
            data = re.findall(r"([\d-]+)", line.strip())
            sensor_coordinates = (int(data[0]), int(data[1]))
            beacon_coordinates = (int(data[2]), int(data[3]))
            sensors_and_beacons.append((sensor_coordinates, beacon_coordinates))
    return sensors_and_beacons


def get_coverage(ss_and_bs: list) -> list:
    master_coverage = []
    for sensor, beacon in ss_and_bs:
        coverage = []
        print(f"sensor: {sensor}, beacon: {beacon}")
        beacon_reached = False
        coordinates_to_check = [sensor]
        while not beacon_reached:
            next_to_check = []
            for position in coordinates_to_check:
                if position not in coverage:
                    coverage.append(position)
                if position == beacon:
                    beacon_reached = True
                if not beacon_reached:
                    for potential_next in find_new_directions(position):
                        if (potential_next not in coverage) and (potential_next not in next_to_check):
                            next_to_check.append(potential_next)
                    coordinates_to_check = next_to_check
        master_coverage += coverage
    return master_coverage


def find_new_directions(position: tuple) -> list:
    directions = [(position[0], position[1] - 1), (position[0] + 1, position[1]), (position[0], position[1] + 1),
                  (position[0] - 1, position[1])]
    return directions


def draw_coverage(coverage: list, sensors_and_beacons: list, row_no):
    min_x = min([position[0] for position in coverage])
    max_x = max([position[0] for position in coverage])
    min_y = min([position[1] for position in coverage])
    max_y = max([position[1] for position in coverage])
    count = 0
    for row in range(min_y, max_y + 1):
        print(f"{row : > 5} ", end="")
        for place in range(min_x, max_x + 1):
            if (place, row) in coverage:
                if (place, row) in [pair[0] for pair in sensors_and_beacons]:
                    print("S", end="")
                elif (place, row) in [pair[1] for pair in sensors_and_beacons]:
                    print("B", end="")
                else:
                    print("#", end="")
                    if row == row_no:
                        count += 1
            else:
                print(".", end="")
        print()
    print(f"count: {count}")


if __name__ == "__main__":
    my_sb_pairs = get_sensors_and_beacons("input.txt")
    my_coverage = get_coverage(my_sb_pairs)
    draw_coverage(my_coverage, my_sb_pairs, row_no=2000000)

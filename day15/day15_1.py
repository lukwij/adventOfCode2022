# day15_1.py

import re
import logging


def get_sensors_and_beacons(filename: str) -> list:
    sensors_and_beacons = []
    with open(filename, mode='r') as f:
        for line in f:
            data = re.findall(r"([\d-]+)", line.strip())
            sensor_coordinates = (int(data[0]), int(data[1]))
            beacon_coordinates = (int(data[2]), int(data[3]))
            sensors_and_beacons.append((sensor_coordinates, beacon_coordinates))
    return sensors_and_beacons


def get_coverage_for_row(ss_and_bs: list, row_no: int) -> list:
    coverage = []
    for sensor, beacon in ss_and_bs:
        logging.info(f"sensor: {sensor}, beacon: {beacon}")
        radius = calculate_radius(sensor, beacon)
        coverage += range_covered_in_row(sensor, radius, row_no)
    positions_wo_beacon = list(set(coverage))
    logging.info(sorted(positions_wo_beacon))
    for pair in ss_and_bs:
        try:
            logging.info(f"Checking if beacon is in given row")
            positions_wo_beacon.remove(pair[1])
            logging.info(f"Beacon found in row and removed!")
        except ValueError:
            logging.warning(f"Beacon {pair[1]} not in that row")
    return positions_wo_beacon


def calculate_radius(sensor: tuple, beacon: tuple) -> int:
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])


def range_covered_in_row(sensor, radius, row_no) -> list:
    row_distance_from_sensor = abs(sensor[1] - row_no)
    radius_less_distance = radius - row_distance_from_sensor
    if radius_less_distance < 0:
        return []
    range_in_row = []
    for column in range(sensor[0] - radius_less_distance, sensor[0] + radius_less_distance + 1):
        range_in_row.append((column, row_no))
    return range_in_row


if __name__ == "__main__":
    row_number = 2_000_000
    logging.basicConfig(level=logging.INFO)
    my_sb_pairs = get_sensors_and_beacons("input.txt")
    my_coverage = get_coverage_for_row(my_sb_pairs, row_no=row_number)
    logging.info(f"Positions without beacon in row {row_number}: {len(my_coverage)}")

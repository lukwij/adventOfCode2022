# day15_2.py

from day15_1 import get_sensors_and_beacons, calculate_radius
import logging


def get_sensors_and_radii(ss_and_bs: list) -> list:
    snr = []
    for sensor, beacon in ss_and_bs:
        sensor_radius = calculate_radius(sensor, beacon)
        snr.append((sensor, sensor_radius))
    return snr


def find_coverage(snr: list, x_range: int, y_range: int):
    for row in range(y_range):
        print(f"row: {row}")
        row_coverage = []
        for sensor, srange in snr:
            # logging.debug(f"row: {row}, sensor: {sensor}")
            row_reach = abs(sensor[1] - row)
            if row_reach <= srange:
                sensor_coverage = (sensor[0] - (srange - row_reach), sensor[0] + (srange - row_reach))
                row_coverage.append(sensor_coverage)
                # logging.info(f"coverage: {row_coverage}")
        if check_coverage(row, row_coverage, x_range):
            return


def check_coverage(row, row_coverage, x_range):
    sorted_coverage = sorted(row_coverage)
    # logging.info(f"Sorted coverage: {sorted_coverage}")
    slimmed_coverage = [coverage for coverage in sorted_coverage if not (coverage[0] > x_range or coverage[1] < 0)]
    # logging.info(f"Slimmed coverage: {sorted_coverage}")
    maximum = 0
    for i in range(len(slimmed_coverage) - 1):
        if sorted_coverage[i][1] < maximum:
            continue
        maximum = sorted_coverage[i][1]
        if maximum + 1 < sorted_coverage[i + 1][0]:
            print(f"Found gap for row {row} in position {sorted_coverage[i][1] + 1}")
            print(calculate_frequency((sorted_coverage[i][1] + 1, row)))
            return True


def calculate_frequency(distress_bacon_coordinates) -> int:
    return distress_bacon_coordinates[0] * 4_000_000 + distress_bacon_coordinates[1]


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    my_sb_pairs = get_sensors_and_beacons("input.txt")
    sensors_radii = get_sensors_and_radii(my_sb_pairs)
    find_coverage(sensors_radii, 4_000_000, 4_000_000)

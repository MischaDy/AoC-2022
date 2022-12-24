import re
from typing import Tuple

RUN_TEST = True
PART = 1

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n')
    print(day_function(input_))


def pos_from_str(pos_str_tup: Tuple[str, str]):
    xstr, ystr = pos_str_tup
    return int(xstr), int(ystr)


def get_sensors_and_beacons(input_):
    coord_pattern = r'x=(-?\d+), y=(-?\d+)'
    sensors_to_beacons = dict()
    for line in input_:
        sensor_pos_str, beacon_pos_str = re.findall(coord_pattern, line)
        sensor_pos, beacon_pos = pos_from_str(sensor_pos_str), pos_from_str(beacon_pos_str)
        sensors_to_beacons[sensor_pos] = beacon_pos
    return sensors_to_beacons


def manhattan_dist(pos1, pos2):
    (x1, y1), (x2, y2) = pos1, pos2
    return abs(x1 - x2) + abs(y1 - y2)


def count_radius_intersections(row, sensor, sensor_beacon_dist):
    sensor_x, sensor_y = sensor
    row_sensor_dist = abs(row - sensor_y)
    delta_dist = sensor_beacon_dist - row_sensor_dist
    if delta_dist <= 0:
        return 0
    # intersections = {-delta_dist, ..., 0, ..., delta_dist}
    num_intersections = 2*delta_dist + 1  # = len(range(-delta_dist, delta_dist+1))
    return num_intersections


def count_occupied_coords_at(row, sensors_to_beacons):
    num_occupied_coords = 0
    for sensor, beacon in sensors_to_beacons.items():
        dist = manhattan_dist(sensor, beacon)
        num_intersections = count_radius_intersections(row, sensor, dist)
        num_occupied_coords += num_intersections
    return num_occupied_coords


def run_part1(input_):
    row = 10 if RUN_TEST else 2_000_000
    sensors_to_beacons = get_sensors_and_beacons(input_)
    num_occupied_coords = count_occupied_coords_at(row, sensors_to_beacons)
    return num_occupied_coords


def run_part2(input_):
    pass


def get_input(file_path, line_sep=None):
    with open(file_path) as f:
        input_ = f.read()

    if line_sep is not None:
        input_ = input_.split(line_sep)
    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)

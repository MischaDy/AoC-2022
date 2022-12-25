import re
from typing import Tuple

RUN_TEST = False
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


def get_radius_intersections(row, sensor, sensor_beacon_dist):
    sensor_x, sensor_y = sensor
    row_sensor_dist = abs(row - sensor_y)
    delta_dist = sensor_beacon_dist - row_sensor_dist
    if delta_dist < 0:
        return []
    lower_x = sensor_x - delta_dist
    upper_x = sensor_x + delta_dist
    return ((int_x, row) for int_x in range(lower_x, upper_x + 1))


def get_occupied_coords_at(row, sensors_to_beacons):
    occupied_coords = set()
    for sensor, beacon in sensors_to_beacons.items():
        dist = manhattan_dist(sensor, beacon)
        intersections = get_radius_intersections(row, sensor, dist)
        occupied_coords.update(intersections)
    return occupied_coords


def run_part1(input_):
    row = 10 if RUN_TEST else 2_000_000
    sensors_to_beacons = get_sensors_and_beacons(input_)
    occupied_coords = get_occupied_coords_at(row, sensors_to_beacons)
    beacons = sensors_to_beacons.values()
    beaconfree_zone = occupied_coords.difference(beacons)
    return len(beaconfree_zone)


def run_part2(input_):
    pass


def get_input(file_path, line_sep=None):
    with open(file_path) as f:
        input_ = f.read()

    if line_sep is not None:
        input_ = input_.split(line_sep)
    return input_


def test():
    sensor = (8, 7)
    beacon = (2, 10)
    dist = manhattan_dist(sensor, beacon)
    for row in range(-3, 17 + 1):
        num_intersections = get_radius_intersections(row, sensor, dist)
        print(f'{row}: {num_intersections}')


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)
    # test()


from typing import List

import numpy as np

RUN_TEST = True
TEST_NUM = 1
PART = 1

TEST_INPUT_PATH1 = 'test_input1.txt'
TEST_INPUT_PATH2 = 'test_input1.txt'
INPUT_PATH = 'input.txt'


def main(run_test, test_num, part, test_input_path1, test_input_path2, input_path):
    if run_test:
        file_path = test_input_path1 if test_num == 1 else test_input_path2
    else:
        file_path = input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n')
    print(day_function(input_))


def get_cube_positions(lines):
    for line in lines:
        yield np.array(line.split(','), dtype=int)


def get_minmax_coords(cube_positions):
    num_coords = 3
    min_coords = np.repeat(np.inf, num_coords)
    max_coords = np.repeat(-np.inf, num_coords)
    for cube_pos in cube_positions:
        min_coords = np.minimum(min_coords, cube_pos)
        max_coords = np.maximum(max_coords, cube_pos)
    return min_coords, max_coords


def shift_to_origin(cube_positions: List[np.array], min_coords):
    rel_cube_positions = cube_positions
    for cube_pos in cube_positions:
        cube_pos -= min_coords
    return rel_cube_positions


def run_part1(input_):
    cube_positions = list(get_cube_positions())
    min_coords, max_coords = get_minmax_coords(cube_positions)
    rel_cube_positions = shift_to_origin(cube_positions, min_coords)

    grid = np.zeros()





def run_part2(input_):
    pass


def get_input(file_path, line_sep=None):
    with open(file_path) as f:
        input_ = f.read()

    if line_sep is not None:
        input_ = input_.split(line_sep)
    return input_


if __name__ == '__main__':
    main(RUN_TEST, TEST_NUM, PART, TEST_INPUT_PATH1, TEST_INPUT_PATH2, INPUT_PATH)

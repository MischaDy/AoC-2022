from itertools import product
from typing import Set

import numpy as np

RUN_TEST = False
TEST_NUM = 2
PART = 1

TEST_INPUT_PATH1 = 'test_input1.txt'
TEST_INPUT_PATH2 = 'test_input2.txt'
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
        yield tuple(map(int, line.split(',')))


def get_offsets(num_dims=3):
    offset_range = [-1, 0, +1]
    offsets = product(offset_range, repeat=num_dims)
    # offset changes exactly one coordinate
    return filter(lambda o: np.abs(o).sum() == 1, offsets)


# def get_neighbors(pos, cube_positions: Set[np.ndarray]):
#     for offset in get_offsets():
#         neighbor = pos + offset
#         if neighbor in cube_positions:
#             yield neighbor


def add_elements(iterable1, iterable2, to=tuple):
    sum_ = []
    for elem1, elem2 in zip(iterable1, iterable2):
        sum_.append(elem1 + elem2)
    return to(sum_)


def count_neighbors(pos, cube_positions: Set[tuple]):
    return sum(1 for offset in get_offsets()
               if add_elements(pos, offset) in cube_positions)


def run_part1(input_):
    cube_positions = set(get_cube_positions(input_))
    num_faces = 0
    for cube_pos in cube_positions:
        num_neighbors = count_neighbors(cube_pos, cube_positions)
        cube_faces = 6 - num_neighbors
        num_faces += cube_faces
    return num_faces


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

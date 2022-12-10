from functools import reduce
from itertools import product, takewhile
# from math import prod
from typing import Set, Tuple

RUN_TEST = True
PART = 2

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n')
    print(day_function(input_))


def run_part1(input_):
    dirs = '><v^'
    heights = [list(map(int, line))
               for line in input_]
    visibles = set()
    for dir_ in dirs:
        new_visibles = get_visibles(heights, dir_)
        visibles.update(new_visibles)
    return len(visibles)


def get_visibles(heights, dir_):
    if dir_ == '>':
        visibles = get_visibles_l2r(heights)
    elif dir_ == '<':
        visibles = get_visibles_r2l(heights)
    elif dir_ == 'v':
        visibles = get_visibles_u2d(heights)
    else:
        visibles = get_visibles_d2u(heights)
    return visibles


def get_visibles_l2r(heights) -> Set[Tuple[int, int]]:
    visibles = set()
    for row, line in enumerate(heights):
        cur_row_max = float('-inf')
        for col, height in enumerate(line):
            if height > cur_row_max:
                visibles.add((row, col))
                cur_row_max = height
    return visibles


def get_visibles_r2l(heights) -> Set[Tuple[int, int]]:
    visibles = set()
    for row, line in enumerate(heights):
        cur_row_max = float('-inf')
        indexed_line = list(enumerate(line))
        for col, height in reversed(indexed_line):
            if height > cur_row_max:
                visibles.add((row, col))
                cur_row_max = height
    return visibles


def get_visibles_u2d(heights) -> Set[Tuple[int, int]]:
    rot_heights = transpose(heights)
    heights_horiz = get_visibles_l2r(rot_heights)
    return switch_coords(heights_horiz)


def get_visibles_d2u(heights) -> Set[Tuple[int, int]]:
    rot_heights = transpose(heights)
    heights_horiz = get_visibles_r2l(rot_heights)
    return switch_coords(heights_horiz)


def switch_coords(tuples: Set[Tuple]):
    return set((col, row) for row, col in tuples)


def transpose(list_2d):
    new_rows_gen = map(list, zip(*list_2d))
    return list(new_rows_gen)


def run_part2(input_):
    indices = range(len(input_))
    positions = product(indices, repeat=2)
    heights = [list(map(int, line))
               for line in input_]
    heights_t = transpose(heights)
    scores = []
    for row, col in positions:
        visible_heights = get_visible_heights_from(row, col, heights, heights_t)
        score = prod(visible_heights)
        scores.append(score)
    return scores


# def get_visibles_heights(visibles, heights, max_=float('inf')):
#     for row, col in visibles:
#         height = heights[row][col]
#         if height < max_:
#             yield height


def get_visible_heights_from(row, col, heights, heights_t):
    visible_heights = set()
    tree_height = heights[row][col]

    new_visible_heights = get_visible_heights_horiz(heights[row][col + 1:], tree_height)
    visible_heights.update(new_visible_heights)
    new_visible_heights = get_visible_heights_horiz(reversed(heights[row][:col - 1]),
                                                    tree_height)
    visible_heights.update(new_visible_heights)

    new_visible_heights = get_visible_heights_vert(heights_t[col][row + 1:], tree_height)
    visible_heights.update(new_visible_heights)
    new_visible_heights = get_visible_heights_vert(reversed(heights_t[col][:row - 1]),
                                                   tree_height)
    visible_heights.update(new_visible_heights)
    return visible_heights


def get_visible_heights_horiz(heights, max_=float('inf')) -> Set[Tuple[int, int]]:
    visibles_gen = takewhile(lambda h: h < max_, heights)
    return set(visibles_gen)


def get_visible_heights_vert(heights, max_=float('inf')) -> Set[Tuple[int, int]]:
    visibles_gen = takewhile(lambda h: h < max_, heights)
    return set(visibles_gen)


def prod(iterable):
    if not iterable:
        return 0
    return reduce(lambda x, y: x * y, iterable)


def get_input(file_path, line_sep='\n'):
    with open(file_path) as f:
        input_ = f.read()

    if line_sep:
        input_ = input_.split(line_sep)
    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)

from typing import Set, Tuple

RUN_TEST = False
PART = 1

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n')
    print(day_function(input_))


# def get_heights(visibles, heights):
#     for row, col in visibles:
#         yield heights[row][col]


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


def get_visibles_l2r(heights):
    visibles = set()
    for row, line in enumerate(heights):
        cur_row_max = float('-inf')
        for col, height in enumerate(line):
            if height > cur_row_max:
                visibles.add((row, col))
                cur_row_max = height
    return visibles


def get_visibles_r2l(heights):
    visibles = set()
    for row, line in enumerate(heights):
        cur_row_max = float('-inf')
        indexed_line = list(enumerate(line))
        for col, height in reversed(indexed_line):
            if height > cur_row_max:
                visibles.add((row, col))
                cur_row_max = height
    return visibles


def switch_coords(tuples: Set[Tuple]):
    return set((col, row) for row, col in tuples)


def get_visibles_u2d(heights):
    rot_heights = transpose(heights)
    heights_horiz = get_visibles_l2r(rot_heights)
    return switch_coords(heights_horiz)


def get_visibles_d2u(heights):
    rot_heights = transpose(heights)
    heights_horiz = get_visibles_r2l(rot_heights)
    return switch_coords(heights_horiz)


def transpose(list_2d):
    new_rows_gen = map(list, zip(*list_2d))
    return list(new_rows_gen)


def run_part2(input_):
    pass


def get_input(file_path, line_sep='\n'):
    with open(file_path) as f:
        input_ = f.read()

    if line_sep:
        input_ = input_.split(line_sep)
    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)

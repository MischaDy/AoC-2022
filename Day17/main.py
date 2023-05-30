from copy import deepcopy
from itertools import cycle
from timeit import default_timer

RUN_TEST = True

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'

NUM_LANDED_ROCKS = int(1e5)  # goal: 1e12!!
PRINT = False  # debug

CHAMBER_WIDTH = 7
START_DIST_LEFT = 2  # left edge starts out two units away from left wall
START_DIST_DOWN = 3  # bottom edge starts out three units above the highest rock/floor

ROCK_PATTERNS = [
    ['####'],

    ['.#.',
     '###',
     '.#.'],

    ['..#',
     '..#',
     '###'],

    ['#',
     '#',
     '#',
     '#'],

    ['##',
     '##'],
]


def main(run_test, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    input_ = get_input(file_path)
    print(run_day17(input_))


def run_day17(input_):
    jets_cycle = cycle(input_)
    rocks_cycle = cycle(ROCK_PATTERNS)
    chamber = [['-'] * CHAMBER_WIDTH]

    num_landed_rocks = 0
    pos, rock = place_new_rock(rocks_cycle, chamber)

    if PRINT:
        print('new rock placed...')
        print_state(rock, pos, chamber)
    while num_landed_rocks < NUM_LANDED_ROCKS:
        jet = next(jets_cycle)
        pos = push_rock(jet, pos, rock, chamber)
        pos, has_landed = let_rock_fall(pos, rock, chamber)
        if not has_landed:
            continue
        num_landed_rocks += 1
        chamber = place_landed_rock(rock, pos, chamber)
        pos, rock = place_new_rock(rocks_cycle, chamber)
        if PRINT:
            print('rock landed. new rock placed...')
            print_state(rock, pos, chamber)
    return get_height(chamber)


def print_chamber(chamber):
    chamber_str = '\n'.join(f"|{''.join(row)}|"
                            for row in reversed(chamber))
    print(chamber_str, end=2*'\n')


def print_state(rock, pos, chamber):
    chamber = place_landed_rock_temp(rock, pos, chamber)
    print_chamber(chamber)


def place_new_rock(rocks_cycle, chamber):
    row_ind = get_height(chamber) + START_DIST_DOWN+1  # number of *additional* spaces down
    col_ind = START_DIST_LEFT
    return (row_ind, col_ind), next(rocks_cycle)


def push_rock(jet, pos, rock, chamber):
    if collides(pos, rock, jet, chamber):
        return pos
    row_ind, col_ind = pos
    col_shift = -1 if jet == '<' else +1
    return row_ind, col_ind + col_shift


def collides(pos, rock, jet, chamber):
    row_ind, leftmost_rock_ind = pos
    rightmost_rock_ind = leftmost_rock_ind + get_width(rock) - 1
    if (jet == '<' and leftmost_rock_ind == 0) or (jet == '>' and rightmost_rock_ind == CHAMBER_WIDTH-1):
        # collision with chamber wall
        return True

    max_chamber_index = len(chamber) - 1
    jet_shift = -1 if jet == '<' else +1
    for row_shift, rock_level in enumerate(reversed(rock)):
        rock_row_ind = row_ind + row_shift
        if max_chamber_index < rock_row_ind:
            # chamber not high enough for collision at this level
            continue

        for col_shift, rock_part in enumerate(rock_level):
            if rock_part == '.':
                # empty space can't collide with chamber
                continue
            cur_col = leftmost_rock_ind + col_shift
            if chamber[rock_row_ind][cur_col + jet_shift] == '#':
                return True
    return False


def get_width(rock):
    return len(rock[0])


def let_rock_fall(pos, rock, chamber):
    """

    :param pos:
    :param rock:
    :param chamber:
    :return: tuple of new position and whether the rock has landed
    """
    max_chamber_index = len(chamber) - 1
    row_ind, leftmost_rock_ind = pos
    for row_shift, rock_level in enumerate(reversed(rock)):
        rock_row_ind = row_ind + row_shift
        if max_chamber_index < rock_row_ind - 1:
            # chamber not tall enough to block this level
            continue
        for col_shift, rock_part in enumerate(rock_level):
            if rock_part == '.':
                # empty space can't collide with chamber
                continue
            cur_col = leftmost_rock_ind + col_shift
            if chamber[rock_row_ind-1][cur_col] in ('#', '-'):
                return pos, True
    return (row_ind-1, leftmost_rock_ind), False


def place_landed_rock(rock, pos, chamber):
    max_chamber_index = len(chamber) - 1
    row_ind, col_ind = pos
    rock_width = get_width(rock)
    for row_shift, rock_level in enumerate(reversed(rock)):
        rock_row_ind = row_ind + row_shift
        if max_chamber_index < rock_row_ind:
            # add new rows to chamber
            num_free_spaces_left = col_ind
            num_free_spaces_right = CHAMBER_WIDTH - rock_width - col_ind
            new_row = list(num_free_spaces_left * '.' + rock_level + num_free_spaces_right * '.')
            chamber.append(new_row)
        else:
            # modify existing rows
            for col_shift, rock_col in enumerate(rock_level):
                if rock_col == '.':
                    # empty space doesn't replace anything
                    continue
                chamber[rock_row_ind][col_ind + col_shift] = rock_col
    return chamber


def place_landed_rock_temp(rock, pos, chamber):
    chamber = deepcopy(chamber)
    max_chamber_index = len(chamber) - 1
    row_ind, col_ind = pos
    rock_width = get_width(rock)
    falling_rock = list(map(lambda row: row.replace('#', '@'), rock))
    # add blanks if needed
    if max_chamber_index < row_ind:
        num_blanks = row_ind - max_chamber_index - 1
        chamber.extend([['.'] * CHAMBER_WIDTH] * num_blanks)
    for row_shift, rock_level in enumerate(reversed(falling_rock)):
        rock_row_ind = row_ind + row_shift
        if max_chamber_index < rock_row_ind:
            # add new rows to chamber
            num_free_spaces_left = col_ind
            num_free_spaces_right = CHAMBER_WIDTH - rock_width - col_ind
            new_row = list(num_free_spaces_left * '.' + rock_level + num_free_spaces_right * '.')
            chamber.append(new_row)
        else:
            # modify existing rows
            for col_shift, rock_col in enumerate(rock_level):
                if rock_col == '.':
                    # empty space doesn't replace anything
                    continue
                chamber[rock_row_ind][col_ind + col_shift] = rock_col
    return chamber


def get_height(chamber):
    return len(chamber) - 1  # floor doesn't count


def run_part2(input_):
    pass


def get_input(file_path, line_sep=None):
    with open(file_path) as f:
        input_ = f.read()

    if line_sep is not None:
        input_ = input_.split(line_sep)
    return input_


if __name__ == '__main__':
    t1 = default_timer()
    main(RUN_TEST, TEST_INPUT_PATH, INPUT_PATH)
    t2 = default_timer()
    print(f'duration: {t2-t1}s')

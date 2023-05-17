from itertools import cycle

RUN_TEST = True
PART = 1

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'

NUM_ITERATIONS = 1

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


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path)
    print(day_function(input_))


def run_part1(input_):
    jets_cycle = cycle(input_)
    rocks_cycle = cycle(ROCK_PATTERNS)
    chamber = []

    pos, rock = place_new_rock(rocks_cycle, chamber)
    for i in range(NUM_ITERATIONS):
        pos = push_rock(jets_cycle, pos, rock, chamber)
        pos = let_rock_fall(pos, rock, chamber)
        if has_last_rock_landed(pos, rock, chamber):
            pos, rock = place_new_rock(rocks_cycle)
    return get_height(chamber)


def place_new_rock(rocks_cycle, chamber):
    row = get_height(chamber) + START_DIST_DOWN
    col = START_DIST_LEFT
    return (row, col), next(rocks_cycle)


def push_rock(jets_cycle, pos, rock, chamber):
    jet = next(jets_cycle)
    row, col = pos

    if (jet == '<' and col == 0) or (jet == '>' and col == CHAMBER_WIDTH-1):
        new_col = col
    else:
        new_col = ...
    return row, new_col


def let_rock_fall(pos, rock, chamber):
    pass


def has_last_rock_landed(pos, rock, chamber):
    pass


def get_height(chamber):
    return len(chamber)


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

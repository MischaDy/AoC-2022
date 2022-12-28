from itertools import cycle

from Day17.rock import Rock
from Day17.volatile_defaultdict import VolatileDefaultDict
from misc.helpers import const_factory

RUN_TEST = True
PART = 1

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'
ROCK_PATH = 'rocks.txt'

CHAMBER_WIDTH = 7
LEFT_WALL_DIST = 2
DIST_TO_BOTTOM = 3

# TODO: floor at -1 or 0?


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n')
    print(day_function(input_))


def store(rock, environment):
    for part in rock.parts:
        pass


def let_rock_fall(environment, rock_shape, jet_cycle):
    rock = Rock.from_shape(rock_shape, CHAMBER_WIDTH-1)
    while not rock.has_landed(environment):
        cur_jet = next(jet_cycle)
        rock.move(cur_jet, environment)
        rock.fall(environment)
    store(rock, environment)


def simulate_falling_rocks(num_rocks, jet_stream):
    rock_shapes_cycle = cycle(get_rock_shapes())
    jet_cycle = cycle(jet_stream)
    environment = VolatileDefaultDict(const_factory('.'))
    for rock_ind in range(num_rocks):
        # print(rock_ind)
        rock_shape = next(rock_shapes_cycle)
        let_rock_fall(environment, rock_shape, jet_cycle)
    return environment


def get_rock_shapes():
    return get_input(ROCK_PATH, line_sep='\n')


def get_height(environment):
    pass


def run_part1(input_):
    """
    - rock types as above
    - jets push rocks around
    - vertical chamber is exactly seven units wide.
    - Each rock appears so that its left edge is two units away from the left wall
      and its bottom edge is three units above the highest rock in the room
      (or the floor, if there isn't one).
    """
    num_rocks = 2022
    jet_stream = input_
    environment = simulate_falling_rocks(num_rocks, jet_stream)
    return get_height(environment)


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

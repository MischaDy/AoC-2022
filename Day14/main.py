from itertools import chain

from helpers import minmax

RUN_TEST = False
PART = 1

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n')
    print(day_function(input_))


def points_to_structure(points):
    structure = []
    for (x1, y1), (x2, y2) in zip(points, points[1:]):
        minx, maxx = minmax(x1, x2)
        miny, maxy = minmax(y1, y2)
        s = ((x, y)
             for x in range(minx, maxx + 1)
             for y in range(miny, maxy + 1))
        structure.extend(s)
    return structure


def get_points(rock_path):
    for pointstr in rock_path.split(' -> '):
        point = tuple(map(int, pointstr.split(',')))
        yield point


def get_rocks(input_):
    rocks = set()
    for rock_path in input_:
        points = list(get_points(rock_path))
        rock_structure = points_to_structure(points)
        rocks.update(rock_structure)
    return rocks


def get_ylim(rocks):
    lowest_rock = max(rocks, key=lambda r: r[1])
    return lowest_rock[1] + 1


def is_blocked(pos, sandpile, rocks):
    return pos in sandpile or pos in rocks


def let_sandgrain_fall(sandpile, rocks, source, ylim):
    cur_x, cur_y = source
    can_next_fall = False
    while cur_y < ylim:
        next_y = cur_y + 1
        pos_below = (cur_x, next_y)
        pos_below_left = (cur_x - 1, next_y)
        pos_below_right = (cur_x + 1, next_y)
        if not is_blocked(pos_below, sandpile, rocks):
            cur_x, cur_y = pos_below
        elif not is_blocked(pos_below_left, sandpile, rocks):
            cur_x, cur_y = pos_below_left
        elif not is_blocked(pos_below_right, sandpile, rocks):
            cur_x, cur_y = pos_below_right
        else:
            # blocked, next might be able to be blocked too
            can_next_fall = True
            break
    if can_next_fall:
        sandpile.add((cur_x, cur_y))
    return can_next_fall


def get_minmax_coords(sandpile, rocks, source):
    minx, miny = float('inf'), float('inf')
    maxx, maxy = float('-inf'), float('-inf')
    for x, y in chain(sandpile, rocks, [source]):
        minx, miny = min(minx, x), min(miny, y)
        maxx, maxy = max(maxx, x), max(maxy, y)
    return minx, maxx, miny, maxy


def get_dims(minmax_coords):
    minx, maxx, miny, maxy = minmax_coords
    num_rows = maxy - miny + 1
    num_cols = maxx - minx + 1
    return num_rows, num_cols


def shift(x, y, minmax_coords):
    minx, _, miny, _ = minmax_coords
    shifted_x = x - minx
    shifted_y = y - miny
    return shifted_x, shifted_y


def place_objects(coords, state, minmax_coords, symb):
    for x, y in coords:
        shifted_x, shifted_y = shift(x, y, minmax_coords)
        state[shifted_y][shifted_x] = symb


def draw(sandpile, rocks, source):
    minmax_coords = get_minmax_coords(sandpile, rocks, source)
    num_rows, num_cols = get_dims(minmax_coords)
    state = [['.' for _ in range(num_cols)]
             for _ in range(num_cols)]
    place_objects(sandpile, state, minmax_coords, symb='o')
    place_objects(rocks, state, minmax_coords, symb='#')
    place_objects([source], state, minmax_coords, symb='+')
    state_str = '\n'.join(map(''.join, state))
    print(state_str, end='\n\n')


def run_part1(input_):
    source = (500, 0)
    rocks = get_rocks(input_)
    ylim = get_ylim(rocks)
    sandpile = set()
    can_fall = True
    while can_fall:
        # draw(sandpile, rocks, source)
        can_fall = let_sandgrain_fall(sandpile, rocks, source, ylim)
    return len(sandpile)


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

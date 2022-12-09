from math import copysign

from Day9.gridpoint import GridPoint

RUN_TEST = False
PART = 1

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n')
    print(day_function(input_))


def run_part1(input_):
    cmds = get_cmds(input_)
    tail, head = GridPoint(0, 0), GridPoint(0, 0)
    dir_vectors = {'L': GridPoint(-1, 0),
                   'R': GridPoint(1, 0),
                   'U': GridPoint(0, 1),
                   'D': GridPoint(0, -1),
                   }
    visited = set()
    visited.add(tail.coords)
    for dir_, steps in cmds:
        dir_vect = dir_vectors[dir_]
        for _ in range(steps):
            head += dir_vect
            move_tail(head, tail)
            visited.add(tail.coords)
    return len(visited)


def is_in_range(head: GridPoint, tail: GridPoint):
    delta = head - tail
    return abs(delta.x) <= 1 and abs(delta.y) <= 1


def move_tail(head: GridPoint, tail: GridPoint):
    if is_in_range(head, tail):
        return
    delta_x, delta_y = head - tail
    x_step = copysign(1, delta_x) if delta_x else 0
    y_step = copysign(1, delta_y) if delta_y else 0
    tail += (x_step, y_step)


def get_cmds(lines):
    for line in lines:
        dir_, steps = line.split(' ')
        yield dir_, int(steps)


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

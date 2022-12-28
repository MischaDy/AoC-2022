import re

from Day16.cave import Cave

RUN_TEST = True
PART = 1

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n')
    print(day_function(input_))


def process_line(line):
    name_match = re.match(r'Valve (\w+)', line)
    name = name_match.groups()[-1]

    flow_rate_match = re.search(r'flow rate=(\d+)', line)
    flow_rate = flow_rate_match.groups()[-1]

    neighbor_names = line.split('valves ')[-1].split(', ')
    return name, int(flow_rate), neighbor_names


def to_input_lines(input_):
    input_lines = []
    for line in input_:
        compact_line = process_line(line)
        input_lines.append(compact_line)
    return input_lines


def run_part1(input_):
    input_lines = to_input_lines(input_)
    graph = Cave.from_input_lines(input_lines)
    time_lim = 30
    pressure_released = graph.release_pressure(time_lim)
    return pressure_released


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

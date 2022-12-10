RUN_TEST = False
PART = 1

TEST_INPUT_PATH = 'test_input2.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n')
    print(day_function(input_))


def execute(cmds):
    x = 1
    hist = [x]  # ind i: state of x AFTER cycle i
    for line in cmds:
        if line == 'noop':
            hist.append(x)
        else:
            val = int(line.split(' ')[-1])
            hist.append(x)
            x += val
            hist.append(x)

    return hist


def run_part1(input_):
    cycles = [20, 60, 100, 140, 180, 220]
    hist = execute(input_)
    signal_strengths = [c * hist[c-1] for c in cycles]
    return sum(signal_strengths)


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

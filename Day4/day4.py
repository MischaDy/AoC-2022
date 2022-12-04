RUN_TEST = False
PART = 2

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = day4_part1 if part == 1 else day4_part2
    input_ = get_input(file_path, line_sep='\n')
    print(day_function(input_))


def day4_part1(input_):
    result = 0
    for pair in input_:
        range1, range2 = pair.split(',')
        min1, max1 = map(int, range1.split('-'))
        min2, max2 = map(int, range2.split('-'))
        range2_in_range1 = min1 <= min2 and max2 <= max1
        range1_in_range2 = min2 <= min1 and max1 <= max2
        if range1_in_range2 or range2_in_range1:
            result += 1
    return result


def day4_part2(input_):
    result = 0
    for pair in input_:
        range1, range2 = pair.split(',')
        min1, max1 = map(int, range1.split('-'))
        min2, max2 = map(int, range2.split('-'))
        overlap = min1 in range(min2, max2 + 1) or min2 in range(min1, max1 + 1)
        if overlap:
            result += 1
    return result


def get_input(file_path, line_sep='\n'):
    with open(file_path) as f:
        input_ = f.read()

    if line_sep:
        input_ = input_.split(line_sep)
    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)

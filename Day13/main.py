RUN_TEST = False
PART = 1

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n\n')
    print(day_function(input_))


def compare_lists(left_list, right_list):
    for val_left, val_right in zip(left_list, right_list):
        is_left_int, is_right_int = isinstance(val_left, int), isinstance(val_right, int)

        if is_left_int and is_right_int:
            if val_left == val_right:
                continue
            return val_left < val_right

        elif not is_left_int and not is_right_int:
            result = compare_lists(val_left, val_right)
            if result is None:
                continue
            return result

        else:
            if is_left_int:
                val_left = [val_left]
            else:
                val_right = [val_right]

            result = compare_lists(val_left, val_right)
            if result is None:
                continue
            return result

    if len(left_list) < len(right_list):
        return True
    elif len(left_list) > len(right_list):
        return False
    else:
        return None


def get_line_pairs(input_):
    for str_group in input_:
        left_str, right_str = str_group.split('\n')
        yield eval(left_str), eval(right_str)


def run_part1(input_):
    ordered_inds = []
    for ind, (left, right) in enumerate(get_line_pairs(input_), start=1):
        are_ordered = compare_lists(left, right)
        if are_ordered:
            ordered_inds.append(ind)
    return sum(ordered_inds)


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

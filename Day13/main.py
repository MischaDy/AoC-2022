from math import prod
from random import choice

RUN_TEST = True
PART = 2

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    line_sep = '\n\n' if part == 1 else '\n'
    input_ = get_input(file_path, line_sep=line_sep)
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


def get_packet_pairs(input_):
    for str_group in input_:
        left_str, right_str = str_group.split('\n')
        yield eval(left_str), eval(right_str)


def run_part1(input_):
    ordered_inds = []
    for ind, (left, right) in enumerate(get_packet_pairs(input_), start=1):
        are_ordered = compare_lists(left, right)
        if are_ordered:
            ordered_inds.append(ind)
    return sum(ordered_inds)


def swap(ind1, ind2, list_):
    list_[ind1], list_[ind2] = list_[ind2], list_[ind1]


def quicksort(list_, is_less_than):
    if len(list_) <= 1:
        return
    pivot_ind = choice(range(len(list_)))
    pivot = list_[pivot_ind]
    cur_ind = 0
    while cur_ind < len(list_):
        item = list_[cur_ind]
        if is_less_than(item, pivot):
            continue
        swap(cur_ind, pivot_ind, list_)
        cur_ind += 1
    quicksort(list_[:pivot_ind])
    quicksort(list_[pivot_ind+1:])


def run_part2(input_):
    packets = list(map(eval, filter(None, input_)))
    dividers = ([[2]], [[6]])
    packets.extend(dividers)
    quicksort(packets, compare_lists)
    divider_inds = map(packets.index, dividers)
    return prod(divider_inds)


def get_input(file_path, line_sep=None):
    with open(file_path) as f:
        input_ = f.read()

    if line_sep is not None:
        input_ = input_.split(line_sep)
    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)

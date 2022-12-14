from functools import reduce
from math import floor
from string import ascii_lowercase, ascii_uppercase

from more_itertools import grouper

RUN_TEST = False
PART = 2

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'

LETTERS = ascii_lowercase + ascii_uppercase


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = day3_part1 if part == 1 else day3_part2
    input_ = get_input(file_path)
    print(day_function(input_))


def day3_part1(input_):
    prio_sum = 0
    for items in input_:
        half_size = floor(len(items) / 2)
        part1, part2 = set(items[:half_size]), set(items[half_size:])
        shared_item_set = part1.intersection(part2)
        prio_sum += get_priority(*shared_item_set)
    return prio_sum


def get_priority(char):
    return LETTERS.index(char) + 1


def day3_part2(input_):
    prio_sum = 0
    for group in grouper(input_, 3):
        item_sets = map(set, group)
        shared_item_set = reduce(intersect, item_sets)
        prio_sum += get_priority(*shared_item_set)
    return prio_sum


def intersect(set1, set2):
    return set1.intersection(set2)


def get_input(file_path):
    with open(file_path) as f:
        input_ = f.read().split('\n')

    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)

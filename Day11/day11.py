from functools import reduce
from typing import List, Tuple

from Day11.monkey import Monkey

RUN_TEST = False
PART = 2

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n\n')
    print(day_function(input_))


def run_part1(input_):
    num_rounds = 20
    monkeys = get_monkeys(input_)
    for _ in range(num_rounds):
        for monkey in monkeys:
            monkey.make_turn()
    max_checked1, max_checked2 = sorted(m.num_items_checked for m in monkeys)[-2:]
    return max_checked1 * max_checked2


def get_monkeys(monkey_strs):
    monkeys, cases = [], []
    for monkey_str in monkey_strs:
        cur_lines = map(str.strip, monkey_str.split('\n')[1:])  # ignore first line - id irrelevant
        cur_lines = map(lambda l: l.split(': ')[-1], cur_lines)  # get interesting i.e. 2nd part
        items_str, op_str, div_str, true_case, false_case = cur_lines
        items = _get_items(items_str)
        op = _get_op(op_str)
        div = get_last_int(div_str)
        monkeys += [Monkey(items, op, div)]
        cases.append((true_case, false_case))

    set_next_monkeys(monkeys, cases)
    return monkeys


def _get_items(items_str):
    return list(map(int, items_str.split(', ')))


def _get_op(op_str):
    op_str = op_str.split('= old ')[-1]
    op_str, arg_str = op_str.split(' ')

    def func(old):
        arg = old if arg_str == 'old' else int(arg_str)

        if op_str == '+':
            return old + arg
        return old * arg

    return func


def set_next_monkeys(monkeys, cases_tups: List[Tuple[str, str]]):
    for monkey, cases in zip(monkeys, cases_tups):
        true_monkey_id, false_monkey_id = map(get_last_int, cases)
        monkey.next_monkeys = [monkeys[true_monkey_id], monkeys[false_monkey_id]]


def get_last_int(string, sep=' '):
    """
    extract the integer at the end of string having the form "...<sep><digits>"
    :param string:
    :param sep:
    :return:
    """
    return int(string.split(sep)[-1])


def run_part2(input_):
    num_rounds = 10_000
    monkeys = get_monkeys(input_)
    worry_reducer = get_worry_div(monkeys)
    for _ in range(num_rounds):
        for monkey in monkeys:
            monkey.make_turn2(worry_reducer)
    max_checked1, max_checked2 = sorted(m.num_items_checked for m in monkeys)[-2:]
    return max_checked1 * max_checked2


def get_worry_div(monkeys):
    return prod(m.test_div for m in monkeys)


def prod(iterable):
    return reduce(lambda x, y: x * y, iterable)


def get_input(file_path, line_sep='\n'):
    with open(file_path) as f:
        input_ = f.read()

    if line_sep:
        input_ = input_.split(line_sep)
    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)

from Day21.monkey import Monkey

RUN_TEST = False
PART = 1

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n')
    print(day_function(input_))


def get_monkeys(input_):
    monkeys = dict()
    for line in input_:
        monkey_name, job = line.split(': ')
        if job.isdigit():
            monkey = Monkey(monkey_name, num=int(job))
        else:
            child_left_name, op_name, child_right_name = job.split(' ')
            monkey = Monkey(monkey_name, child_left_name=child_left_name, child_right_name=child_right_name, op_name=op_name)
        monkeys[monkey_name] = monkey
    return monkeys


def run_part1(input_):
    monkeys = get_monkeys(input_)
    root = monkeys['root']
    return root.yell(monkeys)


def run_part2(input_):
    monkeys = get_monkeys(input_)
    root = monkeys['root']
    root.op = lambda a, b: a == b
    human = monkeys['humn']
    ...
    return root.yell(monkeys)


def get_input(file_path, line_sep=None):
    with open(file_path) as f:
        input_ = f.read()

    if line_sep is not None:
        input_ = input_.split(line_sep)
    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)

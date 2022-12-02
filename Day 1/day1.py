RUN_TEST = False
PART = 2

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = day1_part1 if part == 1 else day1_part2

    input_ = get_input(file_path)
    print(day_function(input_))


def day1_part1(input_):
    elves_calories_strs = input_.splitlines('\n\n')
    elves_total_calories = [sum(map(int, elf_calories_strs.splitlines()))
                            for elf_calories_strs in elves_calories_strs]
    return max(elves_total_calories)


def day1_part2(input_):
    elves_calories_strs = input_.split('\n\n')
    elves_total_calories = [sum(map(int, elf_calories_strs.splitlines()))
                            for elf_calories_strs in elves_calories_strs]
    return sum(sorted(elves_total_calories)[-3:])


def get_input(file_path):
    with open(file_path) as f:
        input_ = f.read()

    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)

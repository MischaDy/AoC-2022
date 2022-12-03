RUN_TEST = False
PART = 2

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = day2_part1 if part == 1 else day2_part2
    input_ = get_input(file_path)
    print(day_function(input_))


def day2_part1(input_):
    points = sum(map(calc_points_part1, input_.splitlines()))
    return points


def calc_points_part1(round_):
    shape_points_dict = dict(zip("XYZ", [1, 2, 3]))
    outcome_points_dict = dict(zip([0, 1, 2], [6, 3, 0]))  # order: I win, I draw, I lose
    outcome_dict = {"X": "CAB", "Y": "ABC", "Z": "BCA"}  # order: I win, I draw, I lose

    shape_opp, shape_me = round_.split(' ')
    shape_points = shape_points_dict[shape_me]

    outcome = outcome_dict[shape_me].index(shape_opp)
    outcome_points = outcome_points_dict[outcome]
    return shape_points + outcome_points


def day2_part2(input_):
    points = sum(map(calc_points_part2, input_.splitlines()))
    return points


def calc_points_part2(round_):
    shape_points_dict = dict(zip("ABC", [1, 2, 3]))
    outcome_points_dict = dict(zip("XYZ", [0, 3, 6]))  # order: I lose, I draw, I win

    shape_me_dict = {"A": dict(zip("XYZ", "CAB")),
                     "B": dict(zip("XYZ", "ABC")),
                     "C": dict(zip("XYZ", "BCA"))}

    shape_opp, outcome_needed = round_.split(' ')
    outcome_points = outcome_points_dict[outcome_needed]
    shape_me = shape_me_dict[shape_opp][outcome_needed]
    shape_points = shape_points_dict[shape_me]
    return outcome_points + shape_points


def get_input(file_path):
    with open(file_path) as f:
        input_ = f.read()

    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)

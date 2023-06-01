RUN_TEST = False
PART = 1

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n')
    print(day_function(input_))


def run_part1_temp(list_):
    positions = range(len(list_))
    old_pos_to_new_pos = dict(zip(positions, positions))  # dict of (old_pos, new_pos)
    for old_pos in positions:
        cur_pos = old_pos_to_new_pos[old_pos]
        num = list_.pop(cur_pos)
        new_pos = cur_pos + num
        list_.insert(new_pos, num)  # TODO: fix negative shift
        update_after_shift(old_pos, new_pos, old_pos_to_new_pos)
    grove_coords = get_grove_coords()
    return grove_coords


def run_part1(input_):
    # ls = [[1, 2, -3, 3, -2, 0, 4], [2, 1, -3, 3, -2, 0, 4], [1, -3, 2, 3, -2, 0, 4], [1, 2, 3, -2, -3, 0, 4], [1, 2, -2, -3, 0, 3, 4], [1, 2, -3, 0, 3, 4, -2], [1, 2, -3, 0, 3, 4, -2], [1, 2, -3, 4, 0, 3, -2]]
    nums = list(map(int, input_))
    init_positions = range(len(nums))
    positions = list(init_positions)
    for old_pos in init_positions:
        cur_pos = positions.index(old_pos)

        num = nums.pop(cur_pos)
        positions.pop(cur_pos)  # = old_pos

        new_pos = (cur_pos + num) % len(nums)

        nums.insert(new_pos, num)
        positions.insert(new_pos, old_pos)
    grove_coords = get_grove_coords(nums)
    return sum(grove_coords)


def get_grove_coords(nums):
    pos_0 = nums.index(0)
    grove_coords = [nums[(pos_0 + shift) % len(nums)]
                    for shift in (1000, 2000, 3000)]
    return grove_coords


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

RUN_TEST = False
PART = 2

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n')
    print(day_function(input_))


def run_part1(input_):
    nums = list(map(int, input_))
    init_positions = range(len(nums))
    positions = list(init_positions)
    nums, positions = mix(nums, positions)
    grove_coords = get_grove_coords(nums)
    return sum(grove_coords)


def mix(nums, positions):
    init_positions = range(len(nums))
    for old_pos in init_positions:
        cur_pos = positions.index(old_pos)

        num = nums.pop(cur_pos)
        positions.pop(cur_pos)  # = old_pos

        new_pos = (cur_pos + num) % len(nums)

        nums.insert(new_pos, num)
        positions.insert(new_pos, old_pos)
    return nums, positions


def get_grove_coords(nums):
    pos_0 = nums.index(0)
    grove_coords = [nums[(pos_0 + shift) % len(nums)]
                    for shift in (1000, 2000, 3000)]
    return grove_coords


def run_part2(input_):
    mixings = 10
    decryption_key = 811589153
    nums = [decryption_key * int(val)
            for val in input_]
    init_positions = range(len(nums))
    positions = list(init_positions)
    for mixing in range(mixings):
        nums, positions = mix(nums, positions)
    grove_coords = get_grove_coords(nums)
    return sum(grove_coords)


def get_input(file_path, line_sep=None):
    with open(file_path) as f:
        input_ = f.read()

    if line_sep is not None:
        input_ = input_.split(line_sep)
    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)

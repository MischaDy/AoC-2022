from numpy import sign

RUN_TEST = True
PART = 1

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n')
    print(day_function(input_))


def run_part1(input_):
    print('start')
    nums = list(map(int, input_))
    mixed_nums = nums[:]
    size = len(mixed_nums)
    inds_dict = dict(zip(range(size), range(size)))
    for old_ind, num in enumerate(nums):
        shift(mixed_nums, old_ind, inds_dict)
    grove_coords = get_grove_coords(mixed_nums, inds_dict)
    print('done')
    return sum(grove_coords), grove_coords


def get_grove_coords(mixed_nums, inds_dict):
    size = len(mixed_nums)
    zero_ind = mixed_nums.index(0)
    grove_coords_inds = ((zero_ind + shift) % size
                         for shift in [1000, 2000, 3000])
    grove_coords = [mixed_nums[ind] for ind in grove_coords_inds]
    return grove_coords


def shift_once(list_, cur_ind, shift_dir, inds_dict):
    new_ind = (cur_ind + shift_dir) % len(list_)
    switch(list_, cur_ind, new_ind)
    inds_dict[cur_ind] = new_ind
    inds_dict[new_ind] = cur_ind
    return new_ind


def shift(list_, old_ind, inds_dict):
    cur_ind = inds_dict[old_ind]
    num = list_[cur_ind]
    shift_dir = sign(num)
    for i in range(abs(num)):
        cur_ind = shift_once(list_, cur_ind, shift_dir, inds_dict)


def switch(list_, ind1, ind2):
    list_[ind1], list_[ind2] = list_[ind2], list_[ind1]


def compute_new_ind(list_, cur_ind):
    num = list_[cur_ind]
    new_ind = cur_ind + num
    shift_dir = -1 if new_ind < 0 else +1
    return new_ind % len(list_), shift_dir


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

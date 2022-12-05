RUN_TEST = False
PART = 2

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = day5_part1 if part == 1 else day5_part2
    input_ = get_input(file_path, line_sep='\n\n')
    print(day_function(input_))


def day5_part1(input_):
    crates, instrs_str = input_
    crates_stacks = crates_to_stacks(crates)
    instrs = process_instrs(instrs_str)
    exec_instrs_part1(crates_stacks, instrs)
    return get_codeword(crates_stacks)


def get_codeword(crates_stacks):
    word = ''
    for _, stack in sorted(crates_stacks.items()):
        if stack:
            word += stack[-1]
    return word


def exec_instrs_part1(stacks, instrs):
    for num_crates, start, end in instrs:
        stacks[start], crates_lifted_rev = split_at(stacks[start], -num_crates)
        crates_lifted = list(reversed(crates_lifted_rev))
        stacks[end] += crates_lifted


def split_at(list_, ind):
    return list_[:ind], list_[ind:]


def exec_instrs_part2(stacks, instrs):
    for num_crates, start, end in instrs:
        stacks[start], crates_lifted = split_at(stacks[start], -num_crates)
        stacks[end] += crates_lifted


def crates_to_stacks(crates_str):
    content_width = 1   # number of symbols between [brackets]
    crate_width = content_width + 2  # total number of symbols including [brackets]

    crates_rows = crates_str.split('\n')
    crates_rows, stack_ids_list = split_at(crates_rows, -1)
    stack_ids = stack_ids_list[0].strip().split(crate_width * ' ')

    stacks = dict()
    for stack_id in map(int, stack_ids):
        cur_stack = []
        for crate_row in reversed(crates_rows):
            start, end = range_from_stack_id(stack_id, content_width)
            content = crate_row[start:end].strip('[] ')
            if content:  # crate content is empty if no crate there - ignore!
                cur_stack.append(content)
        stacks[stack_id] = cur_stack
    return stacks


def range_from_stack_id(stack_id, crate_width):
    start = (stack_id - 1) * (crate_width + 3)  # inclusive
    end = stack_id * (crate_width + 3) - 1  # exclusive
    return start, end


def process_instrs(instrs_str):
    # return instructions in the form (x, y, z) consisting of ints
    instrs = []
    for instr in instrs_str.split('\n'):
        tokens = instr.split(' ')
        nums_gen = filter(lambda t: t.isdigit(), tokens)
        instrs.append(tuple(map(int, nums_gen)))
    return instrs


def day5_part2(input_):
    crates, instrs_str = input_
    crates_stacks = crates_to_stacks(crates)
    instrs = process_instrs(instrs_str)
    exec_instrs_part2(crates_stacks, instrs)
    return get_codeword(crates_stacks)


def get_input(file_path, line_sep='\n'):
    with open(file_path) as f:
        input_ = f.read()

    if line_sep:
        input_ = input_.split(line_sep)
    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)

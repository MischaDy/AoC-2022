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
    exec_instrs1(crates_stacks, instrs)
    return get_codeword(crates_stacks)


def get_codeword(crates_stacks):
    word = ''
    for _, stack in sorted(crates_stacks.items()):
        if stack:
            word += stack[-1]
    return word


def exec_instrs1(crates_stacks, instrs):
    for instr in instrs:
        num_crates, start, end = instr
        for _ in range(num_crates):
            crates_stacks[end].append(crates_stacks[start].pop())


def exec_instrs2(crates_stacks, instrs):
    for instr in instrs:
        num_crates, start, end = instr
        crates_lifted = crates_stacks[start][-num_crates:]
        crates_stacks[start] = crates_stacks[start][:-num_crates]
        crates_stacks[end].extend(crates_lifted)


def crates_to_stacks(crates_str):
    crates = crates_str.split('\n')
    crate_width = 3   # = len('[X]')
    crates, stack_nums = crates[:-1], crates[-1]
    stack_nums = stack_nums.strip().split(crate_width * ' ')
    stacks = dict()
    for stack_num in map(int, stack_nums):
        cur_stack = []
        for crate_row in reversed(crates):
            crate_start, crate_end = crate_range_from_stack_num(stack_num)
            crate_item = crate_row[crate_start:crate_end].strip('[] ')
            if crate_item:
                cur_stack.append(crate_item)
        stacks[stack_num] = cur_stack
    return stacks


def crate_range_from_stack_num(stack_num):
    # based on crate_width = 3
    start = 4 * (stack_num - 1)
    end = 4 * stack_num - 1  # exclusive
    return start, end


def process_instrs(instrs_str):
    instrs = []
    for instr in instrs_str.split('\n'):
        tokens = instr.split(' ')
        instr = map(int, filter(lambda char: char.isdigit(), tokens))
        instr = list(instr)
        instrs.append(instr)
    return instrs


def day5_part2(input_):
    crates, instrs_str = input_
    crates_stacks = crates_to_stacks(crates)
    instrs = process_instrs(instrs_str)
    exec_instrs2(crates_stacks, instrs)
    return get_codeword(crates_stacks)


def get_input(file_path, line_sep='\n'):
    with open(file_path) as f:
        input_ = f.read()

    if line_sep:
        input_ = input_.split(line_sep)
    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)

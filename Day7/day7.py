from Day7.directory import Directory

RUN_TEST = False
PART = 1

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n')
    print(day_function(input_))


def run_part1(input_):
    size_lim = 100000
    root = Directory('/')
    cur_dir = root
    for i, line in enumerate(input_[1:], start=2):  # assume "cd /" as first cmd
        if is_command(line):
            if line == '$ ls':
                continue

            target_dir = line.split(' ')[-1]
            if target_dir == '/':
                cur_dir = root
            elif target_dir == '..':
                cur_dir = cur_dir.parent
            else:
                # TODO: Change!
                # cur_dir.add_child(target_dir)
                child = cur_dir.get_child(target_dir)
                cur_dir = child  # cur_dir.get_child(target_dir)

        else:
            line_prefix, name = line.split(' ')
            size = line_prefix if line_prefix != 'dir' else 0
            cur_dir.add_child(name, size)
        pass

    # root.prettyprint()

    subdirs = root.get_all_subdirs()
    small_sizes = [s.get_size() for s in subdirs
                   if s.get_size() <= size_lim]
    return sum(small_sizes)


def parse_cmd(cmd, cur_path, filesys):
    if 'ls' in cmd:
        return cur_path, filesys

    target_dir = cmd.split(' ')[-1]
    cur_path.append(target_dir)

    return cur_path, filesys


def is_command(line):
    return line.startswith('$')


def run_part2(input_):
    pass


def get_input(file_path, line_sep='\n'):
    with open(file_path) as f:
        input_ = f.read()

    if line_sep:
        input_ = input_.split(line_sep)
    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)

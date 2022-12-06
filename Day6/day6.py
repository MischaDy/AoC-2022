from collections import deque
from functools import partial

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
    maxlen = 4
    # list & map to handle the multiple example inputs
    proc_buf_packet = partial(process_buffer, maxlen=maxlen)
    results = list(map(proc_buf_packet, input_))
    if len(results) == 1:
        results = results.pop()
    return results


def process_buffer(buf, maxlen):
    buf_head, buf_tail = split_at(buf, maxlen)
    q = deque(buf_head, maxlen)
    for pos, char in enumerate(buf_tail, start=maxlen):
        if is_unique(q):
            return pos
        q.append(char)
    raise ValueError('ERROR: buffer has no start-of-packet marker')


def is_unique(queue):
    return len(queue) == len(set(queue))


def split_at(list_, ind):
    return list_[:ind], list_[ind:]


def run_part2(input_):
    maxlen = 14
    # list & map to handle the multiple example inputs
    proc_buf_msg = partial(process_buffer, maxlen=maxlen)
    results = list(map(proc_buf_msg, input_))
    if len(results) == 1:
        results = results.pop()
    return results


def get_input(file_path, line_sep='\n'):
    with open(file_path) as f:
        input_ = f.read()

    if line_sep:
        input_ = input_.split(line_sep)
    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)

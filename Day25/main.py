from math import log, floor

RUN_TEST = True
PART = 1

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'

SNAFU_TO_DEC_DIGITS = dict(zip('=-012', range(-2, 2+1)))


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n')
    print(day_function(input_))


def run_part1(input_):
    pass


def get_next_power(dec, base):
    return floor(log(dec, base))


def convert_dec(dec_str, base):
    dec = int(dec_str)
    converted_str = ''
    next_power = get_next_power(dec, base)
    while next_power >= 0:
        next_power = get_next_power(dec, base)
        next_factor = base ** next_power
        pent_digit = dec // next_factor
        dec -= pent_digit * next_factor
        converted_str = converted_str + str(pent_digit)
    return converted_str


def dec_to_pent(dec_str):
    if dec_str == '0':
        return dec_str
    return convert_dec(dec_str, base=5)


def dec_to_snafu(dec_str):
    pent = dec_to_pent(dec_str)
    snafu = 0
    for ind, pent_digit in enumerate(reversed(pent)):
        # TODO: Adjust!  (0,3) -> (1,=);  (0,4) -> (1,-)
        factor = 5 ** ind
        snafu = SNAFU_TO_DEC_DIGITS[pent_digit]
        snafu += factor * snafu
    return str(snafu)


def snafu_to_dec(snafu_str):
    dec = 0
    for ind, snafu_digit in enumerate(reversed(snafu_str)):
        factor = 5 ** ind
        dec_digit = SNAFU_TO_DEC_DIGITS[snafu_digit]
        dec += factor * dec_digit
    return str(dec)


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

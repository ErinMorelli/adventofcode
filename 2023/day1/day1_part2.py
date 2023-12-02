#!/usr/bin/env python
"""
--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are
actually spelled out with letters: `one`, `two`, `three`, `four`, `five`,
`six`, `seven`, `eight`, and `nine` also count as valid "digits".

Equipped with this new information, you now need to find the real first and
last digit on each line. For example:

    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen

In this example, the calibration values are `29`, `83`, `13`, `24`, `42`,
`14`, and `76`. Adding these together produces `281`.

What is the sum of all of the calibration values?
"""
import re

input_file = 'input.txt'

digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

digit_regex = r'|'.join(digits.keys())
regex = re.compile(rf'(?=(\d|{digit_regex}))\s*.')

total = 0

for line in raw_data:
    res = regex.findall(line)
    first = res[0] if res[0] not in digits.keys() else digits[res[0]]
    last = res[-1] if res[-1] not in digits.keys() else digits[res[-1]]
    calibration_value = int(f'{first}{last}')
    total += calibration_value

print(total)

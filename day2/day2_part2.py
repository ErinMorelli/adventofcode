#!/usr/bin/env python
"""
Each policy actually describes two positions in the password, where 1 means
the first character, 2 means the second character, and so on. (Be careful;
Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of
these positions must contain the given letter. Other occurrences of the letter
are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation
of the policies?
"""
import re

input_file = 'input.txt'
regex = r'(?P<pos1>\d+)\-(?P<pos2>\d+) (?P<char>[a-z]): (?P<pwd>[a-z]+)'

with open(input_file, 'r') as fh:
    valid = []

    for _line in fh:
        line = _line.strip()

        match = re.match(regex, line)
        pos1 = int(match.group('pos1'), 10)
        pos2 = int(match.group('pos2'), 10)
        char = match.group('char')
        pwd = match.group('pwd')

        idx1 = pos1 - 1
        idx2 = pos2 - 1

        if (
                (pwd[idx1] == char and pwd[idx2] != char) or
                (pwd[idx1] != char and pwd[idx2] == char)
        ):
            valid.append(line)

    print(f'valid: {len(valid)}')

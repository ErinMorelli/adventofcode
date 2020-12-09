#!/usr/bin/env python
"""
To try to debug the problem, they have created a list (your puzzle input) of
passwords (according to the corrupted database) and the corporate policy when
that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy
indicates the lowest and highest number of times a given letter must appear
for the password to be valid. For example, 1-3 a means that the password must
contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is
not; it contains no instances of b, but needs at least 1. The first and third
passwords are valid: they contain one a or nine c, both within the limits of
their respective policies.

How many passwords are valid according to their policies?
"""
import re

input_file = 'input.txt'
regex = r'(?P<min>\d+)\-(?P<max>\d+) (?P<char>[a-z]): (?P<pwd>[a-z]+)'

with open(input_file, 'r') as fh:
    valid = []

    for _line in fh:
        line = _line.strip()

        match = re.match(regex, line)
        min = int(match.group('min'), 10)
        max = int(match.group('max'), 10)
        char = match.group('char')
        pwd = match.group('pwd')

        result = re.findall(char, pwd)
        count = len(result)

        if min <= count <= max:
            valid.append(line)

    print(f'valid: {len(valid)}')

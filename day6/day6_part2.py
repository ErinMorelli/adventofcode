#!/usr/bin/env python
"""
You don't need to identify the questions to which anyone answered "yes"; you
need to identify the questions to which everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b

This list represents answers from five groups:

    In the first group, everyone (all 1 person) answered "yes" to 3 questions:
        a, b, and c.
    In the second group, there is no question to which everyone answered "yes".
    In the third group, everyone answered yes to only 1 question, a. Since
        some people did not answer "yes" to b or c, they don't count.
    In the fourth group, everyone answered yes to only 1 question, a.
    In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.

In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes".
What is the sum of those counts?
"""
import re

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read()

groups = re.compile(r'^$', re.M).split(raw_data.strip())

total = 0

for g in groups:
    answers = g.strip().replace('\n', ' ').split(' ')
    unique = [set(a) for a in answers]

    if len(answers) == 1:
        total += len(unique[0])
        continue

    joint = unique[0].intersection(*unique[1:])
    total += len(joint)

print(f'total: {total}')

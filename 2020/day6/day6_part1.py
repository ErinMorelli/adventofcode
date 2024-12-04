#!/usr/bin/env python
"""
Another group asks for your help, then another, and eventually you've
collected answers from every group on the plane (your puzzle input). Each
group's answers are separated by a blank line, and within each group, each
person's answers are on a single line. For example:

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

    The first group contains one person who answered "yes" to 3 questions:
        a, b, and c.
    The second group contains three people; combined, they answered "yes" to
        3 questions: a, b, and c.
    The third group contains two people; combined, they answered "yes" to 3
        questions: a, b, and c.
    The fourth group contains four people; combined, they answered "yes" to
        only 1 question, a.
    The last group contains one person who answered "yes" to only 1 question, b.

In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes".
What is the sum of those counts?
"""
import re

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read()

groups = re.compile(r'^$', re.M).split(raw_data.strip())

total = 0

for g in groups:
    answers = g.strip().replace('\n', '')
    unique = set(answers)
    total += len(unique)

print(f'total: {total}')

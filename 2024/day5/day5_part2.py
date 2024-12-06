#!/usr/bin/env python
"""
--- Part Two ---

While the Elves get to work printing the correctly-ordered updates, you have a
little time to fix the rest of them.

For each of the incorrectly-ordered updates , use the page ordering rules to
put the page numbers in the right order. For the above example, here are the
three incorrectly-ordered updates and their correct orderings:

  * `75,97,47,61,53` becomes `97,75,47 ,61,53`.
  * `61,13,29` becomes `61,29 ,13`.
  * `97,13,75,29,47` becomes `97,75,47 ,29,13`.

After taking only the incorrectly-ordered updates and ordering them correctly,
their middle page numbers are `47`, `29`, and `47`. Adding these together
produces `123`.

Find the updates which are not in the correct order. What do you get if you
add up the middle page numbers after correctly ordering just those updates?
"""
from re import split

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read()

[a, b] = split(r'\n\n', raw_data)

rules = [[int(y) for y in x.split('|')] for x in a.split('\n')]
updates = [[int(y) for y in x.split(',')] for x in b.split('\n')]

def is_valid(u):
    for x, y in rules:
        if x not in u or y not in u:
            continue
        if u.index(x) > u.index(y):
           return False
    return True

bad = set()

for i, update in enumerate(updates):
    if not is_valid(update):
        bad.add(i)

def fix(item):
    for j, k in rules:
        if j not in item or k not in item:
            continue

        ji = item.index(j)
        ki = item.index(k)

        if ji > ki:
            temp = item[ji]
            item[ji] = item[ki]
            item[ki] = temp
            return fix(item)

    return item

total = 0

for idx in bad:
    update = updates[idx]
    fixed = fix(update)
    mid_idx = int(len(update) / 2)
    total += update[mid_idx]

print(total)

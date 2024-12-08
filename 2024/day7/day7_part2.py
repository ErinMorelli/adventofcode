#!/usr/bin/env python
"""
--- Part Two ---

The engineers seem concerned; the total calibration result you gave them is
nowhere close to being within safety tolerances. Just then, you spot your
mistake: some well-hidden elephants are holding a third type of operator.

The concatenation operator (`||`) combines the digits from its left and right
inputs into a single number. For example, `12 || 345` would become `12345`.
All operators are still evaluated left-to-right.

Now, apart from the three equations that could be made true using only
addition and multiplication, the above example has three more equations that
can be made true by inserting operators:

  * `156: 15 6` can be made true through a single concatenation: `15 || 6 = 156`.
  * `7290: 6 8 6 15` can be made true using `6 * 8 || 6 * 15`.
  * `192: 17 8 14` can be made true using `17 || 8 + 14`.

Adding up all six test values (the three that could be made before using only
`+` and `*` plus the new three that can now be made by also using `||`)
produces the new total calibration result of `11387`.

Using your new knowledge of elephant hiding spots, determine which equations
could possibly be true. What is their total calibration result?
"""
from math import prod

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()


class Node:
    def __init__(self, a, b, parent=None):
        self.a = a
        self.b = b
        self.parent = parent
        self.sum = a + b
        self.prod = a * b
        self.concat = int(f'{a}{b}')

good = []

for line in raw_data:
    x, y = line.split(': ')

    ans = int(x)
    nums = [int(x) for x in y.split(' ')]
    concat_nums = int(y.replace(' ', ''))

    if sum(nums) == ans or prod(nums) == ans or concat_nums == ans:
        good.append(ans)
        continue

    if len(nums) == 2:
        continue

    slots = len(nums) - 1
    root = Node(nums[0], nums[1])
    idx = 2

    def check(i, curr):
        is_last = i == slots

        node1 = Node(curr.sum, nums[i], curr)
        node2 = Node(curr.prod, nums[i], curr)
        node3 = Node(curr.concat, nums[i], curr)

        if is_last:
            valid_sum = node1.sum == ans or node2.sum == ans or node3.sum == ans
            valid_prod = node1.prod == ans or node2.prod == ans or node3.prod == ans
            valid_concat = node1.concat == ans or node2.concat == ans or node3.concat == ans
            return valid_sum or valid_prod or valid_concat

        return check(i + 1, node1) or check(i + 1, node2) or check(i + 1, node3)

    if check(idx, root):
        good.append(ans)

print(sum(good))



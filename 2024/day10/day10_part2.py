#!/usr/bin/env python
"""
--- Part Two ---

The reindeer spends a few minutes reviewing your hiking trail map before
realizing something, disappearing for a few minutes, and finally returning
with yet another slightly-charred piece of paper.

The paper describes a second way to measure a trailhead called its rating. A
trailhead's rating is the number of distinct hiking trails which begin at that
trailhead. For example:

    .....0.
    ..4321.
    ..5..2.
    ..6543.
    ..7..4.
    ..8765.
    ..9....

The above map has a single trailhead; its rating is `3` because there are
exactly three distinct hiking trails which begin at that position:

    .....0.   .....0.   .....0.
    ..4321.   .....1.   .....1.
    ..5....   .....2.   .....2.
    ..6....   ..6543.   .....3.
    ..7....   ..7....   .....4.
    ..8....   ..8....   ..8765.
    ..9....   ..9....   ..9....

Here is a map containing a single trailhead with rating `13`:

    ..90..9
    ...1.98
    ...2..7
    6543456
    765.987
    876....
    987....

This map contains a single trailhead with rating `227` (because there are
`121` distinct hiking trails that lead to the `9` on the right edge and `106`
that lead to the `9` on the bottom edge):

    012345
    123456
    234567
    345678
    4.6789
    56789.

Here's the larger example from before:

    89010123
    78121874
    87430965
    96549874
    45678903
    32019012
    01329801
    10456732

Considering its trailheads in reading order, they have ratings of `20`, `24`,
`10`, `4`, `1`, `4`, `5`, `8`, and `5`. The sum of all trailhead ratings in
this larger example topographic map is `81`.

You're not sure how, but the reindeer seems to have crafted some tiny flags
out of toothpicks and bits of paper and is using them to mark trailheads on
your topographic map. What is the sum of the ratings of all trailheads?
"""
import re

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

data = []
trailheads = []

for i, line in enumerate(raw_data):
    row = [int(x) for x in list(line)]
    data.append(row)
    for j in re.finditer(r'0', line):
        trailheads.append((j.start(), i))

max_y = len(data)
max_x = len(data[0])

scores = list()

for th in trailheads:
    ends = list()

    def step(x, y, h):
        next_h = h + 1
        is_end = next_h == 9

        # up
        if y - 1 >= 0 and data[y - 1][x] == next_h:
            if is_end:
                ends.append((x, y - 1))
            else:
                step(x, y - 1, next_h)

        # down
        if y + 1 < max_y and data[y + 1][x] == next_h:
            if is_end:
                ends.append((x, y + 1))
            else:
                step(x, y + 1, next_h)

        # left
        if x - 1 >= 0 and data[y][x - 1] == next_h:
            if is_end:
                ends.append((x - 1, y))
            else:
                step(x - 1, y, next_h)

        # right
        if x + 1 < max_x and data[y][x + 1] == next_h:
            if is_end:
                ends.append((x + 1, y))
            else:
                step(x + 1, y, next_h)

    step(th[0], th[1], 0)

    scores.append(len(ends))

print(sum(scores))

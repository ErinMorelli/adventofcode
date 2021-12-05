#!/usr/bin/env python
"""
--- Part Two ---

Unfortunately, considering only horizontal and vertical lines doesn't give you
the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in
your list will only ever be horizontal, vertical, or a diagonal line at
exactly 45 degrees. In other words:

  * An entry like `1,1 -> 3,3` covers points `1,1`, `2,2`, and `3,3`.
  * An entry like `9,7 -> 7,9` covers points `9,7`, `8,8`, and `7,9`.

Considering all lines from the above example would now produce the following
diagram:

    1.1....11.
    .111...2..
    ..2.1.111.
    ...1.2.2..
    .112313211
    ...1.2....
    ..1...1...
    .1.....1..
    1.......1.
    222111....

You still need to determine the number of points where at least two lines
overlap. In the above example, this is still anywhere in the diagram with a
`2` or larger - now a total of `12` points.

Consider all of the lines. At how many points do at least two lines overlap?
"""
from collections import defaultdict

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

coords = [[[int(z, 10) for z in y.split(',')] for y in x.split(' -> ')] for x in raw_data]

counts = defaultdict(lambda: 0)

for coord in coords:
    x1, y1 = coord[0][0], coord[0][1]
    x2, y2 = coord[1][0], coord[1][1]

    # horizontal
    if x1 == x2:
        if y1 > y2:
            while y1 >= y2:
                counts[f'{x1},{y2}'] += 1
                y2 += 1
        elif y2 > y1:
            while y2 >= y1:
                counts[f'{x1},{y1}'] += 1
                y1 += 1
        else:
            counts[f'{x1},{y1}'] += 1
        continue

    # vertical
    if y1 == y2:
        if x1 > x2:
            while x1 >= x2:
                counts[f'{x2},{y1}'] += 1
                x2 += 1
        elif x2 >= x1:
            while x2 >= x1:
                counts[f'{x1},{y1}'] += 1
                x1 += 1
        else:
            counts[f'{x1},{y1}'] += 1
        continue

    # diagonal
    if x1 > x2:
        if y1 > y2:
            while x1 >= x2 and y1 >= y2:
                counts[f'{x2},{y2}'] += 1
                x2 += 1
                y2 += 1
        elif y2 > y1:
            while x1 >= x2 and y2 >= y1:
                counts[f'{x2},{y2}'] += 1
                x2 += 1
                y2 -= 1
        continue

    if x2 > x1:
        if y1 > y2:
            while x2 >= x1 and y1 >= y2:
                counts[f'{x1},{y1}'] += 1
                x1 += 1
                y1 -= 1
        elif y2 > y1:
            while x2 >= x1 and y2 >= y1:
                counts[f'{x1},{y1}'] += 1
                x1 += 1
                y1 += 1


count = 0

for k, v in counts.items():
    if v >= 2:
        count += 1

print(count)

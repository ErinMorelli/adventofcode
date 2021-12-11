#!/usr/bin/env python
"""
--- Part Two ---

Next, you need to find the largest basins so you know what areas are most
important to avoid.

A basin is all locations that eventually flow downward to a single low point.
Therefore, every low point has a basin, although some basins are very small.
Locations of height `9` do not count as being in any basin, and all other
locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the
low point. The example above has four basins.

The top-left basin, size `3`:

    2199943210
    3987894921
    9856789892
    8767896789
    9899965678

The top-right basin, size `9`:

    2199943210
    3987894921
    9856789892
    8767896789
    9899965678

The middle basin, size `14`:

    2199943210
    3987894921
    9856789892
    8767896789
    9899965678

The bottom-right basin, size `9`:

    2199943210
    3987894921
    9856789892
    8767896789
    9899965678

Find the three largest basins and multiply their sizes together. In the above
example, this is `9 * 14 * 9 = 1134`.

What do you get if you multiply together the sizes of the three largest
basins?
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

from pprint import pprint

data = [[int(y, 10) for y in x] for x in raw_data]

lows = []

for ri, row in enumerate(data):
    for ci, col in enumerate(row):
        n = data[ri-1][ci] if ri-1 >= 0 else 10
        s = data[ri+1][ci] if ri+1 < len(data) else 10
        e = row[ci+1] if ci+1 < len(row) else 10
        w = row[ci-1] if ci-1 >= 0 else 10

        if col < n and col < s and col < e and col < w:
            lows.append(col + 1)

result = sum(lows)

print(f'Result: {result}')
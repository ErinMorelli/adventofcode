#!/usr/bin/env python
"""
--- Part Two ---

Watching over your shoulder as you work, one of The Historians asks if you
took the effects of resonant harmonics into your calculations.

Whoops!

After updating your model, it turns out that an antinode occurs at any grid
position exactly in line with at least two antennas of the same frequency,
regardless of distance. This means that some of the new antinodes will occur
at the position of each antenna (unless that antenna is the only one of its
frequency).

So, these three `T`-frequency antennas now create many antinodes:

    T....#....
    ...T......
    .T....#...
    .........#
    ..#.......
    ..........
    ...#......
    ..........
    ....#.....
    ..........

In fact, the three `T`-frequency antennas are all exactly in line with two
antennas, so they are all also antinodes! This brings the total number of
antinodes in the above example to `9`.

The original example now has `34` antinodes, including the antinodes that
appear on every antenna:

    ##....#....#
    .#.#....0...
    ..#.#0....#.
    ..##...0....
    ....0....#..
    .#...#A....#
    ...#..#.....
    #....#.#....
    ..#.....A...
    ....#....A..
    .#........#.
    ...#......##

Calculate the impact of the signal using this updated model. How many unique
locations within the bounds of the map contain an antinode?
"""
import re
from collections import defaultdict

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

len_y = len(raw_data)
len_x = len(raw_data[0])

ants = defaultdict(list)

for y, line in enumerate(raw_data):
    for a in re.finditer(r'[a-zA-Z0-9]', line):
        x = a.start()
        val = a.group(0)
        ants[val].append((x, y))

antinodes = set()

for ant, nodes in ants.items():
    if len(nodes) < 2:
        continue

    for i in range(0, len(nodes)):
        for j in range(i + 1, len(nodes)):
            x1, y1 = nodes[i]
            antinodes.add(f'{x1},{y1}')

            x2, y2 = nodes[j]
            antinodes.add(f'{x2},{y2}')

            diff_x = x1 - x2
            diff_y = y1 - y2

            anA = (x1 + diff_x, y1 + diff_y)
            anB = (x2 - diff_x, y2 - diff_y)

            while 0 <= anA[0] < len_x and 0 <= anA[1] < len_y:
                antinodes.add(f'{anA[0]},{anA[1]}')
                anA = (anA[0] + diff_x, anA[1] + diff_y)

            while 0 <= anB[0] < len_x and 0 <= anB[1] < len_y:
                antinodes.add(f'{anB[0]},{anB[1]}')
                anB = (anB[0] - diff_x, anB[1] - diff_y)

print(len(antinodes))

#!/usr/bin/env python
"""
--- Day 11: Cosmic Expansion ---

You continue following signs for "Hot Springs" and eventually come across an
[observatory](https://en.wikipedia.org/wiki/Observatory). The Elf within turns
out to be a researcher studying cosmic expansion using the giant telescope
here.

He doesn't know anything about the missing machine parts; he's only visiting
for this research project. However, he confirms that the hot springs are the
next-closest area likely to have people; he'll even take you straight there
once he's done with today's observation analysis.

Maybe you can help him with the analysis to speed things up?

The researcher has collected a bunch of data and compiled the data into a
single giant image (your puzzle input). The image includes empty space (`.`)
and galaxies (`#`). For example:

    ...#......
    .......#..
    #.........
    ..........
    ......#...
    .#........
    .........#
    ..........
    .......#..
    #...#.....

The researcher is trying to figure out the sum of the lengths of the shortest
path between every pair of galaxies. However, there's a catch: the universe
expanded in the time it took the light from those galaxies to reach the
observatory.

Due to something involving gravitational effects, only some space expands. In
fact, the result is that any rows or columns that contain no galaxies should
all actually be twice as big.

In the above example, three columns and two rows contain no galaxies:

       v  v  v
     ...#......
     .......#..
     #.........
    >..........<
     ......#...
     .#........
     .........#
    >..........<
     .......#..
     #...#.....
       ^  ^  ^

These rows and columns need to be twice as big; the result of cosmic expansion
therefore looks like this:

    ....#........
    .........#...
    #............
    .............
    .............
    ........#....
    .#...........
    ............#
    .............
    .............
    .........#...
    #....#.......

Equipped with this expanded universe, the shortest path between every pair of
galaxies can be found. It can help to assign every galaxy a unique number:

    ....1........
    .........2...
    3............
    .............
    .............
    ........4....
    .5...........
    ............6
    .............
    .............
    .........7...
    8....9.......

In these 9 galaxies, there are 36 pairs. Only count each pair once; order
within the pair doesn't matter. For each pair, find any shortest path between
the two galaxies using only steps that move up, down, left, or right exactly
one `.` or `#` at a time. (The shortest path between two galaxies is allowed
to pass through another galaxy.)

For example, here is one of the shortest paths between galaxies `5` and `9`:

    ....1........
    .........2...
    3............
    .............
    .............
    ........4....
    .5...........
    .##.........6
    ..##.........
    ...##........
    ....##...7...
    8....9.......

This path has length `9` because it takes a minimum of nine steps to get from
galaxy `5` to galaxy `9` (the eight locations marked `#` plus the step onto
galaxy `9` itself). Here are some other example shortest path lengths:

  * Between galaxy `1` and galaxy `7`: 15
  * Between galaxy `3` and galaxy `6`: 17
  * Between galaxy `8` and galaxy `9`: 5

In this example, after expanding the universe, the sum of the shortest path
between all 36 pairs of galaxies is `374`.

Expand the universe, then find the length of the shortest path between every
pair of galaxies. What is the sum of these lengths?
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

space = '.'
galaxy = '#'

data = []

rows_with_galaxies = set()
cols_with_galaxies = set()

for row, cols in enumerate([list(x) for x in raw_data]):
    for col, cell in enumerate(cols):
        if cell == galaxy:
            cols_with_galaxies.add(col)
            rows_with_galaxies.add(row)
    data.append(list(cols))

cols = set(range(0, len(data)))
rows = set(range(0, len(data[0])))

cols_to_expand = cols.difference(cols_with_galaxies)
rows_to_expand = rows.difference(rows_with_galaxies)

new_col_count = len(cols) + len(cols_to_expand)
new_row_count = len(rows) + len(rows_to_expand)

expanded_data = []

# Do expansion and find galaxies
for row, cols in enumerate(data):
    expanded_row = []

    for col, cell in enumerate(cols):
        expanded_row.append(cell)
        if col in cols_to_expand:
            expanded_row.append(space)

    expanded_data.append(expanded_row)
    if row in rows_to_expand:
        expanded_data.append([space] * new_col_count)

galaxies = []

for y, row in enumerate(expanded_data):
    for x, cell in enumerate(row):
        if cell == galaxy:
            galaxies.append((x, y))

seen = set()
distances = []
count = 0

for ax, ay in galaxies:
    for bx, by in galaxies:
        if (
                (ax, ay) == (bx, by) or
                (ax, ay, bx, by) in seen or
                (bx, by, ax, ay) in seen
        ):
            continue
        distance = abs(ax - bx) + abs(ay - by)
        distances.append(distance)
        seen.add((ax, ay, bx, by))

print(sum(distances))

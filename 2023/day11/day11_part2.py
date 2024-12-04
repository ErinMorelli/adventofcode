#!/usr/bin/env python
"""
--- Part Two ---

The galaxies are much older (and thus much farther apart) than the researcher
initially estimated.

Now, instead of the expansion you did before, make each empty row or column
one million times larger. That is, each empty row should be replaced with
`1000000` empty rows, and each empty column should be replaced with `1000000`
empty columns.

(In the example above, if each empty row or column were merely `10` times
larger, the sum of the shortest paths between every pair of galaxies would be
`1030`. If each empty row or column were merely `100` times larger, the sum of
the shortest paths between every pair of galaxies would be `8410`. However,
your universe will need to expand far beyond these values.)

Starting with the same initial image, expand the universe according to these
new rules, then find the length of the shortest path between every pair of
galaxies. What is the sum of these lengths?
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

space = '.'
galaxy = '#'

data = [list(x) for x in raw_data]

rows_with_galaxies = set()
cols_with_galaxies = set()

og_galaxies = []

for row, cols in enumerate(data):
    for col, cell in enumerate(cols):
        if cell == galaxy:
            cols_with_galaxies.add(col)
            rows_with_galaxies.add(row)
            og_galaxies.append((col, row))

cols = set(range(0, len(data)))
rows = set(range(0, len(data[0])))

cols_to_expand = cols.difference(cols_with_galaxies)
rows_to_expand = rows.difference(rows_with_galaxies)

mod = 1000000
galaxies = []

for x, y in og_galaxies:
    expanded_x = x
    expanded_y = y

    for c in cols_to_expand:
        if c < x:
            expanded_x += (mod - 1)

    for r in rows_to_expand:
        if r < y:
            expanded_y += (mod - 1)

    galaxies.append((expanded_x, expanded_y))

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

#!/usr/bin/env python
"""
Determine the number of trees you would encounter if, for each of the
following slopes, you start at the top-left corner and traverse the map all
the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s)
respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on
each of the listed slopes?
"""
input_file = 'input.txt'
tree_map = []

with open(input_file, 'r') as fh:
    for line in fh:
        tree_map.append(line.strip())

tree_len = len(tree_map) - 1

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]


def slope_tree_count(right, down):
    col = right
    row = down
    trees = []

    while True:
        sq = tree_map[row][col]

        if sq == '#':
            trees.append(sq)

        prev_col = col
        col = col + right
        row = row + down

        if row > tree_len:
            break

        row_len = len(tree_map[row]) - 1

        if col > row_len:
            diff = row_len - prev_col
            col = (right - diff) - 1

    return len(trees)


tree_product = 1

for r, d in slopes:
    result = slope_tree_count(r, d)
    tree_product = tree_product * result

print(f'trees: {tree_product}')

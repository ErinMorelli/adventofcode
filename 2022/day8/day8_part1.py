#!/usr/bin/env python
"""
--- Day 8: Treetop Tree House ---

The expedition comes across a peculiar patch of tall trees all planted
carefully in a grid. The Elves explain that a previous expedition planted
these trees as a reforestation effort. Now, they're curious if this would be a
good location for a [tree house](https://en.wikipedia.org/wiki/Tree_house).

First, determine whether there is enough tree cover here to keep a tree house
hidden. To do this, you need to count the number of trees that are visible
from outside the grid when looking directly along a row or column.

The Elves have already launched a
[quadcopter](https://en.wikipedia.org/wiki/Quadcopter) to generate a map with
the height of each tree (your puzzle input). For example:

    30373
    25512
    65332
    33549
    35390

Each tree is represented as a single digit whose value is its height, where
`0` is the shortest and `9` is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid
are shorter than it. Only consider trees in the same row or column; that is,
only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible \- since they are
already on the edge, there are no trees to block the view. In this example,
that only leaves the interior nine trees to consider:

  * The top-left `5` is visible from the left and top. (It isn't visible from
    the right or bottom since other trees of height `5` are in the way.)
  * The top-middle `5` is visible from the top and right.
  * The top-right `1` is not visible from any direction; for it to be visible,
    there would need to only be trees of height 0 between it and an edge.
  * The left-middle `5` is visible, but only from the right.
  * The center `3` is not visible from any direction; for it to be visible,
    there would need to be only trees of at most height `2` between it and an
    edge.
  * The right-middle `3` is visible from the right.
  * In the bottom row, the middle `5` is visible, but the `3` and `4` are not.

With 16 trees visible on the edge and another 5 visible in the interior, a
total of `21` trees are visible in this arrangement.

Consider your map; how many trees are visible from outside the grid?
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

data = [[int(y, 10) for y in x] for x in raw_data]


def check_north(x, y, val):
    ny = y - 1
    while ny >= 0:
        if data[ny][x] >= val:
            return False
        ny -= 1
    return True


def check_south(x, y, val):
    sy = y + 1
    while sy < len(data):
        if data[sy][x] >= val:
            return False
        sy += 1
    return True


def check_east(x, y, val):
    ex = x + 1
    while ex < len(data[y]):
        if data[y][ex] >= val:
            return False
        ex += 1
    return True


def check_west(x, y, val):
    wx = x - 1
    while wx >= 0:
        if data[y][wx] >= val:
            return False
        wx -= 1
    return True


visible_count = 0

for ri, row in enumerate(data):
    for ci, cell in enumerate(row):
        n = check_north(ci, ri, cell)
        s = check_south(ci, ri, cell)
        e = check_east(ci, ri, cell)
        w = check_west(ci, ri, cell)
        if n or s or e or w:
            visible_count += 1

print(visible_count)

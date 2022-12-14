#!/usr/bin/env python
"""
--- Part Two ---

Finish folding the transparent paper according to the instructions. The manual
says the code is always eight capital letters.

What code do you use to activate the infrared thermal imaging camera system?
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().split('\n\n')

data = []

for z in raw_data[0].splitlines():
    x, y = z.split(',')
    data.append([int(x), int(y)])


folds = [x.split(' ')[-1].split('=') for x in raw_data[-1].splitlines()]

x_max = 0
y_max = 0

for axis, line in folds:
    if axis == 'x' and x_max == 0:
        x_max = int(line) * 2
    if axis == 'y' and y_max == 0:
        y_max = int(line) * 2


grid = [['.' for _ in range(x_max+1)] for _ in range(y_max+1)]


def print_grid(g):
    for r in g:
        print(''.join(r))


for x, y in data:
    grid[y][x] = '#'


def y_fold(l, g):
    top = g[:l]
    bottom = list(reversed(g[-l:]))

    new_grid = []

    for y in range(len(top)):
        row = []
        for x in range(len(top[0])):
            if bottom[y][x] == '#' or top[y][x] == '#':
                row.append('#')
            else:
                row.append('.')
        new_grid.append(row)

    return new_grid


def x_fold(l, g):
    left = []
    right = []

    for row in g:
        left.append(row[:l])
        right.append(list(reversed(row[-l:])))

    new_grid = []

    for y in range(len(left)):
        row = []
        for x in range(len(left[0])):
            if right[y][x] == '#' or left[y][x] == '#':
                row.append('#')
            else:
                row.append('.')
        new_grid.append(row)

    return new_grid


current = grid

for axis, line in folds:
    line = int(line)

    # Vertical
    if axis == 'y':
        current = y_fold(line, current)

    # Horizontal
    else:
        current = x_fold(line, current)

print_grid(current)

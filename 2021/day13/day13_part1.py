#!/usr/bin/env python
"""
???
"""
input_file = 'input.txt'
# input_file = 'sample.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().split('\n\n')

data = []
x_max = 0
y_max = 0

for z in raw_data[0].splitlines():
    parts = z.split(',')
    x = int(parts[0])
    y = int(parts[1])
    if x > x_max:
        x_max = x
    if y > y_max:
        y_max = y
    data.append([x, y])

folds = [x.split(' ')[-1].split('=') for x in raw_data[-1].splitlines()]

grid = [['.' for _ in range(x_max+1)] for _ in range(y_max+1)]


def print_grid(g):
    for i, r in enumerate(g):
        l = f' {i} ' if i < 10 else f'{i} '
        print(f"{l}{''.join(r)}")
    print('')


for x, y in data:
    grid[int(y)][int(x)] = '#'


def y_fold(l, g):
    top = g[:l]
    bottom = list(reversed(g[-l:]))

    new_grid = top
    visible = 0

    for y, row in enumerate(bottom):
        for x, cell in enumerate(row):
            if cell == '#' or top[y][x] == '#':
                new_grid[y][x] = '#'
                visible += 1

    return visible, new_grid


def x_fold(l, g):
    left = []
    right = []

    for row in g:
        left.append(row[:l])
        right.append(list(reversed(row[-l:])))

    new_grid = left
    visible = 0

    for y, row in enumerate(right):
        for x, cell in enumerate(row):
            if cell == '#' or left[y][x] == '#':
                new_grid[y][x] = '#'
                visible += 1

    return visible, new_grid


current = grid

for axis, line in folds:
    line = int(line)

    # Vertical
    if axis == 'y':
        vis, new_g = y_fold(line, current)

    # Horizontal
    else:
        vis, new_g = x_fold(line, current)

    current = new_g
    print(vis)
    break

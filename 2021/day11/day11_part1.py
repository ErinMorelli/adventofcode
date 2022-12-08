#!/usr/bin/env python
"""
???
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

data = [[int(y, 10) for y in x] for x in raw_data]

flashed = set()


def flash(x, y):
    if (x, y) in flashed:
        return

    flashed.add((x, y))

    # north
    if y-1 >= 0 and (x, y-1) not in flashed:
        data[y-1][x] += 1
        if data[y-1][x] > 9:
            flash(x, y-1)
    # northeast
    if y-1 >= 0 and x+1 < len(data[y]) and (x+1, y-1) not in flashed:
        data[y-1][x+1] += 1
        if data[y-1][x+1] > 9:
            flash(x+1, y-1)
    # east
    if x+1 < len(data[y]) and (x+1, y) not in flashed:
        data[y][x+1] += 1
        if data[y][x+1] > 9:
            flash(x+1, y)
    # southeast
    if y+1 < len(data) and x+1 < len(data[y]) and (x+1, y+1) not in flashed:
        data[y+1][x+1] += 1
        if data[y+1][x+1] > 9:
            flash(x+1, y+1)
    # south
    if y+1 < len(data) and (x, y+1) not in flashed:
        data[y+1][x] += 1
        if data[y+1][x] > 9:
            flash(x, y+1)
    # southwest
    if y+1 < len(data) and x-1 >= 0 and (x-1, y+1) not in flashed:
        data[y+1][x-1] += 1
        if data[y+1][x-1] > 9:
            flash(x-1, y+1)
    # west
    if x-1 >= 0 and (x-1, y) not in flashed:
        data[y][x-1] += 1
        if data[y][x-1] > 9:
            flash(x-1, y)
    # northwest
    if y-1 >= 0 and x-1 >= 0 and (x-1, y-1) not in flashed:
        data[y-1][x-1] += 1
        if data[y-1][x-1] > 9:
            flash(x-1, y-1)

    data[y][x] = 0


def step():
    to_flash = []
    for y, row in enumerate(data):
        for x, _ in enumerate(row):
            data[y][x] += 1
            if data[y][x] > 9:
                to_flash.append((x, y))

    for x, y in to_flash:
        flash(x, y)


flash_count = 0

for x in range(100):
    step()
    flash_count += len(flashed)
    flashed.clear()

print(flash_count)

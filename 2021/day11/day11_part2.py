#!/usr/bin/env python
"""
--- Part Two ---

It seems like the individual flashes aren't bright enough to navigate.
However, you might have a better option: the flashes seem to be synchronizing!

In the example above, the first time all octopuses flash simultaneously is
step `195`:

    After step 193:
    5877777777
    8877777777
    7777777777
    7777777777
    7777777777
    7777777777
    7777777777
    7777777777
    7777777777
    7777777777

    After step 194:
    6988888888
    9988888888
    8888888888
    8888888888
    8888888888
    8888888888
    8888888888
    8888888888
    8888888888
    8888888888

    After step 195:
    0000000000
    0000000000
    0000000000
    0000000000
    0000000000
    0000000000
    0000000000
    0000000000
    0000000000
    0000000000

If you can calculate the exact moments when the octopuses will all flash
simultaneously, you should be able to navigate through the cavern. What is the
first step during which all octopuses flash?
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


i = 1

while True:
    step()
    if len(flashed) == 100:
        break
    flashed.clear()
    i += 1

print(i)
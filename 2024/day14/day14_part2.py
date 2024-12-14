#!/usr/bin/env python
"""
--- Part Two ---

During the bathroom break, someone notices that these robots seem awfully
similar to ones built and used at the North Pole. If they're the same type of
robots, they should have a hard-coded Easter egg: very rarely, most of the
robots should arrange themselves into a picture of a Christmas tree.

What is the fewest number of seconds that must elapse for the robots to
display the Easter egg?
"""
import re

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

data = list()

for r in raw_data:
    res = re.match(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', r)
    px, py, vx, vy = map(int, res.groups())
    data.append(((px, py), (vx, vy)))

max_x = 101
max_y = 103

robots = data.copy()
sec = 1

for sec in range(20000):
    grid = [['.' for _ in range(max_x)] for _ in range(max_y)]
    new_robots = list()

    for robot in robots:
        (x, y), (vx, vy) = robot

        next_x = x + vx
        next_y = y + vy

        if next_x < 0:
            next_x = max_x + next_x
        elif next_x >= max_x:
            next_x = next_x - max_x

        if next_y < 0:
            next_y = max_y + next_y
        elif next_y >= max_y:
            next_y = next_y - max_y

        grid[y][x] = 'R'
        new_robots.append(((next_x, next_y), (vx, vy)))

    robots = new_robots

    for row in grid:
        r =''.join(row)
        if 'RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR' in r:
            print(sec)
            for rr in grid:
                print(''.join(rr))
            print('\n\n')
            break

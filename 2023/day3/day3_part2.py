#!/usr/bin/env python
"""
--- Part Two ---

The engineer finds the missing part and installs it in the engine! As the
engine springs to life, you jump in the closest gondola, finally ready to
ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong?
Fortunately, the gondola has a phone labeled "help", so you pick it up and the
engineer answers.

Before you can explain the situation, she suggests that you look out the
window. There stands the engineer, holding a phone in one hand and waving with
the other. You're going so slowly that you haven't even left the station. You
exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is
wrong. A gear is any `*` symbol that is adjacent to exactly two part numbers.
Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up
so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..

In this schematic, there are two gears. The first is in the top left; it has
part numbers `467` and `35`, so its gear ratio is `16345`. The second gear is
in the lower right; its gear ratio is `451490`. (The `*` adjacent to `617` is
not a gear because it is only adjacent to one part number.) Adding up all of
the gear ratios produces `467835`.

What is the sum of all of the gear ratios in your engine schematic?
"""
import re
from functools import reduce

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    data = fh.read().splitlines()

max_x = len(data)
max_y = len(data[0])

gear_ratios = []
seen = set()

for y, line in enumerate(data):
    for raw_star in re.finditer(r'\*', line):
        x = raw_star.start()
        star = raw_star.group(0)
        nums = []

        for (nx, ny) in [
            (x, y-1),    # north
            (x+1, y-1),  # northeast
            (x+1, y),    # east
            (x+1, y+1),  # southeast
            (x, y+1),    # south
            (x-1, y+1),  # southwest
            (x-1, y),    # west
            (x-1, y-1),  # northwest
        ]:
            cell = f'{nx},{ny}'

            if (
                cell not in seen and
                0 <= nx < max_x and
                0 <= ny < max_y and
                data[ny][nx].isnumeric()
            ):
                seen.add(cell)
                digits = [data[ny][nx]]

                # Forward
                for fx in range(nx+1, max_x):
                    f_cell = f'{fx},{ny}'
                    if f_cell not in seen and data[ny][fx].isnumeric():
                        seen.add(f_cell)
                        digits.append(data[ny][fx])
                    else:
                        break

                # Backward
                for bx in range(nx-1, -1, -1):
                    b_cell = f'{bx},{ny}'
                    if b_cell not in seen and data[ny][bx].isnumeric():
                        seen.add(b_cell)
                        digits.insert(0, data[ny][bx])
                    else:
                        break

                nums.append(int(''.join(digits)))

            else:
                continue

        if len(nums) == 2:
            gear_ratio = reduce(lambda a, b: a*b, nums)
            gear_ratios.append(gear_ratio)

print(sum(gear_ratios))

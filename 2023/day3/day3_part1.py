#!/usr/bin/env python
"""
--- Day 3: Gear Ratios ---

You and the Elf eventually reach a [gondola
lift](https://en.wikipedia.org/wiki/Gondola_lift) station; he says the gondola
lift will take you up to the water source, but this is as far as he can bring
you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem:
they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of
surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working
right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine,
but nobody can figure out which one. If you can add up all the part numbers in
the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation
of the engine. There are lots of numbers and symbols you don't really
understand, but apparently any number adjacent to a symbol, even diagonally,
is a "part number" and should be included in your sum. (Periods (`.`) do not
count as a symbol.)

Here is an example engine schematic:

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

In this schematic, two numbers are not part numbers because they are not
adjacent to a symbol: `114` (top right) and `58` (middle right). Every other
number is adjacent to a symbol and so is a part number; their sum is `4361`.

Of course, the actual engine schematic is much larger. What is the sum of all
of the part numbers in the engine schematic?
"""
import re

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    data = fh.read().splitlines()

max_x = len(data)
max_y = len(data[0])

part_numbers = []

for y, line in enumerate(data):
    for num in re.finditer(r'\d+', line):
        valid = False

        for x in range(num.start(), num.end()):
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
                if (
                    0 <= nx < max_x and
                    0 <= ny < max_y and
                    re.match(r'[^.\d]', data[ny][nx]) is not None
                ):
                    valid = True
                    break

            if valid:
                break

        if valid:
            part_numbers.append(int(num.group(0)))

print(sum(part_numbers))

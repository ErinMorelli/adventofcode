#!/usr/bin/env python
"""
The navigation instructions (your puzzle input) consists of a sequence of
single-character actions paired with integer input values. After staring at
them for a few minutes, you work out what they probably mean:

  * Action `N` means to move north by the given value.
  * Action `S` means to move south by the given value.
  * Action `E` means to move east by the given value.
  * Action `W` means to move west by the given value.
  * Action `L` means to turn left the given number of degrees.
  * Action `R` means to turn right the given number of degrees.
  * Action `F` means to move forward by the given value in the direction the
    ship is currently facing.

The ship starts by facing east. Only the `L` and `R` actions change the
direction the ship is facing. (That is, if the ship is facing east and the
next instruction is `N10`, the ship would move north 10 units, but would still
move east if the following action were `F`.)

For example:

    F10
    N3
    F7
    R90
    F11

These instructions would be handled as follows:

  * `F10` would move the ship 10 units east (because the ship starts by facing
    east) to east 10, north 0.
  * `N3` would move the ship 3 units north to east 10, north 3.
  * `F7` would move the ship another 7 units east (because the ship is still
    facing east) to east 17, north 3.
  * `R90` would cause the ship to turn right by 90 degrees and face south; it
    remains at east 17, north 3.
  * `F11` would move the ship 11 units south to east 17, south 8.

At the end of these instructions, the ship's [Manhattan
distance](https://en.wikipedia.org/wiki/Manhattan_distance) (sum of the
absolute values of its east/west position and its north/south position) from
its starting position is `17 + 8` = `25`.

Figure out where the navigation instructions lead. What is the Manhattan
distance between that location and the ship's starting position?
"""
import re

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    data = fh.read().splitlines()


def rotate(start, dir, degrees):
    """
      N
    W   E
      S
    """
    headings = ['N', 'E', 'S', 'W']
    h_count = len(headings)
    h_index = headings.index(start)
    steps = int(degrees/90)

    if dir == 'R':
        new_index = h_index + steps
        if new_index >= h_count:
            new_index = new_index - h_count
        return headings[new_index]

    elif dir == 'L':
        new_index = h_index - steps
        return headings[new_index]


x = 0
y = 0
heading = 'E'

for cmd in data:
    action, val = re.match(r'([NSEWLRF])(\d+)', cmd).groups()
    val = int(val, 10)

    # Forward
    if action == 'F':
        action = heading

    # Movement
    if action == 'N':
        y += val
    elif action == 'S':
        y -= val
    elif action == 'E':
        x += val
    elif action == 'W':
        x -= val

    # Rotation
    if action in ['L', 'R']:
        heading = rotate(heading, action, val)

result = abs(x) + abs(y)
print(f'Manhattan distance: {result}')

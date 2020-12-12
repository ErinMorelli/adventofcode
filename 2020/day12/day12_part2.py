#!/usr/bin/env python
"""
Almost all of the actions indicate how to move a waypoint which is relative to
the ship's position:

  * Action `N` means to move the waypoint north by the given value.
  * Action `S` means to move the waypoint south by the given value.
  * Action `E` means to move the waypoint east by the given value.
  * Action `W` means to move the waypoint west by the given value.
  * Action `L` means to rotate the waypoint around the ship left (counter-
    clockwise) the given number of degrees.
  * Action `R` means to rotate the waypoint around the ship right (clockwise)
    the given number of degrees.
  * Action `F` means to move forward to the waypoint a number of times equal
    to the given value.

The waypoint starts 10 units east and 1 unit north relative to the ship. The
waypoint is relative to the ship; that is, if the ship moves, the waypoint
moves with it.

For example, using the same instructions as above:

  * `F10` moves the ship to the waypoint 10 times (a total of 100 units east
    and 10 units north), leaving the ship at east 100, north 10. The waypoint
    stays 10 units east and 1 unit north of the ship.
  * `N3` moves the waypoint 3 units north to 10 units east and 4 units north
    of the ship. The ship remains at east 100, north 10.
  * `F7` moves the ship to the waypoint 7 times (a total of 70 units east and
    28 units north), leaving the ship at east 170, north 38. The waypoint
    stays 10 units east and 4 units north of the ship.
  * `R90` rotates the waypoint around the ship clockwise 90 degrees, moving it
    to 4 units east and 10 units south of the ship. The ship remains at east
    170, north 38.
  * `F11` moves the ship to the waypoint 11 times (a total of 44 units east
    and 110 units south), leaving the ship at east 214, south 72. The waypoint
    stays 4 units east and 10 units south of the ship.

After these operations, the ship's Manhattan distance from its starting
position is `214 + 72` = `286`.

Figure out where the navigation instructions actually lead. What is the
Manhattan distance between that location and the ship's starting position?
"""
import re

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    data = fh.read().splitlines()


def rotate(start_x, start_y, dir, degrees):
    """
      N
    W   E
      S
    """
    headings = ['N', 'E', 'S', 'W']
    steps = int(degrees/90)
    diff = steps * -1 if dir == 'L' else steps
    heading = headings[diff]

    if heading == 'E':
        new_x = start_y
        new_y = start_x * -1
    elif heading == 'S':
        new_x = start_x * -1
        new_y = start_y * -1
    elif heading == 'W':
        new_x = start_y * -1
        new_y = start_x

    return new_x, new_y


x = 0
y = 0

wx = 10
wy = 1

for cmd in data:
    action, val = re.match(r'([NSEWLRF])(\d+)', cmd).groups()
    val = int(val, 10)

    # Forward
    if action == 'F':
        x += wx * val
        y += wy * val

    # Movement
    elif action == 'N':
        wy += val
    elif action == 'S':
        wy -= val
    elif action == 'E':
        wx += val
    elif action == 'W':
        wx -= val

    # Rotation
    if action in ['L', 'R']:
        wx, wy = rotate(wx, wy, action, val)

result = abs(x) + abs(y)
print(f'Manhattan distance: {result}')

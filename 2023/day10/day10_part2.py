#!/usr/bin/env python
"""
--- Part Two ---

You quickly reach the farthest point of the loop, but the animal never
emerges. Maybe its nest is within the area enclosed by the loop?

To determine whether it's even worth taking the time to search for such a
nest, you should calculate how many tiles are contained within the loop. For
example:

    ...........
    .S-------7.
    .|F-----7|.
    .||.....||.
    .||.....||.
    .|L-7.F-J|.
    .|..|.|..|.
    .L--J.L--J.
    ...........

The above loop encloses merely four tiles \- the two pairs of `.` in the
southwest and southeast (marked `I` below). The middle `.` tiles (marked `O`
below) are not in the loop. Here is the same loop again with those regions
marked:

    ...........
    .S-------7.
    .|F-----7|.
    .||OOOOO||.
    .||OOOOO||.
    .|L-7OF-J|.
    .|II|O|II|.
    .L--JOL--J.
    .....O.....

In fact, there doesn't even need to be a full tile path to the outside for
tiles to count as outside the loop - squeezing between pipes is also allowed!
Here, `I` is still within the loop and `O` is still outside the loop:

    ..........
    .S------7.
    .|F----7|.
    .||OOOO||.
    .||OOOO||.
    .|L-7F-J|.
    .|II||II|.
    .L--JL--J.
    ..........

In both of the above examples, `4` tiles are enclosed by the loop.

Here's a larger example:

    .F----7F7F7F7F-7....
    .|F--7||||||||FJ....
    .||.FJ||||||||L7....
    FJL7L7LJLJ||LJ.L-7..
    L--J.L7...LJS7F-7L7.
    ....F-J..F7FJ|L7L7L7
    ....L7.F7||L7|.L7L7|
    .....|FJLJ|FJ|F7|.LJ
    ....FJL-7.||.||||...
    ....L---J.LJ.LJLJ...

The above sketch has many random bits of ground, some of which are in the loop
(`I`) and some of which are outside it (`O`):

    OF----7F7F7F7F-7OOOO
    O|F--7||||||||FJOOOO
    O||OFJ||||||||L7OOOO
    FJL7L7LJLJ||LJIL-7OO
    L--JOL7IIILJS7F-7L7O
    OOOOF-JIIF7FJ|L7L7L7
    OOOOL7IF7||L7|IL7L7|
    OOOOO|FJLJ|FJ|F7|OLJ
    OOOOFJL-7O||O||||OOO
    OOOOL---JOLJOLJLJOOO

In this larger example, `8` tiles are enclosed by the loop.

Any tile that isn't part of the main loop can count as being enclosed by the
loop. Here's another example with many bits of junk pipe lying around that
aren't connected to the main loop at all:

    FF7FSF7F7F7F7F7F---7
    L|LJ||||||||||||F--J
    FL-7LJLJ||||||LJL-77
    F--JF--7||LJLJ7F7FJ-
    L---JF-JLJ.||-FJLJJ7
    |F|F-JF---7F7-L7L|7|
    |FFJF7L7F-JF7|JL---7
    7-L-JL7||F7|L7F-7F7|
    L.L7LFJ|||||FJL7||LJ
    L7JLJL-JLJLJL--JLJ.L

Here are just the tiles that are enclosed by the loop marked with `I`:

    FF7FSF7F7F7F7F7F---7
    L|LJ||||||||||||F--J
    FL-7LJLJ||||||LJL-77
    F--JF--7||LJLJIF7FJ-
    L---JF-JLJIIIIFJLJJ7
    |F|F-JF---7IIIL7L|7|
    |FFJF7L7F-JF7IIL---7
    7-L-JL7||F7|L7F-7F7|
    L.L7LFJ|||||FJL7||LJ
    L7JLJL-JLJLJL--JLJ.L

In this last example, `10` tiles are enclosed by the loop.

Figure out whether you have time to search for the nest by calculating the
area within the loop. How many tiles are enclosed by the loop?
"""
from pprint import pprint

# input_file = 'input.txt'
input_file = 'sample.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

start = 'S'
start_x = None
start_y = None

data = []
print(f'  {" ".join([str(i) for i in range(len(raw_data))])}')

for dy, row in enumerate([list(x) for x in raw_data]):
    if start in row:
        start_x = row.index(start)
        start_y = dy
    data.append(list(row))
    print(f'{dy} {" ".join(list(row))}')

print(' ')


def get_moves(x, y, val):
    moves = set()
    # North
    if val in ['|', 'L', 'J', 'S']:
        moves.add((x, y - 1))
    # East
    if val in ['-', 'L', 'F', 'S']:
        moves.add((x + 1, y))
    # South
    if val in ['|', '7', 'F', 'S']:
        moves.add((x, y + 1))
    # West
    if val in ['-', 'J', '7', 'S']:
        moves.add((x - 1, y))
    return moves


(dir_a, dir_b) = [(x, y) for x, y in list(get_moves(start_x, start_y, start))
                  if (start_x, start_y) in get_moves(x, y, data[y][x])]

prev_a = (start_x, start_y)
prev_b = (start_x, start_y)

(ax, ay) = dir_a
(bx, by) = dir_b
a = data[ay][ax]

a_path = []
b_path = []
steps = 1

while True:
    steps += 1

    a_val = data[ay][ax]
    b_val = data[by][bx]

    a_path.append((ax, ay))
    b_path.append((bx, by))

    a_moves = get_moves(ax, ay, a_val)
    b_moves = get_moves(bx, by, b_val)

    new_a = a_moves.difference([prev_a]).pop()
    new_b = b_moves.difference([prev_b]).pop()

    if new_a == new_b:
        a_path.append(new_a)
        break

    prev_a = (ax, ay)
    prev_b = (bx, by)

    (ax, ay) = new_a
    (bx, by) = new_b


paths = [(start_x, start_y)] + a_path + [i for i in reversed(b_path)]
print(paths)

max_y = len(data)
max_x = len(data[0])
size = max_x * max_y

seen = set()
count = 0

for y, row in enumerate(data):
    for x, val in enumerate(row):
        coords = f'{x},{y}'
        if coords in paths or coords in seen:
            continue

        # count += 1
        # seen.add(coords)
        # North
        if y-1 >= 0:
            n
        # Northest
        if y-1 >= 0 and x+1 < max_x:
            pass
        # East
        if x+1 < max_x:
            pass
        # Southeast
        if y+1 < max_y and x+1 < max_x:
            pass
        # South
        if y+1 < max_y:
            pass
        # Southwest
        if y+1 < max_y and x-1 >=0:
            pass
        # West
        if x-1 >= 0:
            pass
        # Northwest
        if y-1 >= 0 and x-1 >=0:
            pass

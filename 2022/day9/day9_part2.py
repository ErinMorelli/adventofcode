#!/usr/bin/env python
"""
--- Part Two ---

A rope snaps! Suddenly, the river is getting a lot closer than you remember.
The bridge is still there, but some of the ropes that broke are now whipping
toward you as you fall through the air!

The ropes are moving too quickly to grab; you only have a few seconds to
choose how to arch your body to avoid being hit. Fortunately, your simulation
can be extended to support longer ropes.

Rather than two knots, you now must simulate a rope consisting of ten knots.
One knot is still the head of the rope and moves according to the series of
motions. Each knot further down the rope follows the knot in front of it using
the same rules as before.

Using the same series of motions as the above example, but with the knots
marked `H`, `1`, `2`, ..., `9`, the motions now occur as follows:

    == Initial State ==

    ......
    ......
    ......
    ......
    H.....  (H covers 1, 2, 3, 4, 5, 6, 7, 8, 9, s)

    == R 4 ==

    ......
    ......
    ......
    ......
    1H....  (1 covers 2, 3, 4, 5, 6, 7, 8, 9, s)

    ......
    ......
    ......
    ......
    21H...  (2 covers 3, 4, 5, 6, 7, 8, 9, s)

    ......
    ......
    ......
    ......
    321H..  (3 covers 4, 5, 6, 7, 8, 9, s)

    ......
    ......
    ......
    ......
    4321H.  (4 covers 5, 6, 7, 8, 9, s)

    == U 4 ==

    ......
    ......
    ......
    ....H.
    4321..  (4 covers 5, 6, 7, 8, 9, s)

    ......
    ......
    ....H.
    .4321.
    5.....  (5 covers 6, 7, 8, 9, s)

    ......
    ....H.
    ....1.
    .432..
    5.....  (5 covers 6, 7, 8, 9, s)

    ....H.
    ....1.
    ..432.
    .5....
    6.....  (6 covers 7, 8, 9, s)

    == L 3 ==

    ...H..
    ....1.
    ..432.
    .5....
    6.....  (6 covers 7, 8, 9, s)

    ..H1..
    ...2..
    ..43..
    .5....
    6.....  (6 covers 7, 8, 9, s)

    .H1...
    ...2..
    ..43..
    .5....
    6.....  (6 covers 7, 8, 9, s)

    == D 1 ==

    ..1...
    .H.2..
    ..43..
    .5....
    6.....  (6 covers 7, 8, 9, s)

    == R 4 ==

    ..1...
    ..H2..
    ..43..
    .5....
    6.....  (6 covers 7, 8, 9, s)

    ..1...
    ...H..  (H covers 2)
    ..43..
    .5....
    6.....  (6 covers 7, 8, 9, s)

    ......
    ...1H.  (1 covers 2)
    ..43..
    .5....
    6.....  (6 covers 7, 8, 9, s)

    ......
    ...21H
    ..43..
    .5....
    6.....  (6 covers 7, 8, 9, s)

    == D 1 ==

    ......
    ...21.
    ..43.H
    .5....
    6.....  (6 covers 7, 8, 9, s)

    == L 5 ==

    ......
    ...21.
    ..43H.
    .5....
    6.....  (6 covers 7, 8, 9, s)

    ......
    ...21.
    ..4H..  (H covers 3)
    .5....
    6.....  (6 covers 7, 8, 9, s)

    ......
    ...2..
    ..H1..  (H covers 4; 1 covers 3)
    .5....
    6.....  (6 covers 7, 8, 9, s)

    ......
    ...2..
    .H13..  (1 covers 4)
    .5....
    6.....  (6 covers 7, 8, 9, s)

    ......
    ......
    H123..  (2 covers 4)
    .5....
    6.....  (6 covers 7, 8, 9, s)

    == R 2 ==

    ......
    ......
    .H23..  (H covers 1; 2 covers 4)
    .5....
    6.....  (6 covers 7, 8, 9, s)

    ......
    ......
    .1H3..  (H covers 2, 4)
    .5....
    6.....  (6 covers 7, 8, 9, s)

Now, you need to keep track of the positions the new tail, `9`, visits. In
this example, the tail never moves, and so it only visits `1` position.
However, be careful: more types of motion are possible than before, so you
might want to visually compare your simulated rope to the one above.

Here's a larger example:

    R 5
    U 8
    L 8
    D 3
    R 17
    D 10
    L 25
    U 20

These motions occur as follows (individual steps are not shown):

    == Initial State ==

    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ...........H..............  (H covers 1, 2, 3, 4, 5, 6, 7, 8, 9, s)
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................

    == R 5 ==

    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ...........54321H.........  (5 covers 6, 7, 8, 9, s)
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................

    == U 8 ==

    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ................H.........
    ................1.........
    ................2.........
    ................3.........
    ...............54.........
    ..............6...........
    .............7............
    ............8.............
    ...........9..............  (9 covers s)
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................

    == L 8 ==

    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ........H1234.............
    ............5.............
    ............6.............
    ............7.............
    ............8.............
    ............9.............
    ..........................
    ..........................
    ...........s..............
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................

    == D 3 ==

    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    .........2345.............
    ........1...6.............
    ........H...7.............
    ............8.............
    ............9.............
    ..........................
    ..........................
    ...........s..............
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................

    == R 17 ==

    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ................987654321H
    ..........................
    ..........................
    ..........................
    ..........................
    ...........s..............
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................

    == D 10 ==

    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ...........s.........98765
    .........................4
    .........................3
    .........................2
    .........................1
    .........................H

    == L 25 ==

    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ...........s..............
    ..........................
    ..........................
    ..........................
    ..........................
    H123456789................

    == U 20 ==

    H.........................
    1.........................
    2.........................
    3.........................
    4.........................
    5.........................
    6.........................
    7.........................
    8.........................
    9.........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ...........s..............
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................

Now, the tail (`9`) visits `36` positions (including `s`) at least once:

    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    ..........................
    #.........................
    #.............###.........
    #............#...#........
    .#..........#.....#.......
    ..#..........#.....#......
    ...#........#.......#.....
    ....#......s.........#....
    .....#..............#.....
    ......#............#......
    .......#..........#.......
    ........#........#........
    .........########.........

Simulate your complete series of motions on a larger rope with ten knots. How
many positions does the tail of the rope visit at least once?
"""
from collections import defaultdict

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

data = [x.split(' ') for x in raw_data]

visited = set()

head_pos = [0, 0]
knots = defaultdict(lambda: [0, 0])
knot_count = 9


def move_knots():
    parent_pos = head_pos

    for i in range(knot_count):
        knot_pos = knots[i+1]

        xdiff = parent_pos[0] - knot_pos[0]
        ydiff = parent_pos[1] - knot_pos[1]

        # UP
        if xdiff == 0 and ydiff == 2:
            knot_pos[1] += 1
        # UP/RIGHT
        if (xdiff == 2 and ydiff > 0) or (xdiff == 1 and ydiff == 2):
            knot_pos[0] += 1
            knot_pos[1] += 1
        # RIGHT
        if xdiff == 2 and ydiff == 0:
            knot_pos[0] += 1
        # DOWN/RIGHT
        if (xdiff == 2 and ydiff < 0) or (xdiff == 1 and ydiff == -2):
            knot_pos[0] += 1
            knot_pos[1] -= 1
        # DOWN
        if xdiff == 0 and ydiff == -2:
            knot_pos[1] -= 1
        # DOWN/LEFT
        if (xdiff == -2 and ydiff < 0) or (xdiff == -1 and ydiff == -2):
            knot_pos[0] -= 1
            knot_pos[1] -= 1
        # LEFT
        if xdiff == -2 and ydiff == 0:
            knot_pos[0] -= 1
        # UP/LEFT
        if (xdiff == -2 and ydiff > 0) or (xdiff == -1 and ydiff == 2):
            knot_pos[0] -= 1
            knot_pos[1] += 1

        if i+1 == knot_count:
            visited.add((knot_pos[0], knot_pos[1]))

        parent_pos = knot_pos


for heading, steps in data:
    for step in range(int(steps)):
        # RIGHT
        if heading == 'R':
            head_pos[0] += 1
        # LEFT
        if heading == 'L':
            head_pos[0] -= 1
        # UP
        if heading == 'U':
            head_pos[1] += 1
        # DOWN
        if heading == 'D':
            head_pos[1] -= 1

        move_knots()

print(len(visited))


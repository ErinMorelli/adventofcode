#!/usr/bin/env python
"""
--- Part Two ---

While The Historians begin working around the guard's patrol route, you borrow
their fancy device and step outside the lab. From the safety of a supply
closet, you time travel through the last few months and record the nightly
status of the lab's guard post on the walls of the closet.

Returning after what seems like only a few seconds to The Historians, they
explain that the guard's patrol area is simply too large for them to safely
search the lab without getting caught.

Fortunately, they are pretty sure that adding a single new obstruction won't
cause a time paradox. They'd like to place the new obstruction in such a way
that the guard will get stuck in a loop , making the rest of the lab safe to
search.

To have the lowest chance of creating a time paradox, The Historians would
like to know all of the possible positions for such an obstruction. The new
obstruction can't be placed at the guard's starting position - the guard is
there right now and would notice.

In the above example, there are only `6` different positions where a new
obstruction would cause the guard to get stuck in a loop. The diagrams of
these six situations use `O` to mark the new obstruction, `|` to show a
position where the guard moves up/down, `-` to show a position where the guard
moves left/right, and `+` to show a position where the guard moves both
up/down and left/right.

Option one, put a printing press next to the guard's starting position:

    ....#.....
    ....+---+#
    ....|...|.
    ..#.|...|.
    ....|..#|.
    ....|...|.
    .#.O ^---+.
    ........#.
    #.........
    ......#...

Option two, put a stack of failed suit prototypes in the bottom right quadrant
of the mapped area:

    ....#.....
    ....+---+#
    ....|...|.
    ..#.|...|.
    ..+-+-+#|.
    ..|.|.|.|.
    .#+-^-+-+.
    ......O.#.
    #.........
    ......#...

Option three, put a crate of chimney-squeeze prototype fabric next to the
standing desk in the bottom right quadrant:

    ....#.....
    ....+---+#
    ....|...|.
    ..#.|...|.
    ..+-+-+#|.
    ..|.|.|.|.
    .#+-^-+-+.
    .+----+O #.
    #+----+...
    ......#...

Option four, put an alchemical retroencabulator near the bottom left corner:

    ....#.....
    ....+---+#
    ....|...|.
    ..#.|...|.
    ..+-+-+#|.
    ..|.|.|.|.
    .#+-^-+-+.
    ..|...|.#.
    #O +---+...
    ......#...

Option five, put the alchemical retroencabulator a bit to the right instead:

    ....#.....
    ....+---+#
    ....|...|.
    ..#.|...|.
    ..+-+-+#|.
    ..|.|.|.|.
    .#+-^-+-+.
    ....|.|.#.
    #..O +-+...
    ......#...

Option six, put a tank of sovereign glue right next to the tank of universal
solvent:

    ....#.....
    ....+---+#
    ....|...|.
    ..#.|...|.
    ..+-+-+#|.
    ..|.|.|.|.
    .#+-^-+-+.
    .+----++#.
    #+----++..
    ......#O..

It doesn't really matter what you choose to use as an obstacle so long as you
and The Historians can put it into position without the guard noticing. The
important thing is having enough options that you can find one that minimizes
time paradoxes, and in this example, there are `6` different positions you
could choose.

You need to get the guard stuck in a loop by adding a single new obstruction.
How many different positions could you choose for this obstruction?
"""
input_file = 'input.txt'
# input_file = 'sample.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

guard = '^'
obstacle = '#'
empty = '.'

start_pos = 'up'
start_x = 0
start_y = 0

data = []
for idx, d in enumerate(raw_data):
    if guard in d:
        start_x = d.index(guard)
        start_y = idx
    data.append(list(d))

def move(x, y, pos):
    new_x = x
    new_y = y
    new_pos = pos

    if pos == 'up':
        new_y = y - 1
        if data[new_y][new_x] == obstacle:
            return move(x, y, 'right')

    elif pos == 'down':
        new_y = y + 1
        if data[new_y][new_x] == obstacle:
            return move(x, y, 'left')

    elif pos == 'left':
        new_x = x - 1
        if data[new_y][new_x] == obstacle:
            return move(x, y, 'up')

    elif pos == 'right':
        new_x = x + 1
        if data[new_y][new_x] == obstacle:
            return move(x, y, 'down')

    return new_x, new_y, new_pos

def patrol(x, y, pos):
    route = []
    route.append(f'{x},{y},{pos}')

    while True:
        try:
            x, y, pos = move(x, y, pos)
            route.append(f'{x},{y},{pos}')
        except IndexError:
            break

    return route

seen = patrol(start_x, start_y, start_pos)

def patrol_loop(x, y, pos):
    route = set()
    route.add(f'{x},{y},{pos}')
    is_loop = False

    while True:
        try:
            x, y, pos = move(x, y, pos)
            log = f'{x},{y},{pos}'

            if log in route:
                is_loop = True
                break

            route.add(f'{x},{y},{pos}')
        except IndexError:
            break

    return is_loop

spots = set()

for coord in seen:
    xs, ys, pos = coord.split(',')
    x = int(xs)
    y = int(ys)

    if (start_x == x and start_y == y) or data[y][x] == obstacle:
        continue

    temp = data[y][x]
    data[y][x] = obstacle

    if patrol_loop(start_x, start_y, start_pos):
        spots.add(f'{x},{y}')

    data[y][x] = temp

# print(spots)
print(len(spots))

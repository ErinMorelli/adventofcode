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
import asyncio

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

max_y = len(raw_data)
max_x = len(raw_data[0])

guard = '^'
obstacle = '#'

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
        if new_y < 0:
            raise IndexError
        if data[new_y][new_x] == obstacle:
            return move(x, y, 'right')

    elif pos == 'down':
        new_y = y + 1
        if new_y >= max_y:
            raise IndexError
        if data[new_y][new_x] == obstacle:
            return move(x, y, 'left')

    elif pos == 'left':
        new_x = x - 1
        if new_x < 0:
            raise IndexError
        if data[new_y][new_x] == obstacle:
            return move(x, y, 'up')

    elif pos == 'right':
        new_x = x + 1
        if new_x >= max_x:
            raise IndexError
        if data[new_y][new_x] == obstacle:
            return move(x, y, 'down')

    return new_x, new_y, new_pos

def patrol(x, y, pos):
    route = list()
    coords = set()
    route.append((x, y, pos))

    while True:
        try:
            x, y, pos = move(x, y, pos)
            if (x, y, pos) in route:
                break
            route.append((x, y, pos))
            coords.add((x, y))
        except IndexError:
            break

    return route

seen = patrol(start_x, start_y, start_pos)
unique_seen = list(set([(s[0], s[1]) for s in seen]))

async def run(seen_list, _data):
    loops = set()

    for idx, spot in enumerate(seen_list):
        if (spot[0], spot[1]) == (start_x, start_y):
            continue

        temp = _data[spot[1]][spot[0]]
        _data[spot[1]][spot[0]] = obstacle

        path = list()

        x = start_x
        y = start_y
        pos = start_pos

        while True:
            try:
                x, y, pos = move(x, y, pos)
                if (x, y, pos) in path:
                    loops.add((spot[0], spot[1]))
                    break
                path.append((x, y, pos))
            except IndexError:
                break

        _data[spot[1]][spot[0]] = temp

    return len(loops)


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

seen_chunks = list(chunks(unique_seen, 500))

async def main():
    return await asyncio.gather(*[run(sc, data) for sc in seen_chunks])

res = asyncio.run(main())
print(sum(res))

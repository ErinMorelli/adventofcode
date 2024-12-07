#!/usr/bin/env python
"""
--- Day 6: Guard Gallivant ---

The Historians use their fancy device again, this time to whisk you all away
to the North Pole prototype suit manufacturing lab... in the year 1518! It
turns out that having direct access to history is very convenient for a group
of historians.

You still have to be careful of time paradoxes, and so it will be important to
avoid anyone from 1518 while The Historians search for the Chief.
Unfortunately, a single guard is patrolling this part of the lab.

Maybe you can work out where the guard will go ahead of time so that The
Historians can search safely?

You start by making a map (your puzzle input) of the situation. For example:

    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#..^.....
    ........#.
    #.........
    ......#...

The map shows the current position of the guard with `^` (to indicate the
guard is currently facing up from the perspective of the map). Any
obstructions - crates, desks, alchemical reactors, etc. - are shown as `#`.

Lab guards in 1518 follow a very strict patrol protocol which involves
repeatedly following these steps:

  * If there is something directly in front of you, turn right 90 degrees.
  * Otherwise, take a step forward.

Following the above protocol, the guard moves up several times until she
reaches an obstacle (in this case, a pile of failed suit prototypes):

    ....#.....
    ....^....#
    ..........
    ..#.......
    .......#..
    ..........
    .#........
    ........#.
    #.........
    ......#...

Because there is now an obstacle in front of the guard, she turns right before
continuing straight in her new facing direction:

    ....#.....
    ........>#
    ..........
    ..#.......
    .......#..
    ..........
    .#........
    ........#.
    #.........
    ......#...

Reaching another obstacle (a spool of several very long polymers), she turns
right again and continues downward:

    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#......v.
    ........#.
    #.........
    ......#...

This process continues for a while, but the guard eventually leaves the mapped
area (after walking past a tank of universal solvent):

    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#........
    ........#.
    #.........
    ......#v..

By predicting the guard's route, you can determine which specific positions in
the lab will be in the patrol path. Including the guard's starting position ,
the positions visited by the guard before leaving the area are marked with an
`X`:

    ....#.....
    ....XXXXX#
    ....X...X.
    ..#.X...X.
    ..XXXXX#X.
    ..X.X.X.X.
    .#XXXXXXX.
    .XXXXXXX#.
    #XXXXXXX..
    ......#X..

In this example, the guard will visit `41` distinct positions on your map.

Predict the path of the guard. How many distinct positions will the guard
visit before leaving the mapped area?
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

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

x = start_x
y = start_y
pos = start_pos

seen = set()
seen.add(f'{x},{y}')

while True:
    try:
        x, y, pos = move(x, y, pos)
        seen.add(f'{x},{y}')
    except IndexError:
        break

print(len(seen))

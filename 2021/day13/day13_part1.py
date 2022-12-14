#!/usr/bin/env python
"""
--- Day 13: Transparent Origami ---

You reach another volcanically active part of the cave. It would be nice if
you could do some kind of thermal imaging so you could tell ahead of time
which caves are too hot to safely enter.

Fortunately, the submarine seems to be equipped with a thermal camera! When
you activate it, you are greeted with:

    Congratulations on your purchase! To activate this infrared thermal imaging
    camera system, please enter the code found on page 1 of the manual.

Apparently, the Elves have never used this feature. To your surprise, you
manage to find the manual; as you go to open it, page 1 falls out. It's a
large sheet of [transparent
paper](https://en.wikipedia.org/wiki/Transparency_\(projection\))! The
transparent paper is marked with random dots and includes instructions on how
to fold it up (your puzzle input). For example:

    6,10
    0,14
    9,10
    0,3
    10,4
    4,11
    6,0
    6,12
    4,1
    0,13
    10,12
    3,4
    3,0
    8,4
    1,10
    2,14
    8,10
    9,0

    fold along y=7
    fold along x=5

The first section is a list of dots on the transparent paper. `0,0` represents
the top-left coordinate. The first value, `x`, increases to the right. The
second value, `y`, increases downward. So, the coordinate `3,0` is to the
right of `0,0`, and the coordinate `0,7` is below `0,0`. The coordinates in
this example form the following pattern, where `#` is a dot on the paper and
`.` is an empty, unmarked position:

    ...#..#..#.
    ....#......
    ...........
    #..........
    ...#....#.#
    ...........
    ...........
    ...........
    ...........
    ...........
    .#....#.##.
    ....#......
    ......#...#
    #..........
    #.#........

Then, there is a list of fold instructions. Each instruction indicates a line
on the transparent paper and wants you to fold the paper up (for horizontal
`y=...` lines) or left (for vertical `x=...` lines). In this example, the
first fold instruction is `fold along y=7`, which designates the line formed
by all of the positions where `y` is `7` (marked here with `-`):

    ...#..#..#.
    ....#......
    ...........
    #..........
    ...#....#.#
    ...........
    ...........
    -----------
    ...........
    ...........
    .#....#.##.
    ....#......
    ......#...#
    #..........
    #.#........

Because this is a horizontal line, fold the bottom half up. Some of the dots
might end up overlapping after the fold is complete, but dots will never
appear exactly on a fold line. The result of doing this fold looks like this:

    #.##..#..#.
    #...#......
    ......#...#
    #...#......
    .#.#..#.###
    ...........
    ...........

Now, only `17` dots are visible.

Notice, for example, the two dots in the bottom left corner before the
transparent paper is folded; after the fold is complete, those dots appear in
the top left corner (at `0,0` and `0,1`). Because the paper is transparent,
the dot just below them in the result (at `0,3`) remains visible, as it can be
seen through the transparent paper.

Also notice that some dots can end up overlapping; in this case, the dots
merge together and become a single dot.

The second fold instruction is `fold along x=5`, which indicates this line:

    #.##.|#..#.
    #...#|.....
    .....|#...#
    #...#|.....
    .#.#.|#.###
    .....|.....
    .....|.....

Because this is a vertical line, fold left:

    #####
    #...#
    #...#
    #...#
    #####
    .....
    .....

The instructions made a square!

The transparent paper is pretty big, so for now, focus on just completing the
first fold. After the first fold in the example above, `17` dots are visible -
dots that end up overlapping after the fold is completed count as a single
dot.

How many dots are visible after completing just the first fold instruction on
your transparent paper?
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().split('\n\n')

data = []
x_max = 0
y_max = 0

for z in raw_data[0].splitlines():
    parts = z.split(',')
    x = int(parts[0])
    y = int(parts[1])
    if x > x_max:
        x_max = x
    if y > y_max:
        y_max = y
    data.append([x, y])

folds = [x.split(' ')[-1].split('=') for x in raw_data[-1].splitlines()]

grid = [['.' for _ in range(x_max+1)] for _ in range(y_max+1)]


def print_grid(g):
    for i, r in enumerate(g):
        l = f' {i} ' if i < 10 else f'{i} '
        print(f"{l}{''.join(r)}")
    print('')


for x, y in data:
    grid[int(y)][int(x)] = '#'


def y_fold(l, g):
    top = g[:l]
    bottom = list(reversed(g[-l:]))

    new_grid = top
    visible = 0

    for y, row in enumerate(bottom):
        for x, cell in enumerate(row):
            if cell == '#' or top[y][x] == '#':
                new_grid[y][x] = '#'
                visible += 1

    return visible, new_grid


def x_fold(l, g):
    left = []
    right = []

    for row in g:
        left.append(row[:l])
        right.append(list(reversed(row[-l:])))

    new_grid = left
    visible = 0

    for y, row in enumerate(right):
        for x, cell in enumerate(row):
            if cell == '#' or left[y][x] == '#':
                new_grid[y][x] = '#'
                visible += 1

    return visible, new_grid


current = grid

for axis, line in folds:
    line = int(line)

    # Vertical
    if axis == 'y':
        vis, new_g = y_fold(line, current)

    # Horizontal
    else:
        vis, new_g = x_fold(line, current)

    current = new_g
    print(vis)
    break

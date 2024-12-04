#!/usr/bin/env python
"""
--- Part Two ---

You realize you misread the scan. There isn't an endless void at the bottom of
the scan - there's floor, and you're standing on it!

You don't have time to scan the floor, so assume the floor is an infinite
horizontal line with a `y` coordinate equal to two plus the highest `y`
coordinate of any point in your scan.

In the example above, the highest `y` coordinate of any point is `9`, and so
the floor is at `y=11`. (This is as if your scan contained one extra rock path
like `-infinity,11 -> infinity,11`.) With the added floor, the example above
now looks like this:

            ...........+........
            ....................
            ....................
            ....................
            .........#...##.....
            .........#...#......
            .......###...#......
            .............#......
            .............#......
            .....#########......
            ....................
    <-- etc #################### etc -->

To find somewhere safe to stand, you'll need to simulate falling sand until a
unit of sand comes to rest at `500,0`, blocking the source entirely and
stopping the flow of sand into the cave. In the example above, the situation
finally looks like this after `93` units of sand come to rest:

    ............o............
    ...........ooo...........
    ..........ooooo..........
    .........ooooooo.........
    ........oo#ooo##o........
    .......ooo#ooo#ooo.......
    ......oo###ooo#oooo......
    .....oooo.oooo#ooooo.....
    ....oooooooooo#oooooo....
    ...ooo#########ooooooo...
    ..ooooo.......ooooooooo..
    #########################

Using your scan, simulate the falling sand until the source of the sand
becomes blocked. How many units of sand come to rest?
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

data = [[y.split(',') for y in x.split(' -> ')] for x in raw_data]

rocks = []
max_x = 0
max_y = 0

for r in data:
    rock = []
    for c in r:
        new_x = int(c[0])
        new_y = int(c[1])
        if new_x > max_x:
            max_x = new_x
        if new_y > max_y:
            max_y = new_y
        rock.append([new_x, new_y])
    rocks.append(rock)

floor = max_y + 2
cave = [['.' for _ in range(max_x*2)] for _ in range(floor+1)]

for rock in rocks:
    for i in range(len(rock))[1:]:
        x1, y1 = rock[i-1]
        x2, y2 = rock[i]

        if x1 == x2:
            yA, yB = (y1, y2) if y1 < y2 else (y2, y1)
            while yB >= yA:
                cave[yA][x1] = '#'
                yA += 1

        elif y1 == y2:
            xA, xB = (x1, x2) if x1 < x2 else (x2, x1)
            while xB >= xA:
                cave[y1][xA] = '#'
                xA += 1


def sand():
    x, y = 500, 0

    while True:
        # Check for floor
        if y+1 == floor:
            cave[y][x] = 'o'
            if x == 500 and y == 0:
                return False
            break
        # Next cell down
        elif cave[y+1][x] == '.':
            y += 1
        # Down/left
        elif cave[y+1][x-1] == '.':
            y += 1
            x -= 1
        # Down/right
        elif cave[y+1][x+1] == '.':
            y += 1
            x += 1
        # Rest
        else:
            cave[y][x] = 'o'
            if x == 500 and y == 0:
                return False
            break

    return True


units = 1

while True:
    if not sand():
        break
    units += 1

print(units)


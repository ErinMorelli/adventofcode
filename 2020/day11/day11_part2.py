#!/usr/bin/env python
"""
As soon as people start to arrive, you realize your mistake. People don't just
care about adjacent seats - they care about the first seat they can see in
each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats,
consider the first seat in each of those eight directions. For example, the
empty seat below would see eight occupied seats:

    .......#.
    ...#.....
    .#.......
    .........
    ..#L....#
    ....#....
    .........
    #........
    ...#.....

The leftmost empty seat below would only see one empty seat, but cannot see
any of the occupied ones:

    .............
    .L.L.#.#.#.#.
    .............

The empty seat below would see no occupied seats:

    .##.##.
    #.#.#.#
    ##...##
    ...L...
    ##...##
    #.#.#.#
    .##.##.

Also, people seem to be more tolerant than you expected: it now takes five or
more visible occupied seats for an occupied seat to become empty (rather than
four or more from the previous rules). The other rules still apply: empty
seats that see no occupied seats become occupied, seats matching no rule don't
change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating
area to shift around as follows.

Again, at this point, people stop shifting around and the seating area reaches
equilibrium. Once this occurs, you count `26` occupied seats.

Given the new visibility method and the rule change for occupied seats
becoming empty, once equilibrium is reached, how many seats end up occupied?
"""
import copy

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

data = [list(x) for x in raw_data]


def find_neighbors(x, y, rows):
    neighbors = []

    # South
    s = x + 1
    while s < len(rows):
        val = rows[s][y]
        if val == '.':
            s += 1
        else:
            neighbors.append(val)
            break

    # North
    n = x - 1
    while n >= 0:
        val = rows[n][y]
        if val == '.':
            n -= 1
        else:
            neighbors.append(val)
            break

    # East
    e = y + 1
    while e < len(rows[x]):
        val = rows[x][e]
        if val == '.':
            e += 1
        else:
            neighbors.append(val)
            break

    # West
    w = y - 1
    while w >= 0:
        val = rows[x][w]
        if val == '.':
            w -= 1
        else:
            neighbors.append(val)
            break

    # South West
    s = x + 1
    w = y - 1
    while w >= 0 and s < len(rows):
        val = rows[s][w]
        if val == '.':
            s += 1
            w -= 1
        else:
            neighbors.append(val)
            break

    # North West
    n = x - 1
    w = y - 1
    while w >= 0 and n >= 0:
        val = rows[n][w]
        if val == '.':
            n -= 1
            w -= 1
        else:
            neighbors.append(val)
            break

    # North East
    n = x - 1
    e = y + 1
    while e < len(rows[x]) and n >= 0:
        val = rows[n][e]
        if val == '.':
            n -= 1
            e += 1
        else:
            neighbors.append(val)
            break

    # South East
    s = x + 1
    e = y + 1
    while e < len(rows[x]) and s < len(rows):
        val = rows[s][e]
        if val == '.':
            s += 1
            e += 1
        else:
            neighbors.append(val)
            break

    return neighbors


tracker = 0


def apply_rules(rows):
    new_rows = copy.deepcopy(rows)
    changes = 0
    occupied = 0

    for x, row in enumerate(rows):
        for y, col in enumerate(row):
            if col == '.':
                continue

            adj = find_neighbors(x, y, rows)

            # Rule 1
            if col == 'L' and '#' not in adj:
                new_rows[x][y] = '#'
                changes += 1

            # Rule 2
            if col == '#' and adj.count('#') >= 5:
                new_rows[x][y] = 'L'
                changes += 1

        occupied += new_rows[x].count('#')

    if changes == 0:
        print(f'occupied: {occupied}')
        return

    apply_rules(new_rows)


apply_rules(data)

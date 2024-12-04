#!/usr/bin/env python
"""
By modeling the process people use to choose (or abandon) their seat in the
waiting area, you're pretty sure you can predict the best place to sit. You
make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (`.`), an
empty seat (`L`), or an occupied seat (`#`). For example, the initial seat
layout might look like this:

    L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL

Now, you just need to model the people who will be arriving shortly.
Fortunately, people are entirely predictable and always follow a simple set of
rules. All decisions are based on the number of occupied seats adjacent to a
given seat (one of the eight positions immediately up, down, left, right, or
diagonal from the seat). The following rules are applied to every seat
simultaneously:

  * If a seat is empty (`L`) and there are no occupied seats adjacent to it,
    the seat becomes occupied.
  * If a seat is occupied (`#`) and four or more seats adjacent to it are also
    occupied, the seat becomes empty.
  * Otherwise, the seat's state does not change.

Floor (`.`) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes
occupied:

    #.##.##.##
    #######.##
    #.#.#..#..
    ####.##.##
    #.##.##.##
    #.#####.##
    ..#.#.....
    ##########
    #.######.#
    #.#####.##

After a second round, the seats with four or more occupied adjacent seats
become empty again:

    #.LL.L#.##
    #LLLLLL.L#
    L.L.L..L..
    #LLL.LL.L#
    #.LL.LL.LL
    #.LLLL#.##
    ..L.L.....
    #LLLLLLLL#
    #.LLLLLL.L
    #.#LLLL.##

This process continues for three more rounds.

At this point, something interesting happens: the chaos stabilizes and further
applications of these rules cause no seats to change state! Once people stop
moving around, you count `37` occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no
seats change state. How many seats end up occupied?
"""
import copy

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

data = [list(x) for x in raw_data]


def apply_rules(rows):
    new_rows = copy.deepcopy(rows)
    changes = 0
    occupied = 0

    for x, row in enumerate(rows):
        prev_row = rows[x-1] if x > 0 else None
        next_row = rows[x+1] if x+1 < len(rows) else None

        for y, col in enumerate(row):
            if col == '.':
                continue

            adj = []

            for i, r in enumerate([row, prev_row, next_row]):
                if r:
                    if i > 0:
                        adj.append(r[y])
                    if y > 0:
                        adj.append(r[y-1])
                    if y+1 < len(row):
                        adj.append(r[y+1])

            # Rule 1
            if col == 'L' and '#' not in adj:
                new_rows[x][y] = '#'
                changes += 1

            # Rule 2
            if col == '#' and adj.count('#') >= 4:
                new_rows[x][y] = 'L'
                changes += 1

        occupied += new_rows[x].count('#')

    if changes == 0:
        print(f'occupied: {occupied}')
        return

    apply_rules(new_rows)


apply_rules(data)

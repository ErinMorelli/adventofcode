#!/usr/bin/env python
"""
As your flight slowly drifts through the sky, the Elves at the Mythical
Information Bureau at the North Pole contact you. They'd like some help
debugging a malfunctioning experimental energy source aboard one of their
super-secret imaging satellites.

The experimental energy source is based on cutting-edge technology: a set of
Conway Cubes contained in a pocket dimension! When you hear it's having
problems, you can't help but agree to take a look.

The pocket dimension contains an infinite 3-dimensional grid. At every integer
3-dimensional coordinate (`x,y,z`), there exists a single cube which is either
active or inactive.

In the initial state of the pocket dimension, almost all cubes start inactive.
The only exception to this is a small flat region of cubes (your puzzle
input); the cubes in this region start in the specified active (`#`) or
inactive (`.`) state.

The energy source then proceeds to boot up by executing six cycles.

Each cube only ever considers its neighbors: any of the 26 other cubes where
any of their coordinates differ by at most `1`. For example, given the cube at
`x=1,y=2,z=3`, its neighbors include the cube at `x=2,y=2,z=2`, the cube at
`x=0,y=2,z=3`, and so on.

During a cycle, all cubes simultaneously change their state according to the
following rules:

  * If a cube is active and exactly `2` or `3` of its neighbors are also
    active, the cube remains active. Otherwise, the cube becomes inactive.
  * If a cube is inactive but exactly `3` of its neighbors are active, the
    cube becomes active. Otherwise, the cube remains inactive.

The engineers responsible for this experimental energy source would like you
to simulate the pocket dimension and determine what the configuration of cubes
should be at the end of the six-cycle boot process.

For example, consider the following initial state:

    .#.
    ..#
    ###

Even though the pocket dimension is 3-dimensional, this initial state
represents a small 2-dimensional slice of it. (In particular, this initial
state defines a 3x3x1 region of the 3-dimensional space.)

Starting with your given initial configuration, simulate six cycles. How many
cubes are left in the active state after the sixth cycle?
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

active = '#'
inactive = '.'


def find_neighbors(x, y, rows):
    """
    NW N NE
    W  x  E
    sW S SE
    """
    neighbors = list()
    row_len = len(rows)
    col_len = len(rows[y])

    try:
        if y + 1 < row_len:
            neighbors.append(rows[y+1][x])    # N
    except IndexError:
        pass
    try:
        if y + 1 < row_len and x + 1 < col_len:
            neighbors.append(rows[y+1][x+1])  # NE
    except IndexError:
        pass
    try:
        if x + 1 < col_len:
            neighbors.append(rows[y][x+1])    # E
    except IndexError:
        pass
    try:
        if y - 1 >= 0 and x + 1 < col_len:
            neighbors.append(rows[y-1][x+1])  # SE
    except IndexError:
        pass
    try:
        if y - 1 >= 0:
            neighbors.append(rows[y-1][x])    # S
    except IndexError:
        pass
    try:
        if y - 1 >= 0 and x - 1 >= 0:
            neighbors.append(rows[y-1][x-1])  # SW
    except IndexError:
        pass
    try:
        if x - 1 >= 0:
            neighbors.append(rows[y][x-1])    # W
    except IndexError:
        pass
    try:
        if x - 1 >= 0 and y + 1 < row_len:
            neighbors.append(rows[y+1][x-1])  # NW
    except IndexError:
        pass
    try:
        neighbors.append(rows[y][x])  # Center
    except IndexError:
        pass

    return neighbors


def find_3d_neighbors(x, y, z, dimensions):
    neighbors = []
    for zx in [z-1, z, z+1]:
        try:
            if zx >= 0:
                rows = dimensions[zx]
                new_neighbors = find_neighbors(x, y, rows)
                neighbors.extend(new_neighbors)
        except IndexError:
            continue

    original = dimensions[z][y][x]
    original_idx = neighbors.index(original)
    del neighbors[original_idx]

    return neighbors


def apply_rules(dimensions):
    new_row = [inactive for _ in range(len(dimensions[0][0])+2)]
    new_dimension = [new_row for _ in range(len(dimensions[0])+2)]

    active_count = 0
    new_dimensions = [new_dimension]

    for z, dimension in enumerate(dimensions):
        new_rows = [new_row]

        for y, row in enumerate(dimension):
            new_cols = [inactive]

            for x, col in enumerate(row):
                new_state = col

                neighbors = find_3d_neighbors(x, y, z, dimensions)
                active_neighbors = neighbors.count(active)

                if col == active and active_neighbors not in [2, 3]:
                    new_state = inactive

                elif col == inactive and active_neighbors == 3:
                    new_state = active

                if new_state == active:
                    active_count += 1

                new_cols.append(new_state)

            new_cols.append(inactive)
            new_rows.append(new_cols)

        new_rows.append(new_row)
        new_dimensions.append(new_rows)

    new_dimensions.append(new_dimension)
    return new_dimensions, active_count


z1 = [[inactive] + list(x) + [inactive] for x in raw_data]

new_row = [inactive for _ in range(len(z1[0]))]
z2 = [new_row] + z1 + [new_row]

new_dimension = [new_row for _ in range(len(z2))]
initial_state = [new_dimension, z2, new_dimension]

state0 = initial_state.copy()
state1, _ = apply_rules(state0)
state2, _ = apply_rules(state1)
state3, _ = apply_rules(state2)
state4, _ = apply_rules(state3)
state5, _ = apply_rules(state4)
state6, active_count = apply_rules(state5)

print(f'active: {active_count}')

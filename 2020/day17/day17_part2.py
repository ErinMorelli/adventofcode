#!/usr/bin/env python
"""
For some reason, your simulated results don't match what the experimental
energy source engineers expected. Apparently, the pocket dimension actually
has four spatial dimensions, not three.

The pocket dimension contains an infinite 4-dimensional grid. At every integer
4-dimensional coordinate (`x,y,z,w`), there exists a single cube (really, a
hypercube) which is still either active or inactive.

Each cube only ever considers its neighbors: any of the 80 other cubes where
any of their coordinates differ by at most `1`. For example, given the cube at
`x=1,y=2,z=3,w=4`, its neighbors include the cube at `x=2,y=2,z=3,w=3`, the
cube at `x=0,y=2,z=3,w=4`, and so on.

The initial state of the pocket dimension still consists of a small flat
region of cubes. Furthermore, the same rules for cycle updating still apply:
during each cycle, consider the number of active neighbors of each cube.

For example, consider the same initial state as in the example above. Even
though the pocket dimension is 4-dimensional, this initial state represents a
small 2-dimensional slice of it. (In particular, this initial state defines a
3x3x1x1 region of the 4-dimensional space.)

Starting with your given initial configuration, simulate six cycles in a
4-dimensional space. How many cubes are left in the active state after the
sixth cycle?
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
    return neighbors


def find_4d_neighbors(x, y, z, w, spaces):
    neighbors = []

    for wx in [w-1, w, w+1]:
        try:
            if wx >= 0:
                dimensions = spaces[wx]
                new_neighbors = find_3d_neighbors(x, y, z, dimensions)
                neighbors.extend(new_neighbors)
        except IndexError:
            continue

    original = spaces[w][z][y][x]
    original_idx = neighbors.index(original)
    del neighbors[original_idx]

    return neighbors


def apply_rules(spaces, debug=False):
    active_count = 0

    new_row = [inactive for _ in range(len(spaces[0][0][0])+2)]
    new_dimension = [new_row for _ in range(len(spaces[0][0])+2)]
    new_space = [new_dimension for _ in range(len(spaces[0])+2)]

    new_spaces = [new_space]

    for w, space in enumerate(spaces):
        new_dimensions = [new_dimension]

        for z, dimension in enumerate(space):
            new_rows = [new_row]

            for y, row in enumerate(dimension):
                new_cols = [inactive]

                for x, col in enumerate(row):
                    new_state = col

                    neighbors = find_4d_neighbors(x, y, z, w, spaces)
                    active_neighbors = neighbors.count(active)

                    if col == active and active_neighbors not in [2, 3]:
                        new_state = inactive

                    elif col == inactive and active_neighbors == 3:
                        new_state = active

                    if new_state == active:
                        active_count += 1

                    if debug:
                        print(f'{(x, y, z, w)} "{col}" --> "{new_state}" '
                              f'neighbors: {len(neighbors)} '
                              f'({active_neighbors})')

                    new_cols.append(new_state)

                new_cols.append(inactive)
                new_rows.append(new_cols)

            new_rows.append(new_row)
            new_dimensions.append(new_rows)

        new_dimensions.append(new_dimension)
        new_spaces.append(new_dimensions)

    new_spaces.append(new_space)
    return new_spaces, active_count


z1 = [[inactive] + list(x) + [inactive] for x in raw_data]

new_row = [inactive for _ in range(len(z1[0]))]
z2 = [new_row] + z1 + [new_row]

new_dimension = [new_row for _ in range(len(z2))]
z3 = [new_dimension, z2, new_dimension]

new_space = [new_dimension for _ in range(len(z3))]
initial_state = [new_space, z3, new_space]

state0 = initial_state.copy()
state1, _ = apply_rules(state0)
state2, _ = apply_rules(state1)
state3, _ = apply_rules(state2)
state4, _ = apply_rules(state3)
state5, _ = apply_rules(state4)
state6, active_count = apply_rules(state5)

print(f'active: {active_count}')

#!/usr/bin/env python
"""
--- Part Two ---

As you walk up the hill, you suspect that the Elves will want to turn this
into a hiking trail. The beginning isn't very scenic, though; perhaps you can
find a better starting point.

To maximize exercise while hiking, the trail should start as low as possible:
elevation `a`. The goal is still the square marked `E`. However, the trail
should still be direct, taking the fewest steps to reach its goal. So, you'll
need to find the shortest path from any square at elevation `a` to the square
marked `E`.

Again consider the example from above:

    Sabqponm
    abcryxxl
    accszExk
    acctuvwj
    abdefghi

Now, there are six choices for starting position (five marked `a`, plus the
square marked `S` that counts as being at elevation `a`). If you start at the
bottom-left square, you can reach the goal most quickly:

    ...v<<<<
    ...vv<<^
    ...v>E^^
    .>v>>>^^
    >^>>>>>^

This path reaches the goal in only `29` steps, the fewest possible.

What is the fewest steps required to move starting from any square with
elevation `a` to the location that should get the best signal?
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()


class Node:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val
        self.visited = False
        self.parent = None

        if val == 'S':
            self.ord = ord('a')
        elif val == 'E':
            self.ord = ord('z') + 1
        else:
            self.ord = ord(val)

    def visit(self, parent):
        self.visited = True
        self.parent = parent

    def reset(self):
        self.visited = False
        self.parent = None

    def can_visit(self):
        return not self.visited

    def __cmp__(self, other):
        return self.x != other.x and self.y != other.y

    def __repr__(self):
        return f'Node<({self.x}, {self.y}) val={self.val} visited={self.visited}>'


init_grid = []
starts = []

for ri, raw_row in enumerate(raw_data):
    row = []
    for ci, cell in enumerate(list(raw_row)):
        new_node = Node(ci, ri, cell)
        if (
            cell == 'S' or (
                (
                    ci == 0 or ci+1 == len(raw_row) or
                    ri == 0 or ri+1 == len(raw_data)
                )
                and cell == 'a'
            )
        ):
            starts.append(new_node)
        row.append(new_node)
    init_grid.append(row)


def find_path(grid, root):
    queue = list()

    root.visit(None)
    grid[root.y][root.x] = root

    queue.append(root)

    while queue:
        curr = queue.pop(0)

        if curr.val == 'E':
            return curr

        adjacent = [
            [curr.x, curr.y-1],  # up
            [curr.x, curr.y+1],  # down
            [curr.x-1, curr.y],  # left
            [curr.x+1, curr.y]   # right
        ]

        for i, (x, y) in enumerate(adjacent):
            if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
                node = grid[y][x]
                if node.can_visit() and node.ord <= curr.ord+1:
                    node.visit(curr)
                    grid[y][x] = node
                    queue.append(node)


lowest = 0

for start in reversed(starts):
    end = find_path(init_grid, start)

    if end:
        p = end.parent
        count = 0
        while p is not None:
            count += 1
            p = p.parent

        if lowest == 0 or count < lowest:
            lowest = count

    for r in init_grid:
        for c in r:
            c.reset()

print(lowest)

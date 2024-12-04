#!/usr/bin/env python
"""
--- Day 12: Hill Climbing Algorithm ---

You try contacting the Elves using your handheld device, but the river you're
following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle
input). The heightmap shows the local area from above broken into a grid; the
elevation of each square of the grid is given by a single lowercase letter,
where `a` is the lowest elevation, `b` is the next-lowest, and so on up to the
highest elevation, `z`.

Also included on the heightmap are marks for your current position (`S`) and
the location that should get the best signal (`E`). Your current position
(`S`) has elevation `a`, and the location that should get the best signal
(`E`) has elevation `z`.

You'd like to reach `E`, but to save energy, you should do it in as few steps
as possible. During each step, you can move exactly one square up, down, left,
or right. To avoid needing to get out your climbing gear, the elevation of the
destination square can be at most one higher than the elevation of your
current square; that is, if your current elevation is `m`, you could step to
elevation `n`, but not to elevation `o`. (This also means that the elevation
of the destination square can be much lower than the elevation of your current
square.)

For example:

    Sabqponm
    abcryxxl
    accszExk
    acctuvwj
    abdefghi

Here, you start in the top-left corner; your goal is near the middle. You
could start by moving down or right, but eventually you'll need to head toward
the `e` at the bottom. From there, you can spiral around to the goal:

    v..v<<<<
    >v.vv<<^
    .>vv>E^^
    ..v>>>^^
    ..>>>>>^

In the above diagram, the symbols indicate whether the path exits each square
moving up (`^`), down (`v`), left (`<`), or right (`>`). The location that
should get the best signal is still `E`, and `.` marks unvisited squares.

This path reaches the goal in `31` steps, the fewest possible.

What is the fewest steps required to move from your current position to the
location that should get the best signal?
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

    def can_visit(self):
        return not self.visited

    def __cmp__(self, other):
        return self.x != other.x and self.y != other.y

    def __repr__(self):
        return f'Node<({self.x}, {self.y}) val={self.val} visited={self.visited}>'


init_grid = []
start = None

for ri, raw_row in enumerate(raw_data):
    row = []
    for ci, cell in enumerate(list(raw_row)):
        new_node = Node(ci, ri, cell)
        if cell == 'S':
            start = new_node
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


end = find_path(init_grid, start)

p = end.parent
count = 0
while p is not None:
    count += 1
    p = p.parent

print(count)

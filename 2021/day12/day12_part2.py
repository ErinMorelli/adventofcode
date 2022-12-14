#!/usr/bin/env python
"""
--- Part Two ---

After reviewing the available paths, you realize you might have time to visit
a single small cave twice. Specifically, big caves can be visited any number
of times, a single small cave can be visited at most twice, and the remaining
small caves can be visited at most once. However, the caves named `start` and
`end` can only be visited exactly once each: once you leave the `start` cave,
you may not return to it, and once you reach the `end` cave, the path must end
immediately.

Now, the `36` possible paths through the first example above are:

    start,A,b,A,b,A,c,A,end
    start,A,b,A,b,A,end
    start,A,b,A,b,end
    start,A,b,A,c,A,b,A,end
    start,A,b,A,c,A,b,end
    start,A,b,A,c,A,c,A,end
    start,A,b,A,c,A,end
    start,A,b,A,end
    start,A,b,d,b,A,c,A,end
    start,A,b,d,b,A,end
    start,A,b,d,b,end
    start,A,b,end
    start,A,c,A,b,A,b,A,end
    start,A,c,A,b,A,b,end
    start,A,c,A,b,A,c,A,end
    start,A,c,A,b,A,end
    start,A,c,A,b,d,b,A,end
    start,A,c,A,b,d,b,end
    start,A,c,A,b,end
    start,A,c,A,c,A,b,A,end
    start,A,c,A,c,A,b,end
    start,A,c,A,c,A,end
    start,A,c,A,end
    start,A,end
    start,b,A,b,A,c,A,end
    start,b,A,b,A,end
    start,b,A,b,end
    start,b,A,c,A,b,A,end
    start,b,A,c,A,b,end
    start,b,A,c,A,c,A,end
    start,b,A,c,A,end
    start,b,A,end
    start,b,d,b,A,c,A,end
    start,b,d,b,A,end
    start,b,d,b,end
    start,b,end

The slightly larger example above now has `103` paths through it, and the even
larger example now has `3509` paths through it.

Given these new rules, how many paths through this cave system are there?
"""
from collections import defaultdict

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

data = [x.split('-') for x in raw_data]
caves = defaultdict()


class Cave:
    def __init__(self, name: str):
        self.name = name
        self.neighbors = set()

    def add_neighbor(self, name):
        if name != 'start':
            self.neighbors.add(name)

    def __repr__(self):
        return f'<Cave name="{self.name}" neighbors={len(self.neighbors)}>'


for name1, name2 in data:
    if name1 in caves.keys():
        cave1 = caves[name1]
    else:
        cave1 = Cave(name1)
        caves[name1] = cave1

    if name2 in caves.keys():
        cave2 = caves[name2]
    else:
        cave2 = Cave(name2)
        caves[name2] = cave2

    cave1.add_neighbor(name2)
    cave2.add_neighbor(name1)


root = caves['start']
routes = set()


def find_paths(node: Cave, route=''):
    route += node.name

    if node.name == 'end':
        routes.add(route)
        return

    for cave_name in node.neighbors:
        cave = caves[cave_name]
        if cave_name.islower() and cave_name in route:
            if not route.startswith('start'):
                continue
            find_paths(cave, cave_name + route)
        else:
            find_paths(cave, route)


find_paths(root)
print(len(routes))

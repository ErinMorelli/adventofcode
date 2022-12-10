#!/usr/bin/env python
"""
???
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
routes = []


def find_paths(node: Cave, route=''):
    route += node.name

    if node.name == 'end':
        routes.append(route)
        return

    for cave_name in node.neighbors:
        if cave_name.islower() and cave_name in route:
            continue
        cave = caves[cave_name]
        find_paths(cave, route)


find_paths(root)
print(len(routes))

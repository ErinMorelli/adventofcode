#!/usr/bin/env python
"""
To completely determine whether you have enough adapters, you'll need to
figure out how many different ways they can be arranged. Every arrangement
needs to connect the charging outlet to your device. The previous rules about
when adapters can successfully connect still apply.

The first example above (the one that starts with 16, 10, 15) supports the
following arrangements:

(0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 12, 15, 16, 19, (22)

(The charging outlet and your device's built-in adapter are shown in
parentheses.) Given the adapters from the first example, the total number of
arrangements that connect the charging outlet to your device is 8.

You glance back down at your bag and try to remember why you brought so many
adapters; there must be more than a trillion valid ways to arrange them!
Surely, there must be an efficient way to count the arrangements.

What is the total number of distinct ways you can arrange the adapters to
connect the charging outlet to your device?
"""
from pprint import pprint

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

data = sorted([int(i) for i in raw_data])

jolt_diff = 3
highest_rating = data[-1]
device_rating = highest_rating + jolt_diff

data = [0] + data
data.append(device_rating)

node_count = 0


class AdapterTree:
    def __init__(self, val):
        self.val = val
        self.nodes = []

    def add_node(self, val):
        self.nodes.append(AdapterTree(val))

    def __repr__(self):
        return f'<AdapterTree val={self.val}, nodes={len(self.nodes)}>'


def set_nodes(parent, adapter):
    if adapter < device_rating:
        for diff in range(1, jolt_diff+1):
            new_adapter = adapter + diff
            if new_adapter in data:
                parent.add_node(new_adapter)
        for node in parent.nodes:
            set_nodes(node, node.val)
    elif adapter == device_rating:
        global node_count
        node_count += 1


tree = AdapterTree(0)
set_nodes(tree, 0)
print(tree)
print(node_count)

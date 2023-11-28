#!/usr/bin/env python
"""
--- Day 16: Proboscidea Volcanium ---

The sensors have led you to the origin of the distress signal: yet another
handheld device, just like the one the Elves gave you. However, you don't see
any Elves around; instead, the device is surrounded by elephants! They must
have gotten lost in these tunnels, and one of the elephants apparently figured
out how to turn on the distress signal.

The ground rumbles again, much stronger this time. What kind of cave is this,
exactly? You scan the cave with your handheld device; it reports mostly
igneous rock, some ash, pockets of pressurized gas, magma... this isn't just a
cave, it's a volcano!

You need to get the elephants out of here, quickly. Your device estimates that
you have 30 minutes before the volcano erupts, so you don't have time to go
back out the way you came in.

You scan the cave for other options and discover a network of pipes and
pressure-release valves. You aren't sure how such a system got into a volcano,
but you don't have time to complain; your device produces a report (your
puzzle input) of each valve's flow rate if it were opened (in pressure per
minute) and the tunnels you could use to move between the valves.

There's even a valve in the room you and the elephants are currently standing
in labeled `AA`. You estimate it will take you one minute to open a single
valve and one minute to follow any tunnel from one valve to another. What is
the most pressure you could release?

For example, suppose you had the following scan output:

    Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
    Valve BB has flow rate=13; tunnels lead to valves CC, AA
    Valve CC has flow rate=2; tunnels lead to valves DD, BB
    Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
    Valve EE has flow rate=3; tunnels lead to valves FF, DD
    Valve FF has flow rate=0; tunnels lead to valves EE, GG
    Valve GG has flow rate=0; tunnels lead to valves FF, HH
    Valve HH has flow rate=22; tunnel leads to valve GG
    Valve II has flow rate=0; tunnels lead to valves AA, JJ
    Valve JJ has flow rate=21; tunnel leads to valve II

All of the valves begin closed. You start at valve `AA`, but it must be
damaged or jammed or something: its flow rate is `0`, so there's no point in
opening it. However, you could spend one minute moving to valve `BB` and
another minute opening it; doing so would release pressure during the
remaining 28 minutes at a flow rate of `13`, a total eventual pressure release
of `28 * 13 = 364`. Then, you could spend your third minute moving to valve
`CC` and your fourth minute opening it, providing an additional 26 minutes of
eventual pressure release at a flow rate of `2`, or `52` total pressure
released by valve `CC`.

Making your way through the tunnels like this, you could probably open many or
all of the valves by the time 30 minutes have elapsed. However, you need to
release as much pressure as possible, so you'll need to be methodical.
Instead, consider this approach:

    == Minute 1 ==
    No valves are open.
    You move to valve DD.

    == Minute 2 ==
    No valves are open.
    You open valve DD.

    == Minute 3 ==
    Valve DD is open, releasing 20 pressure.
    You move to valve CC.

    == Minute 4 ==
    Valve DD is open, releasing 20 pressure.
    You move to valve BB.

    == Minute 5 ==
    Valve DD is open, releasing 20 pressure.
    You open valve BB.

    == Minute 6 ==
    Valves BB and DD are open, releasing 33 pressure.
    You move to valve AA.

    == Minute 7 ==
    Valves BB and DD are open, releasing 33 pressure.
    You move to valve II.

    == Minute 8 ==
    Valves BB and DD are open, releasing 33 pressure.
    You move to valve JJ.

    == Minute 9 ==
    Valves BB and DD are open, releasing 33 pressure.
    You open valve JJ.

    == Minute 10 ==
    Valves BB, DD, and JJ are open, releasing 54 pressure.
    You move to valve II.

    == Minute 11 ==
    Valves BB, DD, and JJ are open, releasing 54 pressure.
    You move to valve AA.

    == Minute 12 ==
    Valves BB, DD, and JJ are open, releasing 54 pressure.
    You move to valve DD.

    == Minute 13 ==
    Valves BB, DD, and JJ are open, releasing 54 pressure.
    You move to valve EE.

    == Minute 14 ==
    Valves BB, DD, and JJ are open, releasing 54 pressure.
    You move to valve FF.

    == Minute 15 ==
    Valves BB, DD, and JJ are open, releasing 54 pressure.
    You move to valve GG.

    == Minute 16 ==
    Valves BB, DD, and JJ are open, releasing 54 pressure.
    You move to valve HH.

    == Minute 17 ==
    Valves BB, DD, and JJ are open, releasing 54 pressure.
    You open valve HH.

    == Minute 18 ==
    Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
    You move to valve GG.

    == Minute 19 ==
    Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
    You move to valve FF.

    == Minute 20 ==
    Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
    You move to valve EE.

    == Minute 21 ==
    Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
    You open valve EE.

    == Minute 22 ==
    Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
    You move to valve DD.

    == Minute 23 ==
    Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
    You move to valve CC.

    == Minute 24 ==
    Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
    You open valve CC.

    == Minute 25 ==
    Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

    == Minute 26 ==
    Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

    == Minute 27 ==
    Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

    == Minute 28 ==
    Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

    == Minute 29 ==
    Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

    == Minute 30 ==
    Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

This approach lets you release the most pressure possible in 30 minutes with
this valve layout, `1651`.

Work out the steps to release the most pressure in 30 minutes. What is the
most pressure you can release?
"""
import re
from collections import defaultdict
from pprint import pprint

# import pdb; pdb.set_trace()

# input_file = 'input.txt'
input_file = 'sample.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

time_limit = 30


class Valve:
    def __init__(self, name, rate=0):
        self.name = name
        self.rate = rate
        self.neighbors = list()
        self.is_open = False

    def open(self):
        self.is_open = True

    def set_rate(self, rate):
        self.rate = rate

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

    def __repr__(self):
        return f'Valve("{self.name}",' \
               f' rate: {self.rate},' \
               f' neighbors: [{", ".join(self.neighbors)}]' \
               f'{" OPEN" if self.is_open else ""})'


valves = dict()
with_value = list()

for row in raw_data:
    parsed = re.match(r'^Valve (\w+).+rate=(\d+);.+valves? ([\w,\s]+)$', row)
    vname = parsed.group(1)
    vrate = int(parsed.group(2))
    vchildren = parsed.group(3).split(', ')

    if vname in valves.keys():
        new_valve = valves[vname]
        new_valve.set_rate(vrate)
    else:
        new_valve = Valve(vname, vrate)

    for vchild in vchildren:
        if vchild in valves.keys():
            child_valve = valves[vchild]
        else:
            child_valve = Valve(vchild)

        child_valve.add_neighbor(vname)
        new_valve.add_neighbor(vchild)

        valves[vchild] = child_valve

    if vrate > 0:
        with_value.append(new_valve)

    valves[vname] = new_valve

pprint(valves)
print('')

with_value.sort(key=lambda x: x.rate, reverse=True)
pprint(with_value)
print('')


def calc_distances(source):
    queue = [source]
    visited = [source]
    distances = defaultdict(lambda: 99)
    while queue:
        node = queue.pop(0)
        if node == source:
            distances[node.name] = 0
        for v in node.neighbors:
            if v not in visited:
                if distances[v] > distances[node.name] + 1:
                    distances[v] = distances[node.name] + 1
                queue.append(valves[v])
                visited.append(v)
    return distances


dists = {}
for vname, vnode in valves.items():
    dists[vname] = calc_distances(vnode)


def calc_power(source, source_dist, opened, remaining):
    queue = [source]
    visited = [source.name]
    power = 0
    d = dists[source.name]

    while queue:
        node = queue.pop(0)
        if node == source:
            dist = source_dist
        else:
            dist = d[node.name]
        if node.rate and node.name not in opened and not node.is_open:
            power += node.rate * (remaining-dist-1)
        for n in node.neighbors:
            nv = valves[n]
            if n not in visited:
                queue.append(nv)
                visited.append(n)
    return power


def get_target(source, opened, time_left):
    largest = 0
    pick = None
    for c in source.neighbors:
        cv = valves[c]
        # Distance
        dist = dists[source.name][cv.name]
        # Power
        power = calc_power(cv, dist, opened, time_left)
        print('c', cv)
        print('power', power)
        # Get largest
        if power > largest:
            largest = power
            pick = cv
    return pick

# All of the valves begin closed. You start at valve AA, but it must be damaged
# or jammed or something: its flow rate is 0, so there's no point in opening it.
# However, you could spend one minute moving to valve BB and another minute
# opening it; doing so would release pressure during the remaining 28 minutes
# at a flow rate of 13, a total eventual pressure release of 28 * 13 = 364.
# Then, you could spend your third minute moving to valve CC and your fourth
# minute opening it, providing an additional 26 minutes of eventual pressure
# release at a flow rate of 2, or 52 total pressure released by valve CC.


node = valves['AA']
pressure = 0
released = 0
minute = 1

opened = list()

# while minute <= time_limit:
while minute <= 6:
    print(f'== Minute {minute} ==')
    print(f'Open: {", ".join(opened)}  Pressure: {pressure}')
    print('Node', node)

    # Increment released count
    released += pressure

    # Open
    if node.rate > 0 and node.name not in opened:
        print(f'Open {node.name}')
        pressure += node.rate
        node.open()
        opened.append(node.name)

    # Move
    else:
        # Calculate best node to visit next
        target = get_target(node, opened, time_limit-minute)
        if target:
            # Set new node
            print(f'Move to {target.name}')
            node = target
        else:
            print('No valid target')

    # Increment time
    minute += 1
    print('')

print(released)

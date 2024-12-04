#!/usr/bin/env python
"""
--- Part Two ---

Your handheld device indicates that the distress signal is coming from a
beacon nearby. The distress beacon is not detected by any sensor, but the
distress beacon must have `x` and `y` coordinates each no lower than `0` and
no larger than `4000000`.

To isolate the distress beacon's signal, you need to determine its tuning
frequency, which can be found by multiplying its `x` coordinate by `4000000`
and then adding its `y` coordinate.

In the example above, the search space is smaller: instead, the `x` and `y`
coordinates can each be at most `20`. With this reduced search area, there is
only a single position that could have a beacon: `x=14, y=11`. The tuning
frequency for this distress beacon is `56000011`.

Find the only possible position for the distress beacon. What is its tuning
frequency?
"""
import re

input_file = 'input.txt'
# input_file = 'sample.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()


min_val = 0
max_val = 4000000
# max_val = 20


# Calc manhattan distance
def distance(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    return abs(x2 - x1) + abs(y2 - y1)


def in_grid(coord):
    x, y = coord
    return (
        min_val <= x <= max_val and
        min_val <= y <= max_val
    )


def get_line(x0, y0, x1, y1):
    deltax = x1-x0
    dxsign = int(abs(deltax)/deltax)
    deltay = y1-y0
    dysign = int(abs(deltay)/deltay)
    deltaerr = abs(deltay/deltax)
    error = 0
    y = y0
    for x in range(x0, x1, dxsign):
        yield x, y
        error = error + deltaerr
        while error >= 0.5:
            y += dysign
            error -= 1
    yield x1, y1


data = list()

for row in raw_data:
    res = re.match(r'Sensor.+x=(-?\d+), y=(-?\d+):.+beacon.+x=(-?\d+), y=(-?\d+)', row)
    # Beacon
    beacon = [int(res.group(3)), int(res.group(4))]
    # Sensor
    sensor = [int(res.group(1)), int(res.group(2))]
    # Distance
    dist = distance(sensor, beacon)
    data.append([sensor, beacon, dist])

to_check = []

for sensor1 in data:
    s1, _, d1 = sensor1
    for sensor2 in data:
        s2, _, d2 = sensor2
        if (
            s1 == s2 or
            [sensor1, sensor2] in to_check or
            [sensor2, sensor1] in to_check
        ):
            continue
        dist = distance(s1, s2)
        val = d1 + d2 + 2
        if dist == val:
            to_check.append([sensor1, sensor2])

lines = []

for pair1, pair2 in to_check:
    (x1, y1), _, d1 = pair1
    (x2, y2), _, d2 = pair2

    up = y1 > y2
    right = x1 > x2

    # pair1 up/right = west -> south
    # pair2 down/left = north -> east
    if up and right:
        a1, b1 = [x1-d1-1, y1], [x1, y1+d1+1]
        a2, b2 = [x2, y2-d2-1], [x2+d2+1, y2]

    # pair1 up/left = east -> south
    # pair2 down/right = north -> west
    if up and not right:
        a1, b1 = [x1+d1+1, y1], [x1, y1+d1+1]
        a2, b2 = [x2, y2-d2-1], [x2-d2-1, y2]

    # pair1 down/right = north -> west
    # pair2 up/left = east -> south
    if not up and right:
        a1, b1 = [x1, y1-d1-1], [x1-d1-1, y1]
        a2, b2 = [x2+d2+1, y2], [x2, y2+d2+1]

    # pair1 down/left = north -> east
    # pair2 up/right = west -> south
    if not up and not right:
        a1, b1 = [x1, y1-d1-1], [x1+d1+1, y1]
        a2, b2 = [x2-d2-1, y2], [x2, y2+d2+1]

    lines.append([a1, b1])
    lines.append([a2, b2])


found = None
seen = []

for (x1, y1), (x2, y2) in lines:
    for x, y in get_line(x1, y1, x2, y2):
        coord = [x, y]
        if not in_grid(coord) or coord in seen:
            continue
        seen.append(coord)
        overlaps = False
        for sensor, beacon, dist in data:
            if (
                coord == sensor or
                coord == beacon or
                distance(sensor, coord) <= dist
            ):
                overlaps = True
                break
        if not overlaps:
            found = coord
            break

print(found)
freq = (found[0]*4000000) + found[1]
print(freq)

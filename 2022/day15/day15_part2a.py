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


# Calc manhattan distance
def distance(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    return abs(x2 - x1) + abs(y2 - y1)


data = list()

min_val = 0
max_val = 4000000
# max_val = 20

top_left = (min_val, min_val)
top_right = (min_val, max_val)
bottom_right = (max_val, max_val)
bottom_left = (max_val, min_val)

grid_corners = [top_left, top_right, bottom_right, bottom_left]

#  _
# | |
#  -
grid_lines = [
    [top_left, top_right],        # top/left -> top/right
    [top_right, bottom_right],    # top/right -> bottom/right
    [bottom_right, bottom_left],  # bottom/right -> bottom/left
    [bottom_left, top_left]       # bottom/left -> top/left
]

for row in raw_data:
    res = re.match(r'Sensor.+x=(-?\d+), y=(-?\d+):.+beacon.+x=(-?\d+), y=(-?\d+)', row)
    # Beacon
    beacon = [int(res.group(3)), int(res.group(4))]
    # Sensor
    sensor = [int(res.group(1)), int(res.group(2))]
    # Distance
    dist = distance(sensor, beacon)
    # Corners
    x, y = sensor
    corners = [
        [x, y-dist],  # north -y
        [x+dist, y],  # east +x
        [x, y+dist],  # south +y
        [x-dist, y]   # west -x
    ]
    data.append([sensor, beacon, dist, corners])


def get_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return int(x), int(y)


# /\
# \/
def get_lines(c):
    n, e, s, w = c
    return [
        [n, e],  # n -> e
        [e, s],  # e -> s
        [s, w],  # s -> w
        [w, n]   # w -> n
    ]


def in_grid(coord):
    x, y = coord
    return (
        min_val <= x <= max_val and
        min_val <= y <= max_val
    )


def get_intersections(dat):
    checked = []
    intersections = []

    for sig1, _, _, corners1 in dat:
        for line1 in get_lines(corners1):
            # Check the grid edges
            for grid_line in grid_lines:
                if [line1, grid_line] in checked:
                    continue
                ins = get_intersection(line1, grid_line)
                if ins is not None and ins not in intersections:
                    intersections.append(ins)
                checked.append([line1, grid_line])
            # Check other signal areas
            for sig2, _, _, corners2 in dat:
                if sig1 == sig2:
                    continue
                for line2 in get_lines(corners2):
                    if [line1, line2] in checked:
                        continue
                    ins = get_intersection(line1, line2)
                    if ins is not None and ins not in intersections and in_grid(ins):
                        intersections.append(ins)
                    checked.append([line1, line2])
    return intersections


def find_unique(points):
    for pt in points:
        pts = [
            pt,
            [pt[0], pt[1]-1],  # up
            [pt[0], pt[1]+1],  # down
            [pt[0]-1, pt[1]],  # left
            [pt[0]+1, pt[1]],  # right

            [pt[0]+1, pt[1]-1],  # up/right
            [pt[0]-1, pt[1]-1],  # up/left
            [pt[0]+1, pt[1]+1],  # down/right
            [pt[0]-1, pt[1]+1],  # down/left
        ]
        for p in pts:
            # if in_grid(p):
            overlaps = False
            for sig, _, dis, _ in data:
                if distance(sig, p) > dis:
                    overlaps = True
                    break
            if not overlaps:
                return p


ints = get_intersections(data)
ints.extend(grid_corners)
print(len(ints))
res = find_unique(ints)
print(res)
freq = (res[0] * 4000000) + res[1]
print(freq)



# P2 involved moving from given coordinates to t = x+y, u = x-y to turn rhombi
# into squares, then noting that since there's exactly one solution, it has to
# be one out of at least 2 sensors range. From there it was identifying t's and
# u's where that happens, and then iterating through the few points that had it
# until only one satisfied all conditions.

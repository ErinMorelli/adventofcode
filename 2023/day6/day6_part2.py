#!/usr/bin/env python
"""
--- Part Two ---

As the race is about to start, you realize the piece of paper with race times
and record distances you got earlier actually just has very bad
[kerning](https://en.wikipedia.org/wiki/Kerning). There's really only one race
\- ignore the spaces between the numbers on each line.

So, the example from before:

    Time:      7  15   30
    Distance:  9  40  200

...now instead means this:

    Time:      71530
    Distance:  940200

Now, you have to figure out how many ways there are to win this single race.
In this example, the race lasts for `71530` milliseconds and the record
distance you need to beat is `940200` millimeters. You could hold the button
anywhere from `14` to `71516` milliseconds and beat the record, a total of
`71503` ways!

How many ways can you beat the record in this one much longer race?
"""
from re import split
from math import sqrt, pow, floor

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

[raw_time, raw_distance] = raw_data

race_time = int(''.join(split(r'\s+', raw_time)[1:]))
race_dist = int(''.join(split(r'\s+', raw_distance)[1:]))

# race time = A, race record = B, pressed = C, traveled = D
# D = (A - C) * C
# C = 1/2 (A - sqrt(A^2 - 4 D))
record_press = floor((race_time - sqrt(pow(race_time, 2) - (4 * race_dist))) / 2)

win_count = len(range(record_press + 1, race_time - record_press))
print(win_count)

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
from math import prod

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

data = sorted([int(i) for i in raw_data])

jolt_diff = 3
highest_rating = data[-1]
device_rating = highest_rating + jolt_diff

data = [0] + data
data.append(device_rating)


def calc_run(run):
    run_length = len(run)
    paths = 1
    for i in range(1, run_length+1):
        paths += run_length - i
    return paths


diffs = [data[i+1] - data[i] for i in range(len(data)-1)]
string_diffs = ''.join([str(i) for i in diffs])
runs = string_diffs.split('3')

result = prod([calc_run(r) for r in runs])
print(f'arrangements: {result}')

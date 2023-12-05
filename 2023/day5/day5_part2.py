#!/usr/bin/env python
"""
--- Part Two ---

Everyone will starve if you only plant such a small number of seeds. Re-
reading the almanac, it looks like the `seeds:` line actually describes ranges
of seed numbers.

The values on the initial `seeds:` line come in pairs. Within each pair, the
first value is the start of the range and the second value is the length of
the range. So, in the first line of the example above:

    seeds: 79 14 55 13

This line describes two ranges of seed numbers to be planted in the garden.
The first range starts with seed number `79` and contains `14` values: `79`,
`80`, ..., `91`, `92`. The second range starts with seed number `55` and
contains `13` values: `55`, `56`, ..., `66`, `67`.

Now, rather than considering four seed numbers, you need to consider a total
of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed
number `82`, which corresponds to soil `84`, fertilizer `84`, water `84`,
light `77`, temperature `45`, humidity `46`, and location `46`. So, the lowest
location number is `46`.

Consider all of the initial seed numbers listed in the ranges on the first
line of the almanac. What is the lowest location number that corresponds to
any of the initial seed numbers?
"""
input_file = 'input.txt'
# input_file = 'sample.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().split('\n\n')

all_seeds = [int(s) for s in raw_data[0].strip().split(':')[1].strip().split(' ')]
seed_pairs = [all_seeds[i:i+2] for i in range(0, len(all_seeds), 2)]
min_location = None


def get_location(seed):
    next_value = seed
    for m in raw_data[1:]:
        for entry in m.strip().split('\n')[1:]:
            raw_ranges = [int(e.strip()) for e in entry.strip().split(' ')]
            length = raw_ranges[2]

            if raw_ranges[1] <= next_value < raw_ranges[1] + length:
                diff = next_value - raw_ranges[1]
                next_value = raw_ranges[0] + diff
                break
    return next_value


for start, length in seed_pairs:
    end = start + length
    for seed in range(start, end+1):
        loc = get_location(seed)
        if min_location is None or loc < min_location:
            min_location = loc

print(min_location)

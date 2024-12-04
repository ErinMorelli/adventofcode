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

with open(input_file, 'r') as fh:
    raw_data = fh.read().split('\n\n')

all_seeds = [int(s) for s in raw_data[0].strip().split(':')[1].strip().split(' ')]
seed_pairs = [all_seeds[i:i+2] for i in range(0, len(all_seeds), 2)]


def do_conversion(maps, start, length):
    end = start + length - 1
    new_ranges = []

    for entry in maps.strip().split('\n')[1:]:
        raw_ranges = [int(e.strip()) for e in entry.strip().split(' ')]

        [dest_start, source_start, range_length] = raw_ranges
        source_end = source_start + range_length - 1

        new_start = dest_start + (start - source_start)

        # Full og range in source range
        #    |----|
        # |----------|
        if (
                (source_start <= start <= source_end) and
                (source_start <= end <= source_end)
        ):
            new_ranges.append((new_start, length))
            break

        # Part of og range overlaps with the end of source range
        #         |------|
        # |----------|
        elif (
                (source_start <= start <= source_end) and
                (source_end < end)
        ):
            new_length = source_end - start + 1
            new_ranges.append((new_start, new_length))
            if new_length != length:
                new_ranges.extend(do_conversion(maps, source_end + 1, length - new_length))
            break

        # Part of og range overlaps with the start of source range
        # |--------|
        #       |----------|
        elif (
                (source_start > start) and
                (source_start <= end <= source_end)
        ):
            new_length = end - source_start + 1
            new_ranges.append((dest_start, new_length))
            if new_length != length:
                new_ranges.extend(do_conversion(maps, start, length - new_length))
            break

        # No part of og range overlaps with the source range
        #                  |------|
        # |---------|

    return [(start, length)] if not new_ranges else new_ranges


final_ranges = []

for og_start, og_length in seed_pairs:
    ranges = [(og_start, og_length)]

    for m in raw_data[1:]:
        new_ranges = []
        for range_start, range_length in ranges:
            new_ranges.extend(do_conversion(m, range_start, range_length))
        ranges = new_ranges

    final_ranges.extend(ranges)


lowest = None

for (s, _) in final_ranges:
    if lowest is None or s < lowest:
        lowest = s

print(lowest)

#!/usr/bin/env python
"""
--- Part Two ---

It seems like there is still quite a bit of duplicate work planned. Instead,
the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (`2-4,6-8` and `2-3,4-5`) don't
overlap, while the remaining four pairs (`5-7,7-9`, `2-8,3-7`, `6-6,4-6`, and
`2-6,4-8`) do overlap:

  * `5-7,7-9` overlaps in a single section, `7`.
  * `2-8,3-7` overlaps all of the sections `3` through `7`.
  * `6-6,4-6` overlaps in a single section, `6`.
  * `2-6,4-8` overlaps in sections `4`, `5`, and `6`.

So, in this example, the number of overlapping assignment pairs is `4`.

In how many assignment pairs do the ranges overlap?
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().strip().splitlines()

data = [[y.split('-') for y in x.split(',')] for x in raw_data]
count = 0

for (elf1, elf2) in data:
    range1 = set(range(int(elf1[0]), int(elf1[1]) + 1))
    range2 = set(range(int(elf2[0]), int(elf2[1]) + 1))
    if range1.intersection(range2) or range2.intersection(range1):
        count += 1

print(count)

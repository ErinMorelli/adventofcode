#!/usr/bin/env python
"""
--- Part Two ---

The Historians sure are taking a long time. To be fair, the infinite corridors
are very large.

How many stones would you have after blinking a total of 75 times?
"""
from collections import defaultdict
from functools import cache

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().strip()

data = defaultdict(lambda: 0)
for x in raw_data.split(' '):
    data[int(x)] += 1


@cache
def evolve(stone):
    if stone == 0:
        return [1]

    str_stone = str(stone)
    if len(str_stone) % 2 == 0:
        mid = len(str_stone) // 2
        left = int(str_stone[:mid])
        right = int(str_stone[mid:])
        return [left, right]

    return [stone * 2024]


stones = data.copy()

for blink in range(75):
    new_stones = defaultdict(lambda : 0)

    for item, count in stones.items():
        for res in evolve(item):
            new_stones[res] += count

    stones = new_stones

print(sum(stones.values()))

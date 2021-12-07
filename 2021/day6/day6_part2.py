#!/usr/bin/env python
"""
--- Part Two ---

Suppose the lanternfish live forever and have unlimited food and space. Would
they take over the entire ocean?

After 256 days in the example above, there would be a total of `26984457539`
lanternfish!

How many lanternfish would there be after 256 days?
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

data = [int(x, 10) for x in raw_data[0].split(',')]
ages = 9
tracker = [0] * ages
days = 256

for num in data:
    tracker[num] += 1

for day in range(days):
    new_tracker = [0] * ages

    for age in reversed(range(1, ages)):
        new_tracker[age - 1] = tracker[age]

    new_tracker[8] = tracker[0]
    new_tracker[6] += tracker[0]

    tracker = new_tracker

result = sum(tracker)

print(f'Result: {result}')

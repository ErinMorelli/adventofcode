#!/usr/bin/env python
"""
--- Part Two ---

Upon completion, two things immediately become clear. First, the disk
definitely has a lot more contiguous free space, just like the amphipod hoped.
Second, the computer is running much more slowly! Maybe introducing all of
that file system fragmentation was a bad idea?

The eager amphipod already has a new plan: rather than move individual blocks,
he'd like to try compacting the files on his disk by moving whole files
instead.

This time, attempt to move whole files to the leftmost span of free space
blocks that could fit the file. Attempt to move each file exactly once in
order of decreasing file ID number starting with the file with the highest
file ID number. If there is no span of free space to the left of a file that
is large enough to fit the file, the file does not move.

The first example from above now proceeds differently:

    00...111...2...333.44.5555.6666.777.888899
    0099.111...2...333.44.5555.6666.777.8888..
    0099.1117772...333.44.5555.6666.....8888..
    0099.111777244.333....5555.6666.....8888..
    00992111777.44.333....5555.6666.....8888..

The process of updating the filesystem checksum is the same; now, this
example's checksum would be `2858`.

Start over, now compacting the amphipod's hard drive using this new method
instead. What is the resulting filesystem checksum?
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read()

data = list(raw_data)

free = '.'
disk_map = list()
block_id = 0

for i, block in enumerate(data):
    for j in range(int(block)):
        item = free if i % 2 == 1 else str(block_id)
        disk_map.append(item)

    if i % 2 == 0:
        block_id += 1

new_map = disk_map.copy()

group = []
char = None

for idx in reversed(range(len(disk_map))):
    block = new_map[idx]

    if block == free:
        continue

    if char is None:
        char = block

    group.append(block)

    if idx - 1 < 0 or new_map[idx - 1] != char:
        size = len(group)
        space = 0
        start = 0

        for i in range(idx + 1):
            if new_map[i] == free:
                if space == 0:
                    start = i
                space += 1
            else:
                space = 0

            if space >= size:
                for ii in range(start, i + 1):
                    new_map[ii] = char

                for fi in range(idx, idx + size):
                    new_map[fi] = free

                break

        group = []
        char = None
        continue

checksum = 0

for i, block in enumerate(new_map):
    if block == free:
        continue

    checksum += i * int(block)

print(checksum)

#!/usr/bin/env python
"""
A version 2 decoder chip doesn't modify the values being written at all.
Instead, it acts as a [memory address
decoder](https://www.youtube.com/watch?v=PvfhANgLrm4). Immediately before a
value is written to memory, each bit in the bitmask modifies the corresponding
bit of the destination memory address in the following way:

  * If the bitmask bit is `0`, the corresponding memory address bit is
    unchanged.
  * If the bitmask bit is `1`, the corresponding memory address bit is
    overwritten with `1`.
  * If the bitmask bit is `X`, the corresponding memory address bit is
    floating.

A floating bit is not connected to anything and instead fluctuates
unpredictably. In practice, this means the floating bits will take on all
possible values, potentially causing many memory addresses to be written all
at once!

For example, consider the following program:

    mask = 000000000000000000000000000000X1001X
    mem[42] = 100
    mask = 00000000000000000000000000000000X0XX
    mem[26] = 1

When this program goes to write to memory address `42`, it first applies the
bitmask:

    address: 000000000000000000000000000000101010  (decimal 42)
    mask:    000000000000000000000000000000X1001X
    result:  000000000000000000000000000000X1101X

After applying the mask, four bits are overwritten, three of which are
different, and two of which are floating. Floating bits take on every possible
combination of values; with two floating bits, four actual memory addresses
are written:

    000000000000000000000000000000011010  (decimal 26)
    000000000000000000000000000000011011  (decimal 27)
    000000000000000000000000000000111010  (decimal 58)
    000000000000000000000000000000111011  (decimal 59)


Next, the program is about to write to memory address `26` with a different
bitmask:

    address: 000000000000000000000000000000011010  (decimal 26)
    mask:    00000000000000000000000000000000X0XX
    result:  00000000000000000000000000000001X0XX

This results in an address with three floating bits, causing writes to eight
memory addresses:

    000000000000000000000000000000010000  (decimal 16)
    000000000000000000000000000000010001  (decimal 17)
    000000000000000000000000000000010010  (decimal 18)
    000000000000000000000000000000010011  (decimal 19)
    000000000000000000000000000000011000  (decimal 24)
    000000000000000000000000000000011001  (decimal 25)
    000000000000000000000000000000011010  (decimal 26)
    000000000000000000000000000000011011  (decimal 27)

The entire 36-bit address space still begins initialized to the value 0 at
every address, and you still need the sum of all values left in memory at the
end of the program. In this example, the sum is `208`.

Execute the initialization program using an emulator for a version 2 decoder
chip. What is the sum of all values left in memory after it completes?
"""
import re
from itertools import permutations

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    data = fh.read().splitlines()


def get_bitmask(n):
    x = bin(n).split('b')[-1]
    return '0'*(36-len(x)) + x


def apply_mask(m, n):
    mx = list(m)
    nx = list(n)
    for i, x in enumerate(mx):
        if x == '0':
            continue
        nx[i] = x
    return ''.join(nx)


def get_permutations(exes):
    x_count = len(exes)
    p = '0' * x_count
    perms = set()
    perms.add(tuple(p))
    for i in range(x_count):
        p = list(p)
        p[i] = '1'
        p = ''.join(p)
        ps = set(permutations(p))
        perms.update(ps)
    return perms


def get_addresses(n):
    addresses = []
    n = list(n)

    exes = [i for i, x in enumerate(n) if x == 'X']
    perms = get_permutations(exes)

    for perm in perms:
        nx = n.copy()
        for i, x in enumerate(exes):
            nx[x] = perm[i]

        applied = ''.join(nx)
        reduced = re.sub(r'^[0]+', '', applied)
        address = int(reduced, 2)
        addresses.append(address)

    return addresses


memory = dict()
mask = None
running_sum = 0

for line in data:
    if line.startswith('mask'):
        mask = line.split('=')[-1].strip()
        continue

    parsed = re.match(r'mem\[(\d+)] = (\d+)', line)
    address = int(parsed.group(1), 10)
    value = int(parsed.group(2), 10)

    bitmask = get_bitmask(address)
    applied = apply_mask(mask, bitmask)
    addresses = get_addresses(applied)

    for a in addresses:
        if a in memory.keys():
            running_sum -= memory[a]
        memory[a] = value
        running_sum += value

print(f'sum = {running_sum}')

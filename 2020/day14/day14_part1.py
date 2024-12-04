#!/usr/bin/env python
"""
The initialization program (your puzzle input) can either update the bitmask
or write a value to memory. Values and memory addresses are both 36-bit
unsigned integers. For example, ignoring bitmasks for a moment, a line like
`mem[8] = 11` would write the value `11` to memory address `8`.

The bitmask is always given as a string of 36 bits, written with the most
significant bit (representing `2^35`) on the left and the least significant
bit (`2^0`, that is, the `1`s bit) on the right. The current bitmask is
applied to values immediately before they are written to memory: a `0` or `1`
overwrites the corresponding bit in the value, while an `X` leaves the bit in
the value unchanged.

For example, consider the following program:

    mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
    mem[8] = 11
    mem[7] = 101
    mem[8] = 0

This program starts by specifying a bitmask (`mask = ....`). The mask it
specifies will overwrite two bits in every written value: the `2`s bit is
overwritten with `0`, and the `64`s bit is overwritten with `1`.

The program then attempts to write the value `11` to memory address `8`. By
expanding everything out to individual bits, the mask is applied as follows:

    value:  000000000000000000000000000000001011  (decimal 11)
    mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
    result: 000000000000000000000000000001001001  (decimal 73)

So, because of the mask, the value `73` is written to memory address `8`
instead. Then, the program tries to write `101` to address `7`:

    value:  000000000000000000000000000001100101  (decimal 101)
    mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
    result: 000000000000000000000000000001100101  (decimal 101)

This time, the mask has no effect, as the bits it overwrote were already the
values the mask tried to set. Finally, the program tries to write `0` to
address `8`:

    value:  000000000000000000000000000000000000  (decimal 0)
    mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
    result: 000000000000000000000000000001000000  (decimal 64)

`64` is written to address `8` instead, overwriting the value that was there
previously.

To initialize your ferry's docking program, you need the sum of all values
left in memory after the initialization program completes. (The entire 36-bit
address space begins initialized to the value `0` at every address.) In the
above example, only two values in memory are not zero - `101` (at address `7`)
and `64` (at address `8`) - producing a sum of `165`.

Execute the initialization program. What is the sum of all values left in
memory after it completes?
"""
import re

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
        if x == 'X':
            continue
        nx[i] = x
    return ''.join(nx)


memory = dict()
mask = None

for line in data:
    if line.startswith('mask'):
        mask = line.split('=')[-1].strip()
        continue

    parsed = re.match(r'mem\[(\d+)] = (\d+)', line)
    address = int(parsed.group(1), 10)
    value = int(parsed.group(2), 10)

    bitmask = get_bitmask(value)
    applied = apply_mask(mask, bitmask)

    reduced = re.sub(r'^[0]+', '', applied)
    new_value = int(reduced, 2)

    memory[address] = new_value


value_sum = sum(memory.values())
print(f'sum = {value_sum}')

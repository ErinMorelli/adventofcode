#!/usr/bin/env python
"""
--- Part Two ---

The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this
isn't actually an `XMAS` puzzle; it's an `X-MAS` puzzle in which you're
supposed to find two `MAS` in the shape of an `X`. One way to achieve that is
like this:

    M.S
    .A.
    M.S

Irrelevant characters have again been replaced with `.` in the above diagram.
Within the `X`, each `MAS` can be written forwards or backwards.

Here's the same example from before, but this time all of the `X-MAS`es have
been kept instead:

    .M.S......
    ..A..MSMS.
    .M.S.MAA..
    ..A.ASMSM.
    .M.S.M....
    ..........
    S.S.S.S.S.
    .A.A.A.A..
    M.M.M.M.M.
    ..........

In this example, an `X-MAS` appears `9` times.

Flip the word search from the instructions back over to the word search side
and try again. How many times does an`X-MAS` appear?
"""
import re

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

data = [list(x) for x in raw_data]

cols = len(data)
rows = len(data[0])

count = 0

for y in range(1, cols - 1):
    for i in re.finditer(r'A', raw_data[y]):
        x = i.start()

        if 0 < x < rows - 1:
            """
            a1           b1
            (-y, -x)     (-y, +x)
                    X . X
                    . X .
                    X . X
            (+y, -x)     (+y, +x)
            b2           a2
            """

            a1 = data[y-1][x-1]
            a2 = data[y+1][x+1]
            aok = (a1 == 'M' and a2 == 'S') or (a1 == 'S' and a2 == 'M')

            b1 = data[y-1][x+1]
            b2 = data[y+1][x-1]
            bok = (b1 == 'M' and b2 == 'S') or (b1 == 'S' and b2 == 'M')

            if aok and bok:
                count += 1

print(count)

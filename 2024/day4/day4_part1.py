#!/usr/bin/env python
"""
--- Day 4: Ceres Search ---

"Looks like the Chief's not here. Next!" One of The Historians pulls out a
device and pushes the only button on it. After a brief flash, you recognize
the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station
tugs on your shirt; she'd like to know if you could help her with her word
search (your puzzle input). She only has to find one word: `XMAS`.

This word search allows words to be horizontal, vertical, diagonal, written
backwards, or even overlapping other words. It's a little unusual, though, as
you don't merely need to find one instance of `XMAS` - you need to find all
of them. Here are a few ways `XMAS` might appear, where irrelevant characters
have been replaced with `.`:

    ..X...
    .SAMX.
    .A..A.
    XMAS.S
    .X....

The actual word search will be full of letters instead. For example:

    MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX

In this word search, `XMAS` occurs a total of `18` times; here's the same word
search again, but where letters not involved in any `XMAS` have been replaced
with `.`:

    ....XXMAS.
    .SAMXMS...
    ...S..A...
    ..A.A.MS.X
    XMASAMX.MM
    X.....XA.A
    S.S.S.S.SS
    .A.A.A.A.A
    ..M.M.M.MM
    .X.X.XMASX

Take a look at the little Elf's word search. How many times does`XMAS` appear?
"""
import re

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

data = [list(x) for x in raw_data]

cols = len(data)
rows = len(data[0])

regex = r'(?=(XMAS|SAMX))'
count = 0

# Vertical
for x in range(rows):
    col = ''.join([y[x] for y in data])
    v = re.findall(regex, col)
    count += len(v)

 # Horizontal
for y, row in enumerate(raw_data):
    h = re.findall(regex, row)
    count += len(h)

# Diagonal 1
for x in range(rows):
    y = 0
    diag = []

    while x < rows and y < cols:
        diag.append(data[y][x])
        x += 1
        y += 1

    d = re.findall(regex, ''.join(diag))
    count += len(d)

    if len(diag) <= 4:
        break

# Diagonal 2
for y in range(1, cols):
    x = 0
    diag = []

    while x < rows and y < cols:
        diag.append(data[y][x])
        x += 1
        y += 1

    d = re.findall(regex, ''.join(diag))
    count += len(d)

    if len(diag) <= 4:
        break

# Diagonal 3
for x in reversed(range(rows)):
    y = 0
    diag = []

    while x >= 0 and y < cols:
        diag.append(data[y][x])
        x -= 1
        y += 1

    d = re.findall(regex, ''.join(diag))
    count += len(d)

    if len(diag) <= 4:
        break

# Diagonal 4
for y in range(1, cols):
    x = rows - 1
    diag = []

    while x >= 0 and y < cols:
        diag.append(data[y][x])
        x -= 1
        y += 1

    d = re.findall(regex, ''.join(diag))
    count += len(d)

    if len(diag) <= 4:
        break

print(count)

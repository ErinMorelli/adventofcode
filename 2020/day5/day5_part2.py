#!/usr/bin/env python
"""
It's a completely full flight, so your seat should be the only missing
boarding pass in your list. However, there's a catch: some of the seats at
the very front and back of the plane don't exist on this aircraft, so they'll
be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1
and -1 from yours will be in your list.

What is the ID of your seat?
"""
input_file = 'input.txt'
row_range = [x for x in range(128)]
seat_range = [x for x in range(8)]
seat_ids = []


def calc_val(range_, code, upper):
    val = code[0]
    mid = int(len(range_)/2)
    new_range = range_[mid:] if val == upper else range_[:mid]
    if len(new_range) == 1:
        return new_range[0]
    return calc_val(new_range, code[1:], upper)


with open(input_file, 'r') as fh:
    for _line in fh:
        line = _line.strip()
        row_code = line[:-3]
        seat_code = line[-3:]

        row = calc_val(row_range, row_code, 'B')
        seat = calc_val(seat_range, seat_code, 'R')

        seat_id = (row * 8) + seat
        seat_ids.append(seat_id)

seat_ids = sorted(seat_ids)

for idx, sid in enumerate(seat_ids):
    if idx == 0:
        continue

    if sid+1 != seat_ids[idx+1]:
        print(f'seat ID: {sid + 1}')
        break

#!/usr/bin/env python
"""
Now that you've identified which tickets contain invalid values, discard those
tickets entirely. Use the remaining valid tickets to determine which field is
which.

Using the valid ranges for each field, determine what order the fields appear
on the tickets. The order is consistent between all tickets: if `seat` is the
third field, it is the third field on every ticket, including your ticket.

For example, suppose you have the following notes:

    class: 0-1 or 4-19
    row: 0-5 or 8-19
    seat: 0-13 or 16-19

    your ticket:
    11,12,13

    nearby tickets:
    3,9,18
    15,1,5
    5,14,9

Based on the nearby tickets in the above example, the first position must be
`row`, the second position must be `class`, and the third position must be
`seat`; you can conclude that in your ticket, `class` is `12`, `row` is `11`,
and `seat` is `13`.

Once you work out which field is which, look for the six fields on your ticket
that start with the word `departure`. What do you get if you multiply those
six values together?
"""
import re
from math import prod

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().strip()

data = raw_data.split('your ticket:\n')
data2 = data[1].split('nearby tickets:\n')

fields = {}
raw_fields = data[0].strip().split('\n')
field_regex = r'(?P<fname>.+): (?P<rangeA1>\d+)-(?P<rangeA2>\d+) or ' \
              r'(?P<rangeB1>\d+)-(?P<rangeB2>\d+)'

for f in raw_fields:
    match = re.match(field_regex, f)
    fname = match.group('fname')
    fields[fname] = [
        [int(match.group('rangeA1')), int(match.group('rangeA2'))],
        [int(match.group('rangeB1')), int(match.group('rangeB2'))]
    ]

raw_ticket = data2[0].strip().split(',')
your_ticket = [int(i) for i in raw_ticket]

raw_nearby_tickets = data2[1].strip().split('\n')
nearby_tickets = [[int(i) for i in t.split(',')] for t in raw_nearby_tickets]


def validate_field(val, ranges):
    range1 = range(ranges[0][0], ranges[0][1] + 1)
    range2 = range(ranges[1][0], ranges[1][1] + 1)

    return val in range1 or value in range2


valid_tickets = [your_ticket]

for ticket in nearby_tickets:
    valid = True
    for value in ticket:
        match = False
        for field in fields.values():
            if validate_field(value, field):
                match = True
                break
        if not match:
            valid = False
            break
    if valid:
        valid_tickets.append(ticket)


possible_fields = [{f: True for f in fields.keys()}
                   for _ in range(len(your_ticket))]

for ticket in valid_tickets:
    for idx, value in enumerate(ticket):
        for fname, fvalues in fields.items():
            if not possible_fields[idx][fname]:
                continue
            if not validate_field(value, fvalues):
                possible_fields[idx][fname] = False


possible_fields_by_index = [set() for _ in range(len(your_ticket))]

for idx, pf in enumerate(possible_fields):
    for fname, valid in pf.items():
        if valid:
            possible_fields_by_index[idx].add(fname)

matched_fields_by_index = {f: None for f in fields.keys()}


def match_fields(to_match, matched):
    for i, pf in enumerate(to_match):
        if not len(pf):
            continue

        field_name = list(pf)[0]

        if len(pf) == 1 and matched[field_name] is None:
            matched[field_name] = i

            for j, pf2 in enumerate(to_match):
                if i == j:
                    to_match[j] = []
                    
                if field_name in pf2:
                    to_match[j] = [p for p in pf2 if p != field_name]
            break

    if None in matched.values():
        return match_fields(to_match, matched)

    return matched


fields_by_index = match_fields(possible_fields_by_index,
                               matched_fields_by_index)

ticket_values = {}

for field, idx in fields_by_index.items():
    if field.startswith('departure'):
        ticket_values[field] = your_ticket[idx]

print(f'product: {prod(ticket_values.values())}')

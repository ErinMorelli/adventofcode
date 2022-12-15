#!/usr/bin/env python
"""
--- Part Two ---

The resulting polymer isn't nearly strong enough to reinforce the submarine.
You'll need to run more steps of the pair insertion process; a total of 40
steps should do it.

In the above example, the most common element is `B` (occurring
`2192039569602` times) and the least common element is `H` (occurring
`3849876073` times); subtracting these produces `2188189693529`.

Apply 40 steps of pair insertion to the polymer template and find the most and
least common elements in the result. What do you get if you take the quantity
of the most common element and subtract the quantity of the least common
element?
"""
from collections import defaultdict

# input_file = 'input.txt'
input_file = 'sample.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().split('\n\n')

template = raw_data[0]

rules = {}
for row in raw_data[1].splitlines():
    parts = row.split(' -> ')
    rules[parts[0]] = parts[1]

letters = list(set(rules.values()))


def step(poly):
    new_poly = ''
    for idx in range(len(poly)-1):
        pair = poly[idx] + poly[idx+1]
        ins = rules[pair]
        new_poly += poly[idx] + ins
        if idx+1 == len(poly)-1:
            new_poly += poly[idx+1]
    return new_poly


counts = defaultdict(lambda: 0)


for i in range(len(template)-1):
    p = template[i] + template[i+1]
    for _ in range(10):
        p = step(p)
    for letter in letters:
        counts[letter] += p.count(letter)

print(counts)

bg_count, bg_letter = 0, None
sm_count, sm_letter = 0, None

for letter, count in counts.items():
    if bg_count == 0 or count > bg_count:
        bg_count = count
        bg_letter = letter

    if sm_count == 0 or count < sm_count:
        sm_count = count
        sm_letter = letter

print('big', bg_letter, bg_count)
print('small', sm_letter, sm_count)

print(bg_count - sm_count)

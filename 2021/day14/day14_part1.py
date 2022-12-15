#!/usr/bin/env python
"""
--- Day 14: Extended Polymerization ---

The incredible pressures at this depth are starting to put a strain on your
submarine. The submarine has
[polymerization](https://en.wikipedia.org/wiki/Polymerization) equipment that
would produce suitable materials to reinforce the submarine, and the nearby
volcanically-active caves should even have the necessary input elements in
sufficient quantities.

The submarine manual contains instructions for finding the optimal polymer
formula; specifically, it offers a polymer template and a list of pair
insertion rules (your puzzle input). You just need to work out what polymer
would result after repeating the pair insertion process a few times.

For example:

    NNCB

    CH -> B
    HH -> N
    CB -> H
    NH -> C
    HB -> C
    HC -> B
    HN -> C
    NN -> C
    BH -> H
    NC -> B
    NB -> B
    BN -> B
    BB -> N
    BC -> B
    CC -> N
    CN -> C

The first line is the polymer template \- this is the starting point of the
process.

The following section defines the pair insertion rules. A rule like `AB -> C`
means that when elements `A` and `B` are immediately adjacent, element `C`
should be inserted between them. These insertions all happen simultaneously.

So, starting with the polymer template `NNCB`, the first step simultaneously
considers all three pairs:

  * The first pair (`NN`) matches the rule `NN -> C`, so element `C` is
    inserted between the first `N` and the second `N`.
  * The second pair (`NC`) matches the rule `NC -> B`, so element `B` is
    inserted between the `N` and the `C`.
  * The third pair (`CB`) matches the rule `CB -> H`, so element `H` is
    inserted between the `C` and the `B`.

Note that these pairs overlap: the second element of one pair is the first
element of the next pair. Also, because all pairs are considered
simultaneously, inserted elements are not considered to be part of a pair
until the next step.

After the first step of this process, the polymer becomes `NCNBCHB`.

Here are the results of a few steps using the above rules:

    Template:     NNCB
    After step 1: NCNBCHB
    After step 2: NBCCNBBBCBHCB
    After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
    After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB

This polymer grows quickly. After step 5, it has length 97; After step 10, it
has length 3073. After step 10, `B` occurs 1749 times, `C` occurs 298 times,
`H` occurs 161 times, and `N` occurs 865 times; taking the quantity of the
most common element (`B`, 1749) and subtracting the quantity of the least
common element (`H`, 161) produces `1749 - 161 = 1588`.

Apply 10 steps of pair insertion to the polymer template and find the most and
least common elements in the result. What do you get if you take the quantity
of the most common element and subtract the quantity of the least common
element?
"""
from collections import defaultdict

input_file = 'input.txt'

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

bg_count, bg_letter = 0, None
sm_count, sm_letter = 0, None

for letter, count in counts.items():
    if bg_count == 0 or count > bg_count:
        bg_count = count
        bg_letter = letter

    if sm_count == 0 or count < sm_count:
        sm_count = count
        sm_letter = letter

print(bg_count - sm_count)

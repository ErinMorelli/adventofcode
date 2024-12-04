#!/usr/bin/env python
"""
--- Part Two ---

Through a little deduction, you should now be able to determine the remaining
digits. Consider again the first example above:

    acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
    cdfeb fcadb cdfeb cdbaf

After some careful analysis, the mapping between signal wires and segments
only make sense in the following configuration:

     dddd
    e    a
    e    a
     ffff
    g    b
    g    b
     cccc

So, the unique signal patterns would correspond to the following digits:

  * `acedgfb`: `8`
  * `cdfbe`: `5`
  * `gcdfa`: `2`
  * `fbcad`: `3`
  * `dab`: `7`
  * `cefabd`: `9`
  * `cdfgeb`: `6`
  * `eafb`: `4`
  * `cagedb`: `0`
  * `ab`: `1`

Then, the four digits of the output value can be decoded:

  * `cdfeb`: `5`
  * `fcadb`: `3`
  * `cdfeb`: `5`
  * `cdbaf`: `3`

Therefore, the output value for this entry is `5353`.

Following this same process for each entry in the second, larger example
above, the output value of each entry can be determined:

  * `fdgacbe cefdb cefbgd gcbe`: `8394`
  * `fcgedb cgb dgebacf gc`: `9781`
  * `cg cg fdcagb cbg`: `1197`
  * `efabcd cedba gadfec cb`: `9361`
  * `gecf egdcabf bgf bfgea`: `4873`
  * `gebdcfa ecba ca fadegcb`: `8418`
  * `cefg dcbef fcge gbcadfe`: `4548`
  * `ed bcgafe cdgba cbgef`: `1625`
  * `gbdfcae bgc cg cgb`: `8717`
  * `fgae cfgab fg bagce`: `4315`

Adding all of the output values in this larger example produces `61229`.

For each entry, determine all of the wire/segment connections and decode the
four-digit output values. What do you get if you add up all of the output
values?
"""
from collections import defaultdict

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

results = []

lens = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8],
}

for line in raw_data:
    parts = line.split(' | ')
    patterns = parts[0].split(' ')
    digits = parts[1].split(' ')

    known = {}
    unknown = defaultdict(list)

    for p in patterns:
        l = len(p)
        if len(lens[l]) == 1:
            known[lens[l][0]] = set(p)
        else:
            for i in lens[l]:
                unknown[i].append(set(p))

    for x in unknown[6]:
        if not known[1].issubset(x) and x not in known.values():
            known[6] = x
            del unknown[6]
            break

    for x in unknown[5]:
        if x.issubset(known[6]) and x not in known.values():
            known[5] = x
            del unknown[5]
            break

    for x in unknown[9]:
        if known[5].issubset(x) and x not in known.values():
            known[9] = x
            del unknown[9]
            break

    for x in unknown[0]:
        if x != known[6] and x != known[9] and x not in known.values():
            known[0] = x
            del unknown[0]
            break

    for x in unknown[3]:
        if x != known[5] and known[7].issubset(x) and x not in known.values():
            known[3] = x
            del unknown[3]
            break

    for x in unknown[2]:
        if x != known[5] and x != known[3] and x not in known.values():
            known[2] = x
            del unknown[2]
            break

    result = ''

    for d in digits:
        digit = set(d)
        for num, val in known.items():
            if digit == val:
                result += str(num)

    results.append(int(result))

answer = sum(results)

print(f'Result: {answer}')

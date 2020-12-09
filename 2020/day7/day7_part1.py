#!/usr/bin/env python
"""
Due to recent aviation regulations, many rules (your puzzle input) are being
enforced about bags and their contents; bags must be color-coded and must
contain specific quantities of other color-coded bags. Apparently, nobody
responsible for these regulations considered how long they would take
to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

These rules specify the required contents for 9 bag types. In this example,
every faded blue bag is empty, every vibrant plum bag contains 11 bags (5
faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other
bag, how many different bag colors would be valid for the outermost bag?
(In other words: how many colors can, eventually, contain at least one shiny
gold bag?)

In the above rules, the following options would be available to you:

    A bright white bag, which can hold your shiny gold bag directly.
    A muted yellow bag, which can hold your shiny gold bag directly, plus some
        other bags.
    A dark orange bag, which can hold bright white and muted yellow bags,
        either of which could then hold your shiny gold bag.
    A light red bag, which can hold bright white and muted yellow bags,
        either of which could then hold your shiny gold bag.

So, in this example, the number of bag colors that can eventually contain
at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag?
(The list of rules is quite long; make sure you get all of it.)
"""
import re

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read()

rules = raw_data.strip().split('\n')
bags = {}

for rule in rules:
    parsed = re.match(r'^(.+) bag[s]? contain (.+)$', rule, re.M)
    if not parsed:
        continue

    color = parsed.group(1)
    contains = parsed.group(2).split(', ')
    contents = {}

    for c in contains:
        b = re.match(r'(\d+) (.+) bag[s]?', c)
        if not b:
            continue

        contents[b.group(2)] = int(b.group(1), 10)

    bags[color] = contents


def count_bags(search, total, found):
    tally = []
    for base in search:
        for color, contents in bags.items():
            if color in found:
                continue
            if base in contents.keys() and contents[base] > 0:
                tally.append(color)
                found.add(color)
    if len(tally) == 0:
        return total
    total += len(tally)
    return count_bags(tally, total, found)


result = count_bags(['shiny gold'], 0, set())

print(f'total: {result}')

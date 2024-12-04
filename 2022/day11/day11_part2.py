#!/usr/bin/env python
"""
--- Part Two ---

You're worried you might not ever get your items back. So worried, in fact,
that your relief that a monkey's inspection didn't damage an item no longer
causes your worry level to be divided by three.

Unfortunately, that relief was all that was keeping your worry levels from
reaching ridiculous levels. You'll need to find another way to keep your worry
levels manageable.

At this rate, you might be putting up with these monkeys for a very long time
\- possibly `10000` rounds!

With these new rules, you can still figure out the monkey business after 10000
rounds. Using the same example above:

    == After round 1 ==
    Monkey 0 inspected items 2 times.
    Monkey 1 inspected items 4 times.
    Monkey 2 inspected items 3 times.
    Monkey 3 inspected items 6 times.

    == After round 20 ==
    Monkey 0 inspected items 99 times.
    Monkey 1 inspected items 97 times.
    Monkey 2 inspected items 8 times.
    Monkey 3 inspected items 103 times.

    == After round 1000 ==
    Monkey 0 inspected items 5204 times.
    Monkey 1 inspected items 4792 times.
    Monkey 2 inspected items 199 times.
    Monkey 3 inspected items 5192 times.

    == After round 2000 ==
    Monkey 0 inspected items 10419 times.
    Monkey 1 inspected items 9577 times.
    Monkey 2 inspected items 392 times.
    Monkey 3 inspected items 10391 times.

    == After round 3000 ==
    Monkey 0 inspected items 15638 times.
    Monkey 1 inspected items 14358 times.
    Monkey 2 inspected items 587 times.
    Monkey 3 inspected items 15593 times.

    == After round 4000 ==
    Monkey 0 inspected items 20858 times.
    Monkey 1 inspected items 19138 times.
    Monkey 2 inspected items 780 times.
    Monkey 3 inspected items 20797 times.

    == After round 5000 ==
    Monkey 0 inspected items 26075 times.
    Monkey 1 inspected items 23921 times.
    Monkey 2 inspected items 974 times.
    Monkey 3 inspected items 26000 times.

    == After round 6000 ==
    Monkey 0 inspected items 31294 times.
    Monkey 1 inspected items 28702 times.
    Monkey 2 inspected items 1165 times.
    Monkey 3 inspected items 31204 times.

    == After round 7000 ==
    Monkey 0 inspected items 36508 times.
    Monkey 1 inspected items 33488 times.
    Monkey 2 inspected items 1360 times.
    Monkey 3 inspected items 36400 times.

    == After round 8000 ==
    Monkey 0 inspected items 41728 times.
    Monkey 1 inspected items 38268 times.
    Monkey 2 inspected items 1553 times.
    Monkey 3 inspected items 41606 times.

    == After round 9000 ==
    Monkey 0 inspected items 46945 times.
    Monkey 1 inspected items 43051 times.
    Monkey 2 inspected items 1746 times.
    Monkey 3 inspected items 46807 times.

    == After round 10000 ==
    Monkey 0 inspected items 52166 times.
    Monkey 1 inspected items 47830 times.
    Monkey 2 inspected items 1938 times.
    Monkey 3 inspected items 52013 times.

After 10000 rounds, the two most active monkeys inspected items 52166 and
52013 times. Multiplying these together, the level of monkey business in this
situation is now `2713310158`.

Worry levels are no longer divided by three after each item is inspected;
you'll need to find another way to keep your worry levels manageable. Starting
again from the initial state in your puzzle input, what is the level of monkey
business after 10000 rounds?
"""
from math import lcm

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read()

data = raw_data.split('\n\n')


class Monkey:
    inspected = 0

    def __init__(self, notes):
        lines = notes.splitlines()
        # Set ID
        self.id = int(lines[0].split(' ')[-1].split(':')[0])
        # Set initial items
        self.items = [int(x) for x in lines[1].strip().split(':')[-1].strip().split(', ')]
        # Set operation string
        self.operation = lines[2].strip().split(':')[-1].strip().split(' = ')[-1]
        # Set test values
        self.div = int(lines[3].strip().split(' ')[-1])
        self.if_true = int(lines[4].strip().split(' ')[-1])
        self.if_false = int(lines[5].strip().split(' ')[-1])

    def take_turn(self, common_div):
        to_throw = []
        for item in self.items:
            worry = self.inspect_item(item)
            mod = worry % common_div
            monkey_id = self.if_true if (mod % self.div) == 0 else self.if_false
            to_throw.append((monkey_id, mod))
        self.items = []
        return to_throw

    def inspect_item(self, item):
        self.inspected += 1
        op = self.operation.replace('old', str(item))
        return eval(op)

    def catch_item(self, item):
        self.items.append(item)

    def __repr__(self):
        return f'Monkey(ID: {self.id}, inspected: {self.inspected})'


monkeys = []
divs = []

for m in data:
    monkey = Monkey(m)
    divs.append(monkey.div)
    monkeys.append(monkey)

cm = lcm(*divs)

for i in range(10000):
    for monkey in monkeys:
        for mid, new_item in monkey.take_turn(cm):
            monkeys[mid].catch_item(new_item)

monkeys.sort(key=lambda x: x.inspected, reverse=True)
monkey_business = monkeys[0].inspected * monkeys[1].inspected

print(monkey_business)

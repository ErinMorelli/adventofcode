#!/usr/bin/env python
"""
???
"""
import re
import sys
from pprint import pprint

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read()

[raw_rules, raw_messages] = raw_data.split('\n\n')

raw_rules = raw_rules.replace('"', '').split('\n')

known = {}
rules = {}

for i, rule in enumerate(raw_rules):
    rule = rule.split(': ')
    rules[rule[0]] = rule[1]

rules['8'] = '42 | 42 8'
rules['11'] = '42 31 | 42 11 31'

regex = re.compile(r'[a-zA-Z]')
for key, rule in rules.items():
    match = regex.search(rule)
    if match:
        known[key] = match.group(0)
        rules[key] = match.group(0)

known['8'] = '(42)+'

rule_11 = []
for n in range(1, 20):
    rule_11.append(f"(42){{{n}}}(31){{{n}}}")
known['11'] = "(" + ")|(".join([i for i in rule_11]) + ")"

find_nums = re.compile(r'[0-9]')

while len(known) < len(rules):
    new_known = {}

    for rule_regex, rule_string in known.items():
        rule_regex = re.compile(fr"\b{rule_regex}\b")

        for key, rule in rules.items():
            rule = rule_regex.sub(f'(?:{rule_string})', rule)
            rules[key] = rule

            match = find_nums.search(rule)
            if match is None:
                rule = re.sub(r' ', '', rule)
                new_known[key] = rule
                rules[key] = rule

    known = new_known


messages = raw_messages.split('\n')

total = 0
rule_regex = re.compile(rules['0'])

for message in messages:
    match = rule_regex.match(message)
    if match and len(match.group(0)) == len(message):
        total += 1

print(f'matches: {total}')

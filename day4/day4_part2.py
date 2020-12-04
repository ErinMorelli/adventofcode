#!/usr/bin/env python
"""
You can continue to ignore the cid field, but each other field has strict
rules about what values are valid for automatic validation:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

Your job is to count the passports where all required fields are both present
and valid according to the above rules. Here are some example values:

byr valid:   2002
byr invalid: 2003

hgt valid:   60in
hgt valid:   190cm
hgt invalid: 190in
hgt invalid: 190

hcl valid:   #123abc
hcl invalid: #123abz
hcl invalid: 123abc

ecl valid:   brn
ecl invalid: wat

pid valid:   000000001
pid invalid: 0123456789

Count the number of valid passports - those that have all required fields and
valid values. Continue to treat cid as optional. In your batch file,
how many passports are valid?
"""
import re
from pprint import pprint

input_file = 'input.txt'


def validate_height(hgt):
    result = re.match(r'(?P<val>\d+)(?P<unit>cm|in)', hgt)
    if not result:
        return False

    val = int(result.group('val'), 10)
    unit = result.group('unit')

    return 150 <= val <= 193 if unit == 'cm' else 59 <= val <= 76


validation_rules = {
    'byr': lambda x: re.match(r'\d{4}', x) and 1920 <= int(x, 10) <= 2002,
    'iyr': lambda x: re.match(r'\d{4}', x) and 2010 <= int(x, 10) <= 2020,
    'eyr': lambda x: re.match(r'\d{4}', x) and 2020 <= int(x, 10) <= 2030,
    'hgt': validate_height,
    'hcl': lambda x: re.match(r'#[0-9a-f]{6}', x),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: re.match(r'[0-9]{9}', x),
    # 'cid'
}

with open(input_file, 'r') as fh:
    raw_data = fh.read()

passports = re.compile(r'^$', re.M).split(raw_data.strip())
# pprint(passports)


def is_valid(fields):
    broken = {}
    for req, validate in validation_rules.items():
        if req not in fields.keys():
            broken[req] = 'missing'
            continue
            # return False
        if not validate(fields[req]):
            broken[req] = 'invalid'
            continue
            # return False
    return broken


all = []
valid = []

for p in passports:
    entries = re.compile(r' ').split(p.replace('\n', ' '))
    keys = []
    pfields = {}

    for e in entries:
        if e == '':
            continue
        [key, value] = e.split(':')
        pfields[key] = value

    broken = is_valid(pfields)
    all.append(pfields)

    if len(broken) == 0:
        # pprint(pfields)
        # print('\n')
        valid.append(pfields)

summary = {}

for req in validation_rules.keys():
    req_list = []

    for v in all:
        if req in v.keys():
            req_list.append(v[req])
        else:
            req_list.append('')

    summary[req] = sorted(req_list)

pprint(summary['byr'])

print(len(passports))
print(f'valid: {len(valid)}')

#!/usr/bin/env python
"""
The final step in breaking the XMAS encryption relies on the invalid number
you just found: you must find a contiguous set of at least two numbers in your
list which sum to the invalid number from step 1.

Again consider the above example:

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576

In this list, adding up all of the numbers from 15 through 40 produces the
invalid number from step 1, 127. (Of course, the contiguous set of numbers
in your actual list might be much longer.)

To find the encryption weakness, add together the smallest and largest number
in this contiguous range; in this example, these are 15 and 47, producing 62.

What is the encryption weakness in your XMAS-encrypted list of numbers?
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

data = [int(i) for i in raw_data]


def get_invalid_num():
    preamble_length = 25

    for idx, num in enumerate(data[preamble_length:]):
        start = idx
        end = start + preamble_length
        preamble = data[start:end]
        found = False

        for x in preamble:
            diff = abs(num - x)

            if diff in preamble:
                found = True
                break

        if not found:
            return num


invalid = get_invalid_num()

for idx, num in enumerate(data):
    running_sum = num
    tally = [num]
    found = False

    while idx + 1 < len(data):
        idx += 1
        running_sum += data[idx]
        tally.append(data[idx])

        if running_sum > invalid:
            break

        if running_sum == invalid:
            found = True
            break

    if found:
        tally = sorted(tally)
        result = tally[0] + tally[-1]
        print(f'sum: {result}')
        break

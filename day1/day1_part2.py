#!/usr/bin/env python
"""
The Elves in accounting are thankful for your help; one of them even offers
you a starfish coin they had left over from a past vacation. They offer you
a second one if you can find three numbers in your expense report that meet
the same criteria.

Using the above example again, the three entries that sum to 2020 are 979,
366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that
sum to 2020?
"""
import pdb
from pprint import pprint

input_file = 'input.txt'

with open('input.txt', 'r') as fh:
    all_nums = [int(l.strip(), 10) for l in fh]


def search(nums):
    for i, num1 in enumerate(nums):
        if i + 1 == len(nums):
            break

        for j, num2 in enumerate(nums[i+1:]):
            diff1 = num1 + num2
            if diff1 >= 2020:
                continue

            diff = 2020 - diff1
            if diff in nums:
                print(f'result: {num1} * {num2} * {diff} = {num1 * num2 * diff}')
                return


search(all_nums)

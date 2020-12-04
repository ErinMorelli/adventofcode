#!/usr/bin/env python
"""

"""
input_file = 'input.txt'

with open('input.txt', 'r') as fh:
    lines = [int(l.strip(), 10) for l in fh]

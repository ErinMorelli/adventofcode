#!/usr/bin/env python
"""
???
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().strip().split(',')

data = [int(n, 10) for n in raw_data]

turns = data.copy()
spoken = set(turns[:-1])
turn = len(data)
current = data[-1]


def find_index(num, history):
    for i in range(len(history)-2, -1, -1):
        if history[i] == num:
            return i + 1
    return 0


while turn <= 2020:
    if turn == 2020:
        print(f'[{turn}] {current}')

    if current in spoken:
        spoken.add(current)
        prev_idx = find_index(current, turns)
        current = turn - prev_idx
    else:
        spoken.add(current)
        current = 0

    turns.append(current)
    turn += 1

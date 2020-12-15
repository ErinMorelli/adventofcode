#!/usr/bin/env python
"""
???
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().strip().split(',')

data = [int(n, 10) for n in raw_data]

spoken = set(data[:-1])
turn = len(data)
current = data[-1]
turn_map = dict()


for idx, start_num in enumerate(data):
    turn_map[start_num] = [idx+1]


while turn <= 30000000:
    if turn == 30000000:
        print(f'[{turn}] {current}')
        break

    if current in spoken:
        spoken.add(current)
        prev_idx = turn_map[current][-1]
        turn_map[current].append(turn)
        current = turn - prev_idx
    else:
        spoken.add(current)
        turn_map[current] = [turn]
        current = 0

    turn += 1

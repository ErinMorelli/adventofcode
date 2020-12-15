#!/usr/bin/env python
"""
Impressed, the Elves issue you a challenge: determine the `30000000`th number
spoken. For example, given the same starting numbers as above:

  * Given `0,3,6`, the `30000000`th number spoken is `175594`.
  * Given `1,3,2`, the `30000000`th number spoken is `2578`.
  * Given `2,1,3`, the `30000000`th number spoken is `3544142`.
  * Given `1,2,3`, the `30000000`th number spoken is `261214`.
  * Given `2,3,1`, the `30000000`th number spoken is `6895259`.
  * Given `3,2,1`, the `30000000`th number spoken is `18`.
  * Given `3,1,2`, the `30000000`th number spoken is `362`.

Given your starting numbers, what will be the `30000000`th number spoken?
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

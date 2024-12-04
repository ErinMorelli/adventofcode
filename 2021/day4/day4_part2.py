#!/usr/bin/env python
"""
--- Part Two ---

On the other hand, it might be wise to try a different strategy: let the giant
squid win.

You aren't sure how many bingo boards a giant squid could play at once, so
rather than waste time counting its arms, the safe thing to do is to figure
out which board will win last and choose that one. That way, no matter which
boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after
`13` is eventually called and its middle column is completely marked. If you
were to keep playing until this point, the second board would have a sum of
unmarked numbers equal to `148` for a final score of `148 * 13 = 1924`.

Figure out which board will win last. Once it wins, what would its final score
be?
"""
from collections import defaultdict

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

numbers = [int(x, 10) for x in raw_data[0].split(',')]

boards = '\n'.join(raw_data[1:]).split('\n\n')
boards = [b.strip().split('\n') for b in boards]
boards = [[r.split(' ') for r in b] for b in boards]
boards = [[[int(c, 10) for c in r if c != ''] for r in b] for b in boards]

row_size = 5


def check_board(board, nums):
    cols = defaultdict(list)

    for row in board:
        if set(row).issubset(nums):
            return True

        for idx, cell in enumerate(row):
            cols[idx].append(cell)

    for col in cols.values():
        if set(col).issubset(nums):
            return True

    return False


def bingo():
    called = set(numbers[:row_size-1])
    uncalled = numbers[row_size-1:]
    winners = []
    remaining = boards

    for next_num in uncalled:
        called.add(next_num)
        new_remaining = []

        for board in remaining:
            if check_board(board, called):
                winners.append(board)
            else:
                new_remaining.append(board)

            if len(winners) == len(boards):
                return board, called, next_num

        remaining = new_remaining


winner, just_called, winning_num = bingo()
score = 0

for r in winner:
    for c in r:
        if c not in just_called:
            score += c

result = score * winning_num

print(f'Result: {result}')

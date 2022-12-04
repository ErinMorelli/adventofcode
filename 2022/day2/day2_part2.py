#!/usr/bin/env python
"""
--- Part Two ---

The Elf finishes helping with the tent and sneaks back over to you. "Anyway,
the second column says how the round needs to end: `X` means you need to lose,
`Y` means you need to end the round in a draw, and `Z` means you need to win.
Good luck!"

The total score is still calculated in the same way, but now you need to
figure out what shape to choose so the round ends as indicated. The example
above now goes like this:

  * In the first round, your opponent will choose Rock (`A`), and you need the
    round to end in a draw (`Y`), so you also choose Rock. This gives you a
    score of 1 + 3 = 4.
  * In the second round, your opponent will choose Paper (`B`), and you choose
    Rock so you lose (`X`) with a score of 1 + 0 = 1.
  * In the third round, you will defeat your opponent's Scissors with Rock for
    a score of 1 + 6 = 7.

Now that you're correctly decrypting the ultra top secret strategy guide, you
would get a total score of `12`.

Following the Elf's instructions for the second column, what would your total
score be if everything goes exactly according to your strategy guide?
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().strip().splitlines()

data = [x.split() for x in raw_data]

outcome = {
    'X': 0,  # LOSE
    'Y': 3,  # DRAW
    'Z': 6   # WIN
}

ROCK = 1
PAPER = 2
SCISSOR = 3

rubric = {
    # ROCK
    'A': {
        'X': SCISSOR,
        'Y': ROCK,
        'Z': PAPER
    },
    # PAPER
    'B': {
        'X': ROCK,
        'Y': PAPER,
        'Z': SCISSOR
    },
    # SCISSOR
    'C': {
        'X': PAPER,
        'Y': SCISSOR,
        'Z': ROCK
    },
}

total = 0

for turn in data:
    move = rubric[turn[0]][turn[1]]
    total += move + outcome[turn[1]]

print(total)
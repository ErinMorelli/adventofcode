#!/usr/bin/env python
"""
--- Part Two ---

To make things a little more interesting, the Elf introduces one additional
rule. Now, `J` cards are
[jokers](https://en.wikipedia.org/wiki/Joker_\(playing_card\)) \- wildcards
that can act like whatever card would make the hand the strongest type
possible.

To balance this, `J` cards are now the weakest individual cards, weaker even
than `2`. The other cards stay in the same order: `A`, `K`, `Q`, `T`, `9`,
`8`, `7`, `6`, `5`, `4`, `3`, `2`, `J`.

`J` cards can pretend to be whatever card is best for the purpose of
determining hand type; for example, `QJJQ2` is now considered four of a kind.
However, for the purpose of breaking ties between two hands of the same type,
`J` is always treated as `J`, not the card it's pretending to be: `JKKK2` is
weaker than `QQQQ2` because `J` is weaker than `Q`.

Now, the above example goes very differently:

    32T3K 765
    T55J5 684
    KK677 28
    KTJJT 220
    QQQJA 483

  * `32T3K` is still the only one pair; it doesn't contain any jokers, so its
    strength doesn't increase.
  * `KK677` is now the only two pair, making it the second-weakest hand.
  * `T55J5`, `KTJJT`, and `QQQJA` are now all four of a kind! `T55J5` gets
    rank 3, `QQQJA` gets rank 4, and `KTJJT` gets rank 5.

With the new joker rule, the total winnings in this example are `5905`.

Using the new joker rule, find the rank of every hand in your set. What are
the new total winnings?
"""
from re import split
from functools import cmp_to_key

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

card_order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

hands = [x.split(' ') for x in raw_data]


# 1 = Five of a kind
# 2 = Four of a kind
# 3 = Full house
# 4 = Three of a kind
# 5 = Two pair
# 6 = One pair
# 7 = High card
def get_hand_type(c):
    unique_cards = list(set(c))
    joker_count = c.count('J')
    unique_card_count = len(unique_cards)
    # Five of a kind
    if unique_card_count == 1:
        return 1
    # Four of a kind OR Full house
    elif unique_card_count == 2:
        # If jokers are present, five of a kind
        if joker_count > 0:
            return 1
        a_count = c.count(unique_cards[0])
        b_count = c.count(unique_cards[1])
        # Four of a kind
        if a_count == 4 or b_count == 4:
            return 2
        # Full house
        return 3
    # Three of a kind OR Two pair
    elif unique_card_count == 3:
        a_count = c.count(unique_cards[0])
        b_count = c.count(unique_cards[1])
        c_count = c.count(unique_cards[2])
        # Three of a kind (Four of a kind for jokers)
        if a_count == 3 or b_count == 3 or c_count == 3:
            return 2 if joker_count > 0 else 4
        # Four of a kind for 2 jokers, full house for 1
        if joker_count > 0:
            return 2 if joker_count == 2 else 3
        # Two Pair
        return 5
    # One pair OR Three of a kind (with jokers)
    elif unique_card_count == 4:
        return 4 if joker_count > 0 else 6
    # High card OR One pair (with jokers)
    else:
        return 6 if joker_count > 0 else 7


def find_high_card(a, b):
    for i in range(0, 5):
        order_a = card_order.index(a[i])
        order_b = card_order.index(b[i])
        if order_a == order_b:
            continue
        return 1 if order_a < order_b else -1


def compare_hands(a, b):
    hand_a = split(r'', a[0])[1:-1]
    hand_b = split(r'', b[0])[1:-1]

    # Check types first
    type_a = get_hand_type(hand_a)
    type_b = get_hand_type(hand_b)
    if type_a != type_b:
        return 1 if type_a < type_b else -1

    # All others
    return find_high_card(hand_a, hand_b)


sorted_hands = sorted(hands, key=cmp_to_key(compare_hands))

result = sum([((i+1)*int(h[1])) for i, h in enumerate(sorted_hands)])
print(result)


#!/usr/bin/env python
"""
--- Part Two ---

Now, you just need to put all of the packets in the right order. Disregard the
blank lines in your list of received packets.

The distress signal protocol also requires that you include two additional
divider packets:

    [[2]]
    [[6]]

Using the same rules as before, organize all packets - the ones in your list
of received packets as well as the two divider packets - into the correct
order.

For the example above, the result of putting the packets in the correct order
is:

    []
    [[]]
    [[[]]]
    [1,1,3,1,1]
    [1,1,5,1,1]
    [[1],[2,3,4]]
    [1,[2,[3,[4,[5,6,0]]]],8,9]
    [1,[2,[3,[4,[5,6,7]]]],8,9]
    [[1],4]
    [[2]]
    [3]
    [[4,4],4,4]
    [[4,4],4,4,4]
    [[6]]
    [7,7,7]
    [7,7,7,7]
    [[8,7,6]]
    [9]

Afterward, locate the divider packets. To find the decoder key for this
distress signal, you need to determine the indices of the two divider packets
and multiply them together. (The first packet is at index 1, the second packet
is at index 2, and so on.) In this example, the divider packets are 10th and
14th, and so the decoder key is `140`.

Organize all of the packets into the correct order. What is the decoder key
for the distress signal?
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().replace('\n\n', '\n').splitlines()

data = [eval(x) for x in raw_data]
data.append([[2]])
data.append([[6]])


def compare_int(left, right):
    if left < right:
        return True
    if left > right:
        return False
    if left == right:
        return None


def compare_list(left, right):
    left_len = len(left)
    right_len = len(right)

    i = 0
    while True:
        # Both lists done
        if i == left_len and i == right_len:
            return None
        elif i == left_len:
            # left is done and shorter
            return True
        elif i == right_len:
            # right is done and shorter
            return False

        # Get next values
        next_left = left[i]
        next_right = right[i]

        # Get types
        left_type = type(next_left)
        right_type = type(next_right)

        # Compare ints
        if right_type == int and left_type == int:
            is_valid = compare_int(next_left, next_right)
        # Convert left int to list
        elif left_type == int:
            is_valid = compare_list([next_left], next_right)
        # Convert right int to list
        elif right_type == int:
            is_valid = compare_list(next_left, [next_right])
        # Compare lists
        else:
            is_valid = compare_list(next_left, next_right)

        if is_valid is not None:
            return is_valid

        i += 1


def sort_packets(packets):
    n = len(packets)

    while True:
        swapped = False

        for i in range(n)[1:]:
            p1 = packets[i-1]
            p2 = packets[i]

            if not compare_list(p1, p2):
                packets[i-1] = p2
                packets[i] = p1
                swapped = True

        n -= 1

        if not swapped:
            break

    return packets


new_list = sort_packets(data)

index1 = new_list.index([[2]]) + 1
index2 = new_list.index([[6]]) + 1

print(index1 * index2)

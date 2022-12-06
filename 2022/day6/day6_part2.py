#!/usr/bin/env python
"""
--- Part Two ---

Your device's communication system is correctly detecting packets, but still
isn't working. It looks like it also needs to look for messages.

A start-of-message marker is just like a start-of-packet marker, except it
consists of 14 distinct characters rather than 4.

Here are the first positions of start-of-message markers for all of the above
examples:

  * `mjqjpqmgbljsphdztnvjfqwrcgsmlb`: first marker after character `19`
  * `bvwbjplbgvbhsrlpgdmjqwftvncz`: first marker after character `23`
  * `nppdvjthqldpwncqszvftbrmjlhg`: first marker after character `23`
  * `nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg`: first marker after character `29`
  * `zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw`: first marker after character `26`

How many characters need to be processed before the first start-of-message
marker is detected?
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().strip()

last_4 = list(raw_data[:13])
marker = 13

for char in raw_data[13:]:
    last_4.append(char)
    marker += 1
    if len(set(last_4)) == 14:
        break
    last_4 = last_4[1:]

print(marker)
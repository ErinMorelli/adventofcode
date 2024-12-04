#!/usr/bin/env python
"""
--- Part Two ---

The engineers are surprised by the low number of safe reports until they
realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety
systems tolerate a single bad level in what would otherwise be a safe report.
It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an
unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

  * `7 6 4 2 1`: Safe without removing any level.
  * `1 2 7 8 9`: Unsafe regardless of which level is removed.
  * `9 7 6 2 1`: Unsafe regardless of which level is removed.
  * `1 3 2 4 5`: Safe by removing the second level, `3`.
  * `8 6 4 4 1`: Safe by removing the third level, `4`.
  * `1 3 6 7 9`: Safe without removing any level.

Thanks to the Problem Dampener, `4` reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can
remove a single level from unsafe reports. How many reports are now safe?
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    raw_data = fh.read().splitlines()

data = [[int(y) for y in x.split(' ')] for x in raw_data]

safe_count = 0

def is_safe(r):
    inc = None
    good = True

    for i in range(len(r) - 1):
        a = r[i]
        b = r[i + 1]

        diff = a - b
        diff_abs = abs(diff)
        diff_inc = diff < 0

        if (
                diff_abs < 1 or
                diff_abs > 3 or
                (
                        inc is not None and
                        inc is not diff_inc
                )
        ):
            good = False

        inc = diff_inc

    return good

for row in data:
    if not is_safe(row):
        for i in range(len(row)):
            new_row = row.copy()
            del new_row[i]

            if is_safe(new_row):
                safe_count += 1
                break
    else:
        safe_count += 1

print(safe_count)

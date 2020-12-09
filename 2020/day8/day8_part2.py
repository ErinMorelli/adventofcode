#!/usr/bin/env python
"""
After some careful analysis, you believe that exactly one instruction is
corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is
supposed to be a jmp. (No acc instructions were harmed in the corruption of
this boot code.)

The program is supposed to terminate by attempting to execute an instruction
immediately after the last instruction in the file. By changing exactly one
jmp or nop, you can repair the boot code and make it terminate correctly.

For example, consider the same program from above:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6

If you change the first instruction from nop +0 to jmp +0, it would create a
single-instruction infinite loop, never leaving that instruction. If you
change almost any of the jmp instructions, the program will still eventually
find another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4),
the program terminates! The instructions are visited in this order:

nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6

After the last instruction (acc +6), the program terminates by attempting to
run the instruction below the last instruction in the file. With this change,
after the program terminates, the accumulator contains the value 8 (acc +1,
acc +1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp
(to nop) or nop (to jmp). What is the value of the accumulator after the
program terminates?
"""
import re

input_file = 'input.txt'

with open(input_file, 'r') as fh:
    code = fh.read().splitlines()


tried = set()

for line_no in range(len(code)):
    acc = 0
    idx = 0
    done = set()
    changed = False
    complete = False

    while True:
        if idx in done:
            break

        if idx == len(code):
            complete = True
            break

        line = code[idx]
        parsed = re.match(r'(acc|jmp|nop) ([+-])(\d+)', line)

        cmd = parsed.group(1)
        op = parsed.group(2)
        pos = int(parsed.group(3), 10)

        done.add(idx)

        if cmd == 'jmp':
            if idx not in tried and not changed:
                changed = True
                tried.add(idx)
                idx += 1
            else:
                idx = idx + pos if op == '+' else idx - pos
            continue

        elif cmd == 'acc':
            acc = acc + pos if op == '+' else acc - pos
            idx += 1

        elif cmd == 'nop':
            if idx not in tried and not changed:
                changed = True
                tried.add(idx)
                idx = idx + pos if op == '+' else idx - pos
            else:
                idx += 1

    if complete:
        print(f'acc: {acc}')
        break

#!/usr/bin/env python
"""
The homework (your puzzle input) consists of a series of expressions that
consist of addition (`+`), multiplication (`*`), and parentheses (`(...)`).
Just like normal math, parentheses indicate that the expression inside must be
evaluated before it can be used by the surrounding expression. Addition still
finds the sum of the numbers on both sides of the operator, and multiplication
still finds the product.

However, the rules of operator precedence have changed. Rather than evaluating
multiplication before addition, the operators have the same precedence, and
are evaluated left-to-right regardless of the order in which they appear.

For example, the steps to evaluate the expression `1 + 2 * 3 + 4 * 5 + 6` are
as follows:

    1 + 2 * 3 + 4 * 5 + 6
      3   * 3 + 4 * 5 + 6
          9   + 4 * 5 + 6
             13   * 5 + 6
                 65   + 6
                     71

Parentheses can override this order; for example, here is what happens if
parentheses are added to form `1 + (2 * 3) + (4 * (5 + 6))`:

    1 + (2 * 3) + (4 * (5 + 6))
    1 +    6    + (4 * (5 + 6))
         7      + (4 * (5 + 6))
         7      + (4 *   11   )
         7      +     44
                51

Before you can help with the homework, you need to understand it yourself.
Evaluate the expression on each line of the homework; what is the sum of the
resulting values?
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    data = fh.read().splitlines()


def solve(expr):
    result = eval(' '.join(expr[:3]))

    if len(expr) > 3:
        for i in range(3, len(expr), 2):
            result = eval(f'{result} {expr[i]} {expr[i+1]}')

    return str(result)


def evaluate_expression(expr):
    start_idx = None
    end_idx = None

    for idx in range(len(expr)):
        char = expr[idx]

        if char == '(':
            start_idx = idx

        elif char == ')':
            end_idx = idx
            break

    if start_idx is None:
        return solve(expr)

    sub_expr = expr[start_idx+1:end_idx]
    result = solve(sub_expr)
    new_expr = expr[:start_idx] + [result] + expr[end_idx+1:]

    return evaluate_expression(new_expr)


solutions = []

for line in data:
    expression = list(line.replace(' ', ''))
    solution = evaluate_expression(expression)
    solutions.append(int(solution))

print(f'sum: {sum(solutions)}')

#!/usr/bin/env python
"""
You manage to answer the child's questions and they finish part 1 of their
homework, but get stuck when they reach the next section: advanced math.

Now, addition and multiplication have different precedence levels, but they're
not the ones you're familiar with. Instead, addition is evaluated before
multiplication.

For example, the steps to evaluate the expression `1 + 2 * 3 + 4 * 5 + 6` are
now as follows:

    1 + 2 * 3 + 4 * 5 + 6
      3   * 3 + 4 * 5 + 6
      3   *   7   * 5 + 6
      3   *   7   *  11
         21       *  11
             231

What do you get if you add up the results of evaluating the homework problems
using these new rules?
"""
input_file = 'input.txt'

with open(input_file, 'r') as fh:
    data = fh.read().splitlines()


def solve(expr):
    plus = expr.count('+')
    result = expr.copy()

    for _ in range(plus):
        idx = result.index('+')
        res = eval(f'{result[idx-1]} {result[idx]} {result[idx+1]}')
        result.insert(idx-1, str(res))
        del result[idx]
        del result[idx]
        del result[idx]

    x = eval(' '.join(result))
    return str(x)


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

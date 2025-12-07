from ..core import open_file
from operator import mul, add

numbers: list[list[int]] = []
operators: list[callable[[int, int], int]] = []

ops = {"*": (1, mul), "+": (0, add)}

with open_file() as f:
    for line in f:
        if line.startswith("*") or line.startswith("+"):
            operators = [ops[op] for op in line.split()]
            break
        numbers.append([int(n) for n in line.split()])

for ns in numbers:
    for i, n in enumerate(ns):
        result, op = operators[i]
        operators[i] = (op(result, n), op)


total = sum(n for n, _ in operators)


print(total)

from functools import reduce
from ..core import open_file
from operator import mul, add


operators: list[callable[[int, int], int]] = []

ops = {"*": (1, mul), "+": (0, add)}

indices = []
lines = []

with open_file() as f:
    for line in f:
        if line.startswith("*") or line.startswith("+"):
            for i, c in enumerate(line):
                if c in ('+', '*'):
                    operators.append(ops[c])
                    indices.append(i)
            break
        lines.append(line.removesuffix('\n'))

slices = [slice(start, None if i == len(indices) - 1 else indices[i + 1])
          for i, start in enumerate(indices)]


columns: list[list[str]] = [[] for _ in range(len(operators))]

for line in lines:
    for i, sl in enumerate(slices):
        columns[i].append(line[sl])

total = 0

for i, col in enumerate(columns):
    numbers = []
    for j in range(len(col[0])):
        n = ''
        for val in col:
            n += val[-j - 1]
        n = n.strip()
        if n:
            numbers.append(int(n))

    inital, op = operators[i]
    total += reduce(op, numbers)

print(total)

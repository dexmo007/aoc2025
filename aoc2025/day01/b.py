from ..core import open_file


with open_file() as f:
    rotations = f.readlines()


def parse(line: str):
    line = line.strip()
    return -1 if line[0] == "L" else 1, int(line[1:])


rotations = [parse(r) for r in rotations if r.strip()]

value = 50
zeros = 0

for dir, rot in rotations:
    started_at_0 = value == 0
    value += dir * rot
    div, value = divmod(value, 100)
    if div <= 0 and value == 0:
        zeros += 1
    if div < 0 and started_at_0:
        div += 1
    div = abs(div)
    zeros += div


print(zeros)

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
    value += dir * rot
    value %= 100
    if value == 0:
        zeros += 1


print(zeros)

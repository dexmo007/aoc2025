from ..core import open_file

grid: list[list[str]] = []
start: tuple[int, int]

with open_file() as f:
    for y, line in enumerate(f):
        row = []
        for x, c in enumerate(line.strip()):
            if c == 'S':
                start = (y, x)
                row.append('.')
            else:
                row.append(c)
        grid.append(row)

assert start

stack = [start]
splits = 0

while stack:
    y, x = stack.pop()
    if y >= len(grid) - 2:
        continue  # beam is at the bottom
    y += 1
    if grid[y][x] == '|':
        continue  # there already is a beam
    if grid[y][x] == '.':
        stack.append((y, x))
        grid[y][x] = '|'
        continue
    splits += 1
    stack.append((y, x-1))
    grid[y][x-1] = '|'
    stack.append((y, x+1))
    grid[y][x+1] = '|'


print(splits)

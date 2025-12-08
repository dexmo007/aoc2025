from ..core import open_file
from collections import deque

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

timelines_map = {start: 1}
stack = deque([start])
timelines = 0


def go_to(coord: tuple[int, int], cur_timelines: int):
    global timelines_map, stack, timelines
    y, x = coord
    if coord in timelines_map:
        timelines_map[(y, x)] += cur_timelines
        return
    timelines_map[(y, x)] = cur_timelines
    stack.append((y, x))


while stack:
    y, x = stack.popleft()
    cur_timelines = timelines_map.pop((y, x))
    if y >= len(grid) - 2:
        timelines += cur_timelines
        continue  # beam is at the bottom
    y += 1
    if grid[y][x] == '.':
        go_to((y, x), cur_timelines)
        continue
    go_to((y, x-1), cur_timelines)
    go_to((y, x+1), cur_timelines)


print(timelines)

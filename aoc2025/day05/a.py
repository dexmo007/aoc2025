from ..core import open_file

ranges: list[tuple[int, int]] = []

def is_in_any_range(n: int):
    for start,end in ranges:
        if n < start or n > end:
            continue
        return True

fresh = 0

with open_file() as f:
    for line in f:
        if not line.strip():
            break
        ranges.append(tuple(int(n) for n in line.split('-')))
    for line in f:
        if is_in_any_range(int(line)):  
            fresh += 1

print(fresh)            
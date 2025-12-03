import math
from ..core import open_file


ranges: list[tuple[int, int]] = []

with open_file() as f:
    for range_spec in f.read().split(","):
        start, end = tuple(map(int, range_spec.split("-")))
        ranges.append((start, end))


def check_pattern(n: int, n_digits: int, length: int):
    if n_digits % length != 0:
        return False
    p = 10**length
    val, pattern = divmod(n, p)
    while val:
        val, group = divmod(val, p)
        if group != pattern:
            return False
    return True


invalid_sum = 0

for start, end in ranges:
    for n in range(start, end + 1):
        n_digits = int(math.log10(n)) + 1
        for length in range(1, n_digits // 2 + 1):
            if check_pattern(n, n_digits, length):
                invalid_sum += n
                break

print(invalid_sum)

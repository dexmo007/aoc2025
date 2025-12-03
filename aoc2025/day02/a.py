import math
from ..core import open_file


ranges: list[tuple[int, int]] = []

with open_file() as f:
    for range_spec in f.read().split(","):
        start, end = tuple(map(int, range_spec.split("-")))
        ranges.append((start, end))

invalid_sum = 0

for start, end in ranges:
    for n in range(start, end + 1):
        n_digits = int(math.log10(n)) + 1
        if n_digits % 2 == 1:
            continue

        p = 10 ** (n_digits / 2)
        if n % p == n // p:
            invalid_sum += n

print(invalid_sum)

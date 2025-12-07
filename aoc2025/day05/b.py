from ..core import open_file

ranges: dict[int, int] = {}


def merge_intersecting_range(range: tuple[int, int]):
    global ranges
    a_start, a_end = range
    for b_start, b_end in ranges.items():
        
        if (
            a_start >= b_start
            and a_start <= b_end
            or a_end >= b_start
            and a_end <= b_end
        ):
            del ranges[b_start]
            merge_intersecting_range((min(a_start, b_start), max(a_end, b_end)))
            return
    remove_sub_ranges(a_start, a_end)
    ranges[a_start] = a_end

def remove_sub_ranges(start: int, end: int):
    global ranges
    to_delete = set()
    for b_start, b_end in ranges.items():
        if b_start >= start and b_end <= end:
            to_delete.add(b_start)
    for key in to_delete:
        del ranges[key]



with open_file() as f:
    for line in f:
        if not line.strip():
            break
        start, end = tuple(int(n) for n in line.split("-"))

        merge_intersecting_range((start, end))

fresh = sum(end - start + 1 for start, end in ranges.items())


print(fresh)

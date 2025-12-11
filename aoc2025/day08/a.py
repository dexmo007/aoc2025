from collections import defaultdict
import heapq
import itertools
import math
from ..core import open_file

type Point = tuple[int, int, int]

junction_boxes: list[Point] = []
n_connections: int

with open_file() as f:
    fit = iter(f)
    n_connections = int(next(fit).strip())
    for line in fit:
        parts = line.strip().split(',')
        coords = tuple((int(p) for p in parts))
        junction_boxes.append(coords)


def dist(c1: Point, c2: Point):
    return math.sqrt(sum((p2 - p1) ** 2 for p1, p2 in zip(c1, c2)))


shortest_connections = heapq.nsmallest(
    n_connections, itertools.combinations(junction_boxes, 2), lambda ps: dist(*ps))

circuits = {}
circuit_seq = itertools.count()


def merge_circuits(c1, c2):
    cid1 = circuits[c1]
    cid2 = circuits[c2]
    if cid1 == cid2:
        return
    for p, cid in circuits.items():
        if cid != cid2:
            continue
        circuits[p] = cid1


for c1, c2 in shortest_connections:
    if c1 in circuits:
        if c2 in circuits:
            merge_circuits(c1, c2)
            continue
        circuits[c2] = circuits[c1]
        continue
    if c2 in circuits:
        circuits[c1] = circuits[c2]
        continue
    cid = next(circuit_seq)
    circuits[c1] = cid
    circuits[c2] = cid

circuit_sizes = defaultdict(int)

for cid in circuits.values():
    circuit_sizes[cid] += 1

largest_circuits = heapq.nlargest(3, circuit_sizes.values())
result = math.prod(largest_circuits)

print(result)

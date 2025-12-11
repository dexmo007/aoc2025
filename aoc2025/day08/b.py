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
circuit_ids = set()


def merge_circuits(c1, c2):
    cid1 = circuits[c1]
    cid2 = circuits[c2]
    if cid1 == cid2:
        return
    for p, cid in circuits.items():
        if cid != cid2:
            continue
        circuits[p] = cid1
    circuit_ids.remove(cid2)


def connect(c1, c2):
    if c1 in circuits:
        if c2 in circuits:
            merge_circuits(c1, c2)
            return
        circuits[c2] = circuits[c1]
        return
    if c2 in circuits:
        circuits[c1] = circuits[c2]
        return
    cid = next(circuit_seq)
    circuits[c1] = cid
    circuits[c2] = cid
    circuit_ids.add(cid)


for c1, c2 in sorted(itertools.combinations(junction_boxes, 2), key=lambda ps: dist(*ps)):
    connect(c1, c2)
    if len(circuits.keys()) == len(junction_boxes) and len(circuit_ids) == 1:
        break

print(c1[0] * c2[0])

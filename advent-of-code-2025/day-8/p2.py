"""
The Elves were right; they definitely don't have enough extension cables. You'll need to keep connecting junction boxes together until they're all in one large circuit.

Continuing the above example, the first connection which causes all of the junction boxes to form a single circuit is between the junction boxes at 216,146,977 and 117,168,530. The Elves need to know how far those junction boxes are from the wall so they can pick the right extension cable; multiplying the X coordinates of those two junction boxes (216 and 117) produces 25272.

Continue connecting the closest unconnected pairs of junction boxes together until they're all in the same circuit. What do you get if you multiply together the X coordinates of the last two junction boxes you need to connect?


"""

import os
from typing import List, Tuple


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True


def parse_points(lines: List[str]) -> List[Tuple[int, int, int]]:
    pts = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        x, y, z = map(int, line.split(","))
        pts.append((x, y, z))
    return pts


def solution():
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_path) as f:
        lines = f.read().strip().split("\n")

    points = parse_points(lines)
    n = len(points)
    if n == 0:
        return 0

    # Compute all pairwise distances.
    distances = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            dist2 = dx * dx + dy * dy + dz * dz
            distances.append((dist2, i, j))

    distances.sort(key=lambda t: t[0])

    dsu = DSU(n)
    last_edge = None

    for _, a, b in distances:
        merged = dsu.union(a, b)
        if merged:
            last_edge = (a, b)
            if dsu.components == 1:
                break

    if last_edge is None:
        return 0

    a, b = last_edge
    x_prod = points[a][0] * points[b][0]
    return x_prod


if __name__ == "__main__":
    print(solution())

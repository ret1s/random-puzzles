"""
The Elves just remembered: they can only switch out tiles that are red or green. So, your rectangle can only include red or green tiles.

In your list, every red tile is connected to the red tile before and after it by a straight line of green tiles. The list wraps, so the first red tile is also connected to the last red tile. Tiles that are adjacent in your list will always be on either the same row or the same column.

Using the same example as before, the tiles marked X would be green:

..............
.......#XXX#..
.......X...X..
..#XXXX#...X..
..X........X..
..#XXXXXX#.X..
.........X.X..
.........#X#..
..............
In addition, all of the tiles inside this loop of red and green tiles are also green. So, in this example, these are the green tiles:

..............
.......#XXX#..
.......XXXXX..
..#XXXX#XXXX..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............
The remaining tiles are never red nor green.

The rectangle you choose still must have red tiles in opposite corners, but any other tiles it includes must now be red or green. This significantly limits your options.

For example, you could make a rectangle out of red and green tiles with an area of 15 between 7,3 and 11,1:

..............
.......OOOOO..
.......OOOOO..
..#XXXXOOOOO..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............
Or, you could make a thin rectangle with an area of 3 between 9,7 and 9,5:

..............
.......#XXX#..
.......XXXXX..
..#XXXX#XXXX..
..XXXXXXXXXX..
..#XXXXXXOXX..
.........OXX..
.........OX#..
..............
The largest rectangle you can make in this example using only red and green tiles has area 24. One way to do this is between 9,5 and 2,3:

..............
.......#XXX#..
.......XXXXX..
..OOOOOOOOXX..
..OOOOOOOOXX..
..OOOOOOOOXX..
.........XXX..
.........#X#..
..............
Using two red tiles as opposite corners, what is the largest area of any rectangle you can make using only red and green tiles?


"""

import os
from typing import List, Tuple, Dict


def parse_points(lines: List[str]) -> List[Tuple[int, int]]:
    pts = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        x_str, y_str = line.split(",")
        pts.append((int(x_str), int(y_str)))
    return pts


def point_on_edge(x: int, y: int, a: Tuple[int, int], b: Tuple[int, int]) -> bool:
    (x1, y1), (x2, y2) = a, b
    if x1 == x2:  # vertical
        return x == x1 and min(y1, y2) <= y <= max(y1, y2)
    if y1 == y2:  # horizontal
        return y == y1 and min(x1, x2) <= x <= max(x1, x2)
    return False  # should not happen (axis-aligned polygon)


def point_in_or_on_polygon(x: int, y: int, poly: List[Tuple[int, int]]) -> bool:
    # Ray casting to the right; includes boundary.
    inside = False
    n = len(poly)
    for i in range(n):
        a = poly[i]
        b = poly[(i + 1) % n]
        if point_on_edge(x, y, a, b):
            return True
        x1, y1 = a
        x2, y2 = b
        # Only vertical edges contribute to crossing for axis-aligned polygon.
        if x1 == x2:
            if ((y1 <= y < y2) or (y2 <= y < y1)) and x1 > x:
                inside = not inside
    return inside


def solution():
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_path) as f:
        lines = f.read().strip().split("\n")

    red_points = parse_points(lines)
    if not red_points:
        return 0

    polygon = red_points  # ordered loop
    points = red_points

    inside_cache: Dict[Tuple[int, int], bool] = {}

    def is_inside(pt: Tuple[int, int]) -> bool:
        if pt not in inside_cache:
            inside_cache[pt] = point_in_or_on_polygon(pt[0], pt[1], polygon)
        return inside_cache[pt]

    edges = []
    for i in range(len(polygon)):
        a = polygon[i]
        b = polygon[(i + 1) % len(polygon)]
        edges.append((a, b))

    def rectangle_inside(min_x: int, max_x: int, min_y: int, max_y: int) -> bool:
        # Corners must be inside or on boundary.
        corners = [
            (min_x, min_y),
            (min_x, max_y),
            (max_x, min_y),
            (max_x, max_y),
        ]
        if not all(is_inside(c) for c in corners):
            return False

        # Ensure polygon boundary doesn't cut through rectangle interior.
        for a, b in edges:
            x1, y1 = a
            x2, y2 = b
            if x1 == x2:  # vertical edge
                x = x1
                if min_x < x < max_x:
                    low = min(y1, y2)
                    high = max(y1, y2)
                    if max(low, min_y) < min(high, max_y):
                        return False
            else:  # horizontal edge
                y = y1
                if min_y < y < max_y:
                    low = min(x1, x2)
                    high = max(x1, x2)
                    if max(low, min_x) < min(high, max_x):
                        return False
        return True

    max_area = 0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            min_x, max_x = sorted((x1, x2))
            min_y, max_y = sorted((y1, y2))
            if not rectangle_inside(min_x, max_x, min_y, max_y):
                continue
            area = (max_x - min_x + 1) * (max_y - min_y + 1)
            if area > max_area:
                max_area = area

    return max_area


if __name__ == "__main__":
    print(solution())

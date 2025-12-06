"""
As the forklifts break through the wall, the Elves are delighted to discover that there was a cafeteria on the other side after all.

You can hear a commotion coming from the kitchen. "At this rate, we won't have any time left to put the wreaths up in the dining hall!" Resolute in your quest, you investigate.

"If only we hadn't switched to the new inventory management system right before Christmas!" another Elf exclaims. You ask what's going on.

The Elves in the kitchen explain the situation: because of their complicated new inventory management system, they can't figure out which of their ingredients are fresh and which are spoiled. When you ask how it works, they give you a copy of their database (your puzzle input).

The database operates on ingredient IDs. It consists of a list of fresh ingredient ID ranges, a blank line, and a list of available ingredient IDs. For example:

3-5
10-14
16-20
12-18

1
5
8
11
17
32
The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh. The ranges can also overlap; an ingredient ID is fresh if it is in any range.

The Elves are trying to determine which of the available ingredient IDs are fresh. In this example, this is done as follows:

Ingredient ID 1 is spoiled because it does not fall into any range.
Ingredient ID 5 is fresh because it falls into range 3-5.
Ingredient ID 8 is spoiled.
Ingredient ID 11 is fresh because it falls into range 10-14.
Ingredient ID 17 is fresh because it falls into range 16-20 as well as range 12-18.
Ingredient ID 32 is spoiled.
So, in this example, 3 of the available ingredient IDs are fresh.

Process the database file from the new inventory management system. How many of the available ingredient IDs are fresh?
"""

import bisect
import os


def parse_ranges(raw: str):
    ranges = []
    for line in raw.splitlines():
        if not line.strip():
            continue
        start, end = map(int, line.split("-"))
        ranges.append((start, end))
    return ranges


def merge_ranges(ranges):
    if not ranges:
        return []
    ranges.sort()
    merged = [list(ranges[0])]
    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
    return [(s, e) for s, e in merged]


def count_fresh(ranges, ids):
    merged = merge_ranges(ranges)
    starts = [s for s, _ in merged]
    ends = [e for _, e in merged]

    fresh = 0
    for val in ids:
        idx = bisect.bisect_right(starts, val) - 1
        if idx >= 0 and val <= ends[idx]:
            fresh += 1
    return fresh


def solution():
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_path) as f:
        content = f.read()

    if not content.strip():
        return 0

    if "\n\n" in content:
        range_part, ids_part = content.split("\n\n", 1)
    else:
        range_part, ids_part = content, ""

    ranges = parse_ranges(range_part)
    ids = [int(line) for line in ids_part.splitlines() if line.strip()]

    return count_fresh(ranges, ids)


if __name__ == "__main__":
    print(solution())

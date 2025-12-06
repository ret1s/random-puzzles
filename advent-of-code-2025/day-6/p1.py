"""
After helping the Elves in the kitchen, you were taking a break and helping them re-enact a movie scene when you over-enthusiastically jumped into the garbage chute!

A brief fall later, you find yourself in a garbage smasher. Unfortunately, the door's been magnetically sealed.

As you try to find a way out, you are approached by a family of cephalopods! They're pretty sure they can get the door open, but it will take some time. While you wait, they're curious if you can help the youngest cephalopod with her math homework.

Cephalopod math doesn't look that different from normal math. The math worksheet (your puzzle input) consists of a list of problems; each problem has a group of numbers that need to either be either added (+) or multiplied (*) together.

However, the problems are arranged a little strangely; they seem to be presented next to each other in a very long horizontal list. For example:

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
Each problem's numbers are arranged vertically; at the bottom of the problem is the symbol for the operation that needs to be performed. Problems are separated by a full column of only spaces. The left/right alignment of numbers within each problem can be ignored.

So, this worksheet contains four problems:

123 * 45 * 6 = 33210
328 + 64 + 98 = 490
51 * 387 * 215 = 4243455
64 + 23 + 314 = 401
To check their work, cephalopod students are given the grand total of adding together all of the answers to the individual problems. In this worksheet, the grand total is 33210 + 490 + 4243455 + 401 = 4277556.

Of course, the actual worksheet is much wider. You'll need to make sure to unroll it completely so that you can read the problems clearly.

Solve the problems on the math worksheet. What is the grand total found by adding together all of the answers to the individual problems?
"""

import os
import math


def solution():
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_path) as f:
        lines = [line.rstrip("\n") for line in f]

    if not lines:
        return 0

    # Pad all lines to equal width for column-wise processing.
    width = max(len(line) for line in lines)
    grid = [line.ljust(width) for line in lines]

    operator_row = grid[-1]
    number_rows = grid[:-1]

    # Identify separator columns: columns that are all spaces.
    is_separator = [all(row[col] == " " for row in grid) for col in range(width)]

    segments = []
    in_seg = False
    start = 0
    for col in range(width + 1):  # iterate one past end to flush last segment
        sep = is_separator[col] if col < width else True
        if not sep and not in_seg:
            start = col
            in_seg = True
        elif sep and in_seg:
            segments.append((start, col))
            in_seg = False

    total = 0

    for start, end in segments:
        # Find operator in this segment.
        op_char = None
        for ch in operator_row[start:end]:
            if ch in "+*":
                op_char = ch
                break
        if op_char is None:
            continue

        nums = []
        for row in number_rows:
            token = row[start:end].strip()
            if token:
                nums.append(int(token))

        if not nums:
            continue

        if op_char == "+":
            result = sum(nums)
        else:
            result = math.prod(nums)

        total += result

    return total


if __name__ == "__main__":
    print(solution())

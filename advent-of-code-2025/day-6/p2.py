"""
The big cephalopods come back to check on how things are going. When they see that your grand total doesn't match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.

Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

Here's the example worksheet again:

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
Reading the problems right-to-left one column at a time, the problems are now quite different:

The rightmost problem is 4 + 431 + 623 = 1058
The second problem from the right is 175 * 581 * 32 = 3253600
The third problem from the right is 8 + 248 + 369 = 625
Finally, the leftmost problem is 356 * 24 * 1 = 8544
Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.

Solve the problems on the math worksheet again. What is the grand total found by adding together all of the answers to the individual problems?
"""

import math
import os


def solution():
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_path) as f:
        lines = [line.rstrip("\n") for line in f]

    if not lines:
        return 0

    width = max(len(line) for line in lines)
    grid = [line.ljust(width) for line in lines]

    op_row = grid[-1]
    number_rows = grid[:-1]
    rows = len(grid)

    is_sep = [all(grid[r][c] == " " for r in range(rows)) for c in range(width)]

    segments = []
    in_seg = False
    start = 0
    for c in range(width + 1):
        sep = is_sep[c] if c < width else True
        if not sep and not in_seg:
            start = c
            in_seg = True
        elif sep and in_seg:
            segments.append((start, c))
            in_seg = False

    total = 0

    for start, end in segments:
        # Operator is on the bottom row somewhere in the segment.
        op = None
        for ch in op_row[start:end]:
            if ch in "+*":
                op = ch
                break
        if op is None:
            continue

        nums = []
        for c in range(end - 1, start - 1, -1):
            digits = []
            for r in range(rows - 1):  # exclude operator row
                ch = grid[r][c]
                if ch.isdigit():
                    digits.append(ch)
            if digits:
                nums.append(int("".join(digits)))

        if not nums:
            continue

        if op == "+":
            result = sum(nums)
        else:
            result = math.prod(nums)

        total += result

    return total


if __name__ == "__main__":
    print(solution())

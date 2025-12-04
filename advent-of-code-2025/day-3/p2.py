"""
--- Day 3: Lobby ---
Part 2

We need the lexicographically largest subsequence of length 12 from each line
of digits (batteries must remain in order). Sum the resulting numbers.
"""

import os

def solution():
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_path) as f:
        lines = f.read().strip().split("\n")

    k = 12
    total_joltage = 0

    def max_subsequence(num_str: str, length: int) -> str:
        """Greedy stack to keep the largest subsequence of given length."""
        if len(num_str) <= length:
            return num_str

        stack = []
        to_remove = len(num_str) - length

        for ch in num_str:
            while to_remove and stack and stack[-1] < ch:
                stack.pop()
                to_remove -= 1
            stack.append(ch)

        if to_remove:
            stack = stack[:-to_remove]

        return "".join(stack[:length])

    for line in lines:
        if not line:
            continue
        best = max_subsequence(line.strip(), k)
        total_joltage += int(best)

    return total_joltage

if __name__ == "__main__":
    print(solution())

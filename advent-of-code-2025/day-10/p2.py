"""
All of the machines are starting to come online! Now, it's time to worry about the joltage requirements.

Each machine needs to be configured to exactly the specified joltage levels to function properly. Below the buttons on each machine is a big lever that you can use to switch the buttons from configuring the indicator lights to increasing the joltage levels. (Ignore the indicator light diagrams.)

The machines each have a set of numeric counters tracking its joltage levels, one counter per joltage requirement. The counters are all initially set to zero.

So, joltage requirements like {3,5,4,7} mean that the machine has four counters which are initially 0 and that the goal is to simultaneously configure the first counter to be 3, the second counter to be 5, the third to be 4, and the fourth to be 7.

The button wiring schematics are still relevant: in this new joltage configuration mode, each button now indicates which counters it affects, where 0 means the first counter, 1 means the second counter, and so on. When you push a button, each listed counter is increased by 1.

So, a button wiring schematic like (1,3) means that each time you push that button, the second and fourth counters would each increase by 1. If the current joltage levels were {0,1,2,3}, pushing the button would change them to be {0,2,2,4}.

You can push each button as many times as you like. However, your finger is getting sore from all the button pushing, and so you will need to determine the fewest total presses required to correctly configure each machine's joltage level counters to match the specified joltage requirements.

Consider again the example from before:

[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
Configuring the first machine's counters requires a minimum of 10 button presses. One way to do this is by pressing (3) once, (1,3) three times, (2,3) three times, (0,2) once, and (0,1) twice.

Configuring the second machine's counters requires a minimum of 12 button presses. One way to do this is by pressing (0,2,3,4) twice, (2,3) five times, and (0,1,2) five times.

Configuring the third machine's counters requires a minimum of 11 button presses. One way to do this is by pressing (0,1,2,3,4) five times, (0,1,2,4,5) five times, and (1,2) once.

So, the fewest button presses required to correctly configure the joltage level counters on all of the machines is 10 + 12 + 11 = 33.

Analyze each machine's joltage requirements and button wiring schematics. What is the fewest button presses required to correctly configure the joltage level counters on all of the machines?
"""

import os
import re
from fractions import Fraction
from typing import List, Tuple


def parse_line(line: str) -> Tuple[List[int], List[List[int]]]:
    target_part = re.search(r"\{([^}]*)\}", line)
    if not target_part:
        return [], []
    targets = [int(x) for x in target_part.group(1).split(",")]

    buttons = []
    for part in re.findall(r"\(([^)]*)\)", line):
        part = part.strip()
        if not part:
            continue
        buttons.append([int(x) for x in part.split(",") if x != ""])

    return targets, buttons


def rref(rows: List[List[Fraction]], m: int) -> Tuple[List[List[Fraction]], List[int]]:
    """Return RREF matrix and list of pivot columns."""
    pivot_cols = []
    r = 0
    n_rows = len(rows)
    for c in range(m):
        pivot = None
        for rr in range(r, n_rows):
            if rows[rr][c] != 0:
                pivot = rr
                break
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        factor = rows[r][c]
        rows[r] = [v / factor for v in rows[r]]
        for rr in range(n_rows):
            if rr != r and rows[rr][c] != 0:
                fac = rows[rr][c]
                rows[rr] = [a - fac * b for a, b in zip(rows[rr], rows[r])]
        pivot_cols.append(c)
        r += 1
    return rows, pivot_cols


def min_presses_for_machine(targets: List[int], buttons: List[List[int]]) -> int:
    n = len(targets)
    m = len(buttons)
    if n == 0 or m == 0:
        return 0

    # Upper bound for each button: cannot exceed smallest target it affects.
    upper_bounds = []
    for b in buttons:
        if not b:
            upper_bounds.append(0)
        else:
            upper_bounds.append(min(targets[i] for i in b))

    # Build augmented matrix.
    rows = []
    for i in range(n):
        row = [Fraction(0)] * (m + 1)
        for j, idxs in enumerate(buttons):
            if i in idxs:
                row[j] = Fraction(1)
        row[-1] = Fraction(targets[i])
        rows.append(row)

    rows, pivot_cols = rref(rows, m)
    pivot_set = set(pivot_cols)
    free_cols = [c for c in range(m) if c not in pivot_set]

    def eval_pivots(free_vals: List[int]) -> Tuple[bool, int]:
        total = sum(free_vals)
        # Map free column to its value.
        free_map = {col: val for col, val in zip(free_cols, free_vals)}
        # Pivot rows are the first len(pivot_cols) rows.
        for idx, pcol in enumerate(pivot_cols):
            val = rows[idx][-1]
            for fcol, fval in free_map.items():
                coeff = rows[idx][fcol]
                if coeff != 0:
                    val -= coeff * fval
            if val.denominator != 1:
                return False, 0
            ival = val.numerator
            if ival < 0 or ival > upper_bounds[pcol]:
                return False, 0
            total += ival
        return True, total

    best = float("inf")

    # Enumerate free variable choices within bounds.
    def backtrack(idx: int, chosen: List[int]):
        nonlocal best
        if idx == len(free_cols):
            ok, total = eval_pivots(chosen)
            if ok and total < best:
                best = total
            return
        col = free_cols[idx]
        ub = upper_bounds[col]
        # Simple pruning: current sum + remaining minimal (0) cannot exceed best check inside eval.
        for val in range(ub + 1):
            # Early rough lower bound: current partial presses + val.
            if sum(chosen) + val >= best:
                # Even if pivots add more, this is already too high; but pivots add >=0, so prune.
                if val == 0:
                    # Can't prune all next values if current sum already too high.
                    if sum(chosen) >= best:
                        return
                else:
                    break
            backtrack(idx + 1, chosen + [val])

    if not free_cols:
        ok, total = eval_pivots([])
        return total if ok else 0

    backtrack(0, [])
    return best


def solution():
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_path) as f:
        lines = [line.strip() for line in f if line.strip()]

    total = 0
    for line in lines:
        targets, buttons = parse_line(line)
        total += min_presses_for_machine(targets, buttons)
    return total


if __name__ == "__main__":
    print(solution())

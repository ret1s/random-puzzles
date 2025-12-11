"""
Thanks in part to your analysis, the Elves have figured out a little bit about the issue. They now know that the problematic data path passes through both dac (a digital-to-analog converter) and fft (a device which performs a fast Fourier transform).

They're still not sure which specific path is the problem, and so they now need you to find every path from svr (the server rack) to out. However, the paths you find must all also visit both dac and fft (in any order).

For example:

svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
This new list of devices contains many paths from svr to out:

svr,aaa,fft,ccc,ddd,hub,fff,ggg,out
svr,aaa,fft,ccc,ddd,hub,fff,hhh,out
svr,aaa,fft,ccc,eee,dac,fff,ggg,out
svr,aaa,fft,ccc,eee,dac,fff,hhh,out
svr,bbb,tty,ccc,ddd,hub,fff,ggg,out
svr,bbb,tty,ccc,ddd,hub,fff,hhh,out
svr,bbb,tty,ccc,eee,dac,fff,ggg,out
svr,bbb,tty,ccc,eee,dac,fff,hhh,out
However, only 2 paths from svr to out visit both dac and fft.

Find all of the paths that lead from svr to out. How many of those paths visit both dac and fft?


"""

import os
from typing import Dict, List, Tuple


def solution():
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_path) as f:
        lines = [line.strip() for line in f if line.strip()]

    graph: Dict[str, List[str]] = {}
    for line in lines:
        name, rhs = line.split(":")
        name = name.strip()
        targets = rhs.strip().split()
        graph[name] = targets

    REQUIRED = ("dac", "fft")
    memo: Dict[Tuple[str, bool, bool], int] = {}

    def dfs(node: str, seen_dac: bool, seen_fft: bool) -> int:
        if node == "out":
            return int(seen_dac and seen_fft)
        key = (node, seen_dac, seen_fft)
        if key in memo:
            return memo[key]
        nd = seen_dac or node == "dac"
        nf = seen_fft or node == "fft"
        total = 0
        for nxt in graph.get(node, []):
            total += dfs(nxt, nd, nf)
        memo[key] = total
        return total

    return dfs("svr", False, False)


if __name__ == "__main__":
    print(solution())

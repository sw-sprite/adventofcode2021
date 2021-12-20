import sys
import heapq
import itertools
import re
import ast
from collections import defaultdict, Counter, deque

with open("input.txt") as f:
# with open("input_example.txt") as f:
    lines = f.read()

lines = lines.split('\n\n')
alg = ["1" if x == '#' else "0" for x in lines[0]]
assert len(alg) == 512

lit = set()

for i, arr in enumerate(lines[1:][0].split('\n')):
    for j, v in enumerate(arr.strip()):
        if v == "#":
            lit.add((i,j))

def step(lit, on):
    lit2 = set()
    rlo = min([r for r,c in lit])
    rhi = max([r for r,c in lit])
    clo = min([c for r,c in lit])
    chi = max([c for r,c in lit])

    for r in range(rlo-5, rhi+5):
        for c in range(rlo-5, chi+5):
            rc_str = ""
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    if ((r+dr, c+dc) in lit) == on:
                        rc_str += "1"
                    else:
                        rc_str += "0"
            assert 0 <= int(rc_str,2) <= 512
            if (alg[int(rc_str,2)] == "1") != on:
                lit2.add((r,c))
    return lit2

for t in range(50):
  if t==2:
    print(len(lit))
  lit = step(lit, t%2==0)
print(len(lit))
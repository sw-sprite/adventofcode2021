import collections 
import string
import re
import math    
import functools
import sys  

with open("input.txt") as f:
# with open("input_sample.txt") as f:
    lines = f.read().strip().split('\n')

# print(lines[0:18])

a = []
b = []
c = []
instrucs = []
for i in range(14):
    instrucs.append(lines[i*18:(i+1)*18])

for i in instrucs:
    # print(i)
    a.append(int(i[4].split()[2]))
    b.append(int(i[5].split()[2]))
    c.append(int(i[15].split()[2]))

# print(a, b, c)
assert(len(a) == len(b) == len(c) == 14)

temp_vars = collections.defaultdict(int)

def run(i, z, w):
    x = b[i] + (z % 26)
    z = z // a[i]
    if x != w:
        z *= 26
        z += w + c[i]
    return z

def monad(num_list):
    z = 0
    for i in range(14):
        z = run(i, num_list[i], z)
    return z == 0

# count number of 26s in a before each digit
Zbudget = [26**len([x for x in range(len(a)) if a[x]==26 and x >= i]) for i in range(len(a))]
print("Threshold for giving up due to Z being too high, at each stage has been calculated as", Zbudget)
# for i in range(len(a)):
#     print([x for x in range(len(a)) if a[x]==26 and x >= i])
# exit()
@functools.lru_cache(maxsize=None)
def solve(index, z):
    if index == 14:
        if z == 0:
            return ['']
        return []
    if z > Zbudget[index]:
        return []
    calc_x = b[index] + (z % 26)
    poss_w = list(range(1,10))

    # if x after calculation is not w then z grows
    if calc_x in range(1,10):
        poss_w = [calc_x]
    
    ret = []
    for w in poss_w:
        z_next_digit = run(index, z, w)
        next_digits = solve(index+1, z_next_digit)
        for x in next_digits:
            ret.append(str(w) + x)
    
    # print(index, z, ret)
    return ret

ans = solve(0,0)
ans = [int(x) for x in ans]
print(ans)
print("num solutions", len(ans))
print(max(ans), min(ans))
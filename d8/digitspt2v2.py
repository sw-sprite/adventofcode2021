from itertools import *
with open("input.txt") as f:
    lines = f.read()
lines = lines.split("\n")[:-1]
t = 0

for k in lines:
    a, b = k.split(" | ")
    do = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
    req = set(do)
    for x in permutations("abcdefg"):
        m = {i: j for i, j in zip(x, "abcdefg")}
        r = {"".join(sorted(map(m.get, q))) for q in a.split()}
        # print(req)
        print(r)
        if r == req:
            b = ["".join(sorted(map(m.get, q))) for q in b.split()]
            print(b)
            b = "".join(str(do.index(q)) for q in b)
            print(b)
            # print(x)
            # print(type(m))
            # print(r)
            # print(req)
            exit()
            t += int(b)

print(t)
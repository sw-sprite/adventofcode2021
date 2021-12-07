import math

with open("input.txt") as f:
    lines = f.read()

lines = lines.split(",")
lines = [int(x) for x in lines]

minx = min(lines)
maxx = max(lines)

def f(n):
    return (n * (n + 1)) // 2

ans = 1e9
for i in range(minx, maxx+1):
    ans = min(ans, sum(f(abs(x-i)) for x in lines))

print(ans)
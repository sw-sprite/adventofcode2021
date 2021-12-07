import math

with open("input.txt") as f:
    lines = f.read()

lines = lines.split(",")
lines = [int(x) for x in lines]

lines.sort()
mid = lines[len(lines) // 2]

fuel = 0
for x in lines:
    fuel += abs(x - mid)

print(fuel)
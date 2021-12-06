import re
from collections import deque

with open("input.txt") as f:
    lines = f.read()

# def reproduce_at_index(index, arr):
#     arr[index] = 6
#     arr.append(8)
#     return arr

lines = re.split("[, \n]", lines)
lines = list(filter(None, lines))
fish = [int(x) for x in lines]
# print(lines)

fish_count = deque([0]*9)
for i in fish:
    fish_count[i] += 1

print(fish_count)

days = 1
while days <= 256:
    fish_count.rotate(-1) 
    fish_count[6] += fish_count[8]
    days += 1
    # print(days)

print(sum(fish_count))
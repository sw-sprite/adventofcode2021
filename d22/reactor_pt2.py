import itertools
import collections 

with open("input.txt") as f:
# with open("input_sample.txt") as f:
# with open("input_sample2.txt") as f:
    lines = f.read()

def clip(base, clip):
    if base.stop <= clip.start or base.start >= clip.stop:
        return range(0)
    return range(max(base.start, clip.start), min(base.stop, clip.stop))

def count_uninterrupted(step, rest):
    _, xr, yr, zr = step

    conflicts = []

    for step in rest:
        state, xr2, yr2, zr2 = step

        xr2 = clip(xr2, xr)
        yr2 = clip(yr2, yr)
        zr2 = clip(zr2, zr)

        if len(xr2) == 0 or len(yr2) == 0 or len(zr2) == 0:
            continue

        conflicts.append((state, xr2, yr2, zr2))
    # print("--------------------")
    # print( step, rest)
    # print(conflicts)
    total = len(xr) * len(yr) * len(zr)
    # print("total is: ", total)
    for idx, step in enumerate(conflicts):
        total -= count_uninterrupted(step, conflicts[idx+1:])

    return total
steps = []

for i in lines.strip().split('\n'):
    on = True
    status, coords = i.split(' ')
    x, y, z = coords.split(',')
    if status == "off":
        on = False
    
    xs, xe = x.split('..')
    xs = xs[2:]
    ys, ye = y.split('..')
    ys = ys[2:]
    zs, ze = z.split('..')
    zs = zs[2:]
    
    steps.append((on, 
        range(int(xs), int(xe)+1), 
        range(int(ys), int(ye)+1), 
        range(int(zs), int(ze)+1)))

# print(steps)
total = 0

for i, v in enumerate(steps):
    if v[0] == False:
        continue
    # print("current step is: ", v)
    # print(v)
    total += count_uninterrupted(v, steps[i+1:])
print(total)

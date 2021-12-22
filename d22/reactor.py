import itertools
import collections 

# with open("input.txt") as f:
# with open("input_sample.txt") as f:
with open("input_sample2.txt") as f:
    lines = f.read()

ipt = []
on_set = set()

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
    
    tmp = itertools.product(range(int(xs), int(xe)+1), range(int(ys),int(ye)+1), range(int(zs),int(ze)+1))
    if on:
        on_set.update(tmp)
    else:
        on_set = set(on_set).difference(tmp)
    
    print(len(on_set))

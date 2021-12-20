import math 
import collections 
from functools import reduce
from itertools import permutations
with open("input.txt") as f:
# with open("input_sample.txt") as f:
    lines = f.read()

lines = lines.split("\n\n")
coord_remaps = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
coord_negations = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]
# print(lines)

# def orientation():
#     for i in range(8):
#         yield coord_negations[i]
def orientation():
    """Yields each of 8 possible orientations"""
    for i in range(8):
        yield (-1) ** (i % 2), (-1) ** ((i // 2) % 2), (-1) ** ((i // 4) % 2)

class Scanner:
    
    def __init__(self, num, pos=None):
        self.beacons = set()
        self.num = num
        self.pos = pos

    def add_beacons(self, ipt_list):
        ipt_list = ipt_list.split("\n")[1:]
        for i in ipt_list:
            x, y, z = i.split(",")
            self.beacons.add((int(x), int(y), int(z)))

    def compare(self, another):
        c = dict()
        for orient in orientation():
            # print(orient)
            for perm in permutations((0,1,2)):
                c[orient, perm] = collections.defaultdict(int)
                for a in self.beacons:
                    for b in another.beacons:
                        c[orient, perm][tuple(da+o*b[dp] for da, o, dp in zip(a, orient, perm))] += 1
        
                for k, v in c[orient, perm].items():
                    if v >= 12:
                        another.pos = k
                        # Reorient all beacons based on absolute position
                        another.reorient(orient, perm)
                        return another.pos
        # exit()

    def reorient(self, orient, perm):
        new_beacons = set()
        for b in self.beacons:
            new_b = tuple(self.pos[order] - o*b[p] for o, p, order in zip(orient, perm, (0,1,2)))
            new_beacons.add(new_b)
        self.beacons = new_beacons
    
    def __str__(self):
        return '--- scanner ' + str(self.num) + ' ---\nPosition: ' \
               + str(self.pos) + '\n' + '\n'.join(str(b) for b in self.beacons)

    def __repr__(self):
        return str(self)

def manhattan(a, b):
    return sum(abs(da - db) for da, db in zip(a, b))
# actural driver code below
scanners = []
for i, line in enumerate(lines):
    scanners.append(Scanner(i))
    scanners[i].add_beacons(line)
    # print(scanners)

known = {0}
scanners[0].pos = (0,0,0)
while set(range(len(scanners))) - known != set():
    new = set()
    for k in known:
        for i in range(len(scanners)):
            if i in known:
                continue
            print("comparing ", k, " and ", i)
            if scanners[k].compare(scanners[i]):
                print("adding new scanner ", i)
                new.add(i)
    known |= new
    print("totall cleared: ", len(known))

# final_beacons = set.union(*(scan.beacons for scan in scanners))
final_beacons = reduce(set.union, (scan.beacons for scan in scanners))
print(len(final_beacons))
p = [scan.pos for scan in scanners]
m = 0

for i in p:
    for j in p:
        m = max(m, manhattan(i, j))

print(m) 
# print(scanners[0].find_matching(scanners[1]))
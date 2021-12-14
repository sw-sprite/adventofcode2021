from collections import defaultdict
import numpy as np
# with open("sample.txt") as f:
with open("input.txt") as f:
    lines = f.read()

lines = lines.split('\n')
lines = [i for i in lines if i]
# print(lines)

starter = []
templates = {}

for l in lines:
    if '-'  not in l:
        starter = l
    else:
        a, b = l.split(' -> ')
        templates[a] = b

# print(starter, templates)

def forward_one(current_pairs):
    global templates
    new_pairs = defaultdict(lambda:0)
    for key, count in current_pairs.items():
        center = templates[key]
        new_pairs[key[0]+center] += count
        new_pairs[center+key[1]] += count
    return new_pairs 

def count_freq(current_pairs):
    counts = defaultdict(lambda:0)
    for key,count in current_pairs.items():
        counts[key[0]]+=count
        counts[key[1]]+=count

    for key in counts.keys():
        counts[key]=np.ceil(counts[key]/2)
    return counts


steps = 40
current_pairs = defaultdict(lambda:0)
for i in range(0,len(starter)-1):
    current_pairs[starter[i:i+2]]+=1

for s in range(steps):
    current_pairs=forward_one(current_pairs)
    # counts=get_counts(current_pairs)
counts = count_freq(current_pairs)
max_val=-1
min_val=10**20
for i,j in counts.items():
    max_val=max(max_val,j)
    min_val=min(min_val,j)

print(int(max_val-min_val))

# for s in range(steps):
#     # cur_line = starter.copy()
#     new_line = ""
#     for i in range(0, len(starter)-1, 1):
#             a,b = starter[i:i+2]
#             c = ''.join(starter[i:i+2])
#             # print(c in templates)
#             if c in templates:
#                 new_line += a + templates[c]
#             else:
#                 new_line += a
            
#             if i+2 == len(starter):
#                 new_line += b
#             # print(curKey)
#     print(s, len(new_line))
#     starter = list(new_line)

# counter = collections.Counter(starter).most_common()
# print(counter)
# diff_letter = counter[0][1] - counter[-1][1]
# print(counter[0])
# print(diff_letter)


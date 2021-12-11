import itertools
with open("input.txt") as f:
    lines = f.read()

lines = [list(map(int, c)) for c in lines.split()]
total_flash = 0
# print(lines)
# exit()
def update_cycle(arr, i,j, updated):
    global total_flash
    if (i,j) not in updated:
        if arr[i][j] == 9:
            total_flash = 0
            updated.add((i,j))
            arr = flash(arr, get_adj(i,j), updated)
            return arr
        else:
            arr[i][j] += 1
            return arr

def flash(arr, index_arr, updated):
    global total_flash
    
    # print("start is: ")
    # for l in index_arr:
        # print(arr[l[0]][l[1]])
    for l in index_arr:
        # print(l, arr[l[0]][l[1]])
        if (l[0], l[1]) not in updated:
            if arr[l[0]][l[1]] == 9:
                arr[l[0]][l[1]] = 0
                updated.add((l[0],l[1]))
                total_flash += 1
                arr = flash(arr, get_adj(l[0],l[1]), updated)
            else:
                arr[l[0]][l[1]] += 1
                # updated.add((l[0],l[1]))
    # print("end is: ")
    # for l in index_arr:
    #     print(arr[l[0]][l[1]])
    # print("current total flash is: ", total_flash)
    # exit()
    return arr

def get_adj(i, j):
    pos = []
    left = right = up = down = 0
    # get up
    if (i-1) < 0:
        up = i
    else:
        up = i-1
    # get down val
    if (i+1) >= len(lines):
        down = i
    else:
        down = i+1
    # get left
    if (j-1) < 0:
        left = j
    else:
        left = j-1
    # get right
    if (j+1) >= len(lines[i]):
        right = j
    else:
        right = j+1
    
    # print(i, j, left, right, up, down)
    all_x = all_y = set()
    all_x.add(left)
    all_x.add(j)
    all_x.add(right)
    all_y.add(up)
    all_y.add(j)
    all_y.add(down)
    # print(list(itertools.product(all_x, all_y)))
    return list(itertools.product(all_x, all_y))

def day1_loop(lines, updated):
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            lines = update_cycle(lines, i, j, updated)
    return lines

n, m = len(lines), len(lines[0])
for _ in range(100):
#     # print("loop: ", cycle)
#     # print(len(lines[0]))
    updated = set()
    # print(lines)
    # for i in range(len(lines)):
    #     print(len(lines[0]))
    #     for j in range(len(lines[0])):
    #         lines = update_cycle(lines, i, j, updated)
    lines = day1_loop(lines, updated)
print(lines)
print(total_flash)
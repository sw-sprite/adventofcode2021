
with open("input.txt") as f:
# with open("input_sample.txt") as f:
    lines = f.read().strip().split('\n')

h = len(lines)
w = len(lines[0])
east_list = set()
south_list = set()

for i, v in enumerate(lines):
    for j, vv in enumerate(v):
        if vv == ".":
            continue
        elif vv == ">":
            east_list.add((i,j))
        elif vv == "v":
            south_list.add((i,j))

def move():
    return move_east() + move_south()

# east move first, then north
def move_east():
    global east_list, south_list
    count = 0
    new_east_list = set()
    for i in east_list:
        new_loc = (i[0], (i[1]+1)%w)
        if new_loc not in east_list and new_loc not in south_list:
            new_east_list.add(new_loc)
            count += 1
        else:
            new_east_list.add(i)
    east_list = new_east_list
    return count

def move_south():
    global east_list, south_list
    # print(east_list)
    count = 0
    new_south_list = set()
    for i in south_list:
        new_loc = ((i[0]+1)%h, i[1])
        # print(new_loc)
        if new_loc not in south_list and new_loc not in east_list:
            # print("not blocked")
            new_south_list.add(new_loc)
            count += 1
        else:
            # print("blocked")
            new_south_list.add(i)
            # print(new_south_list)
    south_list = new_south_list
    return count

def print_map():
    global east_list, south_list
    for i in range(h):
        for j in range(w):
            if (i,j) in east_list:
                print('>', end='')
            elif (i,j) in south_list:
                print('v', end='')
            else:
                print('.', end='')
        print()



# print_map()
count = 1
# for i in range(55):
while True:
    # print(count)
    # print("-----------------")
    if move() == 0:
        print(count)
        # print_map()
        break
    count += 1
    # print_map()
    # print(east_list)
    # print(south_list)


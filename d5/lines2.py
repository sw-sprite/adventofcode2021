with open("input.txt") as f:
    lines = f.read()

lines = lines.split()
lines = [x.split(',') for x in lines]

points = {}
count = 0

def add_or_sub_one(num):
    if num > 0:
        return num+1
    elif num < 0:
        return num-1
    else:
        return 0
def add_point(x, y):
    global count, points
    if (x, y) in points:
        # print("found point")
        points[(x, y)] += 1
        if points[(x, y)] == 2:
            count += 1
    else: 
        # print("adding new point", x1, starting + s)
        points[(x, y)] = 1
    return count

# get x1, y1, x2, y2 from the list
for i in range(len(lines)//3):

    x1 = int(lines[3*i][0])
    y1 = int(lines[3*i][1])
    x2 = int(lines[3*i+2][0])
    y2 = int(lines[3*i+2][1])

    # if x1 != x2 and y1 != y2:
    #     continue

    # print(x1, y1, x2, y2)

    if x1 == x2:
        distance = abs(y1-y2) + 1
        starting = min(y1, y2)
        # print(distance, starting, ending)
        for s in range(distance):
            add_point(x1, starting + s)
    elif y1 == y2:
        distance = abs(x1-x2) + 1
        starting = min(x1, x2)
        # print(distance, starting, ending)
        for s in range(distance):
            add_point(starting + s, y1)
    else:
        x_distance = add_or_sub_one(x1-x2)
        x_starting = min(x1, x2)
        y_distance = add_or_sub_one(y1-y2)
        y_min = min(y1, y2)
        y_max = max(y1, y2)

        print(x1, y1, x2, y2, x_distance, y_distance)
        # nagative slope, x increase, y decrease
        if x_distance + y_distance == 0: 
            for s in range(abs(x_distance)):
                add_point(x_starting+s, y_max-s)
        else:
            for s in range(abs(x_distance)):
                add_point(x_starting+s, y_min+s)




    # exit()


print(count)
with open("input.txt") as f:
    lines = f.read()

lines = lines.split()
lines = [x.split(',') for x in lines]

points = {}
count = 0
# get x1, y1, x2, y2 from the list
for i in range(len(lines)//3):

    x1 = int(lines[3*i][0])
    y1 = int(lines[3*i][1])
    x2 = int(lines[3*i+2][0])
    y2 = int(lines[3*i+2][1])

    if x1 != x2 and y1 != y2:
        continue

    print(x1, y1, x2, y2)

    if x1 == x2:
        distance = abs(y1-y2) + 1
        starting = min(y1, y2)
        ending = max(y1, y2)
        # print(distance, starting, ending)
        for s in range(distance):
            if (x1, starting + s) in points:
                # print("found point")
                points[(x1, starting + s)] += 1
                if points[(x1, starting + s)] == 2:
                    count += 1
            else: 
                # print("adding new point", x1, starting + s)
                points[(x1, starting + s)] = 1
    elif y1 == y2:
        distance = abs(x1-x2) + 1
        starting = min(x1, x2)
        ending = max(x1, x2)
        # print(distance, starting, ending)
        for s in range(distance):
            if (starting + s, y1) in points:
                points[(starting + s, y1)] += 1
                if points[(starting + s, y1)] == 2:
                    count += 1
            else: 
                points[(starting + s, y1)] = 1
    # exit()


print(count)
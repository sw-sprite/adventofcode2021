with open("input.txt") as f:
    lines = f.read()

lines = lines.split('\n')
lines = [i for i in lines if i]
# print(lines)

dots = set()
folds = []

for l in lines:
    if l[0] == 'f':
        temp = l.split()
        direction, num = temp[2].split('=')
        folds.append((direction, int(num)))
    else: 
        x, y = l.split(',')
        dots.add((int(x),int(y)))

# print(dots)
# print(folds)

# handles fold y
def fold_up(points, line):
    arr = set()
    for i in points:
        if i[1] < line:
            arr.add(i)
        else:
            temp = line - abs(i[1] - line)
            arr.add((i[0], temp))
    return arr

# handles fold x
def fold_left(points, line):
    arr = set()
    for i in points:
        if i[0] < line:
            arr.add(i)
        else:
            temp = line - abs(i[0] - line)
            arr.add((temp, i[1]))
    return arr

for f in folds:
    if f[0] == 'x':
        dots = fold_left(dots, f[1])
    else:
        dots = fold_up(dots, f[1])
        # print(len(dots))
        # exit()

for y in range(6):
    print(''.join('■' if (x,y) in dots else ' ' for x in range(39)))
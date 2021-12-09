with open("input.txt") as f:
    lines = f.read()

lines = lines.split()
# print(lines)

max_height = len(lines)
max_width = len(lines[0])

sum = 0
for i in range(len(lines)):
    # print(list(lines[i]))
    for j in range( len(list(lines[i])) ):
        left = right = up = down = 0
        # get up val
        if (i-1) < 0:
            up = 9999
            print("here")
        else:
            up = int(lines[i-1][j])
        # get down val
        if (i+1) >= len(lines):
            down = 9999
        else:
            down = int(lines[i+1][j])

        # get left
        if (j-1) < 0:
            left = 9999
        else:
            left = int(lines[i][j-1])
        # get right
        if (j+1) >= len(lines[i]):
            right = 9999
        else:
            right = int(lines[i][j+1])
        if int(lines[i][j]) < up and int(lines[i][j]) < right and int(lines[i][j]) < left and int(lines[i][j]) < down:
            sum += int(lines[i][j]) + 1
        # print("index: ", i, j)
        # print(lines[i][j], up, down, left, right)
        # print(sum)
        # exit()

print(sum)
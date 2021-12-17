with open("input.txt") as f:
    lines = f.read()
lines = lines.split()
# print(lines)

x = lines[2].split()
y = lines[3].split()
x_min, x_max = int(x[0].split('..')[0].split('=')[1]), int(x[0].split('..')[1].split(',')[0])
y_min, y_max = int(y[0].split('..')[0].split('=')[1]), int(y[0].split('..')[1].split(',')[0])
# print(x_min, x_max)
# print(y_min, y_max)
# print()

def one_sec(cur_pos, cur_velocity):
    cur_pos[0] += cur_velocity[0]
    cur_pos[1] += cur_velocity[1]


    if cur_velocity[0] < 0:
        cur_velocity[0] += 1
    elif cur_velocity[0] > 0:
        cur_velocity[0] -= 1

    cur_velocity[1] -= 1
    
    return cur_pos, cur_velocity

# def find_x(x_range):
#     for i in range()


# print(one_sec([0,0], [7,2]))
ans_pt1 = 0
ans_pt2 = 0
for i in range(100):
    for j in range(-200, 1500):
        pos = [0,0]
        vel = [i, j]
        max_y = 0

        while pos[0] < x_max and pos[1] >= y_min:
            pos, vel = one_sec(pos, vel)
            # print(pos, vel)
            if pos[1] > max_y:
                max_y = pos[1]
            if pos[0] >= x_min and pos[0] <= x_max and pos[1] >= y_min and pos[1] <= y_max:
                
                ans_pt2 += 1
                if ans_pt1 < max_y:
                    ans_pt1 = max_y
                break
            if vel[0] == 0 and pos[0] < x_min:
                break

print(ans_pt1)
print(ans_pt2)
with open('input.txt') as f:
    lines = f.readlines()


# print(lines)
initx = inity = aim = 0

for x in lines:
    command, depth = x[:-1].split()
    print(command, depth)

    if command == "forward":
        initx += int(depth)
        inity += int(depth)*aim
    elif command == "down":
        aim += int(depth)
    elif command == "up":
        aim -= int(depth)

print(initx*inity)
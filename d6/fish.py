import re

with open("input.txt") as f:
    lines = f.read()

# def reproduce_at_index(index, arr):
#     arr[index] = 6
#     arr.append(8)
#     return arr

lines = re.split("[, \n]", lines)
lines = list(filter(None, lines))
fish = [int(x) for x in lines]
# print(lines)


days = 1
while days <= 256:
    temp_fish = fish
    for index in range(len(temp_fish)):
        if temp_fish[index] > 0:
            fish[index] -= 1
        else:
            fish[index] = 6
            fish.append(8)
    days += 1
    print("(", days,",",len(fish), ")")

print("(", days,len(fish), ")")
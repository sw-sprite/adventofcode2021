from typing import Counter


with open("input.txt") as f:
    lines = f.readlines()

# print(lines)

b_length = len(lines[0][:-1])

count_arr = [0] * b_length
input_size = len(lines)
print(count_arr)

for x in lines:
    current = x[:-1]
    for y in range(b_length):
        # counting 0s
        if x[y] == "0":
            count_arr[y] += 1

for x in range(b_length):
    if count_arr[x] > (input_size - count_arr[x]):
        gamme_b += "0"
        epsilon_b += "1"
    else:
        gamme_b += "1"
        epsilon_b += "0"


ans = int(gamme_b, 2) * int(epsilon_b, 2)
print(ans)

from typing import Counter


with open("input.txt") as f:
    lines = f.readlines()

# print(lines)

b_length = len(lines[0][:-1])

# oxy find most, if eql use 1, co2 is opposite, most/least changes as array change
# eg: if pos 5 most common could be 1 in first loop, then 0 second loop
oxy_td_arr = lines
co2_td_arr = lines

# findning most/least common in the array at given index
# need this bc array size change during run time
def fmc(i, arr):
    zero = one = 0
    for x in arr:
        if int(x[i]) == 0: zero += 1 
        else: one += 1
    return 1 if one >= zero else 0
def flc(i, arr):
    zero = one = 0
    for x in arr:
        if int(x[i]) == 0: zero += 1 
        else: one += 1
    return 0 if one >= zero else 1
def remove_mismatch(reference, index, data_list):
    if len(data_list) > 1:
        new_data_list = [i for i in data_list if int(i[index]) == reference]
        return new_data_list
    else:
        return data_list

# have to determine when the sample size cut down to 1, build 2d array with each step
for x in range(b_length):
    oxy_td_arr = remove_mismatch(fmc(x, oxy_td_arr), x, oxy_td_arr)
    co2_td_arr = remove_mismatch(flc(x, co2_td_arr), x, co2_td_arr)

print(int(co2_td_arr[0], 2) * int(oxy_td_arr[0], 2))

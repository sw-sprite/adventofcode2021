

with open('input.txt') as f:
    lines = f.readlines()

# print(lines)

sum3 = sum2 = sum1 = 0
count = 0

for idx, val in enumerate(lines):
    curVal = int(val[:-1])
    if idx <= 2:
        if idx == 0:
            sum3 += curVal
        elif idx == 1:
            sum3 += curVal
            sum2 += curVal
        elif idx == 2:
            sum3 += curVal
            sum2 += curVal
            sum1 += curVal
        continue

    if sum2 + curVal > sum3:
        count += 1
    
    # discard the complete sum
    sum3 = sum2 + curVal
    sum2 = sum1 + curVal
    sum1 = curVal

    # print(curVal)
    # print(sum3, sum2, sum1)


print(count)
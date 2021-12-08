with open("input.txt") as f:
    lines = f.read()

lines = lines.split("\n")[:-1]

# a is the set, b is the target
def contain_all_letter(a, b):
    return all(i in b for i in a)

def sort_digits(str):
    return ''.join(sorted(str))

sum = 0
for x in lines:
    input, output = x.split("|", 1)
    # build the digit look up here then invert it and use it for the output
    digits = {1 : "", 2 : "", 3 : "", 4 : "", 5 : "", 6 : "", 7 : "", 8 : "", 9 : "", 0 : ""}
    for num in input.split(" "):
        if len(num) == 2:
            digits[1] = num
        elif len(num) == 4:
            digits[4] = num
        elif len(num) == 3:
            digits[7] = num
        elif len(num) == 7:
            digits[8] = num

    four_minus_one = digits[4]
    for i in digits[1]:
        four_minus_one = four_minus_one.replace(i, "")
    print(four_minus_one)

    for num in input.split(" "):
        if len(num) == 5:
            if contain_all_letter(digits[1], num):
                digits[3] = num
            elif contain_all_letter(four_minus_one, num):
                digits[5] = num
            else:
                digits[2] = num
        if len(num) == 6:
            if contain_all_letter(digits[4], num):
                digits[9] = num
            elif contain_all_letter(digits[1], num) and not contain_all_letter(digits[4], num):
                digits[0] = num
            else:
                digits[6] = num

    for i in digits:
        digits[i] = sort_digits(digits[i])
    digits_inverted = {value: key for key, value in digits.items()}
    print(digits)
    print(digits_inverted)
    cur_num = ""
    for num in output.split():
        cur_num = cur_num + str(digits_inverted[sort_digits(num)])
    
    sum += int(cur_num)
print(sum)
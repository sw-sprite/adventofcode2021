import collections 
import string
import re
import math      

with open("input.txt") as f:
# with open("input_sample.txt") as f:
    lines = f.read().strip().split('\n')
# print(lines)

def non_zero_next_largest(num):
    if len(str(num)) != 14:
        print("wrong int length")
        exit()
    
    while True:
        num -= 1
        if '0' in str(num):
            continue
        else:
            return num

def is_integer_only(sample_str):
    ''' Returns True if given string contains a
        positive or negative integer only  '''
    result = re.match("[-+]?\d+$", sample_str)
    return result

def alu_add(a, b):
    return a+b

def alu_mul(a, b):
    # print(type(a), type(b))
    # print("a is: ", a, "b is: ", b, "result is: ", a*b)
    return a*b

def alu_div(a, b):
    if b > 0:
        return int(math.floor(a/b))
    else:
        return a

def alu_mod(a, b):
    if a <0 or b <= 0:
        return a 
    else:
        return a%b 

def alu_eql(a,b):
    # print(type(a), type(b))
    # print("a is: ", a, "b is: ", b, "result is: ", a==b)
    return 1 if a == b else 0

def monad(ipt, num_list):
    # print(num_list)
    cur_index = 0
    temp_vars = collections.defaultdict(int)
    for i in ipt:
        instru = i.split(' ')
        print("---------------")
        print(instru)
        print(temp_vars)
        if instru[0] == 'inp':
            temp_vars[instru[1]] = num_list[cur_index]
            cur_index += 1
        elif instru[0] == 'add':
            if is_integer_only(instru[2]):
                temp_vars[instru[1]] = alu_add(temp_vars[instru[1]], int(instru[2]))
            else:
                temp_vars[instru[1]] = alu_add(temp_vars[instru[1]], temp_vars[instru[2]])
        elif instru[0] == 'mul':
            if is_integer_only(instru[2]):
                temp_vars[instru[1]] = alu_mul(temp_vars[instru[1]], int(instru[2]))
            else:
                # print("second letter is not number")
                temp_vars[instru[1]] = alu_mul(temp_vars[instru[1]], temp_vars[instru[2]])
        elif instru[0] == 'div':
            if is_integer_only(instru[2]):
                temp_vars[instru[1]] = alu_div(temp_vars[instru[1]], int(instru[2]))
            else:
                temp_vars[instru[1]] = alu_div(temp_vars[instru[1]], temp_vars[instru[2]])
        elif instru[0] == 'mod':
            if is_integer_only(instru[2]):
                temp_vars[instru[1]] = alu_mod(temp_vars[instru[1]], int(instru[2]))
            else:
                temp_vars[instru[1]] = alu_mod(temp_vars[instru[1]], temp_vars[instru[2]])
        elif instru[0] == 'eql':
            if is_integer_only(instru[2]):
                temp_vars[instru[1]] = alu_eql(temp_vars[instru[1]], int(instru[2]))
            else:
                temp_vars[instru[1]] = alu_eql(temp_vars[instru[1]], temp_vars[instru[2]])
        print(temp_vars)
    
    return temp_vars['z'] == 0

# cur_largest_str = '9'*14
cur_largest_str = '13579246899999'
cur_tmp = int(cur_largest_str)
cur_largest = cur_tmp
cur_largest_list = [int(x) for x in str(cur_largest)]

tmp = monad(lines, cur_largest_list)
exit()

while True:
    tmp = monad(lines, cur_largest_list)
    print(tmp, cur_largest)
    if tmp:
        print(cur_largest)
        exit()
    else:
        cur_largest = non_zero_next_largest(cur_largest)
        cur_largest_list = [int(x) for x in str(cur_largest)]


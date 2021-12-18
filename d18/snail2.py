import collections 
with open("input.txt") as f:
# with open("input_example.txt") as f:
    lines = f.read()

lines = lines.strip().split('\n')
# print(lines)

# helper functions
def pair_addition(a, b):
    return ["["] + a + [","] + b + ["]"]
def isdigit(k):
    return isinstance(k,int)
def convert_to_list(a):
    return [int(s) if s.isdigit() else s for s in a.rstrip()]
def convert_to_str(a):
    return ''.join(str(t) for t in a)
def pair_index(a):
    # add left bracket to set, find matching right bracket
    bracket_set = collections.defaultdict(None)
    index = 0
    index_stack = []
    while True:
        # print(index, a[index])  
        if a[index] == '[':
            index_stack.append(index)
        elif a[index] == ',' or a[index].isdigit():
            index += 1
            continue
        elif a[index] == ']':
            temp = index_stack.pop()
            bracket_set[temp] = index
        index += 1
        if index == len(a):
            break
    # for k, v in bracket_set.iteritems():
    return bracket_set

# calc functions


def explode(a, i):
    # check for 4 pairs
    # bracket_indexes = pair_index(a)
    left_num = a[i+1]
    right_num = a[i+3]

    # search left
    for ii in range(i-1, -1, -1):
        if isdigit(a[ii]):
            # print("found left element, adding:", a[ii], " to ", left_num)     
            a[ii] += left_num
            break
    # search right
    for ii in range(i+5, len(a)):
        if isdigit(a[ii]):
            # print("found right element, adding:", a[ii], " to ", left_num)    
            a[ii] += right_num
            break
    # closing explode, removing pair
    a = a[:i] + [0] + a[i+5:]
    return a

def split(a, i):
    val = a[i]
    return a[:i] + ["[", val//2, ",", (val+1)//2, "]"] + a[i+1:]

def scan(a):
    changed = True
    while changed:
        changed = False
        depth = 0
        # check for explode
        for i, c in enumerate(a):
            if c == "[":
                depth += 1
                if depth == 5:
                    # print("found explode condition:")
                    a = explode(a, i)
                    # print(convert_to_str(a))
                    # because explode condition met and operation complete, we need to check for explode again
                    changed = True
                    break
            elif c == ']':
                depth -= 1
        if changed:
            continue
        # check for split
        for i,c in enumerate(a):
            if isdigit(c) and c >= 10:
                a = split(a, i)
                # back to check for explode
                changed = True
                break
    return a

def magnitude(a):
    while len(a) > 1:
        for i in range(len(a)):
            if isdigit(a[i]) and isdigit(a[i+2]):
                a = a[:i-1] + [a[i]*3 + a[i+2]*2] + a[i+4:]
                break
    return a[0] 

# explode_example = "[7,[6,[5,[4,[3,2]]]]]\n[[6,[5,[4,[3,2]]]],1]\n[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]\n[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
# print(pair_addition("[1,2]", "[[3,4],5]"))
# print(scan(convert_to_list("[7,[6,[5,[4,[3,2]]]]]")))
lines = [convert_to_list(i) for i in lines]

max_val = 0
for a in lines:
    for b in lines:
        if a == b:
            continue
        val = magnitude(scan(pair_addition(a,b)))
        if val > max_val:
            max_val = val
print(max_val) 
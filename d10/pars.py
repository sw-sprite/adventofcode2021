with open("input.txt") as f:
    lines = f.read()

lines = lines.split()
# print(lines)
open = ["(", "[", "{", "<"]
close = [")", "]", "}", ">"]
match = dict({"(":")", "[":"]", "{":"}", "<":">"})
table = dict({")" : 3, "]" : 57, "}":1197, ">":25137})

score = 0
for i in lines:
    stack = []
    for j in i:
        if j  in open:
            stack.append(j)
        else:
            cur = stack.pop()
            if match[cur] != j:
                score += table[j]
                break

print(score)
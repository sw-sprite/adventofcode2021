with open("input.txt") as f:
    lines = f.read()

lines = lines.split()
# print(lines)
open = ["(", "[", "{", "<"]
close = [")", "]", "}", ">"]
match = dict({"(":")", "[":"]", "{":"}", "<":">"})
# rev_match = dict({"(":")", "[":"]", "{":"}", "<":">"})
table = dict({")" : 1, "]" : 2, "}":3, ">":4})

scores = []
for i in lines:
    stack = []
    for j in i:
        if j in open:
            stack.append(j)
        else:
            cur = stack.pop()
            if match[cur] != j:
                stack = []
                break
    # print(stack)
    if len(stack) > 0:
        # print("entered here")
        line_score = 0
        while len(stack) > 0:
            cur = stack.pop()
            # print("poped")
            line_score = line_score*5 + table[match[cur]]
        scores.append(line_score)

        
scores.sort()
print(len(scores))
print(scores[len(scores)//2])
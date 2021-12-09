with open("input.txt") as f:
    lines = f.read()

lines = lines.split()
# print(lines)

max_height = len(lines)
max_width = len(lines[0])

visited = set()

def dfs(graph, i, j, visited, size):
    if int(graph[i][j]) == 9:
        return True
    # keep track of visited and local size
    if (i, j) not in size:

        size.add((i,j))
    if (i, j) not in visited:
        visited.add((i,j))

    # recursive calls for up, down, left, right
    # up
    if (i-1) >= 0 and graph[i-1][j] > graph[i][j] and int(graph[i-1][j]) != 9:
        dfs(graph, i-1, j, visited, size)
    # down
    if (i+1) < len(lines) and graph[i+1][j] > graph[i][j] and int(graph[i+1][j]) != 9:
        dfs(graph, i+1, j, visited, size)
    # left
    if (j-1) >= 0 and graph[i][j-1] > graph[i][j] and int(graph[i][j-1]) != 9:
        # print("dfs left called")
        dfs(graph, i, j-1, visited, size)
    # get right
    if (j+1) < len(lines[i]) and graph[i][j+1] > graph[i][j] and int(graph[i][j+1]) != 9:
        dfs(graph, i, j+1, visited, size)

top_three = [0,0,0]
for i in range(len(lines)):
    # print(list(lines[i]))
    for j in range( len(list(lines[i])) ):
        left = right = up = down = 0
        # get up val
        if (i-1) < 0:
            up = 9999
        else:
            up = int(lines[i-1][j])
        # get down val
        if (i+1) >= len(lines):
            down = 9999
        else:
            down = int(lines[i+1][j])
        # get left
        if (j-1) < 0:
            left = 9999
        else:
            left = int(lines[i][j-1])
        # get right
        if (j+1) >= len(lines[i]):
            right = 9999
        else:
            right = int(lines[i][j+1])
        if int(lines[i][j]) < up and int(lines[i][j]) < right and int(lines[i][j]) < left and int(lines[i][j]) < down:
            if (i, j) not in visited:
                size = set([(i, j)])
                dfs(lines, i, j, visited, size)
                cur_basin_size = len(size)
                top_three.append(cur_basin_size)
                top_three.remove(min(top_three))
                # exit()


ans = 1
for i in top_three:
    ans =  ans*i
print(ans)
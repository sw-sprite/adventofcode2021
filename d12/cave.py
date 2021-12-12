import collections, string
with open("input.txt") as f:
    lines = f.read()

edges = collections.defaultdict(list)
lines = lines.split()

for i in lines:
    x, y = i.split("-")
    edges[x].append(y)
    edges[y].append(x)
print(edges)

def is_not_visited(node, cur_path):
    # print("checking:", node, cur_path)
    if node.isupper():
        return True
    else:
        if node == "start":
            return False
        have_two = False
        freq = {}

        for items in cur_path:
            freq[items] = cur_path.count(items)
        
        if not node in freq:
            return True

        for key, value in freq.items():
            if key.islower() and value > 1:
                have_two = True

        # lower case node, already in path
        # if two lower case node discovered
        # return false (not have_two)
        return not have_two
        # for i in range(len(cur_path)):
        #     if cur_path[i] == node:
        #         return False
    return True

def bfs(graph):

    allPath = []
    queue = collections.deque()
    path = []
    path.append("start")
    queue.append(path.copy())

    while queue:
        cur_path = queue.popleft()
        print("popping: ", cur_path)
        cur_node = cur_path[len(cur_path)-1]

        if (cur_node == "end"):
            allPath.append(cur_path)
            print("found:", cur_path)
            continue

        for i in range(len(graph[cur_node])):
            if is_not_visited(graph[cur_node][i], cur_path):
                new_path = cur_path.copy()
                new_path.append(graph[cur_node][i])
                queue.append(new_path)
    return len(allPath)

print(bfs(edges))




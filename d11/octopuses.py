import itertools
with open("input.txt") as f:
    lines = f.read()

lines = [list(map(int, c)) for c in lines.split()]
n, m = len(lines), len(lines[0])

def flash(i, j, updated):
    global lines
    lines[i][j] = 0
    updated.add((i,j))

    for di, dj in filter(any, itertools.product([-1, 0, 1], repeat=2)):
        ci, cj = i+di, j + dj
        if (0 <= ci < n and 0 <= cj < m and (ci, cj) not in updated):
            lines[ci][cj] += 1
            if lines[ci][cj] == 10:
                flash(ci, cj, updated)

def cycle():
    global lines, n, m 
    updated = set()
    for i in range(n):
        for j in range(m):
            if (i,j) not in updated:
                lines[i][j] += 1
                if lines[i][j] == 10:
                    flash(i, j, updated)
    return updated

# pt 1 
def pt1():
    global lines
    ans = 0
    for _ in range(100):
        # print(cycle())
        ans += len(cycle())
    print(ans)

def pt2():
    global lines, n,m 
    s = 0
    while True:
        s += 1
        flashed = cycle()
        if (len(flashed)) == n*m:
            return s


# pt1()
print(pt2())
# print(lines)
import heapq
with open("input.txt") as f:
    lines = f.read()

lines = [[int(y) for y in x] for x in lines.split()]

# print(lines[0])
row = len(lines)
col = len(lines[0])

# left, up, right, down
DR = [-1,0,1,0]
DC = [0,1,0,-1]

def dijkstras(multiple):
    global row, col, lines
    distance_grid = [[None for _ in range(multiple*col)] for _ in range(multiple*row)]
    pq = [(0,0,0)]

    while pq:
        (distance, x, y) = heapq.heappop(pq)
        if x<0 or x >= multiple*row or y < 0 or y >= multiple*col:
            continue
        val = lines[x%row][y%col] + (x//row) + (y//col)
        while val > 9:
            val -= 9
        real_cost = val + distance
        if distance_grid[x][y] is None or real_cost < distance_grid[x][y]:
            distance_grid[x][y] = real_cost
        else:
            continue
        print("checking:", x, y, val, distance_grid[x][y])
        
        if x == multiple*row-1 and y == multiple*col-1:
            break
        
        for i in range(4):
            new_x = x + DR[i]
            new_y = y + DC[i]
            heapq.heappush(pq, (distance_grid[x][y],new_x,new_y))
        print('\n'.join(map(''.join, distance_grid)))

    return distance_grid[multiple*row-1][multiple*col-1] - lines[0][0]

print(dijkstras(1))
print(dijkstras(5))

    
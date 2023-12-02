grid = []

with open('day8.txt') as f:
    for line in f:
        grid.append([int(x) for x in line.strip()])
        
trees = 0
edges = 0
size = len(grid)

def checkTrees(r, c): #r=row c=col
    down = up = left = right = False
    
    if grid[r - 1][c] < grid[r][c]:
        down = True
        for x in range(r - 1, -1, -1):
            if grid[x][c] >= grid[r][c]:
                down = False

    if grid[r][c - 1] < grid[r][c]:
        right = True
        for y in range(c - 1, -1, -1):
            if grid[r][y] >= grid[r][c]:
                right = False

    if grid[r][c + 1] < grid[r][c]:
        left = True
        for i in range(c + 1, len(grid[r])):
            if grid[r][i] >= grid[r][c]:
                left = False

    if grid[r + 1][c] < grid[r][c]:
        up = True
        for j in range(r + 1, size):
            if grid[j][c] >= grid[r][c]:
                up = False

    if down or up or left or right:
        return True

for x in range(size):
     for y in range(len(grid[x])):
        if x != 0 and y != 0 and x != (size - 1) and y != (len(grid[x]) - 1):
            if checkTrees(x, y):
                trees += 1
        else:
            edges += 1

print(trees + edges)
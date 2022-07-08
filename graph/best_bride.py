from collections import deque


def best_bridge(grid):
    # 1. find first island
    y_0, x_0 = find_land(grid) # initial location with land

    visited = set([(y_0, x_0)]) # set of visited places
    Q = [(y_0, x_0)] # stack to find all land connected to (y_0, x_0) (i.e. all land of the first island)
    queue = deque() # queue that will be used later to 'build the bride'
    while Q:
        y,x = Q.pop()
        if grid[y][x] == 'L':
            queue.append((y,x,0))
            visited.add((y,x))

        find_island(grid, y+1, x, Q, visited)
        find_island(grid, y-1, x, Q, visited)
        find_island(grid, y, x+1, Q, visited)
        find_island(grid, y, x-1, Q, visited)


    # 2. build bridge
    while queue:
        y, x, length  = queue.popleft()
        if length > 0 and grid[y][x] == 'L': # length > 0 is to ensure this is not the first island
            return length - 1

        build_bridge(grid, y+1, x, length, queue, visited)
        build_bridge(grid, y-1, x, length, queue, visited)
        build_bridge(grid, y, x+1, length, queue, visited)
        build_bridge(grid, y, x-1, length, queue, visited)



def find_land(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'L':
                return y, x


def find_island(grid, y, x, Q, visited):
    if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
        if (y,x) not in visited and grid[y][x] == 'L':
            Q.append((y,x))


def build_bridge(grid, y, x, length, queue, visited):
    if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
        if (y,x) not in visited:
            queue.append((y, x, length+1)) 
            visited.add((y,x))



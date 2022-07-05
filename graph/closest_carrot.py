from collections import deque

def closest_carrot(grid, y, x):
    visited = set()

    Q = deque([(y, x, 0)])
    visited.add((y,x))


    while Q:
        y, x, length = Q.popleft()

        if grid[y][x] == 'C':
            return length

        for move in [(1,0), (0,1), (-1,0), (0,-1)]:
            y_new = y + move[0]
            x_new = x + move[1]

            if not (0 <= y_new < len(grid) and 0 <= x_new < len(grid[0])):
                continue
            if grid[y_new][x_new] == 'X':
                continue

            if (y_new,x_new) not in visited:
                Q.append((y_new, x_new, length+1))
                visited.add((y_new, x_new))

    return -1

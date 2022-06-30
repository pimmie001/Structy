def count_paths(grid, x=0, y=0, memo={}):
    n = len(grid)
    m = len(grid[0])


    if x == m-1 and y == n-1:
        return 1

    if (x,y) in memo:
        return memo[(x,y)]


    total = 0
    if x < m-1 and grid[y][x+1] == 'O':
        total += count_paths(grid, x+1, y, memo)
    if y < n-1 and grid[y+1][x] == 'O':
        total += count_paths(grid, x, y+1, memo)
    
    memo[(x,y)] = total
    return total


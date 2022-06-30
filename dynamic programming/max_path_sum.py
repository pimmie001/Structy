def max_path_sum(grid, x=0, y=0, memo={}):
    n = len(grid)
    m = len(grid[0])

    if x == m-1 and y == n-1:
        return grid[y][x]

    if (x,y) in memo:
        return memo[(x,y)]
    
    
    max_sum = 0
    if x < m-1:
        max_sum = max(max_sum, max_path_sum(grid, x+1, y, memo))
    if y < n-1:
        max_sum = max(max_sum, max_path_sum(grid, x, y+1, memo))

    memo[(x,y)] = grid[y][x] + max_sum
    return grid[y][x] + max_sum


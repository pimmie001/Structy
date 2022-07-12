def string_search(grid, string):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if search(grid, string, y, x):
                return True
    return False


def search(grid, string, y, x, ind=0, memo={}):
    if ind == len(string): # objective achieved
        return True

    if not ( 0 <= y < len(grid) and 0 <= x < len(grid[0]) ): # out of grid
        return False

    if grid[y][x] != string[ind]: # wrong character
        return False


    key = (y, x, ind)
    if key in memo:
        return memo[key]


    char = grid[y][x]
    grid[y][x] = '*'

    for move in [(0,1), (1,0), (0,-1), (-1,0)]:
        dx, dy = move
        if search(grid, string, y+dy, x+dx, ind+1, memo):
            memo[key] = True
            return True

    grid[y][x] = char
    memo[key] = False
    return False


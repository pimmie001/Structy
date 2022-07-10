def breaking_boundaries(m, n, k, r, c, memo={}):
    # m rows, n columns
    if r < 0 or c < 0 or r >= m or c >= n: # if out of grid
        return 1
    
    if k == 0: # in grid but no moves left
        return 0

    key = (k, r, c)
    if key in memo:
        return memo[key]


    total = breaking_boundaries(m, n, k-1, r+1, c)
    total += breaking_boundaries(m, n, k-1, r-1, c)
    total += breaking_boundaries(m, n, k-1, r, c+1)
    total += breaking_boundaries(m, n, k-1, r, c-1)

    memo[key] = total
    return total

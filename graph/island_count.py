from connected_components_count import connected_components_count


def island_count(grid):
    edges = make_edges(grid)
    return connected_components_count(edges)



def make_edges(grid):
    edges = {}
    n = len(grid)
    m = len(grid[0])

    for y in range(n):
        for x in range(m):
            item = grid[y][x]
            if item == 'W':
                continue

            adjacent = []

            if y > 0:
                if grid[y-1][x] == 'L':
                    adjacent.append((x,y-1))
            if y < n-1:
                if grid[y+1][x] == 'L':
                    adjacent.append((x,y+1))
            if x > 0:
                if grid[y][x-1] == 'L':
                    adjacent.append((x-1,y))
            if x < m-1:
                if grid[y][x+1] == 'L':
                    adjacent.append((x+1,y))

            edges[(x,y)] = adjacent

    return edges


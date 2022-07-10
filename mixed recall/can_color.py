from collections import deque


def can_color(graph):
    # returns whether or not an undirected graph can be colored using 2 colors
    visited = set()
    visited_edges = set()
    for node in graph:
        if node not in visited:
            if violation(graph, node, visited, visited_edges):
                return False
    return True



def violation(graph, node, visited, visited_edges):
    colors = {} # color is either 0 or 1

    Q = deque([(node, 0)])
    while Q:
        current, current_color = Q.popleft()
        visited.add(current)

        if current in colors:
            if colors[current] != current_color: # check for violation
                return True
        else:
            colors[current] = current_color # color the current node

        for neighbor in graph[current]:
            if (current, neighbor) not in visited_edges:
                Q.append((neighbor, 1-current_color))
                visited_edges.add((current, neighbor))

    return False


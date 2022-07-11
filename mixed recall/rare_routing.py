from collections import deque


def rare_routing(n, roads):
    # time O(n^3)
    graph = make_graph(roads)
    for node in graph:
        if not rare_routing_node(n, node, graph):
            return False
    return True


def rare_routing_node(n, start_node, graph):
    Q = deque([(start_node, None)]) # (node, predecessor)
    visited = set()

    while Q:
        current, predecessor = Q.popleft()

        if current in visited:
            return False

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor != predecessor:
                Q.append((neighbor, current))

    return len(visited) == n 



def make_graph(roads):
    graph = {}
    for a,b in roads:
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
        if b in graph:
            graph[b].append(a)
        else:
            graph[b] = [a]
    return graph


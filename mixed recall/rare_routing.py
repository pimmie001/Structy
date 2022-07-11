def rare_routing(n, roads):
    # time O(n^2)
    graph = make_graph(roads)
    visited = set()
    valid = rare_routing_node(graph, 0, visited)
    return valid and len(visited) == n


def rare_routing_node(graph, node, visited, predecessor=None):
    if node in visited:
        return False

    visited.add(node)

    for neighbor in graph[node]:
        if neighbor != predecessor:
            if not rare_routing_node(graph, neighbor, visited, predecessor=node):
                return False

    return True


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

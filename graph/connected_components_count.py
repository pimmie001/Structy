def connected_components_count(graph):
    # returns the amount of connected components of a graph

    nodes = list(graph.keys())

    count = 0
    while nodes:
        count += 1
        for node in get_connected_components(graph, nodes[0]):
            if node in nodes:
                nodes.remove(node)

    return count



def get_connected_components(graph, node):
    stack = [node]
    components = []
    while stack:
        current = stack.pop()
        if current not in components:
            components.append(current)
            stack.extend(graph[current])
    return components


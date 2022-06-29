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



def get_connected_components(graph, node, components=[]):
    # returns an array of the components connected to a node

    if node not in components:
        components.append(node)
        for neighbor in graph[node]:
            components = get_connected_components(graph, neighbor, components)

    return components


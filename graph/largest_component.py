def largest_component(graph):
    # returns the size of the largest component in a graph

    nodes = list(graph.keys())
    largest = 0
    while nodes:
        components = get_connected_components(graph, nodes[0])

        if len(components) > largest:
            largest = len(components)

        for node in components:
            nodes.remove(node)

    return largest



def get_connected_components(graph, node):
    stack = [node]
    components = []
    while stack:
        current = stack.pop()
        if current not in components:
            components.append(current)
            stack.extend(graph[current])
    return components


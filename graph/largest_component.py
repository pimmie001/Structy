import numpy as np
from connected_components_count import get_connected_components


def largest_component(graph):
    # returns the size of the largest component in a graph

    nodes = list(graph.keys())
    largest = 0
    while nodes:
        components = get_connected_components(graph, nodes[0])
        print(nodes[0], components)
        # print(get_connected_components(graph, 4))

        sizes.append(len(components))

        for node in components:
            if node in nodes:
                nodes.remove(node)

    return np.max(sizes)



(largest_component({
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1]
})) # -> 4













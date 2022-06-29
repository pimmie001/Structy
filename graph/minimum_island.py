from island_count import make_edges
from connected_components_count import get_connected_components


def minimum_island(grid):
    edges = make_edges(grid)

    nodes = list(edges.keys())
    smallest = float("inf")
    while nodes:
        components = get_connected_components(edges, nodes[0])

        if len(components) < smallest:
            smallest = len(components)

        for node in components:
            nodes.remove(node)

    return smallest


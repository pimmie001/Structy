def shortest_path(edges, A, B):
    graph = make_graph(edges)
    length = shortest_path_directed(graph, A, B)
    return -1 if length == float("inf") else length



def shortest_path_directed(graph, A, B, length=0):
    if A == B:
        return length
    
    if length == len(graph):
        return float("inf")

    minimum = float("inf")
    for neighbor in graph[A]:
        minimum = min(minimum, shortest_path_directed(graph, neighbor, B, length+1))
    return minimum



def make_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


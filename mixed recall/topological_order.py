def topological_order(graph):
    num_parents = {}
    for node in graph:
        num_parents[node] = 0
    for node in graph:
        for child in graph[node]:
            num_parents[child] += 1


    L = []
    while len(L) < len(graph):
        for node in num_parents:
            if num_parents[node] == 0:
                L.append(node)
                for child in graph[node]:
                    num_parents[child] -= 1
                num_parents.pop(node)
                break

    return L

from topological_order import topological_order


def safe_cracking(hints):
    graph = make_graph(hints)
    top_order = topological_order(graph)
    code = ''
    for n in top_order: code += str(n)
    return code


def make_graph(hints):
    graph = {}
    nodes = set()
    for a,b in hints:
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
        nodes.add(b)
    for node in nodes:
        if node not in graph:
            graph[node] = []
    return graph

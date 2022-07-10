from can_color import can_color


def tolerant_teams(rivalries):
    graph = make_graph(rivalries)
    return can_color(graph)


def make_graph(rivalries):
    graph = {}
    for a, b in rivalries:
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]

        if b in graph:
            graph[b].append(a)
        else:
            graph[b] = [a]
    
    return graph
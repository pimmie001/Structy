def has_path(graph, src, dst):
    for neighbor in graph[src]:
        if neighbor == dst:
            return True
        if has_path(graph, neighbor, dst):
            return True
    
    return False

def undirected_path(edges, node_A, node_B, checked = []):
    if node_A == node_B:
        return True

    for edge in edges:
        if edge in checked:
            continue 

        if node_A == edge[0]:
            checked.append(edge)
            if undirected_path(edges, edge[1], node_B, checked):
                return True
        elif node_A == edge[1]:
            checked.append(edge)
            if undirected_path(edges, edge[0], node_B, checked):
                return True

    return False

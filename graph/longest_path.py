def longest_path(graph, visited=set()):
    max_length = 0

    for node in graph:
        if node not in visited:
            max_length = max(max_length, longest_path_from(graph, node, visited))

    return max_length


def longest_path_from(graph, start, visited):
    max_length = 0
    stack = [(start, 0)]

    while stack:
        current, length = stack.pop()
        visited.add(current)
        max_length = max(max_length, length)
        for neighbor in graph[current]:
            stack.append((neighbor, length+1))

    return max_length


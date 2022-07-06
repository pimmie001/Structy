from collections import deque

# white-grey-black algorithm: time O(n^2)
def has_cycle(graph):
    visited = set()
    for node in graph:
        if cycle_detect(graph, node, set(), visited):
            return True
    return False


def cycle_detect(graph, node, visiting, visited):
    if node in visiting: 
        return True
    if node in visited:
        return False

    visiting.add(node)
    for neighbor in graph[node]:
        if cycle_detect(graph, neighbor, visiting, visited):
            return True
    
    visiting.remove(node)
    visited.add(node)
    return False




# # own solution: time O(n^3)
# def has_cycle(graph):


#     for node in graph:
#         Q = deque(node)
#         visited = set()
#         while Q:
#             current = Q.popleft()
#             if current in visited:
#                 return True
#             visited.add(current)
#             for neighbor in graph[current]:
#                 if neighbor not in Q:
#                     Q.append(neighbor)

#     return False

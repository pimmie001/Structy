from collections import deque


# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


def lefty_nodes(root):
    if not root:
        return []

    left_nodes = []
    Q = deque([(root, 0)])
    while Q:
        current, level = Q.popleft()

        if current is None:
            continue

        if level >= len(left_nodes):
            left_nodes.append(current.val)

        Q.append((current.left, level+1))
        Q.append((current.right, level+1))

    return left_nodes

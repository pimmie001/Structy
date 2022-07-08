from collections import deque

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


def lowest_common_ancestor(root, val1, val2):
    ancestors_1 = get_ancestors(root, val1)
    ancestors_2 = get_ancestors(root, val2)
    intersection = ancestors_1.intersection(ancestors_2)

    lowest_ancestor = None
    Q = deque([root])
    while Q:
        current = Q.popleft()
        if current.val in intersection:
            lowest_ancestor = current.val
        if current.left:
            Q.append(current.left)
        if current.right:
            Q.append(current.right)
    return lowest_ancestor



def get_ancestors(root, val):
    if root is None:
        return set()

    if root.val == val:
        return set([root.val])

    result = get_ancestors(root.left, val).union(get_ancestors(root.right, val))
    if result:
        result.add(root.val)
    return result


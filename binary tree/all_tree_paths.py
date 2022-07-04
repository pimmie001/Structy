# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


def all_tree_paths(root):
    reversed_paths = _all_tree_paths(root)
    for path in reversed_paths:
        path.reverse()
    return reversed_paths


def _all_tree_paths(root):
    if root is None:
        return []

    if root.right is None and root.left is None:
        return [[root.val]]

    left_paths = _all_tree_paths(root.left)
    right_paths = _all_tree_paths(root.right)
    all_paths = left_paths + right_paths
    for path in left_paths + right_paths:
        path.append(root.val)
    return all_paths

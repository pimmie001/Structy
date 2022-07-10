# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


def binary_search_tree_includes(root, target):
    if root is None:
        return False

    if root.val == target:
        return True

    if root.val < target:
        return binary_search_tree_includes(root.right, target)
    if root.val > target:
        return binary_search_tree_includes(root.left, target)

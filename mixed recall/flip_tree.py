# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


def flip_tree(root):
    _flip_tree(root)
    return root


def _flip_tree(root):
    if root is None:
        return 
    current = root
    current.left, current.right = current.right, current.left
    _flip_tree(current.left)
    _flip_tree(current.right)

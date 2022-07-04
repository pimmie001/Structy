# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


def leaf_list(root):
    stack = []
    if root is not None:
        stack.append(root)

    leaves = []
    while stack:
        current = stack.pop()
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
        if not current.left and not current.right:
            leaves.append(current.val)

    return leaves

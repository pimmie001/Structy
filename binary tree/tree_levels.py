# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


def tree_levels(root):
    current = []
    if root is not None:
        current.append(root)

    all_levels = []
    while current:
        current_level = []
        next = []

        for child in current:
            current_level.append(child.val)
            if child.left:
                next.append(child.left)
            if child.right:
                next.append(child.right)

        all_levels.append(current_level)
        current = next

    return all_levels

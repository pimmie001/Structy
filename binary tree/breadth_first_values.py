# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


def breadth_first_values(root):
    values = []
    children = []
    if root is not None:
        children.append(root)

    while len(children) > 0:
        new_children = []
        for child in children:
            values.append(child.val)
            if child.left is not None:
                new_children.append(child.left)
            if child.right is not None:
                new_children.append(child.right)
        children = new_children

    return values


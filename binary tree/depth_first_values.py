# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


def depth_first_values(root, values=[]):
    if root is not None:
        values.append(root.val)
    else:
        return values

    if root.left is not None:
        values = depth_first_values(root.left, values)
    if root.right is not None:
        values = depth_first_values(root.right, values)

    return values


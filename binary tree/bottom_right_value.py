# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# depth first approach
def bottom_right_value(root):
    return _bottom_right_value(root)[0]


def _bottom_right_value(root, depth=0):
    if root is None:
        return None, float('-inf')

    right_val, right_depth = _bottom_right_value(root.right, depth+1)
    left_val, left_depth = _bottom_right_value(root.left, depth+1)

    if right_val is None and left_val is None:
        return root.val, depth

    if left_depth > right_depth:
        return left_val, left_depth
    else:
        return right_val, right_depth

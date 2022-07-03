# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


def path_finder(root, target):
    reversed_path = _path_finder(root, target)
    if reversed_path is None:
        return None
    return reversed_path[::-1]


def _path_finder(root, target):
    if root is None:
        return None
    
    if root.val == target:
        return [root.val]

    left = _path_finder(root.left, target)
    if left is not None:
        left.append(root.val)
        return left

    right = _path_finder(root.right, target)
    if right is not None:
        right.append(root.val)
        return right

    return None

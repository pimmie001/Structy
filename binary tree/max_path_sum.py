# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


def max_path_sum(root):
    # 0 children
    if root.left is None and root.right is None:
        return root.val

    # 1 child
    if root.right is None:
        return root.val + max_path_sum(root.left)
    if root.left is None:
        return root.val + max_path_sum(root.right)
    
    # 2 children
    return root.val + max(max_path_sum(root.left), max_path_sum(root.right))

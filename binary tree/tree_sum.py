# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


def tree_sum(root, total=0):
    # depth first approach
    if root:
        total += root.val
    else:
        return total

    if root.left:
        total = tree_sum(root.left, total)
    if root.right:
        total = tree_sum(root.right, total)
    
    return total

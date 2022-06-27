# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None



# depth first
def tree_min_value(root):
    if root is None:
        return float('inf')
    
    return my_min((root.val, tree_min_value(root.left), tree_min_value(root.right)))

def my_min(A):
    if len(A) == 1:
        return A[0]
    return min(A[0], my_min(A[1:]))



# breadth first
def tree_min_value(root):
    mini = root.val

    children = [root]
    while len(children) > 0:
        new_children = []
        for child in children:
            if child.left:
                mini = min(mini, child.left.val)
                new_children.append(child.left)
            if child.right:
                mini = min(mini, child.right.val)
                new_children.append(child.right)
        children = new_children

    return mini

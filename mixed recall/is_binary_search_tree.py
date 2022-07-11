# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

def is_binary_search_tree(root):
    values = []
    in_order_values(root, values)

    for i in range(len(values)-1):
        if values[i] > values[i+1]:
            return False
    return True


def in_order_values(root, values):
    if root:
        in_order_values(root.left, values)
        values.append(root.val)
        in_order_values(root.right, values)

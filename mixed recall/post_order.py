# class Node:
    # def __init__(self, val):
    #     self.val = val
    #     self.left = None
    #     self.right = None

def post_order(root):
    values = []
    post_order_traversal(root, values)
    return values


def post_order_traversal(root, values):
    if not root:
        return
    post_order_traversal(root.left, values)
    post_order_traversal(root.right, values)
    values.append(root.val)
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree_in_pre(in_order, post_order):
    if len(in_order) == 0:
        return None


    node = Node(post_order[0])

    index = in_order.index(node.val)
    in_order_left = in_order[:index]
    in_order_right = in_order[index+1:]
    post_order_left = post_order[1:index+1]
    post_order_right = post_order[index+1:]

    node.left = build_tree_in_pre(in_order_left, post_order_left)
    node.right = build_tree_in_pre(in_order_right, post_order_right)
    return node

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree_in_post(in_order, post_order):
    node = Node(post_order[-1])
    build_tree(in_order, post_order, node)
    return node


def build_tree(in_order, post_order, node):
    index = in_order.index(node.val)
    if index > 0:
        node.left = build_tree_in_post(in_order[:index], post_order[:index])
    else:
        node.left = None

    if index < len(in_order)-1:
        node.right = build_tree_in_post(in_order[index+1:], post_order[index:-1])
    else:
        node.right = None    


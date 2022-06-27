class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


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




a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

print(tree_sum(None)) # -> 21
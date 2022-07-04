from tree_levels import tree_levels


# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


mean = lambda A: sum(A)/len(A)


def level_averages(root):
    levels = tree_levels(root)
    result = []
    for x in levels:
        result.append(mean(x))
    return result

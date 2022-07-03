# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


def sum_list(head, total=0):
    if head is None:
        return total
    total += head.val
    return sum_list(head.next, total)


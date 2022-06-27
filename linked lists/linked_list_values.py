# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

def linked_list_values(head, lst=[]):
    if head is None:
        return lst
    lst.append(head.val)
    return linked_list_values(head.next, lst)

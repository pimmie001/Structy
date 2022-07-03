# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


def is_univalue_list(head, value=None):
    if head is None:
        return True

    if value is not None and head.val != value:
        return False
    
    if head is None:
        return True

    return is_univalue_list(head.next, head.val)

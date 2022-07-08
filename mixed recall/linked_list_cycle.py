# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

def linked_list_cycle(head):
    visited = set()
    while head is not None:
        if head in visited:
            return True
        visited.add(head)
        head = head.next
    return False
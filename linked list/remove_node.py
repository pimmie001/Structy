# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


def remove_node(head, target_val):
    if head.val == target_val:
        return head.next

    current = head
    while True:
        if current.next.val == target_val:
            current.next = current.next.next
            return head
        current = current.next

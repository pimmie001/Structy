# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


def linked_palindrome(head):
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values == values[::-1]

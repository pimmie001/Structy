# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


def middle_value(head):
    first = head # 
    second = head # goes 2x fast
    while second is not None and second.next is not None:
        second = second.next
        first = first.next
        second = second.next
    return first.val

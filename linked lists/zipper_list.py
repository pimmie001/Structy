# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


def zipper_lists(head1, head2):
    mainhead = head1

    next1 = head1.next
    next2 = head2.next

    while True:
        next1 = head1.next
        next2 = head2.next

        if head2 is not None:
            head1.next = head2
        if next1 is not None:
            head2.next = next1

        head1 = next1
        head2 = next2

        if head1 is None or head2 is None:
            return mainhead

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


def longest_streak(head, prev_value=None, streak=0):
    if head is None:
        return streak

    if prev_value is None or head.val == prev_value:
        return longest_streak(head.next, head.val, streak+1)

    return max(streak, longest_streak(head))

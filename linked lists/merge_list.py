# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


def merge_lists(head_1, head_2):
    # find out with which head to start:
    if head_1.val < head_2.val:
        main_head = head_1
        current = head_1
        current_1 = head_1.next
        current_2 = head_2
    else:
        main_head = head_2
        current = head_2
        current_1 = head_1
        current_2 = head_2.next

    # while loop for the rest:
    while True:
        if current_1 is None:
            current.next = current_2
            break
        if current_2 is None:
            current.next = current_1
            break

        if current_1.val < current_2.val:
            current.next = current_1
            current = current.next
            current_1 = current_1.next
        else:
            current.next = current_2
            current = current.next
            current_2 = current_2.next


    return main_head

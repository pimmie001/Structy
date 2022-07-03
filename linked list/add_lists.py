from create_linked_list import create_linked_list


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None



def add_lists(head_1, head_2):
    n1 = int(get_number(head_1)[::-1])
    n2 = int(get_number(head_2)[::-1])

    new_number = str(n1+n2)[::-1]
    return create_linked_list(list(new_number))



def get_number(head, string=''):
    if head is None:
        return string
    string += str(head.val)
    return get_number(head.next, string)

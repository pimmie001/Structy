class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def insert_node(head, value, index):
    new_node = Node(value)


    if index == 0:
        new_node.next = head
        return new_node


    i = 1
    current = head
    while True:
        if i == index:
            next_node = current.next
            current.next = new_node
            new_node.next = next_node
            return head

        current = current.next
        i += 1

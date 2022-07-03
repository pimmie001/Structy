class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_linked_list(values):
    if values == []:
        return None
    
    new_node = Node(values[0])
    new_node.next = create_linked_list(values[1:])

    return new_node

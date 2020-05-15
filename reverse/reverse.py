class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # to reverse a linked list, you start at the 
        # head (there are no previous nodes)
        previous = None
        current = self.head
        # this loop goes until it hits the end of the 
        # linked list, which is None
        while current is not None:
            # changes the next pointer 
            next = current.next_node
            # changes the current pointer from next_node
            # to previous node (essentially switching the direction the pointer points)
            current.next_node = previous
            # to mode to the next node, the previous node
            # needs to be set to the current node
            previous = current
            # finally, the current pointer must point 
            # to the next node so that the loop can continue on
            # to other nodes
            current = next
        # the head is reassigned at the end of the loop to the node
        # that is previous to "None", which was the end of the list,
        # but is now the start of the list 
        self.head = previous

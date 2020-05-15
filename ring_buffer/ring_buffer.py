from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        # this is the limit before things get deleted
        self.capacity = capacity
        # this is the current item
        self.current = 0
        # the type of storage is a doubly linked list
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if capacity has not been reached, add the item
        if len(self.storage) < self.capacity:
            self.storage.add_to_head(item)
            # if this is the first item in the list,
            # it gets labeled as the head
            if len(self.storage) == 1:
                self.current = self.storage.head
            return
        # if capacity has been reached
        if len(self.storage) == self.capacity:
            # set the value of the node to the input value
            self.current.value = item
            # if there is a previous node
            if self.current.prev is not None:
                # move pointer
                self.current = self.current.prev
            # if there is not a previous node
            else:
                # make sure end node is labeled as tail
                self.current = self.storage.tail

    def get(self):
        # the list of items to be returned
        list_buffer_contents = []
        # start at the tail
        current = self.storage.tail
        # loop over the entirety of self.storage
        for i in range(len(self.storage)):
            # append the value to the list that will be returned
            list_buffer_contents.append(current.value)
            # change current pointer
            current = current.prev
        # return the list that was filled using the loop
        return list_buffer_contents

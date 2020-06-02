from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):  # queue
        # if list is not full
        if self.capacity > self.storage.length:
            # add item to end
            self.storage.add_to_tail(item)
            # set current old item to the front
            self.current = self.storage.head
        # if list is full
        elif self.capacity == self.storage.length:
            # delete the oldest item
            delete = self.storage.head
            self.storage.remove_from_head()
            # then add new item to the end
            self.storage.add_to_tail(item)
            if delete == self.current:
                self.current = self.storage.tail

    def get(self):
        buffer_list = []

        start_node = self.current
        buffer_list.append(start_node.value)

        if start_node.next is not None:
            next_node = start_node.next
        else:
            next_node = self.storage.head

        while next_node != start_node:
            buffer_list.append(next_node.value)
            if next_node.next is not None:
                next_node = next_node.next
            else:
                next_node = self.storage.head

        return buffer_list

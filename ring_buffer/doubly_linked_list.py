"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # create new node
        new_node = ListNode(value)
        # checks if list has no head and no tail
        if not self.head and not self.tail:
            # assign as new head and tail
            self.head = new_node
            self.tail = new_node
        # handles if list has head
        else:
            # reassigns pointers accordingly
            new_node.next = self.head
            self.head.prev = new_node
            # assigns as new head
            self.head = new_node
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        # store the value of head
        value = self.head.value
        # delete method to remove head
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value)
        # handles if there is no head and no tail
        if not self.head and not self.tail:
            # assigns new tail and head
            self.tail = new_node
            self.head = new_node
        # handles if there is a tail
        else:
            # reassigns pointers
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        # store the value of tail
        value = self.tail.value
        # delete to remove tail
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # check if node is already a head
        if node is self.head:
            return
        # store value of node
        value = node.value
        # delete
        self.delete(node)
        # add_to_head
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        # check if node is already a tail
        if node is self.tail:
            return
        # store value of node
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # if list is empty
        if not self.head and not self.tail:
            return
        # if list has one item
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        # if there are 2 nodes and want to delete the head
        elif self.head == node:
            self.head = node.next
            self.length -= 1
            node.delete()
        # if there are 2 nodes and want to delete the tail
        elif self.tail == node:
            self.tail = node.prev
            self.length -= 1
            node.delete()
        else:
            self.length -= 1
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        # check if list is empty
        if not self.head:
            return 0
        # store the max value to head value
        maximum = self.head.value
        # store current node pointer to head
        current = self.head
        while current.next:
            current = current.next
            # if current value is less than max value
            # replace max value with current value
            if current.value > maximum:
                maximum = current.value
        return maximum

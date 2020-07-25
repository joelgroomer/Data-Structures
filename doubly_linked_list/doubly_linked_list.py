"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value, None, self.head)
        if self.head is not None:
            self.head.prev = new_node
            # new_node.next = self.head
        else:
            # if there was no head before, there was also no tail
            self.tail = new_node
        self.head = new_node
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.head is None:
            return None

        old_head = self.head
        if old_head.next is not None:
            self.head = old_head.next
            self.head.prev = None
        else:
            self.head = None

        if old_head == self.tail:
            self.tail = None

        old_head.next = None
        self.length -= 1
        return old_head.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        print(f'adding {value} to tail')
        new_node = ListNode(value, self.tail, None)
        if self.tail is not None:
            # new_node.prev = self.tail
            self.tail.next = new_node
            print(f'self.tail.next = {self.tail.next.value}')
        else:
            # if there was no tail before, there was also no head
            self.head = new_node
        self.tail = new_node
        print(f'self.tail = {self.tail.value}')
        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.tail is None:
            return None

        old_tail = self.tail
        if old_tail.prev is not None:
            self.tail = old_tail.prev
            self.tail.next = None
        else:
            self.tail = None

        if old_tail == self.head:
            self.head = None

        old_tail.prev = None
        self.length -= 1
        return old_tail.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if node == self.head:
            return

        prev = node.prev
        next = node.next

        node.prev.next = next
        if next is not None:
            node.next.prev = prev

        if node == self.tail:
            self.tail = prev
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        print(f'MOVE TO END: {node.value}')
        if node == self.tail:
            return

        prev = node.prev
        next = node.next

        node.next.prev = prev
        if prev is not None:
            node.prev.next = next

        if node == self.head:
            self.head = next
        node.next = None
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        if self.length == 0:
            return

        if node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        if self.length == 0:
            return None

        cur_max = self.head.value
        cur_node = self.head.next
        while cur_node is not None:
            if cur_node.value > cur_max:
                cur_max = cur_node.value
            cur_node = cur_node.next
        return cur_max

    def __str__(self):
        val = f'length {self.length}: N'
        cur_node = self.head
        while cur_node is not None:
            val += ' <-> '
            if cur_node == self.head:
                val += '(H)'
            val += f'{cur_node.value}'
            if cur_node == self.tail:
                val += '(T)'
            cur_node = cur_node.next
        val += ' <-> N'
        return val

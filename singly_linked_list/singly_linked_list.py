class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:    # (or check for None for both head and tail)
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        # default next node is already None per Node's init
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        # empty LL
        if self.head is None:
            return None
        # list with 1 node
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        # LL with 2 or more nodes
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value

    def remove_tail(self):
        # empty LL
        if self.length == 0:
            return None
        # list with 1 node
        elif self.head == self.tail:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length = 0
            return value
        # LL with 2 or more nodes
        else:
            value = self.tail.get_value()
            cur_node = self.head.get_next()
            while cur_node.get_next() is not self.tail:
                cur_node = cur_node.get_next()
            cur_node.set_next(None)
            self.tail = cur_node
            self.length -= 1
            return value

    def contains(self, value):
        if self.length == 0:
            return False

        if self.head.get_value == value:
            return True

        cur_node = self.head
        while cur_node.get_next() is not None:
            if cur_node.get_value() == value:
                return True
            cur_node = cur_node.get_next()
        if cur_node.get_value() == value:       # test last value after loop finishes
            return True
        else:
            return False

    def get_max(self):
        # iterate through all elements
        if self.length == 0:
            return None
        if self.length == 1:
            return self.head.get_value()

        cur_node = self.head
        cur_max = self.head.get_value()
        while cur_node is not None:
            if cur_node.get_value() > cur_max:
                cur_max = cur_node.get_value()
            cur_node = cur_node.get_next()
        return cur_max

    def find_middle(self):
        """ How do you find and return the middle node of a singly 
        linked list in one pass? You do not have access to the length 
        of the list. If the list is even, you should return the second 
        of the two "middle" nodes. You may not store the nodes in another 
        data structure."""
        if self.head is None:
            return None

        mid_point = self.head
        end_point = self.head
        while end_point is not None and end_point.get_next() is not None:
            mid_point = mid_point.get_next()
            end_point = end_point.get_next().get_next()
        return mid_point.get_value()


# test find_middle()
ll = LinkedList()
ll.add_to_tail(1)
ll.add_to_tail(2)
ll.add_to_tail(3)
ll.add_to_tail(4)
ll.add_to_tail(5)
ll.add_to_tail(6)
ll.add_to_tail(7)
print(ll.find_middle())

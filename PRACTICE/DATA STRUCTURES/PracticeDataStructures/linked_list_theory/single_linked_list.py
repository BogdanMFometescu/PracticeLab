class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, val):
        # create a new node with the given value
        new_node = Node(val)
        # set the next variable of the new node to the current head of the list
        new_node.next = self.head
        # update the head variable to the new node
        self.head = new_node

    def add_last(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_first(self):
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.next
        return val

    def remove_last(self):
        if not self.head:
            return None
        if not self.head.next:
            val = self.head.val
            self.head = None
            return val
        current = self.head
        while current.next.next:
            current = current.next
        val = current.next.val
        current.next = None
        return val


li = LinkedList()
li.add_first(10)
li.add_first(20)
li.add_first(30)
li.add_first(40)

curr = li.head
while curr:
    print(curr.val)
    curr = curr.next


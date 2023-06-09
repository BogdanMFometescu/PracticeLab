class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_first(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def search(self, val):
        current = self.head
        while current is not None:
            if current.val == val:
                return True
            current = current.next
        return False

    def delete(self, val):
        if self.is_empty():
            return
        if self.head.val == val:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
                return
            current = current.next

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end='--')
            current = current.next
        print('None')


my_list = LinkedList()
my_list.add_first(1)
my_list.add_last(2)
my_list.add_last(3)
my_list.add_last(4)
my_list.print_list()
print(my_list.search(3))
my_list.delete(3)
my_list.print_list()

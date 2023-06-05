class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete(self, data):
        if self.is_empty():
            return
        if self.head.data == data:
            self.head = self.head.next

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def remove_duplicates(self):
        if self.is_empty():
            return
        current = self.head
        while current.next is not None:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end='->')
            current = current.next
        print('None')


my_list = LinkedList()
my_list.add_first(1)
my_list.add_last(1)
my_list.add_last(2)
my_list.add_last(3)
my_list.add_last(3)
my_list.print_list()
my_list.remove_duplicates()
my_list.print_list()

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
        # Define new node
        new_node = Node(val)
        # Old Head will become next node
        new_node.next = self.head
        # New Head is the new_node
        self.head = new_node

    def add_last(self, val):
        # Define new node
        new_node = Node(val)
        # Check if list is empty, if it is the new node is the head
        if self.is_empty():
            self.head = new_node
        else:
            # define the pointer as the head of the list
            current = self.head
            # Traverse the list and check if next is not None and set the pointer to the next value
            while current.next is not None:
                current = current.next
            # set the next value to the new_node
            current.next = new_node

    def search(self, val):
        # set the pointer as the head as we need to traverse all the list to search a value
        current = self.head
        # Traverse the list and check if it is empty
        while current is not None:
            if current.val == val:
                return 'Found'
            # increment the loop
            current = current.next

        return False

    def delete(self, val):
        pass

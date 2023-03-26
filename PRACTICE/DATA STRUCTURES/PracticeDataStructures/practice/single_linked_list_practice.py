class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Pre append - means adding to the LEFT - HEAD
    def add_first(self, value):
        # Instantiate new node
        new_node = Node(value)
        # Next value is now the former head value
        new_node.next = self.head
        # New head is now the new node
        self.head = new_node

    # Append - means adding to the RIGHT - TAIL
    def add_last(self, value):
        new_node = Node(value)
        # Check if list is empty
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node

    def search(self, key):
        cur = self.head
        while cur is not None:
            if cur.value == key:
                print("Item found")
                break
            else:
                cur = cur.next

        return None

    def remove_item(self, value):
        cur = self.head
        while cur is not None:
            if cur.next == value:
                cur.next = cur.next.next
            else:
                break


li = LinkedList()
li.add_first(10)
li.add_first(20)
li.add_first(30)
li.add_last(45)

li.search(45)
li.remove_item(10)

current = li.head
while current:
    print(current.value)
    current = current.next

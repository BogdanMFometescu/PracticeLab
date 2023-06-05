#You are given the heads of two sorted linked lists list1 and list2.

#Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

#Return the head of the merged linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    # Create a dummy node as the head of the merged list
    dummy = ListNode(0)
    # Create a pointer to track the current node in the merged list
    current = dummy

    # Iterate through both lists simultaneously
    while list1 and list2:
        # Compare the values of the nodes
        if list1.val < list2.val:
            # If the value in list1 is smaller, add it to the merged list
            current.next = list1
            list1 = list1.next
        else:
            # If the value in list2 is smaller or equal, add it to the merged list
            current.next = list2
            list2 = list2.next
        # Move the pointer to the next node in the merged list
        current = current.next

    # Add the remaining nodes from list1 or list2 (if any) to the merged list
    if list1:
        current.next = list1
    if list2:
        current.next = list2

    # Return the head of the merged list (excluding the dummy node)
    return dummy.next

# Create the first sorted linked list: 1 -> 2 -> 4
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# Create the second sorted linked list: 1 -> 3 -> 4
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# Merge the two lists
merged = mergeTwoLists(list1, list2)

# Print the merged list: 1 -> 1 -> 2 -> 3 -> 4 -> 4
while merged:
    print(merged.val, end=" -> ")
    merged = merged.next
print("None")
# Heap is a special tree structure in which each parent node is less than or equal to its child node.
# Then it is called a Min Heap. If each parent node is greater than or equal to its child node then it
# is called a max heap.
# It is very useful is implementing priority queues where the queue item with higher weightage is given more
# priority in processing.


# Create a heap by importing 'heapq'
import heapq

# Create a list  and use heapify to rearrange it
my_list = [21, 1, 45, 78, 3, 5]

heapq.heapify(my_list)
print(my_list)

# We can add an element at last position using 'heappush', if element already exist it will be added right
# after the existing element. Accepts 2 parameters : a list and the element we want to add

heapq.heappush(my_list, 22)
print(my_list)

# We can remove the last element by using 'heappop'.Accepts 1 parameter : a list
heapq.heappop(my_list)
print(my_list)

# We can replace an element by using 'heapreplace'.This will always remove the smallest element and
# insert the new one at a random position.Accepts 2 parameters : a list and an element

heapq.heapreplace(my_list, 88)
print(my_list)

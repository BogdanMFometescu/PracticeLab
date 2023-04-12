# A queue(deque) works  on the principle of First IN First OUT
# Functions : appendLeft, pop

# First we need to import 'deque' from collections

from collections import deque

# Option 1 - make a list and convert it to a deque
# Make a list
my_list = [1, 2, 3, 4, 5]

# Convert the list to a deque
q = deque(my_list)
print(q)

# Option 2 - make a deque by passing a list
qq = deque([5, 6, 7, 8, 9, ])
print(qq)

# We can add elements to the start of the deque by using 'appendLeft' -O(1) time complexity
q.appendleft(0)
print(q)

# We can also add elements at the end of the deque  -O(1) time complexity
q.append(6)
print(q)

# We can remove the last  element from the deque using 'pop' -O(1) time complexity
q.pop()
print(q)

# We can remove the first element from the deque using 'popleft' -O(1) time complexity
q.popleft()
print(q)

# We can add multiple elements to the end of the deque using 'extend' -O(K) time complexity
q.extend([11, 12, 13])
print(q)

# We can add multiple elements at the start of the deque using 'extendLeft' -O(K) time complexity
q.extendleft([99, 88, 77])
print(q)

# We can reverse the deque by using 'reverse' --O(N) time complexity
q.reverse()
print(q)

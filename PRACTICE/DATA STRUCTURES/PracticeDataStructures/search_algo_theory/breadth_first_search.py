from queue import Queue


def bfs(graph, start):
    visited = set()
    queue = Queue()
    queue.put(start)
    visited.add(start)

    while not queue.empty():
        vertex = queue.get()
        print(vertex, end=' ')

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.put(neighbor)

# BFS is an algorithm for traversing a graph or a tree data structure, visiting all the vertices (nodes)
# in a level-by-level manner.
# Starting from the root node, BFS visits all the vertices at a given level before moving on
# to the vertices at the next level.


# In the above code, we start by initializing an empty set visited to keep track of the vertices that have already been
# visited.
# We also create a Queue data structure to store the vertices that are yet to be visited.
#
# We start by adding the start vertex to the Queue and marking it as visited. We then enter a loop that continues until
# the Queue is empty.
# At each iteration, we get the next vertex from the Queue and print it.
#
# We then loop over all the neighbors of the current vertex, and for each neighbor that has not been visited yet,
# we mark it
# as visited and add it to the Queue.

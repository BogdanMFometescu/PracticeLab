def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# DFS is an algorithm for traversing a graph or a tree data structure, visiting all the vertices (nodes)
# in a depth-first manner.
# Starting from the root node, DFS visits all the vertices in a path before backtracking
# and visiting other paths.

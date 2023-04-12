class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def print_graph(self):
        for vertex in self.graph:
            print(vertex, ':', ' -> '.join(map(str, self.graph[vertex])))


graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'D')
graph.add_edge('D', 'A')
graph.print_graph()

# In the above code, we define a Graph class to represent the undirected graph, using an adjacency list.
# The add_vertex method is used to add a new vertex to the graph, and the add_edge method is used to add
# a new edge between two vertices.
# The print_graph method is used to print out the graph in a readable format,
# showing each vertex and its adjacent vertices.


# Graphs are non-linear data structures that consist of a set of vertices (nodes) and a set of edges that connect them.
# Each edge in a graph represents a relationship or connection between two vertices.
# Graphs can be used to represent a variety of real-world scenarios, such as social networks, road networks,
# electrical circuits, etc.
# There are several types of graphs, including directed graphs, undirected graphs, weighted graphs,
# and cyclic graphs.

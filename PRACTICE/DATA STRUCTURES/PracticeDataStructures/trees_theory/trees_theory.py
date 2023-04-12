class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._add_node(data, self.root)

    def _add_node(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._add_node(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._add_node(data, node.right)

# Trees are non-linear data structures that consist of nodes connected by edges.
# Each node in a tree may have zero or more child nodes.
# The topmost node in a tree is called the root node, and every other node can be reached from it by following edges.
# Nodes that have no child nodes are called leaf nodes.
# Trees can be used to represent hierarchical data such as family trees, organization charts, file systems, etc.
# There are several types of trees, including binary trees, binary search trees, AVL trees, red-black trees,
# and B-trees.

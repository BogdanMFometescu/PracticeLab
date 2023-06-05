# Moris Traversal
def inorder_traversal_optimized(root):
    result = []
    curr = root

    while curr:
        if curr.left is None:
            result.append(curr.val)
            curr = curr.right
        else:
            pre = curr.left
            while pre.right and pre.right != curr:
                pre = pre.right

            if pre.right is None:
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                result.append(curr.val)
                curr = curr.right

    return result


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data is None:
            self.data = data
        elif data is None:
            return
        elif data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data, end=' ')
        if self.right:
            self.right.print_tree()

    def inorder_traversal(self):
        result = []
        if self.left is not None:
            result += self.left.inorder_traversal()
        if self.data is not None:
            result.append(self.data)
        if self.right is not None:
            result += self.right.inorder_traversal()
        return result

    def preorder_traversal(self):
        print(self.data, end=' ')
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()
        print(self.data, end=' ')


binary_tree = Node()
binary_tree.insert(1)
binary_tree.insert(None)
binary_tree.insert(2)
binary_tree.insert(3)

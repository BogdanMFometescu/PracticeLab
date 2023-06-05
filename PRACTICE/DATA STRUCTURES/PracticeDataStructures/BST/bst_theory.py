# Binary Search Tree Construction


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average Time O(log(N)) , space O(N)  Worst Time( O(N), Space (O(N)
    def insertion(self, value):
        current_node = self

        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    current_node = current_node.left

            else:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else:
                    current_node = current_node.right
        return self

    def search(self, value):
        current_node = self

        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return True

    def deletion(self, value, parent_node=None):
        pass

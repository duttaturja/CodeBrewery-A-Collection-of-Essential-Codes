class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = BinaryTreeNode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current, data):
        if data < current.data:
            if current.left:
                self._insert(current.left, data)
            else:
                current.left = BinaryTreeNode(data)
        else:
            if current.right:
                self._insert(current.right, data)
            else:
                current.right = BinaryTreeNode(data)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

# Example Usage
bt = BinaryTree()
bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.inorder_traversal(bt.root)  # Output: 5 10 15

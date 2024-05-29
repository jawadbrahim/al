class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
    def search(self, data):
        current = self.root
        while current is not None:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False
    def remove(self, data):
        self.root = self._remove_node(self.root, data)
    def _remove_node(self, node, data):
        if node is None:
            return node
        if data < node.data:
            node.left = self._remove_node(node.left, data)
        elif data > node.data:
            node.right = self._remove_node(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_right_node = self._min_value_node(node.right)
            node.data = min_right_node.data
            node.right = self._remove_node(node.right, min_right_node.data)
        return node
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)
            
    def display_inorder(self):
        self.inorder_traversal(self.root)
        print()
bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(18)
print(bst.search(7))
print(bst.search(6))


print(bst.search(15))
print("Inorder Traversal:")
bst.display_inorder()
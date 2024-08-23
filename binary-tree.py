class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None 
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if data > current.data:
                if current.right is None:
                    current.right = new_node # type: ignore
                    return
                else:
                    current = current.right
            elif data < current.data:
                if current.left is None:
                    current.left = new_node # type: ignore
                    return
                else:
                    current = current.left
            else:
                return
    
    def inorder_traversal(self, root):
        if root is not None:
            self.inorder_traversal(root.left)
            print(root.data, end=" ")
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root is not None:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.data, end=" ")

tree = BinaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(60)
tree.insert(80)

print("Inorder traversal:")
tree.inorder_traversal(tree.root)

print("\nPreorder traversal:")
tree.preorder_traversal(tree.root)

print("\nPostorder traversal:")
tree.postorder_traversal(tree.root)

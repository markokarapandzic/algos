class TreeNode:
	def __init__(self, key, left=None, right=None) -> None:
		self.key = key	
		self.right = right	
		self.left = left

def inorderSuccessor(root, p):
	successor = None

	while root:
		if p.key < root.key:
			successor = root
			root = root.left
		else:
			root = root.right

	return successor

#       20
#      /  \
#    10    30
#   /  \   / \
#  5   15 25  35
#       \
#        17

root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)
root.left.right = TreeNode(15)
root.left.right.right = TreeNode(17)
root.right.left = TreeNode(25)
root.right.right = TreeNode(35)

node = inorderSuccessor(root, root.right.right)
print(node.key if node else "No Element Found")

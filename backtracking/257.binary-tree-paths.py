class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def binaryTreePaths(root):
	def findPath(node, path, result):
		if node:
			path.append(str(node.val))

			if not node.left and not node.right:
				result.append("->".join(path))
			else:
				findPath(node.left, path, result)
				findPath(node.right, path, result)

			path.pop()

	result = []
	findPath(root, [], result)

	return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

print(binaryTreePaths(root))

from collections import deque

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def levelOrderBottom(root):
	if not root:
		return []

	result = []
	q = deque([root])

	while q:
		level_nodes = len(q)
		current_level_nodes = []

		for _ in range(level_nodes):
			node = q.popleft()
			current_level_nodes.append(node.val)

			if node.left:
				q.append(node.left)

			if node.right:
				q.append(node.right)

		result.append(current_level_nodes)	

	return result[::-1]

node3 = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)

node3.right = node20
node3.left = node9
node20.right = node7
node20.left = node15

print(levelOrderBottom(node3))

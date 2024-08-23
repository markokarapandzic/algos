from collections import deque

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def levelOrder(root):
	if not root:
		return []

	result = []
	q = deque([root])
	level = 1

	while q:
		level_count = len(q)
		level_nodes = []

		for _ in range(level_count):
			currentNode = q.popleft()
			level_nodes.append(currentNode.val)

			if level % 2 == 0:
				if currentNode.left:
					q.append(currentNode.left)

				if currentNode.right:
					q.append(currentNode.right)
			else:
				if currentNode.right:
					q.append(currentNode.right)

				if currentNode.left:
					q.append(currentNode.left)

		result.append(level_nodes)
		level += 1

	return result

node3 = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)

node3.right = node20
node3.left = node9
node20.right = node7
node20.left = node15

print(levelOrder(node3))

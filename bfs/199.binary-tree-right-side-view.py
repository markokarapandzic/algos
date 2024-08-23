from collections import deque

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def rightSideView(root):
	if not root:
		return None

	result = []
	q = deque([root])

	while q:
		index = 0
		level_count = len(q)

		for _ in range(level_count):
			currentNode = q.popleft()

			if index == 0:
				result.append(currentNode.val)

			if currentNode.right:
				q.append(currentNode.right)

			if currentNode.left:
				q.append(currentNode.left)

			index += 1

	return result

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node2.right = node5
node3.right = node4

print(rightSideView(node1))

from collections import deque

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def averageOfLevels(root):
	result = []
	q = deque([root])

	while q:
		level_sum = 0
		level_count = 0
		level_nodes = len(q)

		for _ in range(level_nodes):
			currentNode = q.popleft()
			level_sum += currentNode.val
			level_count += 1

			if currentNode.left:
				q.append(currentNode.left)

			if currentNode.right:
				q.append(currentNode.right)

		average = level_sum / level_count
		result.append(average)

	return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(averageOfLevels(root))

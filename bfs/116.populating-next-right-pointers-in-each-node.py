from collections import deque

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
		self.next = next

def levelOrderBottom(root):
	if not root:
		return None

	q = deque([root])

	while q:
		level_count = len(q)
		pre = None

		for _ in range(level_count):
			currentNode = q.popleft()

			if currentNode.left:
				q.append(currentNode.left)

			if currentNode.right:
				q.append(currentNode.right)

			if not pre:
				pre = currentNode
			else:
				pre.next = currentNode
				pre = currentNode

	return root

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

print(levelOrderBottom(node3))

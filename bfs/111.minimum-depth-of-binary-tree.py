from collections import deque

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def minDepth(root):
	if not root:
		return 0
	
	queue = deque([root])
	
	while queue:
		curr_level = len(queue)

		for _ in range(len(queue)):
			node = queue.popleft()
			
			if not node.left and not node.right:
				return curr_level
			
			if node.left:
				queue.append(node.left)
			
			if node.right:
				queue.append(node.right)

		curr_level += 1
	
	return 0

root = TreeNode(3)
root.left = TreeNode(None)
root.right = TreeNode(20)
root.right.left = TreeNode(None)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(None)
root.right.right.right = TreeNode(7)
root.right.right.right.left = TreeNode(None)
root.right.right.right.right = TreeNode(7)

print(minDepth(root))

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Codec:
	def serialize(self, root):
		"""Encodes a tree to a single string.
		
		:type root: TreeNode
		:rtype: str
		"""
		def dfs(node):
			if not node:
				return ['#']

			return [str(node.val) + dfs(node.left) + dfs(node.right)]

		return ",".join(dfs(root))
			

	def deserialize(self, data):
		"""Decodes your encoded data to tree.
		
		:type data: str
		:rtype: TreeNode
		"""
		def dfs(nodes):
			val = nodes.pop(0)

			if val == '#':
				return None

			node = TreeNode(int(val))
			node.left = dfs(nodes)
			node.right = dfs(nodes)

			return node

		node_list = data.split(',')
		return dfs(node_list)

ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
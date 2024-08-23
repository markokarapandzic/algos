from collections import deque

class Node:
	def __init__(self, val = 0, neighbors = None):
		self.val = val
		self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
	cloned = {}

	q = deque([node])

	cloned[node] = Node(node.val, [])

	while q:
		n = q.popleft()

		for neighbour in n.neighbors:
			if neighbour not in cloned:
				cloned[neighbour] = Node(neighbour.val, [])
				q.append(neighbour)

			cloned[n].neighbors.append(cloned[neighbour])

	return cloned[node]

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2]
node2.neighbors = [node3]
node3.neighbors = [node4]
node4.neighbors = [node1]

cloneGraph(node1)

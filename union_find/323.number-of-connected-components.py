def countComponents(n, edges):
	parent = [i for i in range(n)]
	rank = [1] * n

	def find(node):
		ref = node

		while node != parent[node]:
			node = parent[node]

		return ref

	def union(node1, node2):
		parent1, parent2 = find(node1), find(node2)

		if parent1 == parent2:
			return 0

		if rank[parent2] > rank[parent1]:
			parent[parent1] = parent2
			rank[parent2] += rank[parent1]
		else:
			parent[parent2] = parent1
			rank[parent1] += rank[parent2]

		return 1

	result = n

	for node1, node2 in edges:
		result -= union(node1, node2)

	return result

print(countComponents(5, [[0, 1], [1, 2], [3, 4]]))
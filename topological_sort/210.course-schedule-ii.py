def findOrder(numCourses, prerequisites):
	adj = { i: [] for i in range(numCourses) }

	for course, prereq in prerequisites:
		adj[course].append(prereq) 

	cycle = set()
	visited = set()
	result = []

	def dfs(course):
		if course in cycle:
			return False
		if course in visited:
			return True

		cycle.add(course)

		for prereq in adj[course]:
			if not dfs(prereq):
				return False

		cycle.remove(course)
		visited.add(course)
		result.append(course)

		return True

	for course in range(numCourses):
		if not dfs(course):
			return []

	return result

print(findOrder(2, [[1,0]]))
print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))

def canFinish(numCourses, prerequisites):
	adj = { i: [] for i in range(numCourses) }

	for start, finish in prerequisites:
		adj[start].append(finish)

	visited = set()

	def dfs(course):
		if course in visited:
			return False
		if adj[course] == []:
			return True

		visited.add(course)

		for prereq in adj[course]:
			if not dfs(prereq):
				return False

		visited.remove(course)
		adj[course] = []

		return True

	for course in range(numCourses):
		if not dfs(course):
			return False

	return True

print(canFinish(2, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]))

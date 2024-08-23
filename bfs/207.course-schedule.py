def canFinish(numCourses, prerequisites):
	preMap = { i:[] for i in range(numCourses)}

	for crs, pre in prerequisites:
		preMap[crs].append(pre)

	visited = set()

	def dfs(crs):
		if crs in visited:
			return False
		if preMap[crs] == []:
			return True

		visited.add(crs)

		for neighbour in preMap[crs]:
			if not dfs(neighbour):
				return False

		visited.remove(crs)
		preMap[crs] = []

		return True

	for crs in range(numCourses):
		if not dfs(crs):
			return False

	return True
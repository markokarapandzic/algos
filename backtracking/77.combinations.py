def combine(n, k):
	result = []
	arr = []

	for i in range(n):
		arr.append(i + 1)

	def backtrack(path, start):
		if len(path) == k:
			result.append(path[:])
			return

		for i in range(start, n):
			path.append(arr[i])
			backtrack(path, i + 1)
			path.pop()

	backtrack([], 0)

	return result

print(combine(4, 2))
print(combine(1, 1))

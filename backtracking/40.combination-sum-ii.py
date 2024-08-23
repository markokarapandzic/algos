def combinationSum2(candidates, target):
	candidates.sort()
	n = len(candidates)
	result = []

	def backtrack(path, start, sum):
		if sum == target:
			result.append(path[:])
			return
		elif sum > target:
			return

		for i in range(start, n):
			path.append(candidates[i])
			backtrack(path, i + 1, sum + candidates[i])
			path.pop()

	backtrack([], 0, 0)

	return result

print(combinationSum2([10,1,2,7,6,1,5], 8))
print(combinationSum2([2,5,2,1,2], 5))

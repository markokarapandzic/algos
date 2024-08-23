def combinationSum(candidates, target):
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
			backtrack(path, i, sum + candidates[i])
			path.pop()

	backtrack([], 0, 0)

	return result

print(combinationSum([2,3,6,7], 7))
print(combinationSum([2,3,5], 8))
print(combinationSum([2], 1))

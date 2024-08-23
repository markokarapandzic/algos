def permute(nums):
	result = []

	def backtrack(path, used):
		if len(path) == len(nums):
			result.append(path[:])
			return

		for i in range(len(nums)):
			if not used[i]:
				used[i] = True
				path.append(nums[i])
				backtrack(path, used)
				path.pop()
				used[i] = False

	backtrack([], [False] * len(nums))

	return result

print(permute([1,2,3]))
print(permute([0,1]))
print(permute([1]))

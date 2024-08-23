def subarraySum(nums, k):
	if not nums:
		return 0

	count = 0

	def backtrack(path, index):
		nonlocal count

		if sum(path) >= k:
			if sum(path) == k:
				count += 1
			return

		for i in range(index, len(nums) - 1):
			path.append(nums[i])

			backtrack(path, i)

			path.remove(nums[i])

	backtrack([], 0)

	return count

print(subarraySum([1,1,1], 2))
print(subarraySum([1,2,3], 3))
print(subarraySum([1,], 3))

def findTargetSumWays(nums, target):
	memo = {}

	def backtrack(index, current_sum):
		if index == len(nums):
			return 1 if current_sum == target else 0

		if (index, current_sum) in memo:
			return memo[(index, current_sum)]

		add = backtrack(index + 1, current_sum + nums[index])
		subtrackt = backtrack(index + 1, current_sum - nums[index])

		memo[(index, current_sum)] = add + subtrackt

		return memo[(index, current_sum)]

	return backtrack(0, 0)

print(findTargetSumWays([1, 1, 1, 1, 1], 3))
print(findTargetSumWays([1], 1))

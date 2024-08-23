def twoSum(nums, target):
	left = 0
	right = len(nums) - 1

	while left < right:
		current_sum = nums[left] + nums[right]

		if current_sum == target:
			return [left, right]
		elif current_sum < target:
			left += 1
		else:
			right -= 1

	return []

print(twoSum([2,7,11,15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))

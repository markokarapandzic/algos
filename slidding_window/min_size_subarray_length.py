def minSubArrayLen(nums, target):
	min_len = float('inf')
	current_sum = 0
	left = 0

	for i in range(len(nums)):
		current_sum += nums[i]

		while current_sum >= target:
			min_len = min(min_len, i - left + 1)
			current_sum -= nums[left]
			left += 1

	return min_len if min_len != float('inf') else 0


print(minSubArrayLen([2,3,1,2,4,3], 7))
print(minSubArrayLen([1,4,4], 4))
print(minSubArrayLen([1,1,1,1,1,1,1,1], 11))

def numSubarrayProductLessThanK(nums, k):
	if k <= 1:
		return 0

	result = 0
	left = 0
	current_product = 1

	for right in range(len(nums)):
		current_product *= nums[right]

		while current_product >= k:
			current_product //= nums[left]
			left += 1

		result += right - left + 1	

	return result

print(numSubarrayProductLessThanK([10,5,2,6], 100))
print(numSubarrayProductLessThanK([1, 2, 3], 0))

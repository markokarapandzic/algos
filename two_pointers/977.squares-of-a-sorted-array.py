def sortedSquares(nums):
	n = len(nums)
	result = [0] * n

	left = 0
	right = n - 1
	i = n - 1

	while left <= right:
		if abs(nums[left]) > abs(nums[right]):
			result[i] = nums[left] * nums[left]
			left += 1
		else:
			result[i] = nums[right] * nums[right]
			right -= 1
		i -= 1

	return result

print(sortedSquares([-4,-1,0,3,10]))
print(sortedSquares([-7,-3,2,3,11]))

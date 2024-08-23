def maxSubArray(nums):
	maxSub = nums[0]
	currentSum = 0

	for n in nums:
		if currentSum < 0:
			currentSum = 0
		
		currentSum += n
		maxSub = max(maxSub, currentSum)

	return maxSub

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1]))
print(maxSubArray([5,4,-1,7,8]))
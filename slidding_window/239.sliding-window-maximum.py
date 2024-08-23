def maxSlidingWindow(nums, k):
	current_max = 0
	result = []

	for i in range(len(nums)):
		current_max = max(current_max, nums[i])

		if i >= k - 1:
			result.append(current_max)

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) # [3,3,5,5,6,7]

# [8  3  -1] -3  5  3  6  7       3
#  8 [3  -1  -3] 5  3  6  7       3
#  8  3 [-1  -3  5] 3  6  7       5
#  8  3  -1 [-3  5  3] 6  7       5
#  8  3  -1  -3 [5  3  6] 7       6
#  8  3  -1  -3  5 [3  6  7]      7
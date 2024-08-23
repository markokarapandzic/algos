def longestArithSeqLength(nums):
	if not nums:
		return 0

	dp = {}
	max_length = 0

	for i in range(len(nums)):
		for j in range(i):
			diff = nums[i] - nums[j]
			
			if (j, diff) in dp:
				dp[(i, diff)] = dp[(j, diff)] + 1
			else:
				dp[(i, diff)] = 2
			
			max_length = max(max_length, dp[(i, diff)])

	return max_length

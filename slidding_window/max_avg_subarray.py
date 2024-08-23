def max_avg_subarray(nums, k):
	max_avg = float("-inf")
	current_sum = 0

	for i in range(len(nums)):
		current_sum += nums[i]

		if i >= k - 1:
			current_avg = current_sum / k
			max_avg = max(max_avg, current_avg)
			current_sum -= nums[i - k + 1]

	return max_avg

print(max_avg_subarray([1,12,-5,-6,50,3], 4))
print(max_avg_subarray([5], 1))

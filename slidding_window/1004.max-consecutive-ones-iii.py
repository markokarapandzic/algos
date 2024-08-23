def longestOnes(nums, k):
	max_result = 0
	left = 0
	max_error = 0
	
	for right in range(len(nums)):
		if nums[right] == 0:
			max_error += 1
		
		while max_error > k:
			if nums[left] == 0:
				max_error -= 1
			left += 1
		
		max_result = max(max_result, right - left + 1)

	return max_result

print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)) # 6
print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)) # 10

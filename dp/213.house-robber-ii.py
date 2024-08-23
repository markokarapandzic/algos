def rob(nums):
	prev, curr = 0, 0

	# [prev, curr, n, n + 1]
	for n in nums:
		temp = max(prev + n, curr)
		prev = curr
		curr = temp

	return curr

def rob2(nums):
	return max(nums[0], rob(nums[1:]), rob(nums[:-1]))

print(rob2([1,2,3,1]))
print(rob2([2,7,9,3,1]))

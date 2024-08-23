def rob(nums):
	prev, curr = 0, 0

	# [prev, curr, n, n + 1]
	for n in nums:
		temp = max(prev + n, curr)
		prev = curr
		curr = temp

	return curr

print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))

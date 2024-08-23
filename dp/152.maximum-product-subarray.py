def maxProduct(nums):
	if not nums:
		return 0
		
	# Initialize the maximum and minimum products as the first element
	max_product_so_far = nums[0]
	min_product_so_far = nums[0]
	result = nums[0]
	
	# Iterate through the array starting from the second element
	for num in nums[1:]:
		# Store the current max product temporarily
		temp_max = max_product_so_far
		
		# Update the maximum product up to the current index
		max_product_so_far = max(num, num * max_product_so_far, num * min_product_so_far)
		
		# Update the minimum product up to the current index
		min_product_so_far = min(num, num * temp_max, num * min_product_so_far)
		
		# Update the result if the current max product is greater than the result
		result = max(result, max_product_so_far)
	
	return result

print(maxProduct([2,3,-2,4]))
print(maxProduct([-2,0,-1]))
print(maxProduct([-3,-1,-1]))

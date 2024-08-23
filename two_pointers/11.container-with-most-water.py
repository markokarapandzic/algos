def maxArea(height):
	n = len(height)
	left = 0
	right = n - 1
	max_area = 0

	while left < right:
		area = min(height[left], height[right]) * (right - left)
		max_area = max(max_area, area)

		if height[left] < height[right]:
			left += 1
		else:
			right -= 1
	
	return max_area
	
print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))

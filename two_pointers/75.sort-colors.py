def sortColors(nums):
	left, right = 0, len(nums) - 1	
	current = 0

	while current <= right:
		if nums[current] == 0:
			nums[current], nums[left] = nums[left], nums[current]
			left += 1
			current += 1
		elif nums[current] == 2:
			nums[current], nums[right] = nums[right], nums[current]
			right -= 1
		else:
			current += 1

testArray1 = [2,0,2,1,1,0]
sortColors(testArray1)
print(testArray1)

testArray2 = [2,0,1]
sortColors(testArray2)
print(testArray2)

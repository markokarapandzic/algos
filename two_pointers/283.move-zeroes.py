def moveZeroes(nums):
	left = right = 0

	while right < len(nums):
		while nums[left] == 0 and right < len(nums):
			if nums[right] != 0:
				nums[left] = nums[right]	
				nums[right] = 0
				left += 1
			else:
				right += 1
		
		right += 1
		left += 1

testArray1 = [0,1,0,3,12]
moveZeroes(testArray1)
print(testArray1)

testArray2 = [0]
moveZeroes(testArray2)
print(testArray2)

testArray3 = [1, 2, 3, 0, 0, 0, 9, 12, 0, 53, 0, 0, 123]
moveZeroes(testArray3)
print(testArray3)

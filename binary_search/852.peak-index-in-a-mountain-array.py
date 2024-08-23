def peakIndexInMountainArray(arr):
	left, right = 0, len(arr) - 1

	while left < right:
		mid = left + (right - left) // 2

		if arr[mid] < arr[mid + 1]:
			left = mid + 1
		else:
			right = mid

	return left

print(peakIndexInMountainArray([0,1,0]))
print(peakIndexInMountainArray([0,2,3,0]))
print(peakIndexInMountainArray([0,10,5,2]))

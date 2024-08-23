def search(nums, target):
	def binary_search(arr, x, left, right):
		if left > right:
			return -1

		mid = left + (right - left) // 2

		if arr[mid] == x:
			return mid
		elif x > arr[mid]:
			return binary_search(arr, x, mid + 1, right)
		else:
			return binary_search(arr, x, left, mid - 1)

	return binary_search(nums, target, 0, len(nums) - 1)

print(search([-1,0,3,5,9,12], 9))
print(search([-1,0,3,5,9,12], 2))

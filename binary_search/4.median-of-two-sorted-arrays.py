def findMedianSortedArrays(nums1, nums2):
	arr = []
	index1 = 0
	index2 = 0

	while index1 < len(nums1) and index2 < len(nums2):
		if nums1[index1] < nums2[index2]:
			arr.append(nums1[index1])
			index1 += 1
		else:
			arr.append(nums2[index2])
			index2 += 1

	return arr

print(findMedianSortedArrays([1,3], [2]))
print(findMedianSortedArrays([1,2], [3,4]))

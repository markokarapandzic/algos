def nextGreatestLetter(letters, target):
	left, right = 0, len(letters) - 1

	while left <= right:
		mid = left + (right - left) // 2

		if target < letters[mid]:
			right = mid - 1
		else:
			left = mid + 1

	return letters[left % len(letters)]
	
print(nextGreatestLetter(["c","f","j"], "a"))
print(nextGreatestLetter(["c","f","j"], "c"))
print(nextGreatestLetter(["x","x","y","y"], "z"))
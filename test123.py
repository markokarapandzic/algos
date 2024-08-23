def merge_sort(arr):
	mid = len(arr) // 2
	left = arr[:mid]
	right = arr[mid:]

	merge_sort(left)
	merge_sort(right)

	merge(arr, left, right)

def merge(arr, left_half, right_half):
	i = j = k = 0

	while i < len(left_half) and j < len(right_half):
		if left_half[i] < right_half[j]:
			arr[k] = left_half[i]
			i += 1
		else:
			arr[k] = right_half[j]
			j += 1
		k += 1

	# Check for any remaining elements in left_half
	while i < len(left_half):
		arr[k] = left_half[i]
		i += 1
		k += 1

	# Check for any remaining elements in right_half
	while j < len(right_half):
		arr[k] = right_half[j]
		j += 1
		k += 1

my_list = [38, 27, 43, 3, 9, 82, 10]
merge_sort(my_list)
print(my_list)

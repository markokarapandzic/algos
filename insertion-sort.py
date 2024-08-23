def insertion_sort(arr):
	for index in range(1, len(arr)):
		key = arr[index]
		j = index - 1

		while j >= 0 and arr[j] > key:
			arr[j + 1] = arr[j]
			j -= 1

		arr[j + 1] = key
	
	return arr

print(insertion_sort([5, 3, 4, 1, 2]))
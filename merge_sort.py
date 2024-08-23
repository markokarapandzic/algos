def insertion_sort(arr):
	for index in range(1, len(arr)):
		key = arr[index]
		j = index - 1

		while j >= 0 and arr[j] > key:
			arr[j + 1] = arr[j]
			j -= 1

		arr[j + 1] = key
	
	print("Insertion Sort:", arr)

def merge_sort(arr):
	if len(arr) > 1:
		mid = len(arr) // 2  # Find the middle of the array
		left_half = arr[:mid]  # Divide the array into two halves
		right_half = arr[mid:]

		merge_sort(left_half)  # Recursively sort the left half
		merge_sort(right_half)  # Recursively sort the right half

		if len(arr) > 4:
			# Merge the sorted halves
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
			
			print("Merge Sort:", arr)
		else:
			insertion_sort(arr)

# Example usage:
my_list = [38, 27, 43, 3, 9, 82, 10]
merge_sort(my_list)
print("Sorted array:", my_list)

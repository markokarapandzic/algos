def max_subarray(arr, k):
	current_sum = 0
	max_sum = 0

	for i in range(len(arr)):
		current_sum += arr[i]

		if i >= k - 1:
			max_sum = max(max_sum, current_sum)
			current_sum -= arr[i - k + 1]

	return max_sum

print(max_subarray([3, 5, 2, 1, 7], 2))
print(max_subarray([3, 5, 2, 1, 7], 3))
print(max_subarray([1, 2, 3, 4, 5], 2))

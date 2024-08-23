import sys

def getMinMaxDiff(arr, k):
	max_diff = 0.0
	min_diff = float("inf")
	current_sum = 0

	for i in range(len(arr)):
		current_sum += arr[i]

		if i >= k - 1:
			current_diff = current_sum / k
			max_diff = max(max_diff, current_diff)
			min_diff = min(min_diff, current_diff)
			current_sum -= arr[i - k + 1]

	return max_diff - min_diff

print(getMinMaxDiff([3, 8, 9, 15], 2))
print(getMinMaxDiff([3, 8, 9, 15], 3))
print(getMinMaxDiff([1, 2, 3, 4], 2))

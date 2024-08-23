import heapq

def kthSmallest(matrix, k):
	n = len(matrix)
	min_heap = []

	for r in range(min(k, n)):
		heapq.heappush(min_heap, (matrix[r][0], r, 0))

	count = 0
	while min_heap:
		value, row, col = heapq.heappop(min_heap)
		count += 1

		if count == k:
			return value

		if col + 1 < n:
			heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))

matrix = [
	[1, 5, 9],
	[10, 11, 13],
	[12, 13, 15]
]

k = 8
print(kthSmallest(matrix, k))

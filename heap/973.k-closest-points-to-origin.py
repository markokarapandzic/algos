import heapq
from math import sqrt

def kClosest(points, k):
	maxHeap = []

	for (x, y) in points:
		distance = sqrt(x ** 2 + y ** 2)
		heapq.heappush(maxHeap, (-distance, [x, y]))

		if len(maxHeap) > k:
			heapq.heappop(maxHeap)

	return [point for (_, point) in maxHeap]

	# result = []

	# for (x, y) in points:
	# 	distance = sqrt(x ** 2 + y ** 2)
	# 	result.append((distance, [x, y]))

	# sorted_result = sorted(result, key=lambda x: x[0])
	# sorted_result = [point for (_, point) in sorted_result]

	# return sorted_result[:k]

print(kClosest([[1,3], [-2,2]], 1))
print(kClosest([[3,3], [5,-1], [-2,4]], 2))

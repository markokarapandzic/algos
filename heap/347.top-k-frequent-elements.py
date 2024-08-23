import heapq
from typing import Counter

def topKFrequent(nums, k):
	counter = Counter(nums)
	maxHeap = [(-count, item) for (item, count) in counter.items()]

	heapq.heapify(maxHeap)

	result = []

	for _ in range(k):
		_, val = heapq.heappop(maxHeap)
		result.append(val)

	return result

print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([1], 1))

import heapq
from typing import Counter

def frequencySort(s):
	counter = Counter(s)
	maxHeap = [(-count, item) for item, count in counter.items()]
	heapq.heapify(maxHeap)
	result = ""

	while maxHeap:
		count, val = heapq.heappop(maxHeap)
		count = -count

		for _ in range(count):
			result += val

	return result

print(frequencySort("tree"))
print(frequencySort("cccaaa"))
print(frequencySort("Aabb"))

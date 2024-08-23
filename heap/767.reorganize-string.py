from collections import deque
import heapq
from typing import Counter

def reorganizeString(s):
	counter = Counter(s)
	maxHeap = [(-count, key) for key, count in counter.items()]
	heapq.heapify(maxHeap)

	q = deque()
	time = 0
	result = ""

	while maxHeap or q:
		time += 1

		if maxHeap:
			count, val = heapq.heappop(maxHeap)

			if len(result) > 0 and val == result[-1]:
				return ""

			count = count + 1
			result += val

			if count:
				q.append([time + 1, (count, val)])

		if q and q[0][0] == time:
			heapq.heappush(maxHeap, q.popleft()[1])

	return result

print(reorganizeString("aab"))
print(reorganizeString("aaab"))

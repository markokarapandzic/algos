from collections import deque
import heapq
from typing import Counter

def leastInterval(tasks, n):
	count = Counter(tasks)
	maxHeap = [-cnt for cnt in count.values()]
	heapq.heapify(maxHeap)

	time = 0
	q = deque()

	while maxHeap or q:
		time += 1

		if maxHeap:
			cnt = 1 + heapq.heappop(maxHeap)

			if cnt:
				q.append([cnt, time + n])
		
		if q and q[0][1] == time:
			heapq.heappush(maxHeap, q.popleft()[0])

	return time

print(leastInterval(["A","A","A","B","B","B"], 2))

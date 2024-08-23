import heapq

def findKthLargest(nums, k):
	minHeap = []

	for index in range(len(nums)):
		heapq.heappush(minHeap, nums[index])

		if len(minHeap) > k:
			heapq.heappop(minHeap)

	return heapq.heappop(minHeap)

print(findKthLargest([3,2,1,5,6,4], 2))
print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))

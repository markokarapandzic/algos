import heapq
from typing import List

class KthLargest:
  def __init__(self, k: int, nums: list[int]):
    self.k = k
    self.nums = nums
    heapq.heapify(self.nums)

    while len(self.nums) > k:
      heapq.heappop(self.nums)

  def add(self, val: int) -> int:
    heapq.heappush(self.nums, val)

    if len(self.nums) > self.k:
      heapq.heappop(self.nums)

    return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(1, [])
print(obj.add(-3))
print(obj.add(-2))
print(obj.add(-4))
print(obj.add(0))
print(obj.add(4))

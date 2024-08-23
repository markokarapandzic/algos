from typing import List

class NumArray:
  def __init__(self, nums: List[int]):
    self.nums = [0] * (len(nums) + 1)

    for i in range(len(nums)):
      self.nums[i + 1] = self.nums[i] + nums[i]

  def sumRange(self, left: int, right: int) -> int:
    return self.nums[right + 1] - self.nums[left]

# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2,0,3,-5,2,-1])
print(obj.sumRange(0,2))
print(obj.sumRange(2,5))
print(obj.sumRange(0,5))

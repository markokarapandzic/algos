import sys

def threeSumClosest(nums, target):
	nums.sort()
	best_sum = sys.maxsize

	for i in range(len(nums) - 2):
		left = i + 1
		right = len(nums) - 1

		while left < right:
			current_sum = nums[i] + nums[left] + nums[right]

			if abs(target - current_sum) < abs(target - best_sum):
				best_sum = current_sum

			if current_sum > target:
				right -= 1
			elif current_sum < target:
				left += 1
			else:
				return current_sum

	return best_sum

print(threeSumClosest([-1,2,1,-4], 1))
print(threeSumClosest([0, 0, 0], 1))
print(threeSumClosest([1,1,1,0], 100))
print(threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))
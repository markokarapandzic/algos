table = {}
def majority_element(nums):
  if len(nums) == 1:
    checkRepeating(nums[0])
  else:
    lastItem = nums.pop()
    checkRepeating(lastItem)

    majority_element(nums)

def checkRepeating(lastItem):
  if lastItem in table:
    table[lastItem] = table[lastItem] + 1
  else:
    table[lastItem] = 0

majority_element([3,2,3])

max = 0
for key in table:
  if table[key] > 0:
    max = table[key]

print(max)

from collections import Counter

def totalFruit(fruits):
	types = {}
	unique_types = 0
	max_len = 0
	current_len = 0
	left = 0
	right = 0

	for right in range(len(fruits)):
		current_len += 1
		types[fruits[right]] = types.get(fruits[right], 0) + 1

		if types[fruits[right]] == 1:
			unique_types += 1

		if unique_types <= 2:
			max_len = max(max_len, right - left + 1)
			right += 1

		while unique_types > 2:
			left_type = fruits[left]
			types[left_type] -= 1

			if types[left_type] == 0:
				unique_types -= 1

			left += 1

	return max_len
			
	
print(totalFruit([1,2,1]))
print(totalFruit([0,1,2,2]))
print(totalFruit([1,2,3,2,2]))
print(totalFruit([3,3,3,1,2,1,1,2,3,3,4]))

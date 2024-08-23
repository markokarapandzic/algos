from collections import Counter

def findOriginalArray(changed):
	if len(changed) % 2 != 0:
		return []

	count = Counter(changed)

	changed.sort()

	result = []

	for x in changed:
		if count[x] == 0:
			continue

		if count[x * 2] == 0:
			return []

		result.append(x)

		count[x] -= 1
		count[x * 2] -= 1

	return result

print(findOriginalArray([1,3,4,2,6,8]))

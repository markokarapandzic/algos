def missingRolls(rolls, mean, n):
	mSum = sum(rolls)
	nSum = mean * (n + len(rolls)) - mSum

	if nSum < n or nSum > n * 6:
		return []

	parts, remainders = divmod(nSum, n)

	result = [parts] * n

	for i in range(remainders):
		result[i] += 1

	return result

print(missingRolls([3,2,4,3], 4, 2))
print(missingRolls([1,5,6], 3, 4))
print(missingRolls([1,2,3,4], 6, 4))

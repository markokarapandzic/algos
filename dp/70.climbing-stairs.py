def climbStairs(n):
	first, second = 1, 1

	for _ in range(n - 1):
		first, second = first + second, first

	return first

print(climbStairs(2))
print(climbStairs(3))

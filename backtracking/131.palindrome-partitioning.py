def partition(s):
	n = len(s)
	result = []

	def backtrack(start, path):
		if start == n:
			result.append(path[:])
			return

		for i in range(start + 1, n + 1):
			substring = s[start:i]

			if substring == substring[::-1]: # Is Palindrome
				path.append(substring)
				backtrack(i, path)
				path.pop()

	backtrack(0, [])

	return result

print(partition("aab"))
print(partition("a"))

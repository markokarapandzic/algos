def generateParenthesis(n):
	result = []

	def backtrack(path, open_count, close_count):
		if len(path) == n * 2:
			result.append(path)
			return

		if open_count < n:
			backtrack(path + "(", open_count + 1, close_count)
		if close_count < open_count:
			backtrack(path + ")", open_count, close_count + 1)

	backtrack("", 0, 0)

	return result
	
print(generateParenthesis(3))
print(generateParenthesis(1))

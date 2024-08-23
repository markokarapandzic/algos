def letterCombinations(digits):
	if digits == "":
		return []

	n = len(digits)
	result = []

	numbers = {
		'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
		'6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
	}

	def backtrack(number, path):
		if len(path) == n:
			result.append("".join(path))
			return

		first = numbers[digits[number]]
		for letter in first:	
			path.append(letter)
			backtrack(number + 1, path)
			path.pop()

	backtrack(0, [])

	return result

print(letterCombinations("23"))
print(letterCombinations(""))
print(letterCombinations("2"))

def convertToTitle(columnNumber):
	result = []

	while columnNumber > 0:
		columnNumber -= 1
		result.append(chr(columnNumber % 26 + ord("A")))
		columnNumber //= 26

	return "".join(result[::-1])

# print(convertToTitle(1))
# print(convertToTitle(2))
# print(convertToTitle(701))

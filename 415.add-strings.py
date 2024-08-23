def addStrings(num1, num2):
	index1 = len(num1) - 1
	index2 = len(num2) - 1
	result = ""

	while index1 >= 0 or index2 >= 0:
		first = 0 if index1 < 0 else int(num1[index1])	
		second = 0 if index2 < 0 else int(num2[index2])

		result += str(first + second)

		index1 -= 1
		index2 -= 1

	return result[::-1]

print(addStrings("11", "123"))
print(addStrings("456", "77"))
print(addStrings("0", "0"))
print(addStrings("11111", "11111"))

from collections import Counter

def largestPalindromic(num):
	uniqueNums = Counter(num)

	middle = ""
	leftHalf = []

	for i in range(9, -1, -1):
		numberString = str(i)

		if uniqueNums[numberString] >= 2 and (numberString != '0' or leftHalf):
			leftHalf.append(numberString * (uniqueNums[numberString] // 2))

		if uniqueNums[numberString] % 2 == 1 and middle == "":
			middle = numberString

	leftHalf = "".join(leftHalf)

	if leftHalf == "" and middle == "0":
		return "0"

	return leftHalf + middle + leftHalf[::-1]

num = "444947137"
print(largestPalindromic(num))  # Output: "7449447"
print(largestPalindromic("00009"))

def maxLength(arr):
	def backtrack(index, currentString):
		nonlocal maxLen

		if len(set(currentString)) == len(currentString):
			maxLen = max(maxLen, len(currentString))
		else:
			return

		for i in range(index, len(arr)):
			backtrack(index + 1, currentString + arr[i])

	maxLen = 0
	backtrack(0, "")
	return maxLen

print(maxLength(["un","iq","ue"]))
print(maxLength(["cha","r","act","ers"]))
print(maxLength(["abcdefghijklmnopqrstuvwxyz"]))

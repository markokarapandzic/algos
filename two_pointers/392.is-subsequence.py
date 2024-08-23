def isSubsequence(s, t):
	if s == "":
		return True

	subsequenceIndex = 0

	for i in range(len(t)):
		if s[subsequenceIndex] == t[i]:
			subsequenceIndex += 1

		if subsequenceIndex > len(s) - 1:
			break

	return subsequenceIndex == len(s)

print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("axc", "ahbgdc"))
print(isSubsequence("", "ahbgdc"))
print(isSubsequence("b", "abc"))

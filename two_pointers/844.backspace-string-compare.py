def backspaceCompare(s, t):
	i, j = len(s) - 1, len(t) - 1
	skip_s = skip_t = 0

	while i >= 0 and j >= 0:
		while i >= 0 and (s[i] == "#" or skip_s > 0):
			skip_s += 1 if s[i] == "#" else -1
			i -= 1

		while j >= 0 and (t[j] == "#" or skip_t > 0):
			skip_t += 1 if t[j] == "#" else -1
			j -= 1

		if i < 0 and j < 0:
			return True
		elif i >= 0 and j >= 0 and s[i] == t[j]:
			i -= 1
			j -= 1
		else:
			return False

	return True

s = "ab#c"
t = "ad#c"
print(backspaceCompare(s, t))

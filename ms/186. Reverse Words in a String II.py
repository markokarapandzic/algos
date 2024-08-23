def reverseWords(s):
	def reverse(l, r):
		while l < r:
			s[l], s[r] = s[r], s[l]
			l += 1
			r -= 1

	reverse(0, len(s) - 1)

	start = 0
	n = len(s)

	while start < n:
		end = start

		while end < n and s[end] != " ":
			end += 1

		reverse(start, end - 1)

		start = end + 1

	return s

s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
reverseWords(s)
print(s)
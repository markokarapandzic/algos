def lcs(s1, s2):
	m = len(s1) + 1
	n = len(s2) + 1

	dp = [[0 for _ in range(n)] for _ in range(m)]

	# Fill Table
	for i in range(1, m):
		for j in range(1, n):
			if s1[i - 1] == s2[j - 1]:
				dp[i][j] = 1 + dp[i - 1][j - 1]
			else:
				dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

	# Backtrack to find the LCS
	lcs_str = ""
	i, j = m - 1, n - 1
	while i > 0 and j > 0:
		if s1[i - 1] == s2[j - 1]:
			lcs_str = s1[i - 1] + lcs_str
			i -= 1
			j -= 1
		elif dp[i - 1][j] > dp[i][j - 1]:
			i -= 1
		else:
			j -= 1

	return lcs_str

# Example usage
sentence1 = "shine bright like a diamond"
sentence2 = "let your light shine"

lcs_result = lcs(sentence1.split(), sentence2.split())
print("Longest Common Subsequence:", lcs_result)
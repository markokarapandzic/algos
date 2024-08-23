def pascal_triangle(numRows):
	dp = [[1]]

	for i in range(1, numRows):
		row = [1]

		for j in range(1, i):
			row.append(dp[i - 1][j] + dp[i - 1][j - 1])

		row.append(1)
		dp.append(row)
	
	return dp

print(pascal_triangle(1)) # [[1]]
print(pascal_triangle(2)) # [[1], [1,1]]
print(pascal_triangle(5)) # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

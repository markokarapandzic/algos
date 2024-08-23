def fibo(n):
	if n <= 1:
		return n

	dp = [0] * (n + 1)
	dp[0] = 0
	dp[1] = 1

	for i in range(2, n + 1):
		dp[i] = dp[i - 2] + dp[i - 1]

	return dp[n]

def rod_cutting(prices, n):
	if n <= 0:
		return 0	

	dp = [0] * (n + 1)

	for i in range(1, n + 1):
		for j in range(1, i + 1):
			dp[i] = max(dp[i], prices[j - 1] + dp[i - j])

	return dp[n]

prices = [1, 5, 8, 9, 10]
n = 4
max_revenue = rod_cutting(prices, n)
print("Maximum revenue from cutting rod of length", n, ":", max_revenue)

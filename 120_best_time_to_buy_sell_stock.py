def best_buy(prices):
	prices_length = len(prices)
	dp = [0] * prices_length
	min_price = prices[0]

	for i in range(1, prices_length):
		dp[i] = max(dp[i - 1], prices[i] - min_price)
		min_price = min(prices[i], min_price)

	return dp[-1]

print(best_buy([7,1,5,3,6,4])) # 5
print(best_buy([7,6,4,3,1])) # 0

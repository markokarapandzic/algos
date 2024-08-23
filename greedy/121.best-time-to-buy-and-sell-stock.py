def maxProfit(prices):
	if not prices:
		return 0

	minPrice = float('inf')
	maxRes = 0

	for price in prices:
		minPrice = min(minPrice, price)
		maxRes = max(maxRes, price - minPrice)

	return maxRes

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))

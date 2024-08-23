def buyChoco(prices, money):
	prices.sort()

	total = prices[0] + prices[1]

	if money - total >= 0:
		return money - total
	else:
		return money

print(buyChoco([1,2,2], 3))
print(buyChoco([3,2,3], 3))
print(buyChoco([98,54,6,34,66,63,52,39], 62))

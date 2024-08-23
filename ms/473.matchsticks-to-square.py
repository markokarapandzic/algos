def makesquare(matchsticks):
	if not matchsticks:
		return False

	perimiter = sum(matchsticks)

	if perimiter % 4 != 0:
		return False

	side_length = perimiter / 4	
	sides = [0] * 4

	def backtrack(index):
		if sides[0] == sides[1] == sides[2] == sides[3] == side_length:
			return True

		for i in range(4):
			if sides[i] + matchsticks[index] > side_length:
				continue

			sides[i] += matchsticks[index]

			if backtrack(index + 1):
				return True

			sides[i] -= matchsticks[index]

			if sides[i] == 0:
				break

		return False
	
	return backtrack(0)

print(makesquare([1,1,2,2,2]))
print(makesquare([3,3,3,3,4]))

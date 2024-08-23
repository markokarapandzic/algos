def minimumMoves(grid):
	surplus = []
	deficit = []

	for row in range(3):
		for col in range(3):
			if grid[row][col] > 1:
				surplus.append((row, col, grid[row][col] - 1))
			elif grid[row][col] == 0:
				deficit.append((row, col))

	moves = 0

	for sur in surplus:
		surRow, surCol, amount = sur

		while amount > 0 and deficit:
			defRow, defCol = deficit.pop(0)

			distance = abs(surRow - defRow) + abs(surCol - defCol)
			moves += distance
			amount -= 1

	return moves

print(minimumMoves([[1,1,0],[1,1,1],[1,2,1]]))
print(minimumMoves([[1,3,0],[1,0,0],[1,0,3]]))
print(minimumMoves([[1,2,2],[1,1,0],[0,1,1]]))

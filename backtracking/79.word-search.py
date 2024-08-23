def exist(board, word):
	rows, cols = len(board), len(board[0])
	path = set()

	def dfs(row, col, index):
		if index == len(word):
			return True
		elif (
			row < 0 or col < 0 or
			row >= rows or col >= cols or
			word[index] != board[row][col] or
			(row, col) in path
		):
			return False

		path.add((row, col))

		result = (
			dfs(row + 1, col, index + 1) or
			dfs(row - 1, col, index + 1) or
			dfs(row, col + 1, index + 1) or
			dfs(row, col - 1, index + 1)
		)

		path.remove((row, col))

		return result

	for i in range(rows):
		for j in range(cols):
			if dfs(i, j, 0):
				return True

	return False

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))

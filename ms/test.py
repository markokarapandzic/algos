from collections import deque

def numIslands(grid):
	islands = 0
	visited = set()

	def bfs(r, c):
		q = deque([(r, c)])
		visited.add((r, c))

		while q:
			curRow, curCol = q.popleft()
			directions = [[1, 0], [0, 1]]

			for dr, dc in directions:
				newRow, newCol = curRow + dr, curCol + dc
				if newRow in range(len(grid)) and newCol in range(len(grid[0])) and grid[newRow][newCol] == "1" and (newRow, newCol) not in visited:
					visited.add((newRow, newCol))
					q.append((newRow, newCol))

	for row in range(len(grid)):
		for col in range(len(grid[0])):
			if grid[row][col] == "1" and (row, col) not in visited:
				bfs(row, col)
				islands += 1

	return islands

print(numIslands([
	["1","1","1","1","0"],
	["1","1","0","1","0"],
	["1","1","0","0","0"],
	["0","0","0","0","0"]
]))

print(numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
from collections import deque

def numIslands(grid):
	if not grid:
		return 0

	rows, cols = len(grid), len(grid[0])
	visited = set()
	islands = 0

	def bfs(r, c):
		q = deque()
		q.append((r, c))
		visited.add((r, c))
		
		while q:
			row, col = q.popleft()
			directions = [[1, 0],  [0, 1]]

			for dr, dc in directions:
				dRow, dCol = row + dr, col + dc

				if (
					dRow in range(rows) and
					dCol in range(cols) and
					grid[dRow][dCol] == "1" and
					(dRow, dCol) not in visited
				):
					q.append((dRow, dCol))
					visited.add((dRow, dCol))

	for r in range(rows):
		for c in range(cols):
			if grid[r][c] == "1" and (r, c) not in visited:
				bfs(r, c)
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

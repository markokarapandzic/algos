from typing import List

def minimumEffortPath(heights: List[List[int]]) -> int:
	rows = len(heights)
	columns = len(heights[0])
	min_diff = float('inf')
	visited = set()

	def dfs(row, col, current_diff, prev_value):
		nonlocal min_diff

		if row < 0 or row > rows - 1 or col < 0 or col > columns - 1 or (row, col) in visited:
			return

		new_diff = max(current_diff, heights[row][col] - prev_value)

		if row == rows - 1 and col == columns - 1:
			min_diff = min(min_diff, new_diff)
			return

		visited.add((row, col))
		dfs(row + 1, col, new_diff, heights[row][col])
		dfs(row - 1, col, new_diff, heights[row][col])
		dfs(row, col + 1, new_diff, heights[row][col])
		dfs(row, col - 1, new_diff, heights[row][col])
		visited.remove((row, col))
	
	dfs(0, 0, 0, heights[0][0])

	return min_diff

print(minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))
print(minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))
print(minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))

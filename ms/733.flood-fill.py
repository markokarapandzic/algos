def floodFill(image, sr, sc, color):
	current_color = image[sr][sc]

	if current_color == color:
		return image

	def dfs(r, c):
		if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != current_color:
			return

		image[r][c] = color

		dfs(r + 1, c)
		dfs(r, c + 1)
		dfs(r - 1, c)
		dfs(r, c - 1)

	dfs(sr, sc)

	return image

print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))

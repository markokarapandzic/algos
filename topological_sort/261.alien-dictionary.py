def alienOrder(words):
	adj = { c: set() for word in words for c in word }

	for i in range(len(words) - 1):
		w1, w2 = words[i], words[i + 1]
		minWord = min(len(w1), len(w2))

		if len(w1) > len(w2) and w1[:minWord] == w2[:minWord]:
			return ""

		for j in range(minWord):
			if w1[j] != w2[j]:
				adj[w1[j]].add(w2[j])
				break

	visited = {}
	result = []

	def dfs(char):
		if char in visited:
			return visited[char]

		for neighbour in adj[char]:
			if dfs(neighbour):
				return True

		visited[char] = False
		result.append(char)

	for char in adj:
		if dfs(char):
			return ""

	result.reverse()

	return "".join(result)

print(alienOrder([
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]))

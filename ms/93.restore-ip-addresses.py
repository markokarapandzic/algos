def restoreIpAddresses(s):
	def backtrack(start, path):
		if len(path) == 4:
			if start == len(s):
				result.append(".".join(path))
			return

		for length in range(1, 4):
			if start + length > len(s):
				break

			segment = s[start:start + length]

			if (segment[0] == "0" and len(segment) > 1) or int(segment) > 255:
				continue

			backtrack(start + length, path + [segment])

	result = []
	backtrack(0, [])

	return result

print(restoreIpAddresses("25525511135"))  # Output: ["255.255.11.135","255.255.111.35"]
print(restoreIpAddresses("0000"))         # Output: ["0.0.0.0"]
print(restoreIpAddresses("101023"))       # Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

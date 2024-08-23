def removeDuplicateLetters(s: str) -> str:
	last_occurance = {char: index for index, char in enumerate(s)}
	seen = set()
	stack = []

	for index, char in enumerate(s):
		if char in seen:
			continue

		while stack and char < stack[-1] and last_occurance[stack[-1]] > index:
			seen.remove(stack.pop())

		stack.append(char)
		seen.add(char)

	return "".join(stack)

print(removeDuplicateLetters("bcabc"))  # Output: "abc"
print(removeDuplicateLetters("cbacdcbc"))  # Output: "acdb"

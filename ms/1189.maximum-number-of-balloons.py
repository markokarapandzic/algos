from collections import Counter

def maxNumberOfBalloons(text):
	balloon_count = Counter("balloon")
	text_count = Counter(text)

	return min(text_count[char] // balloon_count[char] for char in balloon_count)

print(maxNumberOfBalloons("nlaebolko"))
print(maxNumberOfBalloons("loonbalxballpoon"))

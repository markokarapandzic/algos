from collections import Counter

def characterReplacement(s, k):
	max_result = 0
	left = 0
	current_char_count = Counter()

	for right in range(len(s)):
		current_char_count[s[right]] += 1

		most_repeated_chars = current_char_count.most_common(1)[0][1]

		if right - left + 1 - most_repeated_chars > k:
			current_char_count[s[left]] -= 1
			left += 1

		max_result = max(max_result, right - left + 1)

	return max_result

print(characterReplacement("ABAB", 2))
print(characterReplacement("AABABBA", 1))
print(characterReplacement("AAAABBA", 1))
print(characterReplacement("AABBBBA", 1))

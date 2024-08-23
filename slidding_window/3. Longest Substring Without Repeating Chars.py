from collections import Counter

def lengthOfLongestSubstring(s):
	max_result = 0
	current_window_count = Counter()
	left = 0

	for right in range(len(s)):
		current_window_count[s[right]] += 1

		most_frequent_char = current_window_count.most_common(1)[0][1]

		while most_frequent_char > 1:
			current_window_count[s[left]] -= 1
			left += 1
			most_frequent_char = current_window_count.most_common(1)[0][1]

		max_result = max(max_result, right - left + 1)

	return max_result

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))

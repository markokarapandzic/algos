vowels = {'a', 'e', 'i', 'o', 'u'}

def maxVowels(s, k):
	max_count = 0
	left = 0
	vowels_count = 0

	for right in range(len(s)):
		if s[right] in vowels and vowels_count < k:
			vowels_count += 1

		if right - left + 1 > k:
			if s[left] in vowels:
				vowels_count -= 1
			left += 1

		max_count = max(max_count, vowels_count)
	
	return max_count

print(maxVowels("abciiidef", 3))
print(maxVowels("aeiou", 2))
print(maxVowels("leetcode", 3))
print(maxVowels("ramadan", 2))

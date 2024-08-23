from collections import Counter

def find_anagram_count(text, word):
	word_char_count = Counter(word)
	window_size = len(word)
	anagram_occurance = 0

	for i in range(len(text)):
		window_char_count = Counter(text[i:i + window_size])

		if window_char_count == word_char_count:
			anagram_occurance += 1

	return anagram_occurance

word = "act"
text = "forxxet ekt cata act ttttac"
anagram_count = find_anagram_count(text, word)
print("The number of occurrences of " + word + "anagrams in the text is: " + str(anagram_count))

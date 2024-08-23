from collections import Counter

def checkInclusion(s1, s2):
	s1_count = Counter(s1)
	s1_len = len(s1)
	s2_len = len(s2)
	
	for i in range(s2_len - (s1_len - 1)):
		current_window_count = Counter(s2[i:i + len(s1)])

		if s1_count == current_window_count:
			return True
	
	return False

print(checkInclusion("ab", "eidbaooo"));
print(checkInclusion("ab", "eidboaoo"));
print(checkInclusion("abc", "eiaaooabc"));
print(checkInclusion("aeg", "eidboaoo"));
print(checkInclusion("klh", "eidbolhk"));

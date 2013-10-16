def is_reverse_pair(word1, word2):
	rev_word1 = word1[::-1]
	if rev_word1 == word2:
		return True
	return False

print is_reverse_pair('keep','peek')
#Trouble downloading the pronouncing dictionary.
#I'm going to pretend it works anyway.
def is_homophone(word1, word2, phonetic):
	if word1 or word2 not in phonetic:
		return False
	return phonetic[word1] == phonetic[word2]

def sovlve_homophone_puzzle(word_list, phonetic):
	for word in word_list:
		word_new = word[1:]
		if word_new in word_list:
			if is_homophone(word, word_new) == True
				new_word_new = word[0] + word[2:]
				if new_word_new in word_list:
					if is_homophone(word, new_word_new) == True:
						return word, word_new, new_word_new
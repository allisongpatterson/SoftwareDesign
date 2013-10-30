def interlock(word1, word2):
	locked = ''
	if len(word1) >= len(word2):
		for i in range(len(word1)):
			locked += word1[i] + word2[i]
	elif len(word1) < len(word2):
		for i in range(len(word2)):
			locked += word1[i] + word2[i]
	return locked

if __name__ == '__main__':
	print interlock('shoe','cold')
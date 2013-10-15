def is_double(word):
	for i in range (len(word)-1):
		if word[i] == word[i+1]:
			return True
	return False 
# print is_double('beachball')

def is_triple_consecutive_double(word):
	i = 0
	count = 0
	while i < (len(word)-1):
		if word[i] == word[i+1]:
			count += 1
			i += 2
			if count == 3:
				return True
		else:
			count = 0
			i += 1
	return False

# print is_triple_consecutive_double('bookkeeper')
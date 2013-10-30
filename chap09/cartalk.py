def is_double(word):
	for i in range (len(word)-1):
		if word[i] == word[i+1]:
			return True
	return False 

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

def whats_my_age():
	diff = 36
	age_mom = 46
	age_kid = 10
	count = 0
	while count < 120:
		if str(age_mom) == str(age_kid)[::-1]:
			print count
			print age_mom
			print age_kid
			count += 1
			age_mom += 1
			age_kid += 1
		else:
			age_mom += 1
			age_kid+= 1
	return

if __name__ == '__main__':
	print is_double('beachball')
	print is_triple_consecutive_double('bookkeeper')
	whats_my_age()
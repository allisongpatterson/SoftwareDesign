def signature(word):
	t = list(word)
	t.sort()
	t = ''.join(t)
	return t

def print_anagram_sets_in_order(d):
	t = []
	for v in d.values():
		t.append(len(v), v)
	t.sort()
	for x in t:
		print x

def anagram_sets(word_list):
	d = {}
	for word in word_list:
		letters = tuple(signature(word))
		if letters not in d:
			d[letters] = [word]
		else:
			d[letters].append(word)
	return d
	print_anagram_sets_in_order(d)
def find_children(word):
	for i in range(len(word)):
		children = []
		child = word[:i] + word[i+1:]
		if child in word_list:
			children.append(child)
	return children

def is_reducible(word_list):
	for word in word_list:
		if word in memo:
			return memo[word]
		children = find_children(word)
		res = []
		for child in children:
			if child in word_list:
				res.append(child)
				is_reducible(child)
		memo[word] = res
		return res
# visual model of how code should work:
"my name is Allison and my favorite color is rainbow and my favorite food is sugar."
{
	'my': ['name','favorite','favorite'],
	'name': ['is'],
	'is': ['Allison','rainbow'],
	'Allison': ['and'],
	'and': ['my'],
	'favorite': ['color','food'],
	'color': ['is'],
	'rainbow': ['and'],
	'food': ['is'],
	'sugar':[]
}
import random
random.choice(seq)

def markov(text, n):
	d = {}
	for word in text:
		t = []
		pre = word
		suff = word+1 # gahh, my syntax is bad
		if word in d:
			d[pre] = t.append(suff)
		if word not in d:
			d.append(pre)
			d[pre] = t.append(suff)
		return d
	print random.choice(d)
	print random.choice(suff)
import string
def rotate_letter(letter, n):
	if letter.islower():
		start = ord('a')
	else:
		return letter

	char = ord(letter) - start
	char_new = (char + n) % 26 + start
	return chr(char_new)

def rotate_word(word, n):
	res = ''
	for letter in word:
		res = res + rotate_letter(letter, n)
	return res

print rotate_word('cheer', 7)
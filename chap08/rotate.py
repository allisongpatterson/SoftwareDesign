import string
def rotate_letter(letter, n):
	start = ord('a')
	char = ord(letter) - start
	char_new = (char + n) % 26 + start
	return chr(char_new)

def rotate_word(word, n):
	res = ''
	for letter in word:
		res = res + rotate_letter(letter, n)
		return res

if__name__ == '__main__':
	print rotate_word('cheer', 7)
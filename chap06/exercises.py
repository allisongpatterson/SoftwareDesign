def is_power(a, b):
	if b == 0:
		print 'Error: b cannot equal zero.'
	if a%b ==0 and a == b:
		print True
		return True
	if a%b != 0:
		print False
		return False
	is_power(a/b, b)

def gcd(a, b):
	r = a%b
	if r == 0:
		print b
		return b
	if r != 0:
		return gcd(b, r)

if __name__ == '__main__':
	is_power(8, 2)
	gcd(120, 288)
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

is_power(8, 2)
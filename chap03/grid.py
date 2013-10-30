def top_line(n):
	"""Draws top line of grid.py.
	n: positive integer
	"""
	print '+',
	print '- - - - + ' * n

def grid(n):
	"""Draws n by n grid.
	n: positive integer
	"""
	for i in range(n):
		top_line(n)
		for i in range(4):
			print '|         ' * (n+1)
	top_line(n)

if __name__ == '__main__':
	grid(2)
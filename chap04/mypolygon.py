from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def square(t, l):
	"""Draws square with side-length l.
	"""
	for i in range(4):
		fd(t, l)
		lt(t)
	print t

def polygon(t, n, l):
	"""Draws n-sided polygon with side-length l.
	"""
	for i in range(n):
		angle = 360.0/n
		fd(t, l)
		lt(t, angle)
	print t

def circle(t, r):
	"""Draws circle with radius r.
	"""
	circumference = 2 * 3.14159 * r
	n = int(circumference/3) + 1
	l = circumference/n
	polygon(t, n, l)

def arc(t, r, angle):
	"""Draws angle degrees of circle with radius r.
	"""
	arc_length = (2 * 3.14159 * r * angle)/360
	n = int(arc_length/3) + 1
	step_length = arc_length/n
	step_angle = float(angle)/n

	for i in range(n):
		fd(t, step_length)
		lt(t, step_angle)
	print t

if __name__ == '__main__':
	square(bob, 100)
	polygon(bob, 6, 70)
	circle(bob, 50)
	arc(bob, 75, 270)
	wait_for_user()
from mypolygon import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.0001

def flower(t, n, r):
	"""Draws a flower with n petals.
	t: Turtle
	n: positive, even integer
	r: radius
	"""
	for i in range(n):
		arc(t, r, angle = 360.0/n)
		lt(t, ((n/2) - 1) * (360.0/n))
		arc(t, r, angle = 360.0/n)
		lt(t, (n/2) * (360.0/n))

def daisy(t):
	"""Draws a sloppy daisy (just for funsies).
	t: Turtle
	"""
	for i in range(6):
		angle = 60
		for i in range(6):
			angle_new = angle + 120
			angle_current = angle_new + 60
		arc(t, 50, angle_current)
		lt(t, angle_new)
	lt(t)
	circle(t, 85)

if __name__ == '__main__':
	#daisy(bob)
	flower(bob, 12, 180)
	wait_for_user()
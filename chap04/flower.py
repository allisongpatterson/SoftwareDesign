from mypolygon import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.0001

def flower(t, n, r):
	for i in range(n):
		arc(t, r, angle = 360.0/n)
		lt(t, ((n/2) - 1) * (360.0/n))
		arc(t, r, angle = 360.0/n)
		lt(t, (n/2) * (360.0/n))

def daisy(t, n):
	for i in range(n):
		angle = 60
		for i in range(n):
			angle_new = angle + 120
			angle_current = angle_new + 60
		arc(t, 50, angle_current)
		lt(t, angle_new)
	lt(t)
	circle(t, 85)

#daisy(bob, 6)
flower(bob, 12, 180)
wait_for_user()
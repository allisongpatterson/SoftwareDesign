from swampy.TurtleWorld import *

#world = TurtleWorld()
#bob = Turtle()
#bob.delay = 0.01
#ray = Turtle()

def square(t, l):
	for i in range(4):
		fd(t, l)
		lt(t)
	print t

#square(bob, 100)
#square(ray, 25)

def polygon(t, n, l):
	for i in range(n):
		angle = 360.0/n
		fd(t, l)
		lt(t, angle)
	print t

#polygon(bob, 6, 60)

def circle(t, r):
	circumference = 2 * 3.14159 * r
	n = int(circumference/3) + 1
	l = circumference/n
	polygon(t, n, l)

#circle(bob, 50)

def arc(t, r, angle):
	arc_length = (2 * 3.14159 * r * angle)/360
	n = int(arc_length/3) + 1
	step_length = arc_length/n
	step_angle = float(angle)/n

	for i in range(n):
		fd(t, step_length)
		lt(t, step_angle)
	print t

#arc(bob, 75, 270)

#wait_for_user()
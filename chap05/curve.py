from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.00001

def dragon(t, l, n):
	x = l*(0.5)**(0.5)
	if n == 0 or x < 1:
		fd(t, l)
		return

	dragon(t,x,n-1)
	lt(t,90)
	funky(t,x,n-1)

def funky(t, l, n):
	x = l*(0.5)**(0.5)
	if n == 0 or x < 1:
		fd(t, l)
		return

	dragon(t,x,n-1)
	lt(t,-90)
	funky(t,x,n-1)

if __name__ == '__main__':
	dragon(bob, 180, 12)
	wait_for_user()
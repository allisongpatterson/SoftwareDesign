from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.9

def draw(t, length, n):
	if n == 0:
		return
	angle = 50
	fd(t, length*n)
	lt(t, angle)
	draw(t, length, n-1)
	rt(t, 2*angle)
	draw(t, length, n-1)
	lt(t, angle)
	bk(t, length*n)

def koch(t, l, n):
	if n == 0 or l/3 < 1 or l < 3:
		fd(t, l)
		return
	koch(t, l/3, n-1)
	lt(t, 60)
	koch(t, l/3, n-1)
	rt(t, 120)
	koch(t, l/3, n-1)
	lt(t, 60)
	koch(t, l/3, n-1)

def snowflake(t, l, n):
	koch(t, l, n)
	rt(t, 120)
	koch(t, l, n)
	rt(t, 120)
	koch(t, l, n)
	rt(t, 120)

wait_for_user()
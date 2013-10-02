def dragon(t, l, n):
	x = l*(0.5)**(0.5)
	if n == 0 or x < 1:
		fd(t, l)
		return
	dragon(t, x, n-1)
	lt(t, 90)
	dragon(t, x, n-1)


dragon(bob, 180, 2)
wait_for_user()
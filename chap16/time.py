class Time(object):
	"""Represents time of day.
	attributes: hour, minute, second
	"""

def print_time(Time):
	print '%2d:%2d:%2d' % (Time.hour, Time.minute, Time.second)

def is_after(t1, t2):
	"""Returns True if t1 and t2 are in chronological order.
	"""
	if t1.hour >= t2.hour:
		if t1.hour > t2.hour:
			return False
		if t1.hour == t2.hour:
			if t1.minute >= t2.minute:
				if t1.minute > t2.minute:
					return False
				if t1.minute == t2.minute:
					if t1.second >= t2.second:
						return False
	return True

if __name__ == '__main__':
	time1 = Time()
	time1.hour = 11
	time1.minute = 59
	time1.second = 30

	time2 = Time()
	time2.hour = 8
	time2.minute = 45
	time2.second = 30

	print_time(time1)
	print_time(time2)
	print is_after(time1, time2)
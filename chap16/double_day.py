import datetime

def weekday(d):
	"""Returns weekday of given date.
	d: datetime.date()
	"""
	year = d.year
	month = d.month
	day = d.day
	dict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4:'Friday', 5: 'Saturday', 6:'Sunday'}
	num = datetime.date(year, month, day).weekday()
	return dict[num]

def birthday_wait(b):
	"""Returns days, hours, minutes, and seconds until next birthday.
	b: birthay in datetime.datetime format
	"""
	year = b.year
	month = b.month
	day = b.day
	hour = b.hour
	minute = b.minute
	second = b.second
	now = datetime.datetime.now()
	age_days = now - b
	age_years = age_days.days/365
	print age_years,
	print 'years old'
	next_b = datetime.datetime(year + age_years + 1, month, day, hour, minute, second)
	wait = next_b - now
	print wait,
	print 'until next birthday'

def double_day(older, younger):
	year_y = younger.year
	month_y = younger.month
	day_y= younger.day
	gap = younger - older
	print gap.days
	double = gap.days * 2
	year_double = year_y + (double / 365)
	month_double = month_y + ((double % 365) / 30) # approximating here. could be improved.
	day_double = day_y + ((double % 365) % 30)
	double_day = datetime.date(year_double, month_double, day_double)
	print double_day

if __name__ == '__main__':
	date = datetime.date(2013, 11, 17)
	print weekday(date)
	birthday = datetime.datetime(1994, 4, 10, 6, 0, 0)
	birthday_wait(birthday)
	Allison = datetime.date(1994, 4, 10)
	Rebecca = datetime.date(1996, 1, 23)
	double_day(Allison, Rebecca)
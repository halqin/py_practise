from datetiem import timedelta, date

def rollover(year=None, date=None, month = None):


	if year is None or month is None or date is None:
		today = date.today

	year = year if year is not None else today.year
	date = date if date is not None else today.date
	month = month if month is not None else today.month

	year += (month - 1) // 12
	month = 1+ (month -1) % 12 


	return date(year, month, 1) + timedelta(day - 1)

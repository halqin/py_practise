def rolloverDate(year = 2016, month = None, day = None):
	'''
	>>> rolloverDate(month=4, day=31)
	datetime.date(2016, 5, 1)
	>>> rolloverDate(year=2016, month=15, day=43)
	datetime.date(2017, 4, 12)
	>>> rolloverDate(year=2016, month=3, day=16)
	datetime.date(2016, 3, 16)
	>>> rolloverDate(year=2016, month=12, day=64)
	datetime.date(2017, 2, 2)
	>>> rolloverDate(year=2016, month=19, day=99)
	datetime.date(2017, 10, 7)
	>>> rolloverDate(year=2016, month=1, day=99999)
	datetime.date(2289, 10, 14)
	>>> rolloverDate(year=2016, month=9999, day=10)
	datetime.date(2849, 3, 10)


	'''

	year_, month_= MtoY(month, year)

	return DtoM(year_, month_, day)

def MtoY(month, year):
	year += int((month-1)/12)
	resi_m = month%12
	if resi_m == 0:
		resi_m = 12
	return year,resi_m



def DtoM(year, month, day):
	month_31 =[1,3,5,7,8,10,12]
	cntDays = 0
	new_m = month
	resi_d = day
	while int(resi_d / 30) >= 1:
		# new_m = month % 12

		if new_m != 2 :
			cntDays += 31 if new_m in month_31 else cntDays += 30
			month += 1
			resi_d = day-cntDays
		else:
			cntDays += 29 if leapYear(year) else cntDays += 28
			month += 1
			resi_d = day - cntDays

		new_m = month % 12

		if new_m == 1:
			year += 1

		
	if int(day/30) == 0:
		new_m = month

	return year, new_m, resi_d



def leapYear(year):
	'''
	How to determine whether a year is a leap year

	To determine whether a year is a leap year, follow these steps:
	1) If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
	2) If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
	3) If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
	4) The year is a leap year (it has 366 days).
	5) The year is not a leap year (it has 365 days).
	>>> leapYear(2016)
	True
	>>> leapYear(1868)
	True
	>>> leapYear(2096)
	True
	>>> leapYear(2017)
	False
	>>> leapYear(2018)
	False
	'''
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False


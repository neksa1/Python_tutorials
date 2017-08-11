month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    ''' Return True for leap years, False for non-leap Years'''
    return year % 4 == 0  and (year % 10 != 0 or year % 400 == 0)

def days_in_month(year, month):
    '''Return n umber of days in the month in the year'''
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print (days_in_month(2200, 2))

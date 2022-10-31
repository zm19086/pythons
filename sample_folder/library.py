# import calendar
# print(calendar.month(2022, 10))

# import calendar as cal
# print(cal.month(2022, 8))

from calendar import month, isleap
print(month(2022, 9))
print(isleap(2024))

from datetime import date
date = date.today()
print(date.strftime('%Y%m%d'))
print(date.strftime('%y/%m/%d'))
print(date.strftime('%Y年%m月%d日'))
print(date.strftime('%Y %B %d %a'))

from datetime import datetime as dt
print(dt.now())
now = dt.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))

from datetime import date, timedelta
today = date.today()
print(today)
one_week = timedelta(days = 7)
print(today + one_week)
print(today - one_week)
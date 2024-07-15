import datetime
today = datetime.datetime.now()
print(today)
# print(today.strfttime("%a %b %Y %I:%m %G"))


#creating a date object
x = datetime.datetime(2018, 6, 1, 12, 8, 50, 100)
print(x)
#date formate code
print(x.strftime("%B"))
""""
%a weekday, short version wed
%A weekday, full version wednesday
%w weekday as a number 0-6, 0 is sunday  3
%d Day of month 01-31 31
%b month name short version dec
%B month full version december
%m month as a number 01-12 12
%y year, short version
%x local version of date 12/31/18
%X local version of time  17:41:00
%% A % charactor %
%G 150 8601 year 2018
%u 150 8601 weekday (1-17) 1
%V 150 8601 weeknumber (01-53)
"""

#timedeita
from datetime import timedelta
today = datetime.datetime.today()
hours_before = today + timedelta(hours=10)
#supports days, seconds, milliseconds, microseconds
print(hours_before)

#subtraction btn dates
days_before = today - timedelta(weeks=6)
print (days_before)
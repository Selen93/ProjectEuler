# DESC: How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
import calendar

count = 0
calendar = calendar.Calendar()
month = []
for i in range(1901,2001):
    for m in range(1,13):
        month = calendar.monthdays2calendar(i,m)
        count += month[0].count((1,6))

print(count)
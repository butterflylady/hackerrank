import calendar

month, day, year = map(int, input().split())
weekday = calendar.weekday(year, month, day)
day_name = list(calendar.day_name)[weekday]
print(day_name.upper())

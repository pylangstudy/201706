import datetime
now = datetime.date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
dt = datetime.date(2022, 1, 2)
print(int(dt.strftime("%m")))

birthday = datetime.date(1964, 7, 31)
age = now - birthday
print(age)
print(age.days)
print(age.days/365)

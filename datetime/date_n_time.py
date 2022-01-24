from datetime import date

timestamp = date.fromtimestamp(0)
print("Date =", timestamp)

from datetime import datetime, date

t1 = date(year=2018, month=7, day=12)
t2 = date(year=2017, month=12, day=23)
t3 = t1 - t2

t4 = datetime(year=2018, month=7, day=12, hour=7, minute=9, second=33)
t5 = datetime(year=2019, month=6, day=10, hour=5, minute=55, second=13)
t6 = t4 - t5

print(abs(t6.days))
print(t6)
print(t6.seconds)

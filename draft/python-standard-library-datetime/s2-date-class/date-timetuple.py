import datetime as date

d = date.date(2020, 4, 6)
t = d.timetuple()

for p in t:
    print(p, end='.')
# 2020.4.6.0.0.0.0.97.-1.
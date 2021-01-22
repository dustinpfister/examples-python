import datetime as date

d1 = date.datetime(1983, 4, 6, 10, 5, 0, 0)
d2 = date.datetime(2010, 8, 22, 10, 5, 0, 0)

td = d2 - d1

print(td.days) # 10000
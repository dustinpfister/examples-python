import datetime as date

d = date.datetime.now()

print(type(d).__name__)  # datetime
print(d.year)            # 2021
print(d.month)           # 1
print(d.day)             # 21
print(d)                 # 2021-01-21 15:27:49.097128
import datetime as date

d1 = date.date(2020, 1, 20)
d2 = date.date(2020, 1, 21)

# subtracting one date from another will result
# in an instance of timedelta
td = d2 - d1

print( type(td).__name__ ) # timedelta
print( td ) # 1 day, 0:00:00
import datetime as date

# a time delta of 1 Billion Seconds
td = date.timedelta(seconds=1000000000)
print(td.days, td.seconds) # 11574 6400

# if I add this time delta to the day I was born
# I get the date at which I turned 1 Billion Seconds old
print(date.date(1983, 4, 6) + td) # 2014-12-13
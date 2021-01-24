import datetime as date

d1 = date.date(1999, 1, 20)
d2 = date.date(1999, 1, 21)

td = d2 - d1
print(type(td).__name__)

d3 = date.date(2021, 4, 5) + td
print(type(d3).__name__)    # date
print( d3 ) # 2021-04-06
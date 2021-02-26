import statistics as stat

data = [100, 50, 75, 25, 12.5]
print( stat.median(data) ) # 50
print( stat.mean(data) )   # 52.5

data = [100, 50, 75, 25]
print( stat.median(data) ) # 62.5
print( stat.mean(data) )   # 62.5
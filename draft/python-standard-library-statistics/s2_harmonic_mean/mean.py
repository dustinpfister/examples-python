import statistics as stat

a = 100
b = 50

print( (a + b) / 2  ) # 75.0
print( 2 / ( 1/a + 1/b ) ) # 66.66666666666667

print( stat.mean([a, b]) )  # 75
print( stat.harmonic_mean([a, b]) )  # 66.66666666666667
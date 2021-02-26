import statistics as stat
import math

data1=[100,50,75]

print( stat.stdev(data1) )   # 25
# it is the sqrt of the sample variance
print( math.sqrt(stat.variance(data1)) ) # 25

print( stat.pstdev(data1) )  # 20.412414523193153

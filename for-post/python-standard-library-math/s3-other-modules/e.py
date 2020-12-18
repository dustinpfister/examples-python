import math

print(math.e)         # 2.718281828459045

n = math.pow(2, 52)
e = math.pow( 1 + 1 / n, n)
print(e)              # 2.718281828459045
print( math.e == e )  # true

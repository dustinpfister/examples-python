
def bias(n, d):
  return 1 - abs( ( n / d ) - 0.5) / 0.5

n=0
d=8
while n <= d:
  print( bias(n, d) )
  n = n + 1
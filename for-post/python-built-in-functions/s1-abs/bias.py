
def bias(n, d):
  return 1 - abs( ( n / d ) - 0.5) / 0.5

n=0
d=8
nums=[]
while n <= d:
  nums.append( bias(n, d) )
  n = n + 1
print(nums)
# [0.0, 0.25, 0.5, 0.75, 1.0, 0.75, 0.5, 0.25, 0.0]

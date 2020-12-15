import math
base=2
nums=[]
for e in range(0,10):
  nums.append(int(math.pow(base, e)))
print(nums)
# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
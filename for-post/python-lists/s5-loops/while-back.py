a=[1,2,3,4]
length=len(a)
i=length
while i > 0:
  i = i - 1
  index = length - i - 1
  el = a[index]
  print(i, el, sep="-", end=" | ")
# 3-1 | 2-2 | 1-3 | 0-4 |
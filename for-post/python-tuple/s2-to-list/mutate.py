t=(1,2,3,4,5)
l=list(t)

i=0
while i < len(l):
    l[i] = l[i] * 7
    i = i + 1

print(l) # [7, 14, 21, 28, 35]
print(t) # (1, 2, 3, 4, 5)
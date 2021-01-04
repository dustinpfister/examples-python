import array

l = [1,2,3]
a = array.array('i', [1,2,3])

for n in a:
    print(n, end="-")   
for n in l:
    print(n, end="-")
# 1-2-3-1-2-3-
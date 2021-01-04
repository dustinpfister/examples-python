import array

a = array.array('i', [1,2,3,4])

for x in a:
    y = pow(2,x)
    print(x, y, sep="-", end="; ")
# 1-2; 2-4; 3-8; 4-16;
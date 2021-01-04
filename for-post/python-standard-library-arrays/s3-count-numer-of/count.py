import array as arr

a = arr.array('i', [1,0,0,1,1,1,0,1,1,1])

print(a.count(0)) # 3
print(a.count(1)) # 7
print(a.count(2)) # 0


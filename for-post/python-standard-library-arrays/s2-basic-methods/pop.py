import array as arr

a = arr.array('i', [1,2,3])

print( a.pop(0) ) # 1
print( a.pop() )  # 3

print( a[0] )     # 2
print( len(a) )   # 1

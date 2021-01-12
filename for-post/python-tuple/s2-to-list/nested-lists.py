t=([1,2,3],[4,5,6])
l=list(t)

# mutating a value in this list can effect the source
l[0][0]= 40
print( type(l).__name__ ) # list
print( l ) # [[40, 2, 3], [4, 5, 6]]
print( t ) # ([40, 2, 3], [4, 5, 6])
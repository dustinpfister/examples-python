t=((1,2,3),(4,5,6))
l=list(t)
l[0] = list(t[0])
l[1] = list(t[1])

# mutating a value in this list will not effect source
l[0][0]= 40
print( type(l).__name__ ) # list
print( l ) # [[40, 2, 3], [4, 5, 6]]
print( t ) # ((1, 2, 3), (4, 5, 6))
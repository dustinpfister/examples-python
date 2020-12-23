a=range(0,10)
# use of range will return a range type
# this is a kind of non mutabule sequence
print(type(a).__name__) # range

# The list function can qucikly turn a range
# into a list which is mutabule
b=list(a)
b[2]="two"
print(type(b).__name__) # list
print(b) # [0, 1, 'two', 3, 4, 5, 6, 7, 8, 9]
import random

def getValue(minval=0, maxval=10, per=0):
    return minval + ( maxval - minval ) * per

print( getValue(0, 359, 0) )
print( getValue(0, 359, 1) )
print( getValue(0, 359, random.random()) )
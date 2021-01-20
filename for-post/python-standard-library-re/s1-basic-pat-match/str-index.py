a='so abc is easy as abc'
b='things are not always so easy'

print( a.index('abc') )
# 3

try:
    print( b.index('abc') )
except ValueError:
    print('abc not found');
# 'abc not found'
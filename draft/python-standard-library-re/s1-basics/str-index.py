a='easy as abc'
b='not so easy'

print( a.index('abc') )
# 8

try:
    print( b.index('abc') )
except ValueError:
    print('abc not found');
# 'abc not found'
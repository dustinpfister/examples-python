# a key is not the same thing as an attribute
# if I try to get an attribute that is not an attribute
# but a key value then that will result in an AttributeError
d = {'foo': 42}
try:
    a = d.foo
except AttributeError:
    print('AttributeError')
# output:
# AttributeError

# to get a key value one way is to use
# this kind of syntax. However if the value
# is not there it will result in a KeyError
print( d['foo'] )
# output:
# foo
try:
    print( d['bar'] )
except KeyError:
    print('KeyError')
# output:
# KeyError

## it might be nest to use the get method
print( d.get('foo', 0) )
print( d.get('bar', 0) )
# output:
# 42
# 0

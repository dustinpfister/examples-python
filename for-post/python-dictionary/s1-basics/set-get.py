# a blank dict
d={}

# keys can be added like this
d['a'] = 1

# The get method of a dict is what can be used
# to get any key in an Error Free way
print( d.get('a', 0) ) # 1
print( d.get('b', 0) ) # 0
print( d.get('b') )    # None

# just getting a key that is not there
# without uisng get will cause an Error
print( d['b']) # Error
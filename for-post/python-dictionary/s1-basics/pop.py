# a blank dict
d={'a': 1, 'b': 2, 'c': 3}

print( len(d) ) # 3

print( d.pop('a', 0) ) # 1
print( d.pop('a', 0) ) # 0

print( len(d) ) # 2

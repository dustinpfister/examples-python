# a blank dict
d={'a': 1, 'b': 2, 'c': 3}

# just using len seems to work okay
print( len(d) ) # 3

# some other ways that give the same result
print( len(d.keys()) )    # 3
print( len(d.values()) )  # 3
print( len(d.items()) )   # 3

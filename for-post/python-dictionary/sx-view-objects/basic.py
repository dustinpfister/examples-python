# creating a dict
d={}

# creating a view of dict
v=d.items()
# creating a list from dict
l=list(d)

# adding key value pairs to the dict after creating view
d['a']=40
d['b']=2

# the view reflects the current state of the dict
print(list(v)) # [('a', 40), ('b', 2)]

# the plain old list does not
print(l) # []

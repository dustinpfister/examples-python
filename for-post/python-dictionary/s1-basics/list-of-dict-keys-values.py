a={'a': 0, 'b': 1}
b=list(a)
c=a.values()
d=list(c)

print(type(b).__name__) # list
print(b) # ['a', 'b']

print(type(c).__name__) # dict_values

print(type(d).__name__) # list
print(d) # [0, 1]

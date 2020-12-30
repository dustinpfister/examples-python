a={'a': 0, 'b': 1}
b=list(a)
c=list(a.values())

print(type(b).__name__) # list
print(b) # ['a', 'b']
print(c) # [0, 1]

# if two strings I can just add
a = 'hello'
b = 'world'
c = a + ' ' + b
print(c) # hello world

# if one value is not a string
# it must be turned into a string first
a = 42
b = 'foo'
try:
    c = a + ' ' + b
except TypeError:
    print('TypeError')
# TypeError

c = str(a) + ' ' + b
print(c)
# 42 foo



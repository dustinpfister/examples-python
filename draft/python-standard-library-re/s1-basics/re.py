import re

a='so abc is easy as abc'
b='things are not always so easy'

m = re.search('abc', a)

# the start and end index of the first group
print(m.start(0)) # 3
print(m.end(0)) # 6

# the text of the first group
print(m.group(0)) # abc


m = re.search('abc', b)
print(m)
# None
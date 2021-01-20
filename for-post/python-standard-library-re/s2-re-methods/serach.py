import re

a = 'I would say that 654 is also like 123 in some ways'

m = re.search('\d+', a);

# can get the match value, and the start and end index values
print(m.group(0)) # '654'
print(m.start(0)) # 17
print(m.end(0))   # 20

# but I can only get the first match
try:
    print( m.group(1) )
except IndexError:
    print('no dice')
# no dice

# a value of None will be the result if no match is found
m = re.search('\d+', 'foo man chew')
print(m) # None
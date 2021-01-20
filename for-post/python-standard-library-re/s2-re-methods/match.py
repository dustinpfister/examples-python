import re

m = re.match('\d+', '654');
print(m.group(0)) # 654

# these work, but of course the start will always be 0
print(m.start(0)) # 0
print(m.end(0)) # 3

# None returned if the start of the string does not match the pattern
m = re.match('\d+', 'abc')
print(m) # None
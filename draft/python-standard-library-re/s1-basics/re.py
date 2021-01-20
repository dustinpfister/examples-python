import re

m = re.search('foobar', 'All things are foobar when you think about if for a moment')

# the start and end index of the first group
print(m.start(0)) # 15
print(m.end(0)) # 15

# the text of the first group
print(m.group(0)) # foobar
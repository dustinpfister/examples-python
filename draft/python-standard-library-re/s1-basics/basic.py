import re

m = re.search('foobar', 'All things are foobar when you think about if for a moment')
print(m.group(0)) # foobar
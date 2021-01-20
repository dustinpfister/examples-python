import re

a = 'I would say that 654 is also like 123 in some ways'

m = re.finditer('\d+', a);

for i in m:
    print(i.group(0), end=',')
    print(i.start(0), end=',')
    print(i.end(0))


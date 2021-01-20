import re

a = 'I would say that 654 is also like 123 in some ways'

regObj = re.compile('\d+');

print(regObj.search(a))
print(regObj.search(a))
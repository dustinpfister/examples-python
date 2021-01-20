import re

a = 'I would say that 654 is also like 123 in some ways'

m = re.findall('\d+', a);

print(m) # ['654', '123']
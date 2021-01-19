d = {'foo': 42}
try:
    a = d.bar
except AttributeError:
    print('AttributeError')
# output:
# AttributeError
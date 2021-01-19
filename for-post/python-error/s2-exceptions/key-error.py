d = {'foo': 42}
try:
    a = d['bar']
except KeyError:
    print('KeyError')
# output:
# keyError
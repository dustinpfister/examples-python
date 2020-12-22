import fileinput

for line in fileinput.input():
    print(line)
    pass

# $ echo -n 'foo' | python basic.py
# 'foo'
# $
import fileinput

f = fileinput.input();

for line in f:
  print(line)
  print(f.filename()) # '<stdin>'
  print(f.isstdin()) # True

# $ echo -n 'foo' | python basic.py
# 'foo'
# $
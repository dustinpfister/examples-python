import fileinput

f=fileinput.input()

def powIt(n):
  if(n == ''):
      return 0
  return pow(2, int(n))

for line in f:
  l=list(line.split(' '))
  p=map(powIt, l)
  print(list(p))
  
# $ python3 nums-gen.py | python3 nums-read.py
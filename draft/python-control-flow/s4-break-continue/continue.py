def stronly(l):
  i=len(l)
  result=[]
  while i > 0 :
    i = i - 1;
    if(ascii(type(l[i])) != '<class \'str\'>'):
        continue
    result.append(l[i])
  return result

l=[1, 'one', 2, 'two', 3.5, 4, 'three', []]  
print( stronly(l) ) # ['three', 'two', 'one']
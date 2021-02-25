import json

f=open('./state.json', 'w+')

if f.read() == '':
    print('blank')

#f.write('hello world\n')
f.close()
 
#f=open('./foo.txt', 'r')
#print(f.read())
#f.close()

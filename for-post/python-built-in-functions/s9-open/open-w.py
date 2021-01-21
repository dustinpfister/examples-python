f=open('./foo.txt', 'w+')
f.write('hello world\n')
f.close()

f=open('./foo.txt', 'r')
print(f.read())
f.close()
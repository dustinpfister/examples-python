f=open('foo.txt', 'w')

f.write('hello world');

print(f.fileno()) # the file no

f.close()
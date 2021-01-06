import os

fd=os.open('foo.txt', os.O_RDWR|os.O_CREAT)
f=os.fdopen(fd, 'w+')

f.write('Okay now');

print(fd) # the file no
print(f) # the file object

f.close()
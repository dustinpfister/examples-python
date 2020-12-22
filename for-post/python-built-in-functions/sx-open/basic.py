f=open('./hello.txt', 'r')
s=f.read()
print(s) # 'Hello World'
print(type(s).__name__) # 'str'
# can start with an int just like this
x = 1
print(x, type(x)) # 1 <class 'int'>
# adding two int values will result in an int
x = 5 + 1
print(x, type(x)) # 6 <class 'int'>

# adding a fraction will result in a switch to float
x += 2.5;
print(x, type(x)) # 8.5 <class 'float'>

# the int built in function can be used to create
# an int value from a float
x = int(x);
print(x, type(x)) # 8 <class 'int'>
str = '0,1,2,3,4,5'
l = str.split(',')

print(type(l).__name__) # list
print(l[3]) # 3

str = '012345'
# I can not give and empty string as a sep
# doing so will result in an error
try:
    l = str.split('')
except ValueError:
    print('ValueError')

# however there are a number of other ways to
# get that kind of list such as passing the string value
# to the list built in function
l = list(str);
print(type(l).__name__) # list
print(l[3]) # 3

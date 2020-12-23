import copy

a = [1,2,3,4]
b = copy.copy(a);

# b is now a copy of a
print(a) # [1, 2, 3, 4]
print(b) # [1, 2, 3, 4]

# mutating b will only effect b
b[1]='two'
print(a) # [1, 2, 3, 4]
print(b) # [1, 'two', 3, 4]
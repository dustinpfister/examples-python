import copy

a = [[0,1,2],[2,4,5],[6,7,8]]
b = copy.copy(a);

# b is now a shallow copy of a
print(a) # [[0, 1, 2], [2, 4, 5], [6, 7, 8]]
print(b) # [[0, 1, 2], [2, 4, 5], [6, 7, 8]]

# mutating a nested list in b will also effect the same
# nested list in a
b[1][1]='two'
print(a) # [[0, 1, 2], [2, 'two', 5], [6, 7, 8]]
print(b) # [[0, 1, 2], [2, 'two', 5], [6, 7, 8]]
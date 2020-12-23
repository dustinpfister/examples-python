import copy

a = [[0,1,2],[2,4,5],[6,7,8]]
b = copy.deepcopy(a);

# b is now a DEEP copy of a
print(a) # [[0, 1, 2], [2, 4, 5], [6, 7, 8]]
print(b) # [[0, 1, 2], [2, 4, 5], [6, 7, 8]]

# mutating a nested list in b WILL NOT effect the same
# nested list in a becuase it is a DEEP COPY
b[1][1]='two'
print(a) # [[0, 1, 2], [2, 4, 5], [6, 7, 8]]
print(b) # [[0, 1, 2], [2, 'two', 5], [6, 7, 8]]

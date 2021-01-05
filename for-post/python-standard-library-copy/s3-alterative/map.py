# a source object (a) with nested objects
a = [[1,2,3],[4,5,6]]

# using list and map to create a deep clone (b),
# at one level of source object (a)
def func(el):
    return list(el)
b = list(map(func, a))

# mutating (b) bolth at the top level
# and one additional level
b.append([7,8,9])
b[1][0] = 0
b[1][1] = 0
b[1][2] = 0

# mutation of (b) did not effect source object (a)
print(b) # [[1, 2, 3], [0, 0, 0], [7, 8, 9]]
print(a) # [[1, 2, 3], [4, 5, 6]]


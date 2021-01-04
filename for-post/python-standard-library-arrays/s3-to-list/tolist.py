import array as arr

a = arr.array('i', [255])
b = a.tolist()

print(type(a), type(b)) # <class 'array.array'> <class 'list'>


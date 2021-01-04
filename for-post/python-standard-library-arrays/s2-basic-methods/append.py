import array as arr

a = arr.array('i', [1,2])

# len can be used to get the length
print(len(a)) # 2

# append can be used to append a new element to the end
a.append(3)

print(a[2]) # 3
print(len(a)) # 3
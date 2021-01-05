# A source object (a)
a = [1,2,3,4,5]

# using the list built in function to create a shallow clone (b)
b = list(a);

# Mutating (b)
i=0
while i < len(b):
    n = b[i]
    b[i] = pow(2, n)
    i = i + 1

# mutation of shallow copy (b) did not effect its source object (a)
print(b) # [2, 4, 8, 16, 32]
print(a) # [1, 2, 3, 4, 5]


def power(n):
  return pow(2, n)

a=[0,1,2,3,4,5]
b=map(power, a)
c=list(b)

# the use of map will create a map type
print(type(b).__name__) # map
# the list function can turn it back into a list
print(c) # [1, 2, 4, 8, 16, 32]
# none of this will mutate the source list
print(a) # [0, 1, 2, 3, 4, 5]
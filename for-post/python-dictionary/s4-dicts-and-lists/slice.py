# a list
l=['zero','one','two','three']

# creating another list that is a slice of a list
b=l[1:3:1]

# in the new slice of the list index values 0 and 1
# are now different values
print(b[0]) # one
print(b[1]) # two

# a dict
d={0:'zero', 1:'one', 2:'two', 3:'three'}

# deleting keys 0 and 3
del d[0]
del d[3]

# key 0 is now None, and key 1 is still 'one'
print(d.get(0)) # None
print(d.get(1)) # one
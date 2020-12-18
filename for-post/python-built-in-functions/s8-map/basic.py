a=[0,1,2,3,4]
def pow2(n):
    return pow(2, n)
b = list( map(pow2, a) )
print(b) # [1, 2, 4, 8, 16]
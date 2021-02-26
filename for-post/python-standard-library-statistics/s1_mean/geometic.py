# nth root
def nroot(num, degree=2):
    return pow(num, 1 / degree)
# product
def prod(data):
    pro=data[0]
    i=1
    while i < len(data):
        pro = pro * data[i]
        i = i + 1
    return pro
# geometric mean
def geometric_mean(data):
    return nroot(prod(data), len(data))

print( geometric_mean([4, 9]) )  # 6.0
print( geometric_mean([14, 32]) )  # 21.166010488516726
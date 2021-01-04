import array

def createMulti(w=3, h=3):
    a = array.array('i')
    i=0
    while(i < w * h):
        a.append(i)
        i = i + 1
    return {'a': a, 'w': w, 'h': h}

def getMultiPos(m, x=0, y=0):
    a=m['a']
    return a[int(y * m['w'] + x)];

m=createMulti(5, 5)
print(getMultiPos(m, 2, 1)) # 7

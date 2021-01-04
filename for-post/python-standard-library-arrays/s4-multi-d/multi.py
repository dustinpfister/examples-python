import array

def createMulti(w=3, h=3):
    m = array.array('i')
    i=0
    while(i < w * h):
        m.append(0)
        i = i + 1
    return {'m': m, 'w': w, 'h': h}

#def getMultiPos(m, x=0, y=0):
    

a=createMulti()

print(a)

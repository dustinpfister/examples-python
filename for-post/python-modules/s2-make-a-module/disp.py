
def createBasic(x=0, y=0, w=32, h=32):
    disp={'x':x,'y':y,'w':w,'h':h}
    return disp

def createPool(count=5, create=createBasic):
    i=0
    pool=[]
    while i < count:
        pool.append(create(0,0,32,32))
        i = i + 1
    return pool
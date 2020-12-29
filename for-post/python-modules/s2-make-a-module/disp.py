# create a basic display object
def createBasic(x=0, y=0, w=32, h=32):
    disp={'x':x,'y':y,'w':w,'h':h}
    return disp
# create an enemy display object
def createEnemy(x=0,y=0,w=32,h=32,hpMax=100,attack=1):
    disp=createBasic(x, y, w, h)
    disp['hpMax']=hpMax
    disp['hp']=hpMax
    disp['attack']=attack
    return disp
# create a pool of display objects
def createPool(count=5, create=createBasic, x=0, y=0):
    i=0
    obj=[]
    while i < count:
        obj.append(create(x,y,32,32))
        i = i + 1
    return {'obj': obj}
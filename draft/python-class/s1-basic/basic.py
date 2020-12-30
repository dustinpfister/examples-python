#!/usr/bin/python3
class Disp:
    w=32 # some props for width and height
    h=32
    def __init__(self, x, y):
        self.x = int(x) # can set position when creating
        self.y = int(y)
    def getPos(self):
        return {'x': self.x, 'y': self.y} # just position
    def getBasicObj(self):
        obj=self.getPos() # position
        obj['w']=self.w   # width and height
        obj['h']=self.w
        return obj

x = Disp(3, 5.7)

print(x.getBasicObj()) # {'x': 3, 'y': 5, 'w': 32, 'h': 32}
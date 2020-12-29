#!/usr/bin/python3
class Disp:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    def getPos(self):
        return {'x': self.x, 'y': self.y}

x = Disp(3, 5.7)

print(x.getPos()) # {'x': 3, 'y': 5}
import random
import math

def echo(n):
    return n

def angleToFrom(toX, toY, fromX, fromY, invert=False, degrees=True):
    angle = math.atan2(toY - fromY, toX - fromX)
    if(invert):
        angle += math.pi
    if(degrees):
        return math.degrees(angle) % 360
    return angle % (math.tau)

# seems to work
print( angleToFrom(0, 0, 100, 0) )   # 180.0
print( angleToFrom(0, 0, -100, 0) )  # 0.0
print( angleToFrom(0, 0,  0, 100) )  # 270.0
print( angleToFrom(0, 0,  0, -100) ) # 90.0
print( angleToFrom(0, 0,  -100, 0, degrees=False, invert=True) ) # 3.141592653589793

def createBlock():
    x = -100 + random.random() * 200;
    y = -100 + random.random() * 200;
    a = angleToFrom(0, 0, x, y)
    return {'x': x, 'y': y, 'a': a}

block = createBlock()

print(block)
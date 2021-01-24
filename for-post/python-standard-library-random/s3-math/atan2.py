import random
import math

def echo(n):
    return n

def angleToFrom(toX, toY, fromX, fromY, invert=False, degrees=True):
    angle = math.atan2(toY - fromY, toX - fromX)
    if(invert == True):
        angle += math.pi
    return angle;

a1 = angleToFrom(0,0,100,0, True)
print(a1)

print(math.degrees(math.pi * -0.5) % 360)
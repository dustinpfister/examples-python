import random
import math

def echo(n):
    return n

def getPointFromCenter(cx=0, cy=0, degree=0, dist=0, roundFunc=echo):
    radian = math.pi / 180 * degree
    return {
        'x': roundFunc( cx + math.cos(radian) * dist ),
        'y': roundFunc( cy + math.sin(radian) * dist )
    }

# get random points that are on a ray
def getRandomPointAlongRay(cx=50, cy=50, degree=90, dist_min=25, dist_max=50, roundFunc=echo):
    return getPointFromCenter(cx, cy, degree, random.uniform(dist_min, dist_max), roundFunc)

print( getRandomPointAlongRay(100, 250, 180, 25, 100, round) )

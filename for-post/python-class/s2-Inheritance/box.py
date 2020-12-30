import math

class Box():
    x=0
    y=0
    w=32
    h=32
    def __init__(self,x=0,y=0,w=32,h=32):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
    def distance(self, box2):
        if(box2 is None):
            return 0
        a=math.pow(self.x - box2.x, 2)
        b=math.pow(self.y - box2.y, 2)
        return math.sqrt(a+b) 

class Ship(Box):
    def __init__(self, hpMax=100, damage=1):
        self.hpMax = hpMax
        self.hp = hpMax
        self.heading = 0
        self.damage = damage

a=Ship()

print(a.hp) # 100

# no properties are set for x,y,w, and h in the Ship Class
# however the Ship Class inherits from Box and as such the
# Class level values of Box are used for these values
print(a.x, a.y)  # 0 0

# on top of Box properties functioning as a default for ship values
# I can also use Box functions with a ship class instance
b=Box(25,30)
d=a.distance(b)
print(d) # 39.05124837953327
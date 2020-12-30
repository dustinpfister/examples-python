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
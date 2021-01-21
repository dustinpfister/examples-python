
class Box():
    def __init__(self, x=0, y=0, w=32, h=32):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
    
class Ship(Box):
    def __init__(self, heading=90, x=0, y=0, w=32, h=32):
        super().__init__(x, y, w, h)
        self.heading = heading
    
s=Ship(180);
print(s.area()) # 1024

print(s.__dict__)
# {'x': 0, 'y': 0, 'w': 32, 'h': 32, 'heading': 180}
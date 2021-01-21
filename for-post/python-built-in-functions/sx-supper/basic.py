
class Box():
    def __init__(self, x=0, y=0, w=32, h=32):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
    
b=Box(10,15,10,5)

print(b.area()) # 50
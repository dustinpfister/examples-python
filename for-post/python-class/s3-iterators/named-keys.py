class Foo:
    loopKeys=['a','d']
    def __init__(self, a=1, b=2, c=3, d=4):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.index=0
        
    def __iter__(self):
        self.index=0
        return self
    
    def __next__(self):
        if self.index == len(Foo.loopKeys):
            raise StopIteration
        prop=Foo.loopKeys[self.index]
        self.index = self.index + 1
        return self.__dict__[prop]

x=Foo();
for prop in x:
    print(prop)
# 1
# 4
#!/usr/bin/python3
class MyClass:
    a=40
    c=None
    def __init__(self, b):
        self.b=int(b)
        self.c=self.a + self.b
    def out(self):
        print(self.a, self.b, self.c)

x=MyClass(2)
x.out()
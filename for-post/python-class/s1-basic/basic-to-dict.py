#!/usr/bin/python3
class MyClass:
    a=40
    def __init__(self, b):
        self.b = b
        self.a = MyClass.a

# when I create an instnace of a class
# it will be a type of that class
x=MyClass(5)
print(type(x).__name__) # MyClass

# if I want a plan dictionary there is the __dict__ property
d = x.__dict__
print(d) # {'b': 5, 'a': 40}

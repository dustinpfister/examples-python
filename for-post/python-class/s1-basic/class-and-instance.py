
class MyClass:
    a=40
    def __init__(self, b):
        self.b=b

# when creating a class instance
# that instnace will have properties for 'a' and 'b'
x=MyClass(2)
print(x.a) # 40
print(x.b) # 2

# however only the 'b' propery is an 'own property' of
# the class instance
d=x.__dict__
print(d) # {'b': 2}
import inspect

class P(object):
    def __init__(self, n):
        self.n = n
    def get_n(self):
        return self.n

a=P(2)
# when working with a class I want to use
# is method over is function
print(inspect.isfunction(a.get_n)) # false
print(inspect.ismethod(a.get_n))   # True

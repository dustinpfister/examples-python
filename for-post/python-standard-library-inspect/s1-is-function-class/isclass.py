import inspect

class P(object):
    """Definition for P class."""

    def __init__(self, b, e):
        self.b = b
        self.e = e

    def get_p(self):
        return pow(self.b, self.e)

a=P(2, 4)
print(a.get_p()) # 16
print(inspect.isclass(P)) # True
print(inspect.isclass(a)) # False

# when working with a class I want to use
# is method over is function
print(inspect.isfunction(a.get_p)) # false
print(inspect.ismethod(a.get_p))   # True

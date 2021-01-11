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

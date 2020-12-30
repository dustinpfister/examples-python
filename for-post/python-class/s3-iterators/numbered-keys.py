class Numbered:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        d={'value': self.data[self.index], 'index': self.index}
        self.index = self.index + 1
        return d
    
x = Numbered('foo')

for prop in x:
    print(prop)
    

import inspect

f=inspect.currentframe()

print(inspect.isframe(f)) # True
print(inspect.getsource(f));